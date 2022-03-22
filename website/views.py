#make home page for website

from flask import Blueprint, render_template #it has a bunch of urls/roots inside of it

views = Blueprint('views',__name__)

@views.route('/') #whenever we go to home(/) the home function will run
def home():
    return render_template("home.html")


