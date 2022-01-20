# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from src.models.engine import Engine


class GetEngineListResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GetEngineListResponse - a model defined in OpenAPI

        page_count: The page_count of this GetEngineListResponse.
        items: The items of this GetEngineListResponse.
    """

    page_count: int
    items: List[Engine]

    @validator("page_count")
    def page_count_min(cls, value):
        assert value >= 1
        return value

GetEngineListResponse.update_forward_refs()
