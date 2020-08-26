import os

class GreetingMessageGenerator:

  def greet_visitor(self, name: str, *names: [str]) -> str:
    visitor: str = name
    if name is None:
        visitor = "my friend"
    elif not name:
        visitor = "my friend"

    if visitor.isupper():
        return f"HELLO {self._create_visitor_list(visitor, *names)}!"
    else:
        return f"Hello, {self._create_visitor_list(visitor, *names)}."


  def _two_names_list(self, name1: str, name2: str) -> str:
    other: str = "my friend" if name2 is None else name2
    return f"{name1} and {other}"


  def _multiple_names_list(self, name: str, *names) -> str:
    names_list: str = name
    for i in range(len(names)):
        separator: str = ", " if i < len(names) - 1 else ", and "
        names_list += separator + names[i]

    return names_list


  def _create_visitor_list(self, name: str, *names: [str]) -> str:
    if names:
        if len(names) == 1:
            return self._two_names_list(name, names[0])
        else:
            return self._multiple_names_list(name, *names)

    return name


if __name__ == "__main__":
    os.system("pytest")  # comment out if needed
