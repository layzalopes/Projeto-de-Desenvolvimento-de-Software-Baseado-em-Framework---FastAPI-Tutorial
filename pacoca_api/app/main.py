from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

security = HTTPBasic()

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "aluno"
    correct_password = "123"
    
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

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
def read_pacoca(pacoca_id: int, db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(authenticate)):
    db_pacoca = crud.get_pacoca(db, pacoca_id=pacoca_id)
    if db_pacoca is None:
        raise HTTPException(status_code=404, detail="Paçoca not found")
    return db_pacoca

@app.post("/pacocas/", response_model=schemas.Pacoca)
def create_pacoca(pacoca: schemas.PacocaCreate, db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(authenticate)):
    return crud.create_pacoca(db=db, pacoca=pacoca)

@app.put("/pacocas/{pacoca_id}", response_model=schemas.Pacoca)
def update_pacoca(pacoca_id: int, pacoca: schemas.PacocaCreate, db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(authenticate)):
    return crud.update_pacoca(db=db, pacoca_id=pacoca_id, pacoca=pacoca)

@app.delete("/pacocas/{pacoca_id}", response_model=schemas.Pacoca)
def delete_pacoca(pacoca_id: int, db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(authenticate)):
    return crud.delete_pacoca(db=db, pacoca_id=pacoca_id)
