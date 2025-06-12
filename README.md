
# 🚀 Mi Proyecto CI/CD con FastAPI

Este proyecto implementa un flujo CI/CD completo para una aplicación FastAPI con Docker, incluyendo testing automatizado, linting, despliegue automatizado a Amazon ECR y AWS EC2 con notificaciones de Slack.

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Instalación y Configuración](#-instalación-y-configuración)
- [Build Local con Docker](#-build-local-con-docker)
- [Workflow de CI/CD](#-workflow-de-cicd)
- [Deploy en AWS](#-deploy-en-aws)
- [Testing](#-testing)
- [Linting](#-linting)
- [Contribución](#-contribución)

## 🌟 Características

- **FastAPI** - Framework web moderno y rápido para APIs
- **Docker** - Containerización con imagen optimizada multi-stage
- **CI/CD Automatizado** - GitHub Actions para integración y despliegue continuo
- **Testing** - Suite de pruebas con pytest
- **Linting** - Verificación de calidad de código con flake8
- **Notificaciones Slack** - Alertas automáticas de build y despliegue
- **Amazon ECR** - Registro de contenedores para despliegue
- **AWS EC2 Deploy** - Despliegue automatizado a instancia EC2
- **Makefile** - Comandos simplificados para desarrollo


## 🚀 Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone <tu-repositorio>
cd mi-proyecto-CI-CD
```

### 2. Crear entorno virtual (desarrollo local)

```bash
python -m venv venv
source venv/bin/activate  # En Linux/Mac
# o
venv\Scripts\activate     # En Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 🐳 Build Local con Docker

### Usando Makefile (Recomendado)

```bash
# Build completo: construir imagen + tests + linting
make all

```

### Comandos Docker directos

```bash
# Construir la imagen
docker build -t mi-fastapi-app:latest .

# Ejecutar la aplicación
docker run -p 8000:8000 mi-fastapi-app:latest

# Ejecutar tests
docker run --rm mi-fastapi-app:latest pytest tests/ -v

# Ejecutar linting
docker run --rm mi-fastapi-app:latest flake8 app/

# Acceder al shell del contenedor
docker run -it --rm mi-fastapi-app:latest sh
```

## 🔄 Workflow de CI/CD

### Pipeline de CI/CD (Integración y Despliegue Continuo)

**Archivo**: `.github/workflows/ci.yml`

**Triggers**: Pull Requests a la rama `main`

**Jobs**:

1. **Build & Test**
   - ✅ Construye la imagen Docker
   - ✅ Ejecuta tests con pytest dentro del contenedor
   - ✅ Ejecuta linting con flake8
   - ✅ Detecta tipo de fallo específico

2. **Build Notification**
   - 📢 Notifica resultado del CI a Slack
   - 🎯 Identifica tipo específico de error si falla

3. **Build and Push to ECR**
   - 🏗️ Construye imagen final
   - 📤 Sube a Amazon ECR con tags SHA y latest
   - ⚠️ Solo se ejecuta si el CI pasa

4. **Deploy to EC2**
   - 🚀 Despliega automáticamente a instancia EC2
   - 🔄 Actualiza el contenedor con la nueva imagen
   - 🌐 Configura proxy reverso en puerto 80

5. **Deployment Notification**
   - 📢 Notifica resultado del despliegue a Slack
   - 🔗 Incluye URL de la aplicación desplegada

## 🚀 Deploy en AWS

### Arquitectura de Despliegue

El proyecto utiliza una arquitectura de contenedores en AWS con los siguientes componentes:

- **Amazon ECR**: Registro de contenedores para almacenar las imágenes Docker
- **AWS EC2**: Instancia para ejecutar la aplicación containerizada
- **GitHub Actions**: Orquestación del pipeline CI/CD


### URL de la Aplicación

Una vez desplegada, la aplicación está disponible en:
- **Aplicación**: http://18.228.193.11/
- **Documentación API**: http://18.228.193.11/docs
- **Documentación alternativa**: http://18.228.193.11/redoc

### Estados de Notificación

#### CI Pipeline
- ✅ **Éxito**: "CI Pipeline Exitoso"
- ❌ **Fallos específicos**:
  - 🐳 Error al construir la imagen Docker
  - 🧪 Error en las pruebas (pytest)
  - 🔍 Error en la verificación de estilo (flake8)

#### Deploy Pipeline
- ✅ **Éxito**: "Despliegue Exitoso a EC2"
- ❌ **Fallo**: "Despliegue Fallido"


## 🧪 Testing

### Estructura de tests

```
tests/
├── test_main.py    # Tests del endpoint principal y funciones utilitarias
└── test_items.py   # Tests CRUD completos del router de items
```

### Ejecutar tests

```bash
# Localmente
pytest tests/ -v

# Con Docker
docker run --rm mi-fastapi-app:latest pytest tests/ -v

# Con cobertura
pytest tests/ --cov=app --cov-report=html
```

### Tests incluidos

- ✅ Test del endpoint raíz
- ✅ Test de función utilitaria `edad()`
- ✅ Tests CRUD completos para items:
  - Listar items
  - Obtener item específico
  - Crear item
  - Actualizar item
  - Eliminar item

## 🔍 Linting

### Configuración flake8

Archivo: `.flake8`

```ini
[flake8]
extend-ignore = E203, W503
max-line-length = 88
```

### Ejecutar linting

```bash
# Localmente
flake8 app/

# Con Docker
docker run --rm mi-fastapi-app:latest flake8 app/

# Con Makefile
make docker-lint
```

