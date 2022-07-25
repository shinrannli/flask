from flask import Blueprint, render_template

views = Blueprint('views', __name__)


# whenever you hit this route, the following functions will run
@views.route('/')
def home():
    return render_template("home.html")
