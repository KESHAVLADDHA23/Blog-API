from fastapi import APIRouter,Depends,HTTPException,status
from ..import schemas,models,hashing
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import user

router=APIRouter(
    prefix='/user',
    tags=['User']
)

@router.post("/")
def create_user(request:schemas.User,db:Session=Depends(get_db),):
   return user.create(request,db)


@router.get("/{id}",response_model=schemas.ShowUser)
def get_user(id:int,db:Session=Depends(get_db)):
   return user.show(id,db)
