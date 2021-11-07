# Set Up Heroku

### Sign up 

Go to https://signup.heroku.com and create an account. Heroku will send a verification email to you. Check your email and click on the link. Create a password.


### Download Heroku CLI

Go to https://devcenter.heroku.com/articles/heroku-cli#download-and-install and download Windows installer. It will download an .exe file. Run it. 

Open a cmd or Pycharm terminal and run the command `heroku`. Many commands will appear. This means heroku has been installed. 

If it has not, delete heroku files from everywhere and install it again. 


### Authentification

In your terminal run the `heroku login`. Then press any key but `q`. It will open the browser and you will login. 


### Initialize Git Repo 

In your project directory run `git init`. 

Then run `git status` which will show all your files that need to be pushed to git. 

Before commiting run 
```
pip install gunicorn
pip install django-heroku
pip freeze > requirements.txt
```

Create a **.gitignore** file in your project directory and put this text in it.
```
/venv
.idea/
```

### Create your heroku app

```
heroku create yourdomainname
```
Note: you might get this message `Name testappforfun is already taken`. It means your app has not been created. Pick a name that does not exist. 
Then you will get this message `Creating ⬢ yourdomainname... done`

### Settings configuration
Add the following text to your settings.py

```
import django_heroku
django_heroku.settings(locals())

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
ALLOWED_HOSTS = ['yourdomainname.heroku.com']
```


### Procfile
In your project directory create a text file named `Procfile`. It must not have .txt ending.

Put this line of code in it `web: gunicorn mysite.wsgi`

`mysite` is where your settings.py file is. 

### Push everything

Run this in your terminal 
```
heroku config:set DISABLE_COLLECTSTATIC=1
```
Then push the code
```
git add . 
git commit -m "initial commit"
git push heroku master
```

## Postgres setup

Go to https://content-www.enterprisedb.com/downloads/postgres-postgresql-downloads and download latest windows version.

Run the .exe. file. 

Next, next, next... in the password field create a simple password and remember it. 

Leave the port the same. Next, next, next..

## addons
Go to terminal. 
Create a db on your heroku with this command.
```
heroku addons:create heroku-postgresql:hobby-dev
```
Check if the db is create with this command.
```
heroku addons
```

You should see something like this
```
Add-on                                       Plan       Price  State  
───────────────────────────────────────────  ─────────  ─────  ───────
heroku-postgresql (postgresql-closed-05408)  hobby-dev  free   created
 └─ as DATABASE

```

## Heroku bash
Enter heroku bash, migrate and create a super user.
```
> heroku run bash
$ python manage.py migrate
$ python manage.py createsuperuser 
```

