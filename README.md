# myDrive

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

Idea behind this project was to make my dirty to implement few simmilar functionality used by Big Giants in FIle Storing Campaign like Google Drive , DropBox , OneDrive etc.

So This is backend by Flask , MySQL (DB) , SQLALchemy For Object Relational Mapping , Jinja2 for Rendering HTML/CSS 

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) 

### Prerequisites

```
  A little about Terminal in unix or Linux
  python3
  pip
  git
  Flask
```

### Installing  <a name = "deployment"></a>
A step by step series of examples that tell you how to get a development env running.

<!-- ''' -->
```bash
 
  git clone 
  cd myDrive/
  pip install pipenv
  pipenv shell (This will load a virtualenv)
  pipenv -r requirements.txt
  python runDrive.py

```
Create a MySQL Database And User

After that

  Create a .env file for dotenv in root directory of project
```
 SECRET_KEY = value
 TRACK_VALUE = value
 DB_USER = value
 DB_PASSWORD = value
 DB_NAME = value
 And just go to :  http://localhost:5000/
```


## Usage <a name = "usage"></a>

```
Following Routes are Available:
http://localhost:5000 + address

address : /
address : /login
address : /signup
address : /logout
address : /dashboard
address : /profile
address : /about
address : /contact-us