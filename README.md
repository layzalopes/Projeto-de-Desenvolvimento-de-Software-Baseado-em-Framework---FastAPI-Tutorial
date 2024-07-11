![logo](https://github.com/lyzlopess/Projeto-de-Desenvolvimento-de-Software-Baseado-em-Framework---FastAPI-Tutorial/assets/112975441/6a77ad02-c244-4ad7-b130-333a383a525e)

# Tutorial FastAPI
Este repositório contém o projeto desenvolvido para a disciplina "Desenvolvimento de Software Baseado em Framework". O foco principal é fornecer um tutorial abrangente sobre a criação de APIs web utilizando o framework FastAPI em Python, integrado com Docker para facilitar a configuração e o gerenciamento do ambiente de desenvolvimento.

# Sobre o FastAPI
FastAPI é um framework moderno, rápido (de alta performance) para a construção de APIs web com Python 3.7+ baseado em padrões, como tipo de dicas, para validar automaticamente os dados e gerar documentação interativa das APIs. Ele foi projetado para ser fácil de usar e desenvolver, com o objetivo de oferecer uma experiência rápida e eficiente tanto para os desenvolvedores quanto para os usuários finais.

![logoo](https://github.com/lyzlopess/Projeto-de-Desenvolvimento-de-Software-Baseado-em-Framework---FastAPI-Tutorial/assets/112975441/de330529-52fe-4014-856d-ee6a71796d9b)
# Integração com Docker
Docker é uma plataforma que permite aos desenvolvedores automatizar a implantação de aplicativos dentro de contêineres, que são unidades leves e portáteis de software. Usando Docker, podemos garantir que o ambiente de desenvolvimento seja consistente e replicável, independentemente do sistema operacional ou das configurações do desenvolvedor.

# Usando o Insomnia

O Insomnia é uma ferramenta poderosa para testar APIs de forma eficiente e intuitiva. Ele permite enviar solicitações HTTP para endpoints específicos da sua API e visualizar as respostas retornadas. 

# Objetivos do Projeto
- Demonstrar como criar e configurar um projeto FastAPI.
- Ensinar como criar endpoints para diferentes operações HTTP (GET, POST, PUT, DELETE).
- Integrar o projeto FastAPI com Docker para facilitar o desenvolvimento e a implantação.
- Fornecer exemplos práticos e tutoriais passo a passo para ajudar os desenvolvedores a entender e implementar suas próprias APIs.

# Passo a Passo
1. **Instalar Dependências**
   
   - Certifique-se de ter o Python 3.7+ e o Docker instalados na sua máquina.
   - Instale o FastAPI e o Uvicorn:

```bash
pip install fastapi uvicorn
```
2. **Clonando o Projeto do GitHub**
   
   Localize e clique no botão "Code"
   - No repositório do tutorial FastAPI, você verá um botão verde ou cinza com a palavra "Code" no topo da página, próximo ao botão "Go to file".
   - Clique nesse botão.
   - Após clicar no botão "Code", uma caixa de diálogo aparecerá com diferentes opções para clonar o repositório.
   - Certifique-se de que a opção "HTTPS" está selecionada.
   - Clique no ícone de cópia (um pequeno botão com um ícone de prancheta) ao lado da URL para copiar o endereço do repositório.
   - Abra o terminal ou prompt de comando clicando com o botão direito do mouse na área de trabalho e selecionando a opção "Abrir no Terminal"
   - Executar o seguinte comando:
```bash
git clone https://github.com/layzalopes/Projeto-de-Desenvolvimento-de-Software-Baseado-em-Framework---FastAPI-Tutorial.git
```

3. **Construindo e Executando com Docker**
   
   - Dentro do VisualStudio clicar em "View" localizado na parte superior.
   - Selecionar a opção "Terminal" para abrir o terminal já dentro do diretório.
   - Executar o comando para **contruir a Imagem do Docker**.
```bash
docker build -t pacoca_api .
```
   - Executar o comando para o executar o Contêiner Docker.
```bash
docker run -d -p 80:80 pacoca_api
```

4. **Baixando o Insomnia**
   
   - Acesse o Site Oficial https://insomnia.rest/download
   - Na página inicial, clique no botão “Download” ou “Get Started”.
   - Na página de download, escolha a versão correspondente ao seu sistema operacional (Windows, macOS, Linux).
   - **Windows:** Execute o arquivo .exe baixado e siga as instruções na tela.
   - **macOS:** Abra o arquivo .dmg baixado e arraste o ícone do Insomnia para a pasta “Aplicativos”.
   - **Linux:** As instruções podem variar dependendo da distribuição, mas geralmente incluem comandos para baixar e instalar o pacote usando o terminal. As instruções específicas estarão na página de download.

Assim que o Insomnia for instalado crie uma conta para poder usar mais recursos da ferramenta, como por exemplo **importar os requests**
  
5. **Importar Requests**
   
   - Clique no botão "Run In Insomnia" localizado logo abaixo. Isso pode abrir automaticamente o aplicativo Insomnia no seu computador, se estiver instalado, e importar os requests diretamente.
   - Se o Insomnia não abrir automaticamente, ele pode solicitar que você confirme a importação dos requests.
   - Depois de importar, verifique no painel esquerdo do Insomnia para encontrar a nova coleção de requests importada.
   - Clique na coleção para expandir e ver todos os requests dentro dela. Você pode então clicar em cada request para ver os detalhes, como método HTTP, URL e corpo da requisição.

[![Run in Insomnia}](https://insomnia.rest/images/run.svg)](https://insomnia.rest/run/?label=Pa%C3%A7oca%20API&uri=https%3A%2F%2Fgithub.com%2Flayzalopes%2FProjeto-de-Desenvolvimento-de-Software-Baseado-em-Framework---FastAPI-Tutorial%2Fblob%2Fmain%2FInsomnia_2024-07-10.json)

Caso não consiga fazer a importação, siga os próximos passos.

6. **Criar o Request POST**

   - Após a instalação, abra o Insomnia.
   - Você verá uma interface onde pode criar e gerenciar suas requisições.
   - Clique no botão "+ New Request".
   - Nomeie o request como "Create Paçoca".
   - Selecione o método HTTP "POST".
   - Clique em "Create".
  
   - Defina a URL para http://localhost:80/pacocas

7. **Adicionar Autenticação**

   - Clique na aba "Auth" na barra de navegação do request.
   - Selecione "Basic" no menu suspenso.
   - Insira o username 'aluno' e password '123'

8. **Adicionar o corpo**

   - Clique na aba "Body" na barra de navegação do request.
   - Selecione "JSON".
   - Adicione o corpo JSON com os dados da paçoca.
```bash
{
  "name": "Paçoca Tradicional",
  "description": "Deliciosa paçoca",
  "price": 5.99
}
```
   - Clique no botão "Send" para enviar a requisição.
   - Verifique a resposta para confirmar que a paçoca foi criada com sucesso e o ID que foi gerado.

9. **Criar Request GET**

   - Clique no botão "+ New Request".
   - Nomeie o request como "Get Paçoca".
   - Selecione o método HTTP "GET".
   - Clique em "Create".
  
   - Defina a URL para http://localhost:80/pacocas/{pacoca_id}.
   - Certifique-se de substituir {pacoca_id} pelo ID real da paçoca que deseja **buscar**.

10. **Adicionar Autenticação**

   - Clique na aba "Auth" na barra de navegação do request.
   - Selecione "Basic" no menu suspenso.
   - Insira o username 'aluno' e password '123'
   - Clique no botão "Send" para enviar a requisição.
   - Verifique a resposta para confirmar que a paçoca foi buscada com sucesso.

11. **Criar o Request PUT**

   - Clique no botão "+ New Request".
   - Nomeie o request como "Update Paçoca".
   - Selecione o método HTTP "PUT".
   - Clique em "Create".
  
   - No campo URL, insira o endpoint completo da API para atualização de paçoca, por exemplo: http://localhost:80/pacocas/{pacoca_id}.
   - Certifique-se de substituir {pacoca_id} pelo ID real da paçoca que deseja atualizar.

12. **Adicionar Autenticação**

   - Clique na aba "Auth" na barra de navegação do request.
   - Selecione "Basic" no menu suspenso.
   - Insira o username 'aluno' e password '123'

13. **Adicionar o corpo**

   - Clique na aba "Body" na barra de navegação do request.
   - Selecione "JSON".
   - Adicione o corpo JSON com os dados atualizados da paçoca.
```bash
  {
  "name": "Nova Paçoca",
  "description": "Descrição atualizada da paçoca",
  "price": 7.99
}
```
   - Clique no botão "Send" para enviar a requisição.
   - Verifique a resposta para confirmar que a paçoca foi atualizada com sucesso.

14. **Criar o Request DELETE**

   - Clique no botão "+ New Request".
   - Nomeie o request como "Delete Paçoca".
   - Selecione o método HTTP "DELETE".
   - Clique em "Create".
  
   - No campo URL, insira o endpoint completo da API para deletar alguma paçoca que foi criada, por exemplo: http://localhost:80/pacocas/{pacoca_id}.
   - Certifique-se de substituir {pacoca_id} pelo ID real da paçoca que deseja deletar.

15. **Adicionar Autenticação**

   - Clique na aba "Auth" na barra de navegação do request.
   - Selecione "Basic" no menu suspenso.
   - Insira o username 'aluno' e password '123'
   - Clique no botão "Send" para enviar a requisição.
   - Verifique a resposta para confirmar que a paçoca foi apagada com sucesso.
```
{
	"detail": "Paçoca not found"
}
```
# Sobre o código
1 . **database.py**
- Importa o sqlalchemy, para criação da fábrica de sessões, definição da URL do banco de dados, criação da engine, configuração com a fábrica de sessões e criação da classe Base:
```bash
{
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
}
```
Cria a engine de conexão com o banco de dados, passa a url e parâmetro thread, para permitir múltiplos acessos ao banco de dados. Importa o sqlalchemy, para criação da fábrica de sessões e configura a sessão local para não fazer commit ou flush automaticamente. Cria uma classe base, todos modelos são definidos no sqlalchemy que herda dessa classe.


2. **models.py**
- Realiza a definição dos atributos da classe paçoca herdando da classe Base, mapeando para a  tabela chamada “pacocas” no banco de dados.
```bash
{from sqlalchemy import Column, Integer, String, Float
from .database import Base


class Pacoca(Base):
    __tablename__ = "pacocas"


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float, index=True)
}
```

3. **schemas.py**
- Definição de modelos de dados relacionados à entidade "Paçoca", estabelece estruturas de dados para representar e validar informações na aplicação. 

- Importa BaseModel:
```bash
{
from pydantic import BaseModel
}
```
- Indica atributos básicos do produto no schema de dados:
```bash
{class PacocaBase(BaseModel):
    name: str
    description: str
    price: float
}
```
- Herda de PacocaBase, usada para criação de novos objetos:
```bash
{
class PacocaCreate(PacocaBase):
    pass
}
```
- Herda de PacocaBase e aciona o produto ID, usado para representar uma instância de completa de paçoca:
```bash
{
class Pacoca(PacocaBase):
    id: int


    class Config:
        from_attributes = True
}
```
Config: configuração para facilitar a conversão de objetos no sqlalchemy.

4. **crud.py**
- Faz a definição das funções crud (create, read, update, delete).
```bash
{from .schemas import PacocaCreate
from sqlalchemy.orm import Session
from . import models, schemas
}
```
Usa os modelos para consultar e manipular os registros no banco de dados e os schemas para criar e atualizar os registros.

- Define a função get para consultar a tabela e obter um registro referente ao id fornecido:
```bash
{def get_pacoca(db: Session, pacoca_id: int):
    return db.query(models.Pacoca).filter(models.Pacoca.id == pacoca_id).first()
}
```
- Cria um novo registro, usando os dados fornecidos pelo usuário:
```bash
{def create_pacoca(db: Session, pacoca: schemas.PacocaCreate):
    db_pacoca = models.Pacoca(**pacoca.dict())
    db.add(db_pacoca)
    db.commit()
    db.refresh(db_pacoca)
    return db_pacoca
}
```
- Atualiza o registro existente na tabela com base no id e nos novos dados, faz um commit e atualiza os objetos:
```bash
{def update_pacoca(db: Session, pacoca_id: int, pacoca: schemas.PacocaCreate):
    db_pacoca = db.query(models.Pacoca).filter(models.Pacoca.id == pacoca_id).first()
    if db_pacoca:
        for key, value in pacoca.dict().items():
            setattr(db_pacoca, key, value)
        db.commit()
        db.refresh(db_pacoca)
    return db_pacoca
}
```
- Deleta um registro existente com base no registro informado:
```bash
{def delete_pacoca(db: Session, pacoca_id: int):
    db_pacoca = db.query(models.Pacoca).filter(models.Pacoca.id == pacoca_id).first()
    if db_pacoca:
        db.delete(db_pacoca)
        db.commit()
    return db_pacoca
}
```



5. **main.py**
- Este é o arquivo principal do projeto, responsável pela criação da aplicação FastAPI, gerenciamento das rotas, injeção das dependências com o banco de dados, inicialização da aplicação e autenticação HTTP através de credenciais básicas.
```bash
{from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)


app = FastAPI()


security = HTTPBasic()
}
```
Importação de bibliotecas e arquivos, criação da classe fast API e criação das tabelas definidas na classe de modelo no banco de dados.


- Definição da função authenticate, para validar as credenciais de usuário fornecidas através da autenticação básica HTTP:
```bash
{def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "aluno"
    correct_password = "123"
   
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
}
```

- Define a função get_db, para fornecer uma sessão do banco de dados:
```bash
{def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
}
```
- Definição de rotas:
Retorna uma mensagem de boas vindas:
```bash
{@app.get("/")
def read_root():
    return {"message": "Welcome to the Paçoca API"}
}
```
- Retorna os detalhes de uma paçoca específica com base no ID fornecido:
```bash
{@app.get("/pacocas/{pacoca_id}", response_model=schemas.Pacoca)
def read_pacoca(pacoca_id: int, db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(authenticate)):
    db_pacoca = crud.get_pacoca(db, pacoca_id=pacoca_id)
    if db_pacoca is None:
        raise HTTPException(status_code=404, detail="Paçoca not found")
    return db_pacoca
}
```


- Define a rota post, para criação de uma nova paçoca com base nos dados fornecidos no corpo da requisição:
```bash
{@app.post("/pacocas/", response_model=schemas.Pacoca)
def create_pacoca(pacoca: schemas.PacocaCreate, db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(authenticate)):
}
```    return crud.create_pacoca(db=db, pacoca=pacoca)
}
```
- Atualiza os dados de uma paçoca existente com base no ID fornecido:
```bash
{@app.put("/pacocas/{pacoca_id}", response_model=schemas.Pacoca)
def update_pacoca(pacoca_id: int, pacoca: schemas.PacocaCreate, db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(authenticate)):
    return crud.update_pacoca(db=db, pacoca_id=pacoca_id, pacoca=pacoca)
}
```
- Define a rota para exclusão do produto, através do ID fornecido:
```bash
{@app.delete("/pacocas/{pacoca_id}", response_model=schemas.Pacoca)
def delete_pacoca(pacoca_id: int, db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(authenticate)):
    return crud.delete_pacoca(db=db, pacoca_id=pacoca_id)
}
```




**Conclusão**

  Neste tutorial, exploramos como desenvolver uma API usando FastAPI, integrando Docker para facilitar a implantação e utilizamos o Insomnia para testar as funcionalidades criadas.
  
  Utilizamos Docker para criar um ambiente isolado e replicável para nossa aplicação FastAPI.
  
  Criamos endpoints básicos para operações CRUD (Create, Read, Update, Delete) de paçocas, usando FastAPI para a criação rápida de APIs RESTful.
  
  Implementamos autenticação básica usando HTTP Basic Auth para proteger certas operações da API.
  
  Demonstramos como usar o Insomnia para enviar requests HTTP para os endpoints da API, permitindo testar as funcionalidades desenvolvidas de forma eficiente e visualizar as respostas retornadas pela API.
  
  Exportamos os requests configurados no Insomnia para facilitar o compartilhamento e a reutilização em equipe.
  
  Discutimos como integrar esses requests exportados ao README do GitHub para uma documentação clara e acessível.

**Considerações Finais**

  Ao final do tutorial, você deve ser capaz de desenvolver, testar e documentar APIs usando FastAPI, integrando Docker para um ambiente de desenvolvimento e também fazer utilização do Insomnia que permite uma validação muito precisa das operações da API, assegurando que todas as funcionalidades estejam operando conforme o esperado.
