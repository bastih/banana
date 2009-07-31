from registration import matches
from calculator import Calculator

@matches(r'Given the user opens the calculator')
def calculusInit(t):
    t.calculator = Calculator()
    
@matches(r'When entering (?P<num1>\d+) and (\d+)')
def calcAddNums(t, num1, num2):
    t.calculator.num1 = int(num1)
    t.calculator.num2 = int(num2)

@matches(r'Expect a result of (\d+)')
def expectedResult(t, result):
    assert t.calculator.sum() == int(result), "Correct result"
