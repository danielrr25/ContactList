#TODO: update this file for deployment
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Enable cross-origin requests
CORS(app)

# Configurations for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///friends.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize SQLAlchemy (database ORM)
db = SQLAlchemy(app)

# Create tables when the app starts
with app.app_context():
    db.create_all()

# Import routes after app and db initialization to avoid circular imports
import routes

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
