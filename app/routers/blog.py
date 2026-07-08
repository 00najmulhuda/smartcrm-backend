from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from app.database import get_session
from app.dependencies import get_current_user, require_role
from app.models.category import Category
from app.schemas.blogpostschemas import BlogPostRead, BlogPostCreate, BlogPostUpdate
from app.models.blog_post import BlogPost
from app.schemas.categoryschemas import CategoryCreate, CategoryRead


router = APIRouter(
    prefix="/blog",
    tags=["Blog"]
)

@router.post("/categories", response_model= CategoryRead)
def create_category(
    category: CategoryCreate, 
    session:Session = Depends(get_session),
    current_user = Depends(require_role("admin"))
): 
   check_categ_name = session.exec(
    select(Category)
    .where(Category.name == category.name)
   ).first()

   if check_categ_name:
    raise HTTPException(status_code=409, detail="already exist")

   db_category = Category(
    name = category.name
   )
   session.add(db_category)
   session.commit()
   session.refresh(db_category)

   return db_category


@router.get("/categories", response_model=list[CategoryRead])
def get_all_categories(session:Session = Depends(get_session)):
    all_categories = session.exec(select(Category)).all()
    return all_categories

    
@router.put("/categories/{category_id}", response_model=CategoryRead)
def update_category(
    category_id : int,
    category:CategoryCreate,
    session:Session = Depends(get_session),
    current_user = Depends(require_role("admin"))
):
   db_category = session.get(Category, category_id)
   if not db_category:
    raise HTTPException(
        status_code=404, detail = "category not found"
    )
   
   check_categ = session.exec(
    select(Category)
    .where(Category.name == category.name)
   ).first()
   if check_categ and check_categ.id != category.id:
    raise HTTPException(
        status_code=409, detail="already exist"
    )
   db_category.name = category.name

   session.add(db_category)
   session.commit()
   session.refresh(db_category)

   return db_category
   

@router.delete("/categories/{category_id}")
def delete_categ(
    category_id:int,
    session:Session = Depends(get_session),
    current_user = Depends(require_role("admin"))
):
   db_category = session.get(Category, category_id)
   if not db_category:
    raise HTTPException(
        status_code=404, detail = "category not found"
    )

   session.delete(db_category)
   session.commit()
   return {
    "message": "category delete successful "
   }


#BLOG POST ---------------------------------------------------------------------
@router.post("/blogs", response_model=BlogPostRead)
def create_blog(
    blog : BlogPostCreate,
    session:Session = Depends(get_session),
    current_user = Depends(get_current_user)
):
   category = session.get(Category, blog.category_id)
   if not category:
    raise HTTPException(
        status_code=404,
        detail="category not found"
     )

   db_blog = BlogPost(
        title = blog.title,
        content=blog.content,
        category_id=blog.category_id,
        image_url=blog.image_url,
        user_id=current_user.id
   )

   session.add(db_blog)
   session.commit()
   session.refresh(db_blog)

   return db_blog


@router.get("/blogs",response_model=list[BlogPostRead])
def get_all_blogs(session:Session = Depends(get_session)):
    all_blogs = session.exec(select(BlogPost)).all()
    return all_blogs

@router.get("/blogs/{blog_id}", response_model=BlogPostRead)
def get_blog(blog_id: int, session:Session = Depends(get_session)):
    blogBy_id = session.get(BlogPost,blog_id)
    if not blogBy_id:
        raise HTTPException(status_code=404, detail="id not found")
    return blogBy_id


@router.put("/blogs/{blog_id}", response_model=BlogPostRead)
def update_blog(
    blog_id:int, 
    blog:BlogPostUpdate,
    session:Session = Depends(get_session),
    current_user = Depends(get_current_user)
):
   db_blog = session.get(BlogPost, blog_id)
   if not db_blog:
    raise HTTPException(status_code=404, detail="id not found")
   
   if db_blog.user_id != current_user.id and current_user.role != "admin":
    raise HTTPException(status_code=403,detail="access denied")

   if blog.title:
    check_blog = session.exec(
        select(BlogPost)
        .where(BlogPost.title == blog.title)
        .where(BlogPost.id != blog_id)
    ).first()

    if check_blog:
        raise HTTPException(status_code=409, detail="blog title already exist")
   
   if blog.category_id is not None:
    category = session.get(Category, blog.category_id)
    if not category:
        raise HTTPException(status_code=404, detail="category not found")
    db_blog.category_id = blog.category_id


   if blog.title is not None:
    db_blog.title = blog.title

   if blog.content is not None:
    db_blog.content = blog.content

   if blog.status is not None:
    db_blog.status = blog.status

   if blog.image_url is not None:
    db_blog.image_url = blog.image_url

   session.commit()
   session.refresh(db_blog)

   return db_blog


@router.delete("/blogs/{blog_id}")
def delete_blog(
    blog_id:int,
    session:Session = Depends(get_session),
    current_user = Depends(get_current_user)
):
   db_blog = session.get(BlogPost, blog_id)
   if not db_blog:
    raise HTTPException(
        status_code=404, detail="blog not found"
    )
   
   if db_blog.user_id != current_user.id and current_user.role != "admin":
    raise HTTPException(status_code=403, detail="access denied")

   session.delete(db_blog)
   session.commit()
 
   return{
    "message": "blog delete successfully"
   }


