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
djangoApp
│   README.md
│   manage.py    
│
└───djangoApp
   │   settings.py
   │   urls.py
   |   wsgi.py
   |   __init__.py     

```

- Outer djangoApp is just a container and has no impact on the django project
- manage.py - Helps with command line utility
- Inner djangoApp is the actual base application
- djangoApp/\_\_init__.py: An empty file that tells Python that this directory should be considered a Python package
- djangoApp/settings.py All settings related to the django app goes here
- djangoApp/urls.py URL declarations 
- djangoApp/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project
