from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Paçoca API"}

@app.get("/pacocas/{pacoca_id}", response_model=schemas.Pacoca)
def read_pacoca(pacoca_id: int, db: Session = Depends(get_db)):
    db_pacoca = crud.get_pacoca(db, pacoca_id=pacoca_id)
    if db_pacoca is None:
        raise HTTPException(status_code=404, detail="Paçoca not found")
    return db_pacoca

@app.post("/pacocas/", response_model=schemas.Pacoca)
def create_pacoca(pacoca: schemas.PacocaCreate, db: Session = Depends(get_db)):
    return crud.create_pacoca(db=db, pacoca=pacoca)

@app.put("/pacocas/{pacoca_id}", response_model=schemas.Pacoca)
def update_pacoca(pacoca_id: int, pacoca: schemas.PacocaCreate, db: Session = Depends(get_db)):
    return crud.update_pacoca(db=db, pacoca_id=pacoca_id, pacoca=pacoca)

@app.delete("/pacocas/{pacoca_id}", response_model=schemas.Pacoca)
def delete_pacoca(pacoca_id: int, db: Session = Depends(get_db)):
    return crud.delete_pacoca(db=db, pacoca_id=pacoca_id)
