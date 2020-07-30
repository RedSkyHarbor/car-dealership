## Car dealership

# Built with
[Flask](https://palletsprojects.com/p/flask/) - Python web framework

[Gunicorn](https://gunicorn.org/) - Production ready WSGI server

[Heroku](https://www.heroku.com/) - Deployed here

[SQLAlchemy](https://www.sqlalchemy.org/) - Python SQL toolkit / Object Relational Mapper

[PostgresQL](https://www.postgresql.org/) - Open source object-relational database

[Psycopg2](https://www.psycopg.org/) - Python adapter for PostgresQL 

# Details
This project is meant to emulate how a car dealership would manage their inventory. Sticking with this theme, all cars in this inventory are Mazda.

# This project includes
1. A flask server in `/src`
	* Usage: ...
2. A python script to upload data from `.csv` files to the database `upload.py`
	* Usage: `python upload.by name-of-csv-file.csv tablename`
	* name-of-csv-file and tablename must match or else error
3. Sample data to populate the database `/sample_data`
	* Sample data is in `.csv` files since the format is strictly tabular 
	* `inventory.csv` Cars that the dealership sells
	* `sales.csv` Cars that the dealership has sold
	* `employees.csv` A list of people the dealership employs
4. A network diagram of my project `network_diagram.jpeg`
5. Explenation of network diagram `network_diagram.txt` 

:)
