from flask import Blueprint

newton = Blueprint('newton', __name__, url_prefix='/api/newton')

from . import routes