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
   - Selecione "Basic Auth" no menu suspenso.
   - Insira o username 'aluno' e password '123'

8. **Adicionar o corpo**

   - Clique na aba "Body" na barra de navegação do request.
   - Selecione "JSON".
   - Adicione o corpo JSON com os dados atualizados da paçoca.
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
   - Selecione "Basic Auth" no menu suspenso.
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
   - Selecione "Basic Auth" no menu suspenso.
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
   - Selecione "Basic Auth" no menu suspenso.
   - Insira o username 'aluno' e password '123'
   - Clique no botão "Send" para enviar a requisição.
   - Verifique a resposta para confirmar que a paçoca foi apagada com sucesso.
```
{
	"detail": "Paçoca not found"
}
```

