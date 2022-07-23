from flask import Blueprint

views = Blueprint('views', __name__)


# whenever you hit this route, the following functions will run
@views.route('/')
def home():
    return "<h1>Test</h1>"
