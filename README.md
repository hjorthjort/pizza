#PIZZA - Your pizza generator

This is a small python script that generates a pizza for you with by randomly picking components and adds them togeather.
It also gives it a fancy name.

##Dependencies
-----------
* Python

##Install with homebrew
-----------

Run `brew install hjorthjort/pizza/pizza`

##Install on other platform
-----------

Run `git clone https://github.com/hjorthjort/pizza.git`

##Running the script
-----------
Run `pizza` to get suggestions.

Run `pizza meat` if you want to get non-vegetarian ingredients.

Starting the web interface
==========================

Make sure you have `Flask` installed via `pip`. If not (or you are unsure), run

    pip install Flask

The web application lives in the file `api.py`. To start the application, simply run

    python api.py
