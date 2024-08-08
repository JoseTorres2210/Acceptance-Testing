from behave import given, when, then
from TodoList import ToDoList

@given('the to-do list is empty')
def step_impl(context):
    context.TodoList = ToDoList()

@when('the user adds a task "{title}" with description "{description}" and due date "{due_date}"')
def step_impl(context, title, description, due_date):
    context.TodoList.add_task(title, description, due_date)

@then('the to-do list should contain "{title}"')
def step_impl(context, title):
    tasks = context.TodoList.list_tasks()
    assert any(title in task for task in tasks), f'Task "{title}" not found in the list.'

@given('the to-do list contains tasks')
def step_impl(context):
    context.TodoList = ToDoList()
    for row in context.table:
        context.TodoList.add_task(row['Task'], 'Sample description', '2024-08-01')

@when('the user lists all tasks')
def step_impl(context):
    context.tasks = context.TodoList.list_tasks()

@then('the output should contain')
def step_impl(context):
    for row in context.table:
        assert any(row['Tasks'] in task for task in context.tasks), f'Task "{row["Tasks"]}" not found in the list.'

@when('the user marks task "{title}" as completed')
def step_impl(context, title):
    result = context.TodoList.mark_task_completed(title)
    assert result, f'Could not mark task "{title}" as completed.'

@then('the to-do list should show task "{title}" as completed')
def step_impl(context, title):
    tasks = context.TodoList.list_tasks()
    assert any(f'{title} [Low] - Completed' in task for task in tasks), f'Task "{title}" not marked as completed.'

@when('the user clears the to-do list')
def step_impl(context):
    context.TodoList.clear_tasks()

@then('the to-do list should be empty')
def step_impl(context):
    tasks = context.TodoList.list_tasks()
    assert not tasks, "The to-do list is not empty."