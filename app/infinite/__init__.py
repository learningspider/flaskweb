from flask import Blueprint

infinite = Blueprint('infinite',__name__)
from . import views
