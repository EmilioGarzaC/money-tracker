from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('charts.html')


@app.route('/submit-form', methods=['POST'])
def submit_form():
    amount = request.form.get('amount')
    description = request.form.get('description')
    date = request.form.get('date')

    return [amount, description, date]