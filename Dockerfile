# Usar una imagen base de Jupyter
FROM jupyter/base-notebook:latest

# Establecer el directorio de trabajo
WORKDIR /home/ibarraortizdev/work

# Copiar los archivos del cuaderno al contenedor
COPY . .

# Instalar dependencias adicionales si es necesario
RUN pip install -r requirements.txt

# Exponer el puerto 8888 para Jupyter Notebook
EXPOSE 8888

# Comando para iniciar Jupyter Notebook
CMD ["start-notebook.sh", "--NotebookApp.token=''"]