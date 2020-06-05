from main import greet_visitor

def testGreetVisitorSimpleHelloPositiveCase():
    assert greet_visitor("Bob") == "Hello, Bob."

def testGreetVisitorNoneAsInput():
    assert greet_visitor(None) == "Hello, my friend."

def testGreetVisitorEmptyNameAsInput():
    assert greet_visitor("") == "Hello, my friend."

def testGreetVisitorShouting():
    assert greet_visitor("BOB") == "HELLO BOB!"

def testGreetTwoVisitors():
    assert greet_visitor("Jill", "Jane") == "Hello, Jill and Jane."

def testGreetTwoVisitorsFirstOneNone():
    assert greet_visitor(None, "Jane") == "Hello, my friend and Jane."

def testGreetTwoVisitorsSecondtOneNone():
    assert greet_visitor("Jill", None) == "Hello, Jill and my friend."

def testGreetTwoVisitorsFirstOneEmpty():
    assert greet_visitor("", "Jane") == "Hello, my friend and Jane."

def testGreetThreeVisitors():
    assert greet_visitor("Amy", "Brian", "Charlotte") == "Hello, Amy, Brian, and Charlotte."

def testGreetThreeVisitorsOneShouting():
    assert greet_visitor("Amy", "BRIAN", "Charlotte") == "Hello, Amy and Charlotte. AND HELLO BRIAN!"
