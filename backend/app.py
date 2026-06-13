from flask import Flask, jsonify, request # Importing Flask class from the flask package
from flask_cors import CORS # import CORS from flask_cors to allow React to communicate with our API

#Creating an instance of the Flask application
app = Flask(__name__)

# Apply CORS to our app so react can make requests to this server
CORS(app)

#Temporary in-mem list to wiork with and test
workouts = [
    {
        "id": 1,
        "title": "Push Day",
        "exercises": ["Bench Press", "Shoulder Press"],
        "date": "2024-01-01"
    }
]

# defining a route - this will be our root URL endpoint on our server.
#@app.route('/')
#def home():
#    return 'Workout Tracker API is running!'

#Route to get all workouts
# GET req to /workouts returns all workouts in the list
@app.route('/workouts', methods=['GET'])
def get_workouts():
    # jsonift converts our python list into a json responce
    return jsonify(workouts)

#Route to add a new workout
# POST request to /workouts adds a new workout to the list
@app.route('/workouts', methods=['POST'])
def add_workout():
    # request.json grabs the JSON data sent in the request body
    data = request.json
    # Append the new workout to our workouts list
    workouts.append(data)
    # Return the newly added workout with a 201 status code (means "created")
    return jsonify(data), 201

#Route to get a single workout by its id
# <int:id> is a URL parameter that captures the id from the URL
@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    # loop through the workouts and find the one with the matching id
    for workout in workouts:
        if workout["id"] == id:
            return jsonify(workout)
        return jsonify({"error": "Workout not found"}), 404
    
#Route to update a workout by its id
# PUT request to /workouts/<id> updates the workout with the matching id
@app.route('/workouts/<int:id>', methods=['PUT'])
def update_workout(id):
    # find the workout, if not found, return error
    for workout in workouts:
        if workout["id"] == id:
            # set current workout
            curr_workout = workout
            # Get the new data from the request body
            data = request.json
            # Update the workout with the new data
            curr_workout.update(data)
            return jsonify(workout)
        return jsonify({"error": "Workout not found"}), 404

#Route to delete a workout by its id
@app.route('/workouts/<int:id>', methods=['DELETE'])
def remove_workout(id):
    for workout in workouts:
        if workout["id"] == id:
            workouts.remove(workout)
            return jsonify({"message": "Workout deleted"})
        return jsonify({"error": "Workout not found"}), 404

#Only run the server if this file is being run directly
if __name__ == '__main__':
    #Start the Flask development server with debug mode on
    # Debug mode auto-restarts the server when you make code changes
    app.run(debug=True)

