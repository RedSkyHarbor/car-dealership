import csv
from datetime import datetime
from sqlalchemy import create_engine, Table, Column, String, Integer, MetaData, ForeignKey, DateTime
import sys

# for local development
#db_user = 'jessebreuer-penello'
#db_port = 5432
#db_host = 'localhost'
#db_name = 'car_dealership'
#db_string = 'postgresql://{}@{}:{}/{}'.format(db_user,db_host,db_port,db_name)
db_string = os.environ.get('DATABASE_URL')

def main(args):
    fname = args[0]
    tablename = args[1]

    db = create_engine(db_string)
    meta = MetaData(db)

    if tablename == 'inventory':
        upload_inventory(fname, db, meta)
    elif tablename == 'sales':
        upload_sales(fname, db, meta)
    elif tablename == 'employees':
        upload_employees(fname, db, meta)
    else:
        print('Invalid table name')
        return -1

    print('Completed')
    return 1

def upload_inventory(fname, db, meta):
    print('upload inventory')
    inventory_table = Table('inventory', meta,
                            Column('id', Integer, primary_key=True),
                            Column('vehicle_make', String),
                            Column('vehicle_year', Integer),
                            Column('vehicle_model', String))

    with db.connect() as conn:
        inventory_table.create()
        with open(fname, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader) # skip header
            for row in reader:
                insert_stmt = inventory_table.insert().values(vehicle_make=row[1], vehicle_year=row[2], vehicle_model=row[3])
                conn.execute(insert_stmt)

def upload_sales(fname, db, meta):
    print('upload sales')
    sales_table = Table('sales', meta,
                        Column('id', Integer, primary_key=True),
                        Column('car_id', Integer),
                        Column('employee_id', Integer),
                        Column('date_sold', DateTime, default=datetime.utcnow))

    with db.connect() as conn:
        sales_table.create()
        with open(fname, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader) # skip header
            for row in reader:
                insert_stmt = sales_table.insert().values(car_id=row[1], employee_id=row[2])
                conn.execute(insert_stmt)


def upload_employees(fname, db, meta):
    print('upload employees')
    employees_table = Table('employees', meta,
                            Column('id', Integer, primary_key=True),
                            Column('name', String))

    with db.connect() as conn:
        employees_table.create()
        with open(fname, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader) # skip header
            for row in reader:
                insert_stmt = employees_table.insert().values(name=row[1])
                conn.execute(insert_stmt)

if __name__ == '__main__':
    main(sys.argv[1:])
