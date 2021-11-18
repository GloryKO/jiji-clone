# jijiclone

## A Web App Created with Django and Django-rest Framework

This app is a jiji clone app that allows you to sign up as a seller and upload product(s), and other buyer can contact the seller to get the product

### The Deployed Project

The project was hosted on heroku, you can view it [here](https://crop-2-cash.herokuapp.com/) and the swagger api documentation [here](https://crop-2-cash.herokuapp.com/swagger/)

### How to run the program

> Ensure you have Python installed in your system, if not visit [python.org](https://www.python.org/) to download and install

* clone this repository
* open the folder in the code editor
* create a virtual environment using : `python -m venv <nameofven>`
* activate the virtual environment using (in a bash terminal): `. venv/scripts/activate`
> To know your virtual environment is activated, you would see the nameofvenv in brackets - (nameofvenv)
* Install the requirements for the project using: `pip install -r requirements.txt`
* Migrate the database using `python manage.py migrate`
* Run the server using `python manage.py runserver`
* Check the project at [here](http://localhost:8000/)

> To visit the api, click [here](http://localhost:8000/swagger/)