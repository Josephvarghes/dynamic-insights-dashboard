from flask import Flask, render_template, request, jsonify
from models import get_filtered_data

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/data', methods=['GET'])
def fetch_data():
    filters = {
        "end_year": request.args.get('end_year'),
        "topic": request.args.get('topic'),
        "sector": request.args.get('sector'),
        "region": request.args.get('region'),
        "pest": request.args.get('pest'),
        "source": request.args.get('source'),
        "swot": request.args.get('swot'),
        "country": request.args.get('country'),
        "city": request.args.get('city')
    }
    data = get_filtered_data(filters)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)




# from config import Config
# import MySQLdb 
# from flask import Flask, render_template, jsonify, request
# # from flask_mysql import MySQL

# app = Flask(__name__)
# app.config.from_object(Config)

# # Function to connect to the MySQL database
# def get_db_connection():
#     connection = MySQLdb.connect(
#         host=app.config['MYSQL_HOST'],
#         user=app.config['MYSQL_USER'],
#         password=app.config['MYSQL_PASSWORD'],
#         db=app.config['MYSQL_DB']
#     )
#     return connection

# @app.route('/')
# def index():
#     return render_template('dashboard.html') 



# @app.route('/get_data')
# def get_data():
#     year = request.args.get('year', default='all')
#     sector = request.args.get('sector', default='all')
    
#     query = 'SELECT * FROM dashboard_data_table WHERE 1=1'
    
#     if year != 'all':
#         query += f" AND end_year = {year}"
#     if sector != 'all':
#         query += f" AND sector = '{sector}'"

#     connection = get_db_connection()
#     cursor = connection.cursor()
#     cursor.execute(query)
#     data = cursor.fetchall()
#     return jsonify(data)


# if __name__ == "__main__":
#     app.run(debug=True)

