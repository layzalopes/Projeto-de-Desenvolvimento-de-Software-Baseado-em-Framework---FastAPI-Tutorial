from .schemas import PacocaCreate
from sqlalchemy.orm import Session
from . import models, schemas

def get_pacoca(db: Session, pacoca_id: int):
    return db.query(models.Pacoca).filter(models.Pacoca.id == pacoca_id).first()

def create_pacoca(db: Session, pacoca: schemas.PacocaCreate):
    db_pacoca = models.Pacoca(**pacoca.dict())
    db.add(db_pacoca)
    db.commit()
    db.refresh(db_pacoca)
    return db_pacoca

def update_pacoca(db: Session, pacoca_id: int, pacoca: schemas.PacocaCreate):
    db_pacoca = db.query(models.Pacoca).filter(models.Pacoca.id == pacoca_id).first()
    if db_pacoca:
        for key, value in pacoca.dict().items():
            setattr(db_pacoca, key, value)
        db.commit()
        db.refresh(db_pacoca)
    return db_pacoca

def delete_pacoca(db: Session, pacoca_id: int):
    db_pacoca = db.query(models.Pacoca).filter(models.Pacoca.id == pacoca_id).first()
    if db_pacoca:
        db.delete(db_pacoca)
        db.commit()
    return db_pacoca
