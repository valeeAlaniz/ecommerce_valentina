# Alto Rango - Sistema de E-Commerce 🛒

Proyecto final desarrollado para la cátedra de Programación de la **Tecnicatura en Desarrollo de Software** en el **ITEC (Río Cuarto)**.

**Desarrolladora:** Valentina Alaniz  
**Entorno de desarrollo:** Linux (Linux Mint)

---

## 📝 Descripción del Proyecto
"Alto Rango" es una plataforma de comercio electrónico diseñada y desarrollada desde cero utilizando el framework Django. El sistema gestiona un catálogo completo de productos, familias de categorías con navegación fluida para los clientes, y un panel operativo con control estricto de roles y permisos para el personal de la tienda (Empleados, Dueños y Administradores).

---

## 🚀 Características y Requisitos Implementados

* **Modelo de Usuario Personalizado:** Extendiendo `AbstractUser` para incluir campos requeridos por el negocio (DNI, Teléfono).
* **Autenticación y Autorización Estricta:** Uso de decoradores `@login_required` y `@permission_required` para asegurar las rutas sensibles del backend.
* **Catálogo Dinámico e Inteligente:** * Los clientes ven únicamente los productos activos en stock.
  * Los administradores/empleados pueden visualizar productos pausados (con opacidad visual diferenciada) y contar con una función exclusiva de **Reactivación Lógica** desde la misma interfaz.
* **Gestión de Categorías:** Listado público para clientes con filtrado dinámico de productos asociados y formulario de creación protegido para el personal.
* **CRUD de Proveedores:** Acceso restringido según el sistema de permisos de Django, mostrando de forma prolija los campos de la base de datos (`nombre_empresa`, `contacto`, `telefono`, `email`) y ordenados automáticamente en **orden alfabético (A-Z)**.
* **Context Processors:** Inyección de variables globales (`nombre_tienda` y `todas_las_categorias`) disponibles de forma automática en todas las plantillas del sitio.

---

## 🛠️ Tecnologías Utilizadas
* **Backend:** Python 3.12, Django 5.x / 6.x
* **Frontend:** HTML5, CSS3, Bootstrap 5 (a través de CDN para un diseño limpio e industrial-elegante).
* **Base de Datos:** SQLite3.
* **Manejo de Imágenes:** Pillow.

---

## 📸 Capturas del Sistema

*(Podés guardar tus capturas en una carpeta dentro del proyecto y enlazar las rutas acá para la corrección del profesor)*

**1. Catálogo Principal (Vista Administrador con productos activos e inactivos):**
![Catálogo Principal](templates/tienda/img/captura_inicio.png)

**2. Listado de Proveedores (Orden Alfabético y Control de Permisos):**
![Proveedores](templates/tienda/img/captura_proveedores.png)

---

## ⚙️ Pasos para la Ejecución Local

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/valeeAlaniz/ecommerce_valentina.git](https://github.com/valeeAlaniz/ecommerce_valentina.git)
