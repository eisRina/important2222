from datetime import datetime
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column,relationship
from typing import List
from sqlalchemy import ForeignKey, Table,Column, Integer, String

engine = create_async_engine("sqlite+aiosqlite:///rnh.db")
new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass

class UserOrm(Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]
    
class DeckOrm(Model):
    __tablename__ = "decks"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] 
    id_player: Mapped[int] = mapped_column(ForeignKey("users.id"))
    cards: Mapped[str] = mapped_column(String)
    
    owner = relationship("UserOrm", back_populates="decks")

class AccountOrm(Model):
    tablename = "accounts"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]
    decks: Mapped[List["DeckOrm"]] = relationship("DeckOrm", back_populates="owner")


class PlayerOrm(Model):
    tablename = "players"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    health_points: Mapped[int] = mapped_column(default=20)
    deck_id: Mapped[int] = mapped_column(ForeignKey("decks.id"))

    deck = relationship("DeckOrm")
    
           
async def create_tables():
   async with engine.begin() as conn:
       await conn.run_sync(Model.metadata.create_all)

async def delete_tables():
   async with engine.begin() as conn:
       await conn.run_sync(Model.metadata.drop_all)