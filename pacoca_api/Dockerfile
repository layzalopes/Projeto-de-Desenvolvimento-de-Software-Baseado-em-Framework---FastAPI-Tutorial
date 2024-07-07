FROM python:3.10

# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo requirements.txt para o contêiner
COPY requirements.txt /app/

# Instala as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação para o contêiner
COPY . .

# Comando para rodar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
