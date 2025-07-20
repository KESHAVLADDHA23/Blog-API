from fastapi import APIRouter,Depends,status,Response,HTTPException
from typing import List
from ..database import get_db
from ..import schemas,models
from sqlalchemy.orm import Session
from ..repository import blog
from ..import oauth2
router=APIRouter(
    prefix='/blog',
    tags=['blogs']
)

@router.get("/",response_model=List[schemas.ShowBlog])
def all(db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.get_blog(db)


@router.post("/",status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.create(request,db)



@router.get("/{id}",status_code=200,response_model=schemas.ShowBlog)
def show(id,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.show_one(id,db)



@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
   return blog.destroy(id,db)



@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def update_blog(id,request:schemas.Blog,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)

