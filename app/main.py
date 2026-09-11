from fastapi import FastAPI, HTTPException, Response, status

from app.database import products_db, categories_db
from app.schemas import (
    Product, ProductCreate, ProductUpdate,
    Category, CategoryCreate, CategoryUpdate,
)

app = FastAPI(
    title="Products & Categories API",
    description="API REST con dos recursos: productos y categorías",
    version="1.0.0",
)


# =====================================================
# ROOT + HEALTH
# =====================================================
@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"message": "Hello, World! api Functional!"}


@app.get("/health", status_code=status.HTTP_200_OK)
def health():
    return {"status": "healthy"}


# =====================================================
# ENDPOINTS DE PRODUCTOS
# =====================================================
@app.get("/products/", response_model=list[Product], status_code=status.HTTP_200_OK)
def get_products(
    category: str | None = None,
    available: bool | None = None,
    search: str | None = None,
):
    result = products_db

    if category is not None:
        result = [p for p in result if p["category"].lower() == category.lower()]

    if available is not None:
        result = [p for p in result if p["available"] == available]

    if search is not None:
        result = [
            p for p in result
            if search.lower() in p["name"].lower()
            or search.lower() in p["category"].lower()
        ]

    return result


@app.get("/products/{product_id}", response_model=Product, status_code=status.HTTP_200_OK)
def get_product_by_id(product_id: int):
    for product in products_db:
        if product["id"] == product_id:
            return product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product with id {product_id} not found",
    )


@app.post("/products/", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate):
    new_id = max((p["id"] for p in products_db), default=0) + 1

    new_product = {"id": new_id, **product.model_dump()}

    if new_product.get("available") is None:
        new_product["available"] = new_product["stock"] > 0

    products_db.append(new_product)
    return new_product


@app.patch("/products/{product_id}", response_model=Product, status_code=status.HTTP_200_OK)
def update_product(product_id: int, product_update: ProductUpdate):
    for index, product in enumerate(products_db):
        if product["id"] == product_id:
            update_data = product_update.model_dump(exclude_unset=True)
            updated = {**product, **update_data}

            if "stock" in update_data and "available" not in update_data:
                updated["available"] = updated["stock"] > 0

            products_db[index] = updated
            return updated

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product with id {product_id} not found",
    )


@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int):
    for index, product in enumerate(products_db):
        if product["id"] == product_id:
            products_db.pop(index)
            return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product with id {product_id} not found",
    )


# =====================================================
# ENDPOINTS DE CATEGORÍAS
# =====================================================
@app.get("/categories", response_model=list[Category], status_code=status.HTTP_200_OK)
def get_categories(
    active: bool | None = None,
    search: str | None = None,
):
    result = categories_db

    if active is not None:
        result = [c for c in result if c["active"] == active]

    if search is not None:
        result = [c for c in result if search.lower() in c["name"].lower()]

    return result


@app.get("/categories/{category_id}", response_model=Category, status_code=status.HTTP_200_OK)
def get_category(category_id: int):
    for category in categories_db:
        if category["id"] == category_id:
            return category

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Category with id {category_id} not found",
    )


@app.post("/categories", response_model=Category, status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate):
    new_id = max((c["id"] for c in categories_db), default=0) + 1

    new_category = {"id": new_id, **category.model_dump()}

    categories_db.append(new_category)
    return new_category


@app.patch("/categories/{category_id}", response_model=Category, status_code=status.HTTP_200_OK)
def update_category(category_id: int, category_update: CategoryUpdate):
    for index, category in enumerate(categories_db):
        if category["id"] == category_id:
            update_data = category_update.model_dump(exclude_unset=True)
            updated = {**category, **update_data}
            categories_db[index] = updated
            return updated

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Category with id {category_id} not found",
    )


@app.delete("/categories/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int):
    for index, category in enumerate(categories_db):
        if category["id"] == category_id:
            categories_db.pop(index)
            return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Category with id {category_id} not found",
    )