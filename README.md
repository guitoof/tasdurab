# tasdurab
Web application for the food sharing &amp; recycling project TAsduRAB

## Creating a virtual env

You obviously need Python and pip installed for this to work. Please use a virtual env to work on this repository.

You will need to have both of these tools installed

	pip install virtualenv virtualenvwrapper

Add in your .bashrc or .zshrc the following lines

	export WORKON_HOME=~/.virtualenvs
	source /usr/local/bin/virtualenvwrapper.sh

You can then open a new terminal window, or resource your .bashrc (or .zshrc) and create the virtual env

	mkvirtualenv tasdurab
	workon tasdurab

## Installing dependencies

cd into the repository and run the following command to install all dependencies

	pip install -r requirements.txt


## Creating the database

	python manage.py migrate

## Running the development server

	python manage.py runserver
