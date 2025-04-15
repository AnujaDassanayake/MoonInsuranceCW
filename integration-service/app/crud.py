from sqlalchemy.orm import Session
from . import models, schemas

def create_sale(db: Session, sale: schemas.SaleCreate):
    db_sale = models.Sale(
        agent_code=sale.agent_code,
        product_name=sale.product_name,
        sale_amount=sale.sale_amount
    )
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale

# New function to fetch all sales records
def get_sales(db: Session):
    return db.query(models.Sale).all()
