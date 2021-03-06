from fastapi import APIRouter, Depends, status
from .. import schemas
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import blog
from ..oauth2 import get_current_user

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"],
)


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ShowBlog,
)
def show(
    id,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    return blog.show(db, id)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(
    request: schemas.blog,
    db: Session = Depends(get_db),
    user_id: int = 1,
    current_user: schemas.User = Depends(get_current_user),
):
    return blog.create(request, db, user_id)


@router.get("/", tags=["Blogs"])
def all(
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    return blog.get_all(db)


@router.delete("/{id}", status_code=status.HTTP_202_ACCEPTED)
def destroy(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    return blog.destroy(db, id)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(
    id: int,
    request: schemas.blog,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    return blog.update(id, request, db)
