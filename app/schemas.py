from pydantic import BaseModel, Field


class CategoryCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=60)


class Category(CategoryCreate):
    id: int


class ProductCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=80)
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    category_id: int


class Product(ProductCreate):
    id: int


class ProductUpdate(ProductCreate):
    pass
