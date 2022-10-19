# Chorestack

## A bug tracking system


Chorestack is a simple bug tracking and issues management system built to allow users to register and log into a web client, create records of bugs found during developement of their projects 


Within the project, the three apps worthy of note are:
1. Bugstack - Creation, display and update of bugs  
2. Projects - Creation, display and update of projects currently in development  
3. Users - Handles user authentication and authorisation (in development)

### Prerequisite
1. As this is a Django application you will need to have Python installed on your system. You can download and install Python from 
[https://www.python.org/downloads/]. This will allow you to be able to run 'python' commands.


## Getting Started
* Create a new directory where you would like this project stored. e.g BugApp

* Change into that new directory

```
cd BugApp
```

* Get a copy of the source code of this project into your local repository.

```
git clone https://github.com/KelvinJC/Chorestack.git
```

* The code will be packaged in a directory named MyHackerNews so change into that directory

```
cd Chorestack
```

<br><br>
* *In accordance with best practices, run this project within a virtual environment.*<br>
<br><br>

* Create a virtual environment. (Windows OS. Check out how to create and activate a virtual environment if you are on a different OS.)

```
python -m venv <name_of_environment> 
```

* Activate that environment

```
source venv/Scripts/activate 
```

* Install project dependencies

```
pip install django
pip install requests
```


### Database Creation

This project makes use of a sqlite database for storage of articles and job posts as well as user information. If you require a different database, customisation is possible via the settings.py file. <br>
For the sake of simplicity however, we will focus on using sqlite3. <br><br>


Change into the source code directory

```
cd src 
```

Run the following commands in succession

```
python manage.py makemigrations
python manage.py migrate
```


### Create a Django Admin User
This step is not critical to the usage of the app but if you are familiar with the Django Admin UI you can create a superuser i.e Admin

```
python manage.py createsuperuser 
```

Following the prompts you may enter your details for username, e-mail address (optional), password, password re-entry. <br><br>



### Run the server:

To begin using the application. Initiate the server by running the following command

``` 
python manage.py runserver 
```

By default, Django apps listen on http://127.0.0.1:8000 so once the server is running, that is the link to copy and paste into your preferred browser


### Screenshots

