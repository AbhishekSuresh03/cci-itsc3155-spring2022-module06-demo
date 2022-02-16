from flask import Flask, render_template, request

app = Flask(__name__)

foods = []


@app.get('/')
def index():
    py_name = request.args.get('queryname')
    return render_template('index.html', name=py_name)


@app.get('/about')
def about():
    return render_template('about.html')


@app.post('/submit')
def submit():
    food = request.form.get('food', 'Nothing')
    foods.append(food)
    return render_template('submit.html', foods=foods)
