from flask import Blueprint

# Declare Blueprint
homepage = Blueprint('homepage', __name__, template_folder='templates')

# Import routes after declaring Blueprint
from application.bp.homepage import routes
