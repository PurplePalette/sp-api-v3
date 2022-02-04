from dataclasses import dataclass
from typing import List
from src.config import (
    SKIN_VERSION,
    BACKGROUND_VERSION,
    EFFECT_VERSION,
    PARTICLE_VERSION,
    LEVEL_VERSION,
    ENGINE_VERSION,
)


@dataclass
class SRLBridge:
    locator_names: List[str]
    object_version: int


ENGINE_LOCATORS = ["thumbnail", "data", "configuration"]
BACKGROUND_LOCATORS = ["thumbnail", "data", "image", "configuration"]
EFFECT_LOCATORS = ["thumbnail", "data"]
LEVEL_LOCATORS = ["thumbnail", "data"]
PARTICLE_LOCATORS = ["thumbnail", "data"]
SKIN_LOCATORS = ["thumbnail", "data"]

BRIDGE_DICT = {
    "skin": SRLBridge(SKIN_LOCATORS, SKIN_VERSION),
    "engine": SRLBridge(ENGINE_LOCATORS, ENGINE_VERSION),
    "background": SRLBridge(BACKGROUND_LOCATORS, BACKGROUND_VERSION),
    "effect": SRLBridge(EFFECT_LOCATORS, EFFECT_VERSION),
    "level": SRLBridge(LEVEL_LOCATORS, LEVEL_VERSION),
    "particle": SRLBridge(PARTICLE_LOCATORS, PARTICLE_VERSION),
}