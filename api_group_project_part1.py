# https://zoo-animal-api.herokuapp.com/

from dataclasses import dataclass, field

@dataclass
class Mammal:
    name: str
    latin_name: str
    animal_type: str
    active_time: str
    length_min: float = field(metadata={"units":"feet"})
    length_max: float = field(metadata={"units":"feet"})
    weight_min: float = field(metadata={"units":"pounds"})
    weight_max: float = field(metadata={"units":"pounds"})
    lifespan: int = field(metadata={"units":"years"})
    habitat: str
    diet: str
    geo_range: str
    image_link: str
    id: int

@dataclass
class Reptile:
    name: str
    latin_name: str
    animal_type: str
    active_time: str
    length_min: float = field(metadata={"units":"feet"})
    length_max: float = field(metadata={"units":"feet"})
    weight_min: float = field(metadata={"units":"pounds"})
    weight_max: float = field(metadata={"units":"pounds"})
    lifespan: int = field(metadata={"units":"years"})
    habitat: str
    diet: str
    geo_range: str
    image_link: str
    id: int

@dataclass
class Bird:
    name: str
    latin_name: str
    animal_type: str
    active_time: str
    length_min: float = field(metadata={"units":"feet"})
    length_max: float = field(metadata={"units":"feet"})
    weight_min: float = field(metadata={"units":"pounds"})
    weight_max: float = field(metadata={"units":"pounds"})
    lifespan: int = field(metadata={"units":"years"})
    habitat: str
    diet: str
    geo_range: str
    image_link: str
    id: int

@dataclass
class Amphibian:
    name: str
    latin_name: str
    animal_type: str
    active_time: str
    length_min: float = field(metadata={"units":"feet"})
    length_max: float = field(metadata={"units":"feet"})
    weight_min: float = field(metadata={"units":"pounds"})
    weight_max: float = field(metadata={"units":"pounds"})
    lifespan: int = field(metadata={"units":"years"})
    habitat: str
    diet: str
    geo_range: str
    image_link: str
    id: int

@dataclass
class Fish:
    name: str
    latin_name: str
    animal_type: str
    active_time: str
    length_min: float = field(metadata={"units":"feet"})
    length_max: float = field(metadata={"units":"feet"})
    weight_min: float = field(metadata={"units":"pounds"})
    weight_max: float = field(metadata={"units":"pounds"})
    lifespan: int = field(metadata={"units":"years"})
    habitat: str
    diet: str
    geo_range: str
    image_link: str
    id: int