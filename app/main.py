from fastapi import FastAPI, HTTPException, Response, status

from app.database import categories_db, products_db
from app.schemas import Category, CategoryCreate, Product, ProductCreate, ProductUpdate

app = FastAPI(
    title="TechStore Products & Categories API",
    description="API de auditoría funcional para categorías y productos",
    version="1.0.0",
)


def _category_exists(category_id: int) -> bool:
    return any(category["id"] == category_id for category in categories_db)


def _ensure_category_exists(category_id: int) -> None:
    if not _category_exists(category_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category with id {category_id} not found",
        )


@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"message": "TechStore API is running"}


@app.get("/health", status_code=status.HTTP_200_OK)
def health():
    return {"status": "healthy"}


@app.post("/categories", response_model=Category, status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate):
    if any(existing["name"].casefold() == category.name.casefold() for existing in categories_db):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Category name already exists")
    new_category = {"id": max((item["id"] for item in categories_db), default=0) + 1, **category.model_dump()}
    categories_db.append(new_category)
    return new_category


@app.get("/categories", response_model=list[Category], status_code=status.HTTP_200_OK)
def list_categories(search: str | None = None):
    if search is None:
        return categories_db
    return [category for category in categories_db if search.casefold() in category["name"].casefold()]


@app.get("/categories/{category_id}", response_model=Category, status_code=status.HTTP_200_OK)
def get_category(category_id: int):
    for category in categories_db:
        if category["id"] == category_id:
            return category
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category with id {category_id} not found")


@app.post("/products", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate):
    _ensure_category_exists(product.category_id)
    new_product = {"id": max((item["id"] for item in products_db), default=0) + 1, **product.model_dump()}
    products_db.append(new_product)
    return new_product


@app.get("/products", response_model=list[Product], status_code=status.HTTP_200_OK)
def list_products(category_id: int | None = None):
    if category_id is None:
        return products_db
    return [product for product in products_db if product["category_id"] == category_id]


@app.get("/products/{product_id}", response_model=Product, status_code=status.HTTP_200_OK)
def get_product(product_id: int):
    for product in products_db:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {product_id} not found")


@app.put("/products/{product_id}", response_model=Product, status_code=status.HTTP_200_OK)
def update_product(product_id: int, product_update: ProductUpdate):
    _ensure_category_exists(product_update.category_id)
    for index, product in enumerate(products_db):
        if product["id"] == product_id:
            updated = {"id": product_id, **product_update.model_dump()}
            products_db[index] = updated
            return updated
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {product_id} not found")


@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int):
    for index, product in enumerate(products_db):
        if product["id"] == product_id:
            products_db.pop(index)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {product_id} not found")
