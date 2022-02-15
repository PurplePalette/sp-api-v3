from dataclasses import dataclass
from typing import List


@dataclass
class SRLDefine:
    obj_name: str
    obj_version: int
    locators: List[str]


@dataclass
class SRLDict:
    background: SRLDefine
    effect: SRLDefine
    engine: SRLDefine
    level: SRLDefine
    particle: SRLDefine
    skin: SRLDefine


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
PARTICLE_LOCATORS = ["thumbnail", "data", "texture"]
SKIN_LOCATORS = ["thumbnail", "data"]


SRL_BRIDGES = SRLDict(
    SRLDefine("background", BACKGROUND_VERSION, BACKGROUND_LOCATORS),
    SRLDefine("effect", EFFECT_VERSION, EFFECT_LOCATORS),
    SRLDefine("engine", ENGINE_VERSION, ENGINE_LOCATORS),
    SRLDefine("level", LEVEL_VERSION, LEVEL_LOCATORS),
    SRLDefine("particle", PARTICLE_VERSION, PARTICLE_LOCATORS),
    SRLDefine("skin", SKIN_VERSION, SKIN_LOCATORS),
)
