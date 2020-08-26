import os

def greet_visitor(name, *names):
    visitor = name
    if name is None:
        visitor = "my friend"
    elif not name:
        visitor = "my friend"

    if visitor.isupper():
        return "HELLO " + _create_visitor_list(visitor, *names) + "!"
    else:
        return "Hello, " + _create_visitor_list(visitor, *names) + "."


def _two_names_list(name1, name2):
    other = "my friend" if name2 is None else name2
    return name1 + " and " + other


def _multiple_names_list(name, *names):
    names_list = name
    for i in range(len(names)):
        separator = ", " if i < len(names) - 1 else ", and "
        names_list += separator + names[i]

    return names_list


def _create_visitor_list(name, *names):
    if names:
        if len(names) == 1:
            return _two_names_list(name, names[0])
        else:
            return _multiple_names_list(name, *names)

    return name


if __name__ == "__main__":
    os.system("pytest")  # comment out if needed