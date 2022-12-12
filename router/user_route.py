from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from database.config import conn
from database.model import User
from database.schema import UserSchema
from service.jwttoken import create_access_token
from service.oauth import get_current_user
from service.hashing import Hash

user = APIRouter()

@user.post("/register")
async def register(user: UserSchema):
    user.password = Hash.bcrypt(user.password)
    query = User.insert().values(Username=user.username,Password=user.password,Email=user.email)
    conn.execute(query)
    return {"status_code":"200","message": "User created successfully"}

@user.post("/login")
async def login(request: OAuth2PasswordRequestForm = Depends()):
    user = conn.execute(User.select().where(User.c.Username == request.username)).fetchone()
    if not user:
        raise HTTPException(status_code=404, detail=f"Invalid credentials")
    if not Hash.verify(user.Password, request.password):
        raise HTTPException(status_code=404, detail=f"Incorrect password")
    access_token = create_access_token(data={"username": user.Username, "email": user.Email})
    return {"access_token": access_token, "token_type": "bearer"}

@user.get("/user_verify_token")
async def verify_token(current_user:UserSchema = Depends(get_current_user)):
    return current_user

@user.get("/user")
async def get_user():
    query = User.select()
    return conn.execute(query).fetchall()

@user.get("/user/{id}")
async def get_user_by_id(id:int):
    query = User.select().where(User.c.id == id)
    return conn.execute(query).fetchone()

@user.put("/user/{id}")
async def update_user(id:int,user:UserSchema):
    query = User.update().where(User.c.id == id).values(Username=user.username,Email=user.email)
    conn.execute(query)
    return {"status_code":"200","message": "User updated successfully"}

@user.delete("/user/{id}")
async def delete_user(id:int):
    query = User.delete().where(User.c.id == id)
    conn.execute(query)
    return {"status_code":"200","message": "User deleted successfully"}