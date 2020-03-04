# SCROW
 
##Requirements
* Python3.6+
* Redis
* Nodejs
* Yarn

##Setup

* Install redis apt-get redis
* pip install virtualenv
* Setup virtualenv with virtualenv .scrowenv
* pip install -r requirements.txt

##Usage
* Rename `.env.example` to `.env` file to fit usage
* Make sure redis-server is running
* run `yarn` to install npm dependencies
* run `yarn dev`
* run `python manage.py migrate && python manage.py runserver` 
