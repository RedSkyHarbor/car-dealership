from flask import Flask, render_template
from sqlalchemy import create_engine

app = Flask(__name__)

db_user = 'jessebreuer-penello'
db_port = 5432
db_host = 'localhost'
db_name = 'car_dealership'
db_string = 'postgresql://{}@{}:{}/{}'.format(db_user,db_host,db_port,db_name)
db = create_engine(db_string)

@app.route('/')
def homepage():
    car_details = []
    cars_sold_per_employee = []

    # get best selling car
    try:
        most_sold_car = 'SELECT sales.car_id, COUNT(sales.car_id), inventory.vehicle_model, inventory.vehicle_make, inventory.vehicle_year FROM sales, inventory WHERE sales.car_id=inventory.id GROUP BY sales.car_id, inventory.id ORDER BY COUNT(car_id) DESC LIMIT 1;'
        result = db.execute(most_sold_car)
        if result:
            car_details = result.fetchone()
            car_id = car_details.car_id
    except Exception as e:
        print(e)
        return -1

    # get employees who sold the best selling car
    try:
        cars_sold = 'SELECT sales.employee_id, COUNT(sales.car_id), employees.name FROM sales, employees WHERE car_id={} AND sales.employee_id=employees.id GROUP BY sales.employee_id, employees.id ORDER BY COUNT(car_id) DESC;'.format(car_id)
        result = db.execute(cars_sold)
        if result:
            for row in result:
                cars_sold_per_employee.append({'name': row['name'], 'cars_sold': row['count']})
    except Exception as e:
        print(e)
        return -1

    return render_template('homepage.html', car_details=car_details, cars_sold_per_employee=cars_sold_per_employee)
