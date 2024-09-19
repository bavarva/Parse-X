
import os
import tweepy
from flask import Flask, request, jsonify, render_template, url_for
from tweepy.errors import Forbidden, NotFound, TweepyException

app = Flask(__name__)

# Twitter API v2 credentials
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAM3OvwEAAAAAdeA9CI59%2F81J8PGc0C9hMMl7Ad0%3Du28xF9sNdRdWXFvZZjd3MJHgUL6jK6JMEibZQC7Uk9CukQa450'

# Tweepy Client for Twitter API v2
client = tweepy.Client(bearer_token=bearer_token)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/user', methods=['POST'])
def get_user_data():
    user_id = request.form['user_id']
    
    try:
        # Fetch user information using Twitter API v2
        user = client.get_user(username=user_id, user_fields=['id', 'name', 'username', 'description', 'created_at', 'public_metrics'])

        # Convert the user object to a serializable dictionary
        user_data = {
            'id': user.data.id,
            'name': user.data.name,
            'username': user.data.username,
            'description': user.data.description,
            'created_at': user.data.created_at,
            'public_metrics': user.data.public_metrics
        }

        # Return user data as a JSON response
        return jsonify(user_data)
    except Forbidden as e:
        return f"Error: Access denied for user '{user_id}'. Details: {e}"
    except NotFound as e:
        return f"Error: User '{user_id}' not found. Details: {e}"
    except TweepyException as e:
        return f"Error: Unable to fetch data for user '{user_id}'. Details: {e}"

if __name__ == '__main__':
    app.run(debug=True)

