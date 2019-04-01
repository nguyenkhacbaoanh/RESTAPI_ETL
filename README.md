# Set POSTGRES DataBase
- install postgres db
```terminal
$ pip install spycopg2
```
- create db
```terminal
$ psql
# create owner database
$ CREATE USER name_owner WITH PASSWORD pw;
# create database using in project
$ CREATE DATABASE name_db WITH OWNER name_owner;
# give a permission for access oublic to this database
$  GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO name_owner;
```
- change in `setting.py`
- To cached your secret variable like password, email ... I recommended using `dotenv`
- install dotenv
```terminal
$ pip install python-dotenv
```
- create a file named `.env` in your BASEDIR and add in `setting.py` like below:
```text
# content in .env file
NAME_DB=...
ADMIN_DB=...
PW_DB=...
HOST_DB=localhost
PORT_DB=5432
```
```python
# after declare `BASEDIR`
# for load variable in dotenv
from dotenv import load_dotenv
dotenv_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path)
# for postgres database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('NAME_DB'),
        'USER': os.getenv('ADMIN_DB'),
        'PASSWORD': os.getenv('PW_DB'),
        'HOST': os.getenv('HOST_DB'),
        'PORT': os.getenv('PORT_DB'),
    }
}
```
- nowaday, your model data will be automatically create table instance in database like `sqlite3.db`
- Test it by migration db
```shell
$ python manage.py makemigrations
$ python manage.py migrate
```
# Create ORM (Object relational Mapping)
- I try to use ManytoOne relationship in this project
```shell
from github.models import *
a = Githuber.objects.create(useracc="anh",username="Bao Anh",bio="Data Scientist",location="Paris")
repo = Repository(repo_owner=a,repo="learing Python",used_lang="Python")
```