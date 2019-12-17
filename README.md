# DJANGO TEST APP

At first I repeated code from [Video](https://www.youtube.com/watch?v=e1IyzVyrLSU&t) but not as v2, like in this.Video , I will create project django v3, then I do some stuff. 

All examples in code, the sequence of actions can be tracked by commits!

# learning documentation

### `DECEMBER 2019`

### `learning difficulty level: ? of 10`

# lets install all dependencies

At first I download latest version python on my Windows [From this site](https://www.python.org/) and delete from PATH old version. Then I upgrade `pip` version 

    python -m pip install --upgrade pip

After that I install `pipenv`. As I understand, it is a virtual and lockal copy of global python. More precisely - `virtual environment`

    pip install pipenv

Then

    pipenv shell

Now I have file in this folder - `Pipfile`:

    pipenv install django

And again create progect:

    django-admin startproject pollster

    cd pollster

  # Work with project

    python manage.py runserver 8081

  where 8081 is what you want.

  `ctrl z` in the terminal and we need to migrate database:

      python manage.py migrate

  In `settings.py` has `DATABASES = {...` when need to define the required for you DB as `default`

But now, I need create python app, not just a project....

    python manage.py startapp polls

This is installed itself `& pipenv install pylint --dev`

# Work with app

To select correct Interpreter `ctrl shift p` and `python select interpreter` and select with addition caption `polster_project: pipenv`

Models creating occurs in the models.py... some syntax inside

Do not forget enter in correct folder to perform some code

    cd polls or cd pollster

Need to add inside `INSTALLED_APPS = [` this `
     'polls.apps.PollsConfig  in the  `pollster` `settings` file. 

To create migration from models in `models.py` to database need to:

    python manage.py makemigrations polls

To migrate: 
  
    python manage.py migrate

Now we can work with database: 

    python manage.py shell

After work with console and database needs to manage the app, create user:

    python manage.py createsuperuser

Run server and go to the "/admin/"

Then we can access to admin panel django.

<hr>

  for brief display use `def __str__(self):`  in models and ` return self.choice_text` . Notice, Before and after `str` two of `_` 
  

<hr>


<hr>

