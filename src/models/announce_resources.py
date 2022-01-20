# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class AnnounceResources(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AnnounceResources - a model defined in OpenAPI

        icon: The icon of this AnnounceResources [Optional].
        bgm: The bgm of this AnnounceResources [Optional].
        level: The level of this AnnounceResources [Optional].
    """

    icon: Optional[str] = None
    bgm: Optional[str] = None
    level: Optional[str] = None

AnnounceResources.update_forward_refs()
