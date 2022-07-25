from flask import Blueprint, render_template
from flask_login import login_user, login_required, logout_user, current_user

views = Blueprint('views', __name__)


# whenever you hit this route, the following functions will run
@views.route('/')
@login_required
def home():
    return render_template("home.html",user=current_user)
