from flask import Flask
from application.bp.homepage import homepage  # Import Blueprint

app = Flask(__name__)

# Register Blueprint
app.register_blueprint(homepage, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)


