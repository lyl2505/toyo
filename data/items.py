from dataclass import dataclasses 

@dataclasses
class Category:
    name: str
    description: str
    section: dict

class Maki:
    name: str
    price: float
    topping: list
    top: list
    inside: list
    pieces: int
    special: str
    vegetarian: bool

class Item:
    name: str
    price: str
    description: str
    vegetarian: bool

class DinnerCombo:
    items: list
    price: float

class NigiriSushi:
    nigiri: dict

class Nigiri:
    name: str
    description: str