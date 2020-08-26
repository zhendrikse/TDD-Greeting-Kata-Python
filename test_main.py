from main import GreetingMessageGenerator

def testGreetVisitorSimpleHelloPositiveCase():
    assert GreetingMessageGenerator().greet_visitor("Bob") == "Hello, Bob."

def testGreetVisitorNoneAsInput():
    assert GreetingMessageGenerator().greet_visitor(None) == "Hello, my friend."

def testGreetVisitorEmptyNameAsInput():
    assert GreetingMessageGenerator().greet_visitor("") == "Hello, my friend."

def testGreetVisitorShouting():
    assert GreetingMessageGenerator().greet_visitor("BOB") == "HELLO BOB!"

def testGreetTwoVisitors():
    assert GreetingMessageGenerator().greet_visitor("Jill", "Jane") == "Hello, Jill and Jane."

def testGreetTwoVisitorsFirstOneNone():
    assert GreetingMessageGenerator().greet_visitor(None, "Jane") == "Hello, my friend and Jane."

def testGreetTwoVisitorsSecondtOneNone():
    assert GreetingMessageGenerator().greet_visitor("Jill", None) == "Hello, Jill and my friend."

def testGreetTwoVisitorsFirstOneEmpty():
    assert GreetingMessageGenerator().greet_visitor("", "Jane") == "Hello, my friend and Jane."

def testGreetThreeVisitors():
    assert GreetingMessageGenerator().greet_visitor("Amy", "Brian", "Charlotte") == "Hello, Amy, Brian, and Charlotte."

def testGreetThreeVisitorsOneShouting():
    assert GreetingMessageGenerator().greet_visitor("Amy", "BRIAN", "Charlotte") == "Hello, Amy and Charlotte. AND HELLO BRIAN!"
