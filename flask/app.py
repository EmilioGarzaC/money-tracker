from flask import Flask, render_template, request
from database.DDL.dim_moneyGroup import dimMoneyGroup
from database.DDL.dim_account import dimAccount
from database.DDL.fact_movement import factMovement

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
    # Get form field values
    
    requestData = {
        'amount': int(request.form.get('amount')),
        'description': request.form.get('description'),
        'dateId': int(request.form.get('date').replace('-', '')),
        'transactionTypeId': int(request.form.get('transactionType')),
        'accountId': int(request.form.get('accountDropdown')),
        'moneyGroupId': int(request.form.get('moneyGroupDropdown')),
    }
    
    
    
    # Insert record into fact
    factMovementController = factMovement()
    factMovementController.insert(**requestData)
    
    return requestData
    
    

    #  return [amount, movementType, moneyGroupDropdown, account, description, date]