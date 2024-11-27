PART 1: SETUP AND INTRODUCTION for linux
1. Install Vscode

2. Test python version
python3 --version

3. Create Virtual Environment where you install python packages to isolate from other packages in your system
python3 -m venv env

4. Activate Environment
source env/bin/activate

5. create a requirements.txt file, manually

6. activate the requirements.txt file
pip install -r requirements.txt

7. create a git ignore file

8. Install Django
pip install django

9. Test Django
python -m django --version

10. Start a new project in the directory
django-admin startproject nameofproject . 
it is important that you add that . after the name of the project.


11. Create an app.
python manage.py startapp nameofapp

12. install django rest framework
pip install djangorestframework
 'rest_framework', in settings.py file

13. Add app and rest framework to settings

14. do the migration. do not migrate yet if you are using a customuser 
python manage.py makemigrations
python manage.py migrate

15. Check project 
python manage.py runserver

PART 2: MODELS AND ADMIN INTERFACE

1. customize your models
Add string methods

def __str__(self):
        return str(self.id)

2. add the config to the settings.py

3. Create Models, and apply migrations 
python manage.py makemigrations
python manage.py migrate

4. Register Models in Admin Interface 

5. Create superuser 
python manage.py createsuperuser

confirm by adding /admin/login to the url aftrewards try running the server with 'python manage.py runserver'

6. create a serializers.py file

7. edit your views.py file

8. edit your url.py file in your app, but create the urls.py manually 

9. edit url.py file in your django project. add the path

15- Configure static files path and urls

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root/')
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root/')

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
16- Tell Django where to find the static files while on the browser

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
PART 3: VIEWS AND TEMPLATES

17- Write basic view, add index.html in app template folder and configure app url

def index(request):
    return render(request, 'index.html')
18- Add assets folder to static_root folder

Frontend https://github.com/bedimcode/responsive-portfolio-website-JhonDoe
19- Load static files in html file

20- Write Views

21- Add Data in Admin interface

22- Load content from views to Templates

{% static 'assets/css/styles.css' %}

{{ model.field }}
Check DEPLOYMENT

GIT RESET

rm -rf .git*