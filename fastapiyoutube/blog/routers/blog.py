from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas
from ..database import get_db
from .. import models
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"],
)


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ShowBlog,
)
def show(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog not found with {id}"
        )
    return blog


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.blog, db: Session = Depends(get_db), user_id: int = 1):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.get("/", tags=["Blogs"])
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@router.delete("/{id}", status_code=status.HTTP_202_ACCEPTED)
def destroy(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog not found with {id}"
        )
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return {"blog": f"blog {id} is Deleted"}


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.blog, db: Session = Depends(get_db)):
    blogger = db.query(models.Blog).filter(models.Blog.id == id)
    if not blogger.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog not found with {id}"
        )
    # return request
    blogger.update(vars(request))
    db.commit()
    return {"blog": f"blog {id} is Updated Successfully"}
