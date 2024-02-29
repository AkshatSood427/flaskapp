from flask import Flask, render_template

app = Flask(__name__)

name = 'Akshat Sood'

@app.route('/')
def rendfile():
    return render_template('addform.html')

if __name__ == '__main__':
    app.run(debug=True)

