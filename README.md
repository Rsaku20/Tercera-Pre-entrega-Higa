Pasos para testear mi proyecto

1. El proyecto es sobre un estudio de Yoga. El cual cuenta con 3 modelos (Curso, estudiante y profesor) que pueden ser visualizados en  ../app_coder/models.py.

2. Correr el siguiente comando:
    Python manage.py runserver


3. Para visualizar la página ingresar a:
    http://127.0.0.1:8000/app-coder/
    El contenido de Inicio, Profesores, Cursos y Estudiantes fue modifico pero mantienen la estructura del archivo padre.html, a través de Herencia.

4. Para buscar un curso en la base de datos ingresar a la url y colocar el nombre del curso
    http://127.0.0.1:8000/app-coder/busqueda-curso/
    Ejemplo: Yoga - busqueda exitosa / Python - busqueda fallida

5. Para agregar cursos a la base de datos e ingresar curso y código.
    http://127.0.0.1:8000/app-coder/curso-formulario/
    Ejemplo: curso: Ashtanga código: 6004

6. Para visualizar la información de los modelos ingresar a:
    http://127.0.0.1:8000/admin
    Usuario: coder
    Contraseña:coder1234










