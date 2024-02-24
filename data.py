from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'akshat427'
app.config['MYSQL_DB'] = 'mydatabase'

mysql = MySQL(app)

# API route to insert data into the 'users' table
@app.route('/api/add_user', methods=['POST'])
def add_user():
    try:
        name = request.json['name']
        marks = request.json['marks']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, marks) VALUES (%s, %s)", (name, marks))
        mysql.connection.commit()
        cur.close()

        return jsonify(message='User added successfully')

    except Exception as e:
        return jsonify(error=str(e))

# API route to retrieve all users from the 'users' table
@app.route('/api/get_users', methods=['GET'])
def get_users():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM mytable")
        data = cur.fetchall()
        cur.close()

        return jsonify(users=data)

    except Exception as e:
        return jsonify(error=str(e))

if __name__ == '__main__':
    app.run(debug=True)


