# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from src.models.skin import Skin


class GetSkinResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GetSkinResponse - a model defined in OpenAPI

        item: The item of this GetSkinResponse.
        description: The description of this GetSkinResponse.
        recommended: The recommended of this GetSkinResponse.
    """

    item: Skin
    description: str
    recommended: List[Skin]

    @validator("description")
    def description_min_length(cls, value):
        assert len(value) >= 1
        return value

GetSkinResponse.update_forward_refs()
