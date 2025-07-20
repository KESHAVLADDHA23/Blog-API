from sqlalchemy.orm import Session
from ..import models,schemas
from fastapi import HTTPException,status

def get_blog(db:Session):
    blogs=db.query(models.Blog).all()    
    return blogs


def create(request:schemas.Blog,db:Session):
    new_Blog=models.Blog(title=request.title,body=request.body,user_id=request.user_id)
    db.add(new_Blog)
    db.commit()
    db.refresh(new_Blog)
    return new_Blog


def destroy(id,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not available")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'deleted'



def update(id,request:schemas.Blog,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not available")
    blog.update(request.model_dump())
    db.commit()
    return 'updated'


def show_one(id,db:Session):
    blogs=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} is not availabale")
    return blogs