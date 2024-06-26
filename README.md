# Proyecto Alumnos

<br/>

![Logo carena](https://iscarena-cba.infd.edu.ar/sitio/wp-content/uploads/2018/07/logocarenacirculo.png)

<br/>

## **Instituto Superior Dr. Carlos Maria Carena**

<br/>

### Presentación
* Asignatura: Validación y Verificación de Programas
* Curso: Tercero
* Ciclo: 2024
* Alumno: Matias Nicolas Arregui
* Enlace al perfil del alumno: [**@MatiasAshegui**](https://gitlab.com/MatiasAshegui)
* Docente: [**@carlosmurua**](https://gitlab.com/carlosmurua)
* Autor: [@MatiasAshegui](https://gitlab.com/MatiasAshegui)

<br/>

### Descripción breve del proyecto

El proyecto es sobre desarrollar una API con Django Rest Framework que nos devuelva los detalles de un libro en concreto, modificarlo, eliminarlo y agregar más libros al registro. El código base fue proporcionado por el profesor, sobre el cual debimos realizar modificaciones, logrando de esta forma el correcto funcionamiento del mismo.

<br/>

#### Clonar el repositorio
```
git clone https://gitlab.com/matias5322015/readme_api_vv.git
```
<br/>

### Indicaciones para el despliegue del proyecto

Creación del entorno virtual
El entorno virtual debe ser creado en el nivel anterior al de la carpeta clonada del repositorio. Debes darle el nombre de api_vv y de esta forma los componentes del mismo (Lib, Include, Scripts y pyvenv.cfg) se crearan dentro de la misma carpeta del repositorio clonado, permitiendo elegir el entorno como python interpreter. Al abrir la consola cmd en nuestro visual studio code, automaticamente se levantara el entorno ((api_vv) C:\user\api_vv>). En caso que no se seleccione solo, tocando F1 dentro de VSC, escribes: select interpreter si tienes lenguaje predeterminado ingles, y seleccionas el recommended; en caso de tener VSC en español escribes: seleccionar interprete y seleccionas el recomendado.

#### Creación del entorno virtual

```
python3 -m venv api_vv
```

#### Activación del entorno virtual

* En Windows
```
api_vv\Scripts\activate
```

* En Unix o MacOS
```
source api_vv/bin/activate
```


<br/>

### Instalación de requerimientos

En la carpeta principal del proyecto existe el archivo de texto “requirements.txt”, el cual nos va a instalar los paquetes necesarios para el funcionamiento del programa.

En la carpeta principal del proyecto:
```
(api_vv) pip install -r requirements.txt
```

<br/>

### Ejecución del programa

* Ejecutar el siguiente comando en tu cmd:
```
py manage.py runserver
```

* Abrir tu navegador e ingresar la siguiente ruta:
```
http://localhost:8000/
```
<br/>

### Aclaraciones

#### Migraciones

En caso de querer realizar una modificacion de models y querer realizar migraciones (makemigrations / migrate) es necesario crear una carpeta llamada "migrations" dentro de la carpeta del proyecto api_vv y dentro de la carpeta "migrations" crear un archivo init llamado de la siguiente manera: 

```
__init__.py
```

* Comando cmd para crear la carpeta dentro del proyecto:
```
(api_vv) api_vv\api_vv>mkdir migrations
```
<br/>

#### Archivo user.txt

En este archivo detallamos el "user" y "password" del mismo, permitiendo cargar datos por django-admin a la base de datos.