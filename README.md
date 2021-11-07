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
pip freeze > requirements.txt
```

Create a **.gitignore** file in your project directory and put this text in it.
```

```
