from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def show(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog not found with {id}"
        )
    return blog


def create(request, db: Session, user_id: int):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog not found with {id}"
        )
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return {"blog": f"blog {id} is Deleted"}


def update(id: int, request, db: Session):
    blogger = db.query(models.Blog).filter(models.Blog.id == id)
    if not blogger.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog not found with {id}"
        )
    # return request
    blogger.update(vars(request))
    db.commit()
    return {"blog": f"blog {id} is Updated Successfully"}
