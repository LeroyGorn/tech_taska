from sqlalchemy import Column, ForeignKey, Integer, String, Table, Boolean
from sqlalchemy.orm import validates, relationship

from .database import Base


users_games = Table('users_games', Base.metadata,
                    Column('user_id', ForeignKey('users.id'), primary_key=True),
                    Column('game_id', ForeignKey('games.id'), primary_key=True))


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    age = Column(Integer, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    games = relationship(
        "Game",
        secondary=users_games,
        backref="games")

    @validates('name')
    def validate_name(self, key, value):
        assert value != ''
        return value

    @validates('age')
    def validate_name(self, key, value):
        assert value >= 0
        assert value <= 100
        return value


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    users = relationship(
        "User",
        secondary=users_games,
        backref="users")

    @validates('name')
    def validate_name(self, key, value):
        assert value != ''
        return value
