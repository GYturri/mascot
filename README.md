Welcome to your Django project on Cloud9 IDE!

Your Django project is already fully setup. Just click the "Run" button to start
the application. On first run you will be asked to create an admin user. You can
access your application from 'https://mascot-rvstiven.c9users.io/' and the admin page from 
'https://mascot-rvstiven.c9users.io/admin'.

## Starting from the Terminal

In case you want to run your Django application from the terminal just run:

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

    $ python manage.py migrate

2) Run Django

    $ python manage.py runserver $IP:$PORT
    
## Configuration

You can configure your Python version and `PYTHONPATH` used in
Cloud9 > Preferences > Project Settings > Language Support.

## Support & Documentation

Django docs can be found at https://www.djangoproject.com/

You may also want to follow the Django tutorial to create your first application:
https://docs.djangoproject.com/en/1.9/intro/tutorial01/

Visit http://docs.c9.io for support, or to learn more about using Cloud9 IDE.
To watch some training videos, visit http://www.youtube.com/user/c9ide 

        start project
        
------------------------------------------------------------------------------------------------------
11/07/2016 - Rubick .- Se creo el modelo nuevo de usuarios
            * cree un nuevo super usuario, usuario = usuario1
                                            contraseña = laclavees123
            * cree el modelo pets y lo registre en el admin
=> intale la dependencia Django-braces - para manejar usuarios logueados en clases
            * cree la vista y el template para registrar nueva mascota ?aun falta que funcione y mejorar?
11/07/2016 -malogre los archivos base.html, home.html y login.html

19/07/2016 -se creo el url para mostrar detalle de mascota, se accede desde el inicio usuario