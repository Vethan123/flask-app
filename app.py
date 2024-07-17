from flask import Flask, jsonify, request
from pymongo import MongoClient,errors

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['admin']
collection = db['zomato']


@app.route('/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):
    try:
        restaurant = collection.find_one({'Restaurant_Id': int(restaurant_id)})


        if restaurant:
            restaurant['_id'] = str(restaurant['_id'])
            return jsonify(restaurant), 200
        else:
            return jsonify({'error': 'Restaurant not found'}), 404
    except Exception as e:
        print("Exception occurred:", e)
        return jsonify({'error msg': str(e)}), 500

@app.route('/<string:restaurant_name>', methods=['GET'])
def get_restaurant_by_name(restaurant_name):
    try:
        restaurant = collection.find_one({'Restaurant_Name': restaurant_name})


        if restaurant:
            restaurant['_id'] = str(restaurant['_id'])
            return jsonify(restaurant), 200
        else:
            return jsonify({'error': 'Restaurant not found'}), 404
    except Exception as e:
        print("Exception occurred:", e)
        return jsonify({'error msg': str(e)}), 500


@app.route('/', methods=['GET'])
def get_restaurants():
    try:
        page = int(request.args.get('page', 1))
        page_size = 10

        skip = (page - 1) * page_size
        restaurants = collection.find().skip(skip).limit(page_size)

        restaurants = [{**restaurant, '_id': str(restaurant['_id'])} for restaurant in restaurants]

        return jsonify({'restaurants': restaurants}), 200

    except Exception as e:
        print("Exception occurred:", e)
        return jsonify({'error msg': str(e)}), 500


