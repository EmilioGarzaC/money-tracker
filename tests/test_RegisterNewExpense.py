
import modules.movementManagers.expenseManager as expenseManager

def test_ReturnsHello():
    expMan = expenseManager.ExpenseManager()
    assert expMan.test_func() == 1