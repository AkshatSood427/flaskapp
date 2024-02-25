from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def rendfile():
    template_path = os.path.join(os.path.dirname(__file__), 'templates/home.html')
    return render_template(template_path)

if __name__ == '__main__':
    app.run(debug=True)
