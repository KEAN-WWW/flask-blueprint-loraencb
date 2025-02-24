from flask import render_template
from application.bp.homepage import (homepage)  # Import Blueprint object

# Default homepage route
@homepage.route('/')
def home():
    return render_template('homepage.html')

# About page route
@homepage.route('/about')
def about():
    return render_template('about.html')
