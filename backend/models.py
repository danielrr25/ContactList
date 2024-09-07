from app import db  # Import the db instance from the app

# Friend model (represents a table in the database)
class Friend(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Auto-incrementing primary key
    name = db.Column(db.String(100), nullable=False)  # Friend's name (required)
    role = db.Column(db.String(50), nullable=False)  # Friend's role (required)
    description = db.Column(db.String(250))  # Optional description
    gender = db.Column(db.String(10))  # Friend's gender
    img_url = db.Column(db.String(250))  # URL for the friend's image

    # Method to serialize Friend object (Python) to JSON
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role,
            "description": self.description,
            "gender": self.gender,
            "imgUrl": self.img_url
        }
