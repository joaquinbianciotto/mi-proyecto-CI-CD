# Nombre de la imagen para entorno local
IMAGE_NAME := fastapi-local
CONTAINER_NAME := fastapi-container
APP_MODULE := .app.main:app

.PHONY: build docker-test docker-lint docker-shell docker-run clean
# 👷 DEFAULT: Ejecuta todo (build, test, lint, format check)
all: build docker-test docker-lint
	@echo "✅ Build + Test + Lint finalizados correctamente"

## 🔨 Construye la imagen local
build:
	docker build -t $(IMAGE_NAME):latest .

## 🧪 Ejecuta pytest dentro del contenedor
docker-test: build
	docker run --rm $(IMAGE_NAME):latest pytest tests

## 🧹 Ejecuta flake8 dentro del contenedor
docker-lint: build
	docker run --rm $(IMAGE_NAME):latest flake8 app/

## 🧹 Limpia todo
clean:
	docker rmi $(IMAGE_NAME) || true