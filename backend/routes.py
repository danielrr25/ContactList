from app import app, db  # Import the app and db instances
from flask import request, jsonify
from models import Friend  # Import the Friend model


# CRUD Operations
# Get all friends
@app.route("/api/friends", methods=["GET"])
def get_friends():
    friends = Friend.query.all()  # Retrieve all friends from the database
    result = [friend.to_json() for friend in friends]  # Convert friends to JSON
    return jsonify(result)  # Return JSON response


# Create a friend
@app.route("/api/friends",methods=["POST"])
def create_friend():
    try:
        data = request.json

        required_fields = ["name","role","description","gender"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error":f'Missing required field: {field}'}), 400

        name = data.get("name")
        role = data.get("role")
        description = data.get("description")
        gender = data.get("gender")

        # Fetch avatar image based on gender
        if gender == "male":
            img_url = f"http://avatar.iran.liara.run/public/boy?username={name}"
        elif gender == "female":
            img_url = f"http://avatar.iran.liara.run/public/girl?username={name}"
        else:
            img_url = None

        new_friend = Friend(name=name, role=role, description=description, gender= gender, img_url=img_url)

        db.session.add(new_friend)

        db.session.commit()

        return jsonify({"msg":"Friend created successfully"}),201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({})
    
# Delete Function
@app.route("/api/friends/<int:id>",methods=["DELETE"])
def delete_friend(id):
    try:
        friend = Friend.query.get(id)
        if friend is None:
            return jsonify({"error":"Friend not found"}), 404
        
        db.session.delete(friend)
        db.session.commit()
        return jsonify({"msg":"Friend deleted"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Update a friend profile 
@app.route("/api/friends/<int:id>", methods=["PATCH"])
def update_friend(id):
    try:
        friend = Friend.query.get(id)
        if friend is None:
            return jsonify({"error": "Friend not found"}), 404
        
        data = request.json
        
        friend.name = data.get("name", friend.name)
        friend.role = data.get("role", friend.role)
        friend.description = data.get("description", friend.description)
        friend.gender = data.get("gender", friend.gender)

        db.session.commit()
        return jsonify({"msg": "Friend updated successfully"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
