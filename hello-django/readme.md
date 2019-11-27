# Creating a Django website from scratch
## Environment setup
### Conda virtual environment
To create a new virtual environment and activate it run the below commands in anaconda command prompt.

```

conda env create -f environment.yml

conda activate django

```

## Creating Django project

`
django-admin startproject djangoApp
`

Once you execute the above command, a project named djangoApp should be created below folder structure.

```
djangoApp  - (This was later rename to hello-django to avoid confusion)
│   README.md
│   manage.py    
│
└───djangoApp
   │   settings.py
   │   urls.py
   |   wsgi.py
   |   __init__.py     

```

- Outer djangoApp is just a container and has no impact on the django project. I have renamed it to hello-django for this demo project
- manage.py - Helps with command line utility
- Inner djangoApp is the actual base application
- djangoApp/\_\_init__.py: An empty file that tells Python that this directory should be considered a Python package
- djangoApp/settings.py All settings related to the django app goes here
- djangoApp/urls.py URL declarations 
- djangoApp/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project

## Running the development server
Django comes with a liht weight server than can be used for development purpose. Once the setup is complete.Running the djangoApp using below command

`
python manage.py runserver
`

You should see below logger once the server startup begins

```
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

November 27, 2019 - 15:50:53
Django version 2.2, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

After this you can access the application in browser at http://127.0.0.1:8000/ or https://localhost:8000

### Managing the server port
Start the server on a particular port by passing the port explicility in the command line
`
python manage.py runserver 8081
`

### Printing custom message for home page

Create a file views.py under hello-django/djangoApp. Update the file with below content. This will be source from which our HTTPResponse is rendered.

```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the home.")
```

Update the urls.py with below content. Essentially we are adding urls patterns for django servers to check for before routing to particular views

```
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name='index'),
    path('admin/', admin.site.urls),
]
```
