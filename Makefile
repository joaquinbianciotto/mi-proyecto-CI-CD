# Nombre de la imagen para entorno local
IMAGE_NAME := fastapi-lambda-local
CONTAINER_NAME := fastapi-lambda-container
APP_MODULE := .app.main:app

.PHONY: build docker-test docker-lint docker-shell docker-run clean
# 👷 DEFAULT: Ejecuta todo (build, test, lint, format check)
all: build docker-test
	@echo "✅ Build + Test + Lint finalizados correctamente"

## 🔨 Construye la imagen local
build:
	docker build -t $(IMAGE_NAME):latest .

## 🧪 Ejecuta pytest dentro del contenedor
docker-test: build
	docker run --rm $(IMAGE_NAME):latest pytest tests

## 🧹 Ejecuta ruff dentro del contenedor
#docker-lint: build
#	docker run --rm $(IMAGE_NAME) ruff check .
#
## 🧹 Corrige errores de formato (autoformat)
#docker-format: build
#	docker run --rm $(IMAGE_NAME) ruff check . --fix

## 🧹 Limpia todo
clean:
	docker rmi $(IMAGE_NAME) || true