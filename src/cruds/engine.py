import asyncio
from dataclasses import dataclass
from typing import Any, Dict, Union

from fastapi import HTTPException
from fastapi_cloudauth.firebase import FirebaseClaims
from fastapi_pagination import Page, Params
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from src.cruds.abstract import AbstractCrud
from src.cruds.search import buildDatabaseQuery
from src.cruds.utils import (
    db_to_resp,
    get_current_unix,
    get_first_item_or_404,
    get_new_name,
    is_owner_or_admin_otherwise_409,
    patch_to_model,
    req_to_db,
    save_to_db,
)
from src.database.objects import (
    BackgroundSave,
    EffectSave,
    EngineSave,
    ParticleSave,
    SkinSave,
)
from src.models.add_engine_request import AddEngineRequest
from src.models.default_search import defaultSearch
from src.models.edit_engine_request import EditEngineRequest
from src.models.engine import Engine as EngineReqResp
from src.models.get_engine_list_response import GetEngineListResponse
from src.models.get_engine_response import GetEngineResponse
from src.models.search_query import SearchQueries
from src.models.sonolus_page import SonolusPage, toSonolusPage


@dataclass
class SRLConvert:
    obj: Any
    name: str


SRLConvertDict = [
    SRLConvert(BackgroundSave, "background"),
    SRLConvert(EffectSave, "effect"),
    SRLConvert(SkinSave, "skin"),
    SRLConvert(ParticleSave, "particle"),
]


class EngineCrud(AbstractCrud):  # type: ignore
    async def create_dict(
        self, db: AsyncSession, model: EngineReqResp, exclude_unset: bool = False
    ) -> Dict[str, Any]:
        """モデルに指定されたSonolusオブジェクトをDBから取り出してIDを埋めます"""
        model_import: Dict[str, Any] = model.dict(exclude_unset=exclude_unset)
        # SRL周りをDB側のIDに変換
        for convert in SRLConvertDict:
            if convert.name in model_import:
                obj_req = model_import[convert.name]
                if obj_req:
                    obj_db = await get_first_item_or_404(
                        db, select(convert.obj.id).filter(convert.obj.name == obj_req)
                    )
                    model_import[convert.name + "Id"] = obj_db
        # 存在してると変換できないフィールドを消す
        for key in [s.name for s in SRLConvertDict]:
            if key in model_import:
                del model_import[key]
        return model_import

    async def get_single_engine(
        self, stmt: Any, db: AsyncSession, localization: str
    ) -> EngineReqResp:
        # 保存するとリレーション周りのデータが消し飛ぶのでjoinedして取得し直す
        engine_db: EngineSave = await get_first_item_or_404(
            db,
            stmt.options(
                joinedload(EngineSave.background),
                joinedload(EngineSave.skin),
                joinedload(EngineSave.particle),
                joinedload(EngineSave.effect),
            ),
        )
        # 各地のSRLを応答型に変換し回る
        for db_obj in [
            engine_db,
            engine_db.skin,
            engine_db.background,
            engine_db.particle,
            engine_db.effect,
        ]:
            await db_to_resp(db, db_obj, localization)
        return engine_db  # type: ignore

    async def add(
        self, db: AsyncSession, model: AddEngineRequest, auth: FirebaseClaims
    ) -> Union[HTTPException, GetEngineResponse]:
        """エンジンを追加します"""
        model_import = await self.create_dict(db, model)
        engine_db = EngineSave(**model_import)
        engine_db.name = await get_new_name(db, EngineSave)
        engine_db.userId = auth["user_id"]
        await req_to_db(db, engine_db, is_new=True)
        await save_to_db(db, engine_db)
        item = await self.get_single_engine(
            select(EngineSave).filter(EngineSave.id == engine_db.id), db, "ja"
        )
        resp = GetEngineResponse(
            item=item,
            description=item.description,
            recommended=[],
        )
        return resp

    async def get(
        self, db: AsyncSession, name: str, localization: str
    ) -> GetEngineResponse:
        """エンジンを取得します"""
        item = await self.get_single_engine(
            select(EngineSave).filter(EngineSave.name == name), db, localization
        )
        return GetEngineResponse(
            item=item,
            description=item.description,
            recommended=[],
        )

    async def edit(
        self,
        db: AsyncSession,
        name: str,
        model: EditEngineRequest,
        auth: FirebaseClaims,
    ) -> Union[HTTPException, GetEngineResponse]:
        """エンジンを編集します"""
        engine_db: EngineSave = await get_first_item_or_404(
            db,
            select(EngineSave).filter(
                EngineSave.name == name,
            ),
        )
        await is_owner_or_admin_otherwise_409(db, engine_db, auth)
        model_import = await self.create_dict(db, model, True)
        patch_to_model(engine_db, model_import)
        await save_to_db(db, engine_db)
        item = await self.get_single_engine(
            select(EngineSave).filter(EngineSave.id == engine_db.id), db, "ja"
        )
        return GetEngineResponse(
            item=item,
            description=item.description,
            recommended=[],
        )

    async def delete(
        self,
        db: AsyncSession,
        name: str,
        auth: FirebaseClaims,
    ) -> Union[HTTPException, None]:
        """エンジンを削除します"""
        engine_db: EngineSave = await get_first_item_or_404(
            db, select(EngineSave).filter(EngineSave.name == name)
        )
        await is_owner_or_admin_otherwise_409(db, engine_db, auth)
        engine_db.isDeleted = True
        engine_db.updatedTime = get_current_unix()
        await save_to_db(db, engine_db)
        return None

    async def list(
        self, db: AsyncSession, page: int, queries: SearchQueries
    ) -> GetEngineListResponse:
        """エンジン一覧を取得します"""
        select_query = buildDatabaseQuery(EngineSave, queries)
        userPage: Page[EngineSave] = await paginate(
            db,
            select_query,
            Params(page=page + 1, size=20),
        )  # type: ignore
        resp: SonolusPage = toSonolusPage(userPage)
        await asyncio.gather(
            *[db_to_resp(db, r, queries.localization) for r in resp.items]
        )
        return GetEngineListResponse(
            pageCount=resp.pageCount if resp.pageCount > 0 else 1,
            items=resp.items,
            search=defaultSearch,
        )
