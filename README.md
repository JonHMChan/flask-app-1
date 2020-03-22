# Flask App 1: Pokedex Front End
For this exercise, you'll be creating a Pokedex that displays all of the original 151 Pokemon and detail pages for each Pokemon. This repository is also live at https://sleepy-earth-06238.herokuapp.com/ if you would like to see how it works.

## What you'll practice
 - HTML
 - CSS
 - JavaScript
 - jQuery
 - AJAX
 - API calls
 - Command Line
 - Git
 - GitHub

 ## Files and folders

 **For you**
 - `/templates` - Contains all of the HTML templates in your application. There are two: `index.html` is for the homepage located at `localhost:5000`, and `detail.html` is for an individual pokemon's page located at `localhost:5000/:id` where `:id` is the pokemon's ID number. For example, `localhost:5000/1` should be the page for Bulbasaur.
 - `/static/css` - Contains each of the CSS files for each of the HTML files in `/templates`. So `index.css` is for `index.html` and `detail.css` is for `detail.html`
 - `/static/js` - Contains each of the JavaScript files for each of the HTML files in `templates`. So `index.js` is for `index.html` and `detail.js` is for `detail.html`. This folder also contains `jquery.min.js` for jQuery. It's already installed in each of your HTML files in `/templates` and you can see how it's installed there.

 **Do not touch**
 - `README.md` - The instructions you're reading right now.
 - `setup.sh` - The file that will set your application up for you. See the "Setup" instructions below.
 - `requirements.txt` - A file that stores all of your Python dependencies (e.g. Flask) so when you run `pip install -r requirements.txt`, you'll download all the dependencies you need. For more information, see "How setup.sh works"
 - `app.py` - The Python file that starts your web application. This file is written using the Flask framework, and it's been commented with some information to help you understand how it works. For this exercise, you should not change anything in this file, but feel free to explore. We will be working on the server side code in the next exercise.
 - `.gitignore` - A file that tells `git` which files to ignore when you use version control.
 - `/data` - A folder that contains all of the pokemon data for your application. In future exercises, this will be replaced with other ways of storing data.
 - `/venv` - A folder that contains all of your virtual environment files and downloaded dependencies from `pip`. For more information, see "How setup.sh works"
 - `/__pycache__` - You'll probably have this folder generated. It is something created by Python 3 when you run it, and you can safely ignore it.

# Setup
These instructions are a simplified version of the Flask [installation instructions](https://flask.palletsprojects.com/en/1.1.x/installation/) and [quickstart](https://flask.palletsprojects.com/en/1.1.x/quickstart/). If you have any questions, feel free to reach out to me.

1. Clone this repository using `git clone` and `cd` from your command line into the repository folder.
2. Make sure you have Python 3 installed. You can check this by seeing if the command `python3` works in your command line. If you successfully run `python3`, you can exit the interpreter by typing `quit()` then hitting Enter. If you don't have Python 3 installed, follow [these instructions](https://realpython.com/installing-python/).
3. From the root of the repository, run the following command: `sh setup.sh`. This is a file I've written to automate the initial setup of this application. It will start your app automatically, and you can go to `localhost:5000` in a web browser to view it. If you want detailed instructions on how this file works, go to "How setup.sh works" below.
4. Whenever you're about to work on your application, make sure to run `. venv/bin/activate` first to start your virtual environment, then you can run `flask run` from the root of your repository to start your application.
 - To stop your server it's running in the command line, hit `Control + C` to stop the server.
 - If you change your HTML files, you'll have to restart the server to see changes.

## How setup.sh works
1. Python 3 comes with venv, a "virtual environment" to manage packages like `Flask` that you'll need to run your application. When you first clone this repository, run `python3 -m venv venv` from the root of the repository to create a virtual environment for your application. This will create a few folders and files related to venv, in a `venv` folder.
2. Once you've set up a virtual environment, whenever you're about to work on your app, make sure to run `. venv/bin/activate` from the root of the repository. You should then see `(venv)` prefixed in your command line to show that you're using the virtual environment. After you do this, you should be able to download packages and run your application.
3. Once you are using the virtual environment, make sure you install all the dependencies for this application by running `pip install -r requirements.txt` (if you're using Python 3, you might need to use `pip3` instead of `pip`. You only need to do this once and don't need to again when you want to run your application.
4. Once you have `Flask` properly installed, make sure you set your environment variables so Flask knows what file to start with. In this repository, the app starts with the file `app.py`. If you rename `app.py` or want to use a different file as the entrypoint, you'll have to run `export FLASK_APP={FILENAME}` and replace `{FILENAME}` with the correct filename to make sure the app runs.
5. Once you have everything setup, you should be able to run `flask run` and your server should start listening. Go to a browser at `localhost:5000` and you should see your app running.
