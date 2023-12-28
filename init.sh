#!/bin/bash
# Levantar los servicios con Docker Compose
docker-compose up -d

# Ejecutar el script generate_data.py en el contenedor data-loader
echo "Ejecutando generate_data.py en data-loader..."
docker-compose exec -t data-loader python generate_data.py

# Ejecutar sqlacodegen y escribir la salida a un archivo
echo "Ejecutando sqlacodegen..."
sqlacodegen_v2 --generator declarative-dataclasses postgresql://myuser:mypassword@localhost:5432/mydatabase > app/modules/models_gen.py

echo "Proceso completado. Revisa "app/modules/models_gen.py" para ver los modelos generados."