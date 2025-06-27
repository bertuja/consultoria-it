# Consultoría IT - Proyecto Final Django

Este es un proyecto web desarrollado en Django que simula una tienda de servicios de consultoría IT. Está orientado a presentar servicios por categorías como DevOps, Infraestructura, Seguridad, Desarrollo y más, con funciones similares a Tienda Nube, pero enfocado en contenido estilo blog.

## 🧩 Funcionalidades principales

- Registro, login y logout de usuarios
- Perfiles de usuario editables (avatar, bio, cumpleaños, etc.)
- Listado y detalle de servicios (posts)
- Crear, editar y eliminar servicios (solo logueado)
- Página "Acerca de mí"
- Sistema de mensajería entre usuarios
- Navegación con barra de menú (navbar)
- Estilo blog con CKEditor para texto enriquecido
- Subida de imágenes para cada servicio
- Formularios con validaciones

## 🛠️ Tecnologías utilizadas

- Python 3.x
- Django 4.x
- Django CKEditor
- Bootstrap 5
- SQLite (en desarrollo)
- HTML + CSS

## 🏗️ Estructura del proyecto

consultoriait/
├── accounts/ # Gestión de usuarios (registro, login, perfil)
├── services/ # Servicios (modelo principal tipo blog)
├── messenger/ # Mensajes entre usuarios
├── static/ # Archivos estáticos (CSS, JS, imágenes globales)
├── media/ # Archivos subidos por usuarios
├── templates/ # Templates globales y base.html
├── core/ # Configuración principal de Django
├── manage.py


## 🚀 Cómo ejecutar el proyecto localmente

1. Clonar el repositorio:

```bash
git clone https://github.com/bertuja/consultoria-it.git
cd consultoria-it

    Crear entorno virtual y activarlo:

python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate

    Instalar dependencias:

pip install -r requirements.txt

    Ejecutar migraciones:

python manage.py migrate

    Crear superusuario (opcional):

python manage.py createsuperuser

    Ejecutar servidor:

python manage.py runserver

Luego, accedé a http://127.0.0.1:8000/
✅ Requisitos cumplidos del proyecto final

    Herencia de templates (base.html)

    Uso de CBV (Class-Based Views)

    Uso de al menos un mixin y un decorador

    Funcionalidad completa de CRUD sobre el modelo principal

    App separada para usuarios y mensajería

    Mensajes en pantalla si no hay objetos creados

    .gitignore con exclusiones de BD, media y caché

    requirements.txt actualizado

    Base de datos no incluida

    Subido a GitHub correctamente

📹 Video de demostración

(Insertar enlace a YouTube o archivo del video)
📝 Autor

Javier Bertucci
https://d-byte.com.ar
Consultor IT | Especialista en Infraestructura y DevOps