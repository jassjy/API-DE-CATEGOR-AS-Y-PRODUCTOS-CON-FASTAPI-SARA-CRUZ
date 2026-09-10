from pydantic import BaseModel, Field


# =====================================================
# SCHEMAS DE PRODUCTOS
# =====================================================
class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, json_schema_extra={"example": "Product Name"})
    category: str = Field(..., min_length=2, max_length=100, json_schema_extra={"example": "Category Name"})
    price: float = Field(..., gt=0, json_schema_extra={"example": 19.99})
    stock: int = Field(..., ge=0, json_schema_extra={"example": 100})
    available: bool | None = None


class Product(ProductCreate):
    id: int


class ProductUpdate(BaseModel):
    name: str | None = Field(None, min_length=2, max_length=100)
    category: str | None = Field(None, min_length=2, max_length=100)
    price: float | None = Field(None, gt=0)
    stock: int | None = Field(None, ge=0)
    available: bool | None = None


# =====================================================
# SCHEMAS DE CATEGORÍAS
# =====================================================
class CategoryCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, json_schema_extra={"example": "Computadores"})
    description: str | None = Field(None, max_length=200, json_schema_extra={"example": "Equipos de cómputo"})
    active: bool = Field(default=True, json_schema_extra={"example": True})


class Category(CategoryCreate):
    id: int


class CategoryUpdate(BaseModel):
    name: str | None = Field(None, min_length=3, max_length=50)
    description: str | None = Field(None, max_length=200)
    active: bool | None = None