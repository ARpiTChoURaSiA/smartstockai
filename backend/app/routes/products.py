from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..schemas.product import ProductCreate, ProductRead
from ..database import get_db
from sqlalchemy.orm import Session
from ..models.product import Product as ProductModel

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", response_model=List[ProductRead])
def list_products(db: Session = Depends(get_db)):
    """Return all products."""
    items = db.query(ProductModel).all()
    return items

@router.post("/", response_model=ProductRead)
def create_product(payload: ProductCreate, db: Session = Depends(get_db)):
    """Create a new product in DB."""
    db_obj = ProductModel(**payload.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

@router.get("/{product_id}", response_model=ProductRead)
def get_product(product_id: int, db: Session = Depends(get_db)):
    """Get a product by ID."""
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.delete("/{product_id}", status_code=200)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """Delete a product by ID."""
    try:
        product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail=f"Product with id {product_id} not found")
        
        db.delete(product)
        db.commit()
        return {"message": f"Product {product_id} deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
