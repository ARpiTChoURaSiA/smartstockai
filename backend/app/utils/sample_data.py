from sqlalchemy.orm import Session
from ..models.product import Product
from ..database import get_db, engine
import random

sample_products = [
    {
        "name": "Laptop",
        "description": "High-performance laptop with SSD",
        "price": 999.99,
        "sku": "LAP001",
        "quantity": 15
    },
    {
        "name": "Smartphone",
        "description": "Latest model with 5G support",
        "price": 699.99,
        "sku": "PHN002",
        "quantity": 25
    },
    {
        "name": "Wireless Headphones",
        "description": "Noise-cancelling Bluetooth headphones",
        "price": 199.99,
        "sku": "AUD003",
        "quantity": 30
    },
    {
        "name": "Gaming Mouse",
        "description": "RGB gaming mouse with programmable buttons",
        "price": 79.99,
        "sku": "MOU004",
        "quantity": 40
    },
    {
        "name": "Mechanical Keyboard",
        "description": "RGB mechanical keyboard with blue switches",
        "price": 129.99,
        "sku": "KEY005",
        "quantity": 20
    },
    {
        "name": "4K Monitor",
        "description": "32-inch 4K HDR display",
        "price": 399.99,
        "sku": "MON006",
        "quantity": 10
    },
    {
        "name": "Wireless Charger",
        "description": "Fast wireless charging pad",
        "price": 29.99,
        "sku": "CHG007",
        "quantity": 50
    },
    {
        "name": "USB-C Hub",
        "description": "7-in-1 USB-C hub with HDMI",
        "price": 49.99,
        "sku": "HUB008",
        "quantity": 35
    },
    {
        "name": "External SSD",
        "description": "1TB portable SSD with USB 3.2",
        "price": 159.99,
        "sku": "SSD009",
        "quantity": 25
    },
    {
        "name": "Webcam",
        "description": "1080p webcam with microphone",
        "price": 89.99,
        "sku": "CAM010",
        "quantity": 45
    }
]

def add_sample_products(db: Session):
    """Add sample products to the database."""
    for product_data in sample_products:
        # Check if product with this SKU already exists
        existing = db.query(Product).filter(Product.sku == product_data["sku"]).first()
        if not existing:
            product = Product(**product_data)
            db.add(product)
    
    db.commit()
    return len(sample_products)

def main():
    """Main function to add sample data."""
    db = next(get_db())
    try:
        count = add_sample_products(db)
        print(f"Successfully added {count} sample products")
    except Exception as e:
        print(f"Error adding sample data: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main()