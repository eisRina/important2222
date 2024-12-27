from sqlalchemy import select
from database import UserOrm, new_session,DeckOrm, AccountOrm, PlayerOrm
from schemas import User, UserEntity,Deck, Player,Account


async def add_user(data: dict) -> int:
    async with new_session() as session:
        new_user = UserOrm(**data)
        session.add(new_user)
        await session.flush()
        await session.commit()
        return new_user.id
    

async def get_users():
   async with new_session() as session:
      query = select(UserOrm)
      result = await session.execute(query)
      user_models = result.scalars().all()
      return user_models
  

class UserRepository:
    @classmethod
    async def add_user(cls, user: User) -> int:
        async with new_session() as session:
            data = user.model_dump()
            new_user = UserOrm(**data)
            session.add(new_user)
            await session.flush()
            await session.commit()
            return new_user.id

    @classmethod
    async def get_users(cls) -> list[UserEntity]:
        async with new_session() as session:
            query = select(UserOrm)
            result = await session.execute(query)
            user_model = result.scalars().all()
            users = [UserEntity.model_validate(user_model) for user_model in user_model]
            return users
        
        

class AccountRepository:
    @classmethod
    async def add_account(cls, account: Account) -> int:
        async with new_session() as session:
            data = account.model_dump()
            new_account = AccountOrm(**data)
            session.add(new_account)
            await session.flush()
            await session.commit()
            return new_account.id

    @classmethod
    async def get_accounts(cls):
        async with new_session() as session:
            query = select(AccountOrm)
            result = await session.execute(query)
            return result.scalars().all()


class DeckRepository:
    @classmethod
    async def add_deck(cls, deck: Deck, owner_id: int) -> int:
        async with new_session() as session:
            new_deck = DeckOrm(name=deck.name, owner_id=owner_id)
            session.add(new_deck)
            await session.flush()
            await session.commit()
            return new_deck.id

    @classmethod
    async def get_decks(cls):
        async with new_session() as session:
            query = select(DeckOrm)
            result = await session.execute(query)
            return result.scalars().all()


from database import PlayerOrm, new_session
from schemas import Player

class PlayerRepository:
    @classmethod
    async def add_player(cls, player: Player, deck_id: int) -> int:
        async with new_session() as session:
            new_player = PlayerOrm(name=player.name, deck_id=deck_id)
            session.add(new_player)
            await session.flush()
            await session.commit()
            return new_player.id

    @classmethod
    async def get_players(cls):
        async with new_session() as session:
            query = select(PlayerOrm)
            result = await session.execute(query)
            return result.scalars().all()