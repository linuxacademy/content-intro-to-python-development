def print_todo(todo):
    """
    print_todo takes in a todo dictionary and prints it out
    with by separating the `name` from the `body` using a colon (:).

    >>> todo = {'name': 'Example 1', 'body': 'This is a test task'}
    >>> print_todo(todo)
    Example 1: This is a test task
    >>>
    """
    pass

def take_first(todos):
    """
    take_first receives a list of todos and removes the first todo
    and returns that todo and the remaining todos in a touple

    >>> todos = [{'name': 'Example 1', 'body': 'This is a test task', 'points': 3},
    ... {'name': 'Task 2', 'body': 'Yet another example task', 'points': 2}]
    >>> todo, todos = take_first(todos)
    >>> todo
    {'name': 'Example 1', 'body': 'This is a test task'}
    >>> todos
    [{'name': 'Task 2', 'body': 'Yet another example task'}]
    """
    return

def sum_points(todo1, todo2):
    """
    sum_points receives two todo dictionaries and returns sum of their `point` values.

    >>> todos = [{'name': 'Example 1', 'body': 'This is a test task', 'points': 3},
    ... {'name': 'Task 2', 'body': 'Yet another example task', 'points': }]
    >>> sum_points(todos[0], todos[1])
    5
    """
    return
