from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# from flask_material import Material
# https://github.com/HellerCommaA/flask-materialize

app = Flask(__name__)
# Material(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/quienes-somos')
def quienes_somos():
    return render_template('quienes-somos.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')


if __name__ == '__main__':
    app.run(debug=True)