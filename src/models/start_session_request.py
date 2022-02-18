# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class StartSessionRequest(BaseModel):
    """
    StartSessionRequest

        idToken: The idToken generated at frontend.
    """

    idToken: str

    @validator("idToken")
    def idToken_min_length(cls, value):
        assert len(value) >= 100
        return value

    @validator("idToken")
    def idToken_max_length(cls, value):
        assert len(value) <= 3000
        return value


StartSessionRequest.update_forward_refs()
