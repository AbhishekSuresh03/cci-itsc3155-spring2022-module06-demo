from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/result')
def result():
    number = request.args.get('number')
    try:
        number = int(number)
        is_integer = True
        is_even = number % 2 == 0
    except (TypeError, ValueError):
        is_integer = False
        is_even = False
    return render_template('result.html', number=number, is_integer=is_integer, is_even=is_even)


if __name__ == '__main__':
    app.run(debug=True)
