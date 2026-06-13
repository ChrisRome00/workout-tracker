from flask import Flask # Importing Flask class from the flask package
from flask_cors import CORS # import CORS from flask_cors to allow React to communicate with our API

#Creating an instance of the Flask application
app = Flask(__name__)

# Apply CORS to our app so react can make requests to this server
CORS(app)

# defining a route - this will be our root URL endpoint on our server.
@app.route('/')
def home():
    return 'Workout Tracker API is running!'

#Only run the server if this file is being run directly
if __name__ == '__main__':
    #Start the Flask development server with debug mode on
    # Debug mode auto-restarts the server when you make code changes
    app.run(debug=True)