
import modules.movementManagers.expenseManager as expenseManager

def test_ReturnsHello():
    expMan = expenseManager.ExpenseManager()
    assert expMan.test_func() == 1
    
    #gunicorn --bind=0.0.0.0 --timeout 600 flask/app:app