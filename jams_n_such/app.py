from flask import Flask, render_template

from controllers."controller_name" import "contoller_name"_blueprint

app = Flask(__name__)

app.register_blueprint("controller_name"_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)