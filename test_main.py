from main import GreetingMessageGenerator

def test_greet_visitor_simple_hello_positive_case():
    assert GreetingMessageGenerator().greet_visitor("Bob") == "Hello, Bob."

def test_greet_visitor_none_as_input():
    assert GreetingMessageGenerator().greet_visitor(None) == "Hello, my friend."

def test_greet_visitor_empty_name_as_input():
    assert GreetingMessageGenerator().greet_visitor("") == "Hello, my friend."

def test_greet_visitor_shouting():
    assert GreetingMessageGenerator().greet_visitor("BOB") == "HELLO BOB!"

def test_greet_two_visitors():
    assert GreetingMessageGenerator().greet_visitor("Jill", "Jane") == "Hello, Jill and Jane."

def test_greet_two_visitors_first_one_none():
    assert GreetingMessageGenerator().greet_visitor(None, "Jane") == "Hello, my friend and Jane."

def test_greet_two_visitors_second_one_none():
    assert GreetingMessageGenerator().greet_visitor("Jill", None) == "Hello, Jill and my friend."

def test_greet_two_visitors_first_one_empty():
    assert GreetingMessageGenerator().greet_visitor("", "Jane") == "Hello, my friend and Jane."

def test_greet_three_visitors():
    assert GreetingMessageGenerator().greet_visitor("Amy", "Brian", "Charlotte") == "Hello, Amy, Brian, and Charlotte."

def test_greet_three_visitors_one_shouting():
    assert GreetingMessageGenerator().greet_visitor("Amy", "BRIAN", "Charlotte") == "Hello, Amy and Charlotte. AND HELLO BRIAN!"
