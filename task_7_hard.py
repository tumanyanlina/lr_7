from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from pydantic import BaseModel

app = FastAPI()
Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String)

engine = create_engine('sqlite:///fastapi.db', connect_args={"check_same_thread": False})
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

class ItemCreate(BaseModel):
    name: str 
@app.get("/items")
def get_items():
    session = Session()
    try:
        items = session.query(Item).all()
        return items
    finally:
        session.close()  

@app.post("/items")
def create_item(item: ItemCreate):
    session = Session()
    try:
        new_item = Item(name=item.name)
        session.add(new_item)
        session.commit()
        session.refresh(new_item)
        return new_item
    finally:
        session.close()

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    session = Session()
    try:
        item = session.query(Item).filter(Item.id == item_id).first()
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        session.delete(item)
        session.commit()
        return {"message": "Item deleted"}
    finally:
        session.close()