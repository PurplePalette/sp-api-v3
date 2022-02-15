from dataclasses import dataclass
from typing import List


@dataclass
class SRL:
    obj_name: str
    obj_version: int
    locators: List[str]


@dataclass
class SRLDict:
    background: SRL
    effect: SRL
    engine: SRL
    level: SRL
    particle: SRL
    skin: SRL


SKIN_VERSION = 2
ENGINE_VERSION = 4
BACKGROUND_VERSION = 2
EFFECT_VERSION = 2
LEVEL_VERSION = 1
PARTICLE_VERSION = 1

ENGINE_LOCATORS = ["thumbnail", "data", "configuration"]
BACKGROUND_LOCATORS = ["thumbnail", "data", "image", "configuration"]
EFFECT_LOCATORS = ["thumbnail", "data"]
LEVEL_LOCATORS = ["thumbnail", "data"]
PARTICLE_LOCATORS = ["thumbnail", "data"]
SKIN_LOCATORS = ["thumbnail", "data"]


BRIDGE_DICT = SRLDict(
    SRL("background", BACKGROUND_VERSION, BACKGROUND_LOCATORS),
    SRL("effect", EFFECT_VERSION, EFFECT_LOCATORS),
    SRL("engine", ENGINE_VERSION, ENGINE_LOCATORS),
    SRL("level", LEVEL_VERSION, LEVEL_LOCATORS),
    SRL("particle", PARTICLE_VERSION, PARTICLE_LOCATORS),
    SRL("skin", SKIN_VERSION, SKIN_LOCATORS),
)
