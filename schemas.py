from pydantic import BaseModel, ConfigDict
from typing import List, Optional

class User(BaseModel):
    username: str
    password: str
    

class UserEntity(User):
    id: int
    model_config = ConfigDict(from_attributes=True)
    

class Card_schemas(BaseModel):
    card_name: str
    card_mana: str

class Deck_schemas(BaseModel):
    card_list: Optional [List[Card_schemas] ] = []
    class Config:
        orm_mode = True

class Account(BaseModel):
    username: str
    password: str
    decks: Optional[List[Deck_schemas]] = []

    class Config:
        orm_mode = True

class PlayerSchema(BaseModel):
    name: str
    health_points: int = 20
    deck: Optional[Deck_schemas] = None
    mana_pool: Optional[List[int]] = []

    class Config:
        orm_mode = True
    
class Account(BaseModel):
    username: str
    password: str

class Deck(BaseModel):
    name: str

class Player(BaseModel):
    name: str
    health_points: Optional[int] = 20