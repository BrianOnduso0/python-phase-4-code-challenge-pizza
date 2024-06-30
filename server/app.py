#!/usr/bin/env python3

import os
from flask import Flask
from flask_restful import Api, Resource
from flask_migrate import Migrate
from models import db, Restaurant, RestaurantPizza, Pizza

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

api = Api(app)

@app.route("/")
def index():
    return "<h1>Code challenge</h1>"

# Example resource using Flask-RESTful
class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}

# Add resources to the Api
api.add_resource(HelloWorld, '/hello')

# Example resource for Restaurants
class RestaurantResource(Resource):
    def get(self, restaurant_id):
        restaurant = Restaurant.query.get_or_404(restaurant_id)
        return restaurant.to_dict()

# Add restaurant resource
api.add_resource(RestaurantResource, '/restaurants/<int:restaurant_id>')

if __name__ == "__main__":
    app.run(port=5555, debug=True)
