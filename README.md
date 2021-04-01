# FC712 September 2020 starts

## Final Project - Task 1

In the first task of the project you are required to build a web form using `flask` and `wtforms`. The web form should be a questionnaire for your courses to rate how well you have done in the course. The questionnaire should contain questions about your name, GIC enrolment number, and email address, each in a `TextField` with a label. It should also have various questions where you can write long answers in a `TextAreaField`, have Boolean answers in a `BooleanField` or have radio buttons in a `RadioField`. The form should have a submit button which when pressed should save the answers in a `.txt` file. You should use a template to design your webpage. You must comment well throughout your code.

This repo contains a template that should help you work on **Task 1** of your final project. This Flask application has a login page that takes a user and a password, and saves them in `.txt` files. You can use this as a template to build your final Task 1 with all the requirements. 

### What is Flask?

Flask is a microframework for Python based on Werkzeug and Jinja2.


## Template Project Structure

```
├─── appsite
|   ├─── config.py             # app configuration details
|   ├───__init.py__            # setup our app
|   ├─── routes.py             # main app routes
|   ├─── forms.py              # user related forms
|   ├─── requirements.txt      # for local deployment
|   ├─── README.md
|   |
|   ├───templates
|   |   ├── base.html          # base html
|   |   ├── index.html         # show the home page
|   |   └── login.html         # show the login form
|
└─── run.py                    # run app
```

## Quick start

1. Clone or download the repo

```
git clone https://github.com/gracecarrillo/FC712-Flask-boilerplate.git
cd FC712-Flask-boilerplate
```

2. Initialise a virtual environment

```
# linux
$virtualenv --no-site-packages env
$source env/bin/activate

# windows
virtualenv --no-site-packages env
.\env\Scripts\activate
```

3. Install the dependencies:

```
pip install -r requirements.txt
```

4. Run the development server:

```
python run.py
```

6. Navigate to http://localhost:5000 , where `localhost` is your IP address. 


## Learn more

1. [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/)
2. [Flask Extensions](https://flask.palletsprojects.com/en/1.1.x/extensions/)
3. [Python long online tutorial](https://www.youtube.com/watch?v=MwZwr5Tvyxo)
