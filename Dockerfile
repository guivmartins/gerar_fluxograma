# Usar imagem Python
FROM python:3.13-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y graphviz && rm -rf /var/lib/apt/lists/*

# Criar diretório da app
WORKDIR /app

# Copiar arquivos
COPY . .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor porta
EXPOSE 10000

# Comando de inicialização
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:10000", "app:app"]
