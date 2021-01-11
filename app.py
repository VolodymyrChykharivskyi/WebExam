from flask import jsonify, request
from models import Car
from appInit import app, db
import database

# database.drop()
database.createdb()

@app.route('/cars', methods=['GET'])
def api_get_all_cars():
    cars = Car.query.all()

    output = []

    for car in cars:
        car_data = {}
        car_data['id'] = car.id
        car_data['license_plate'] = car.license_plate
        car_data['technical_condition'] = car.technical_condition
        car_data['under_way'] = car.under_way
        car_data['price'] = car.price
        car_data['date_of_manufacture'] = car.date_of_manufacture
        car_data['car_brand'] = car.car_brand
        output.append(car_data)

    return jsonify({'cars': output})

@app.route('/cars/<id>', methods=['GET'])
def api_get_one_car(id):
    car = Car.query.filter_by(id=id).first()

    if not car:
        return jsonify({'message': 'Car not found'})

    car_data = {}
    car_data['id'] = car.id
    car_data['license_plate'] = car.license_plate
    car_data['technical_condition'] = car.technical_condition
    car_data['under_way'] = car.under_way
    car_data['price'] = car.price
    car_data['date_of_manufacture'] = car.date_of_manufacture

    return jsonify({'car': car_data})

@app.route('/cars', methods=['POST'])
def api_create_car():
    data = request.json
    new_car = Car(
        car_brand=data['car_brand'],
        license_plate=data['license_plate'],
        technical_condition=data['technical_condition'],
        under_way=data['under_way'],
        price=data['price'],
        date_of_manufacture=data['date_of_manufacture'],
    )
    db.session.add(new_car)
    db.session.commit()
    return jsonify({'message': 'New car created'})

@app.route('/cars/<id>', methods=['DELETE'])
def api_delete_car(id):
    car = Car.query.filter_by(id=id).first()

    if not car:
        return jsonify({'message': 'No car found'})

    db.session.delete(car)
    db.session.commit()
    return jsonify({'message': 'The car has been deleted'})

@app.route('/cars/<id>', methods=['PUT'])
def api_edit_car(id):
    data = request.json
    car = Car.query.filter_by(id=id).first()

    if not car:
        return jsonify({'message': 'No car found'})

    car.car_brand = data['car_brand']
    car.license_plate = data['license_plate']
    car.technical_condition = data['technical_condition']
    car.under_way = data['under_way']
    car.price = data['price']
    car.date_of_manufacture = data['date_of_manufacture']

    db.session.commit()

    return jsonify({'message': 'The post has been updated'})

if __name__ == '__main__':
    app.run(debug=True)
