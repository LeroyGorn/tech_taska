from pydantic import BaseModel


class UserGame(BaseModel):
    user_id: int
    game_id: int


class UserPlay(UserGame):
    pass


class GameBase(BaseModel):
    name: str


class GameCreate(GameBase):
    name: str


class Game(GameBase):
    id: int
    name: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    username: str
    age: int
    hashed_password: str


class User(UserBase):
    id: int
    username: str
    age: int
    email: str

    class Config:
        orm_mode = True


class UserInDB(User):
    hashed_password: str


class Player(User):
    games: list[Game]


class Team(Player):
    users: list[User]


class GameInfo(Game):
    users: list[User]


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
