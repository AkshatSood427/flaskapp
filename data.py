from flask import Flask , render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'akshat1'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'userdata'

mysql = MySQL(app)

@app.route('/')
def welcome():
    return render_template('home.html')

@app.route('/adduser')
def rendtemp():
    return render_template('addform.html')

@app.route('/adduser', methods = ['get','POST'])
def insertuser():
    name = request.form.get('name')
    email = request.form.get('email')

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (username , email) VALUES(%s , %s)", (name , email))

    cur.connection.commit()
    cur.close()

    return render_template('success.html', name = name)

if __name__ == '__main__':
    app.run(debug=True)




    

 