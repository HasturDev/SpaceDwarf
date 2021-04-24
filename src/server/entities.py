from dataclasses import dataclass

import numpy as np
from server.components import Location, Inside_Solar_System_Location, Inside_Planet_Location


@dataclass
class Planet:
    _id: int
    name: str
    x: int
    y: int
    is_there: bool
    slocation: Inside_Solar_System_Location


@dataclass
class Inside_Atmosphere_Location:
    _id: int
    name: str
    chance: int
    plocation: Inside_Planet_Location
    is_there: bool

    # Links
    planet_id: int


@dataclass
class Item:
    _id: int
    name: str
    weight: int
    size: int
    cost: int
    is_there: bool
    magic: bool

    # Links
    owner_id: int


@dataclass
class Character:
    _id: int
    name: str
    age: int
    height: int
    weight: int
    display_size: int  # inverse square for negative numbers, -2 is 1/2, 1 == -1 etc, 0 is invis
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int
    experience: int
    level: int
    is_true: bool
    magic: bool
    plocation: Inside_Planet_Location
    slocation: Inside_Solar_System_Location