from flask import Flask, render_template, request
from database.DDL.dim_moneyGroup import dimMoneyGroup
from database.DDL.dim_account import dimAccount

app = Flask(__name__)


@app.route('/')
def hello():
    moneyGroupController = dimMoneyGroup()
    accountController = dimAccount()
    
    return render_template(
        'charts.html', 
        moneyGroups = [[i[0], i[1]] for i in moneyGroupController.getAll()],
        accounts = [[i[1], i[2], i[0]] for i in accountController.getAll()]
    )


@app.route('/submit-form', methods=['POST'])
def submit_form():
    amount = request.form.get('amount')
    movementType = request.form.get('movementType')
    moneyGroupDropdown = int(request.form.get('moneyGroupDropdown'))
    account = int(request.form.get('accountDropdown'))
    description = request.form.get('description')
    date = request.form.get('date')
    
    

    return [amount, movementType, moneyGroupDropdown, account, description, date]