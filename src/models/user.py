from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr


class UserIn(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    username: str



class UserInDB(BaseModel):
    username: str
    hashed_password: str
    full_name: str | None = None

    password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def ged_hashed_password(self, password: str) -> str:
        return password_context.hash(password)
