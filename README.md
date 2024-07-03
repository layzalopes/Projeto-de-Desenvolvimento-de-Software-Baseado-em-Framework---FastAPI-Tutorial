![logo](https://github.com/lyzlopess/Projeto-de-Desenvolvimento-de-Software-Baseado-em-Framework---FastAPI-Tutorial/assets/112975441/6a77ad02-c244-4ad7-b130-333a383a525e)

# Tutorial FastAPI
Este repositório contém o projeto desenvolvido para a disciplina "Desenvolvimento de Software Baseado em Framework". O foco principal é fornecer um tutorial abrangente sobre a criação de APIs web utilizando o framework FastAPI em Python, integrado com Docker para facilitar a configuração e o gerenciamento do ambiente de desenvolvimento.

# Sobre o FastAPI
FastAPI é um framework moderno, rápido (de alta performance) para a construção de APIs web com Python 3.7+ baseado em padrões, como tipo de dicas, para validar automaticamente os dados e gerar documentação interativa das APIs. Ele foi projetado para ser fácil de usar e desenvolver, com o objetivo de oferecer uma experiência rápida e eficiente tanto para os desenvolvedores quanto para os usuários finais.

![logoo](https://github.com/lyzlopess/Projeto-de-Desenvolvimento-de-Software-Baseado-em-Framework---FastAPI-Tutorial/assets/112975441/de330529-52fe-4014-856d-ee6a71796d9b)
# Integração com Docker
Docker é uma plataforma que permite aos desenvolvedores automatizar a implantação de aplicativos dentro de contêineres, que são unidades leves e portáteis de software. Usando Docker, podemos garantir que o ambiente de desenvolvimento seja consistente e replicável, independentemente do sistema operacional ou das configurações do desenvolvedor.

# Objetivos do Projeto
- Demonstrar como criar e configurar um projeto FastAPI.
- Ensinar como criar endpoints para diferentes operações HTTP (GET, POST, PUT, DELETE).
- Integrar o projeto FastAPI com Docker para facilitar o desenvolvimento e a implantação.
- Fornecer exemplos práticos e tutoriais passo a passo para ajudar os desenvolvedores a entender e implementar suas próprias APIs.

# Passo a Passo
1. Configurando o Ambiente
   Instalar Dependências
   - Certifique-se de ter o Python 3.7+ e o Docker instalados na sua máquina.
   - Instale o FastAPI e o Uvicorn:

```bash
pip install fastapi uvicorn
```
2. Clonando o Projeto do GitHub
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
Estrutura:
```bash
pacoca_api/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── crud.py
├── Dockerfile
└── requirements.txt
```
3. Construindo e Executando com Docker
   - Dentro do VisualStudio clicar em "View" localizado na parte superior.
   - Selecionar a opção "Terminal" para abrir o terminal já dentro do diretório.
   - Executar o comando para **contruir a Imagem do Docker**.
```bash
docker build -t pacoca_api .
```
   - Executar o comando para o executar o Contêiner Docker.
```bash
docker run -d --name pacoca_api_container -p 8000:80 pacoca_api
```

