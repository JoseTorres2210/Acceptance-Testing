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

@given('the to-do list contains a task with title "{title}" and description "{description}"')
def step_add_task_with_description(context, title, description):
    context.list_manager = ToDoList()
    context.list_manager.add_task(title, description, '2024-08-01')

@when('the user updates the task "{title}" to have a new description "{new_description}"')
def step_update_task_description(context, title, new_description):
    task_found = False
    for task in context.list_manager.tasks:
        if task.title == title:
            task.update(description=new_description)
            task_found = True
            break
    assert task_found, f'Task "{title}" not found.'

@then('the task "{title}" should have description "{expected_description}"')
def step_verify_task_description(context, title, expected_description):
    tasks = context.list_manager.list_tasks()
    task_str = next((task for task in tasks if title in task), None)
    assert task_str and expected_description in task_str, f'Task "{title}" does not have the expected description "{expected_description}".'

@given('the to-do list contains a task with title "{title}" and priority "{priority}"')
def step_add_task_with_priority(context, title, priority):
    context.list_manager = ToDoList()
    context.list_manager.add_task(title, 'Sample description', '2024-08-01', priority)

@when('the user updates the task "{title}" to have a new priority "{new_priority}"')
def step_update_task_priority(context, title, new_priority):
    task_found = False
    for task in context.list_manager.tasks:
        if task.title == title:
            task.update(priority=new_priority)
            task_found = True
            break
    assert task_found, f'Task "{title}" not found.'

@then('the task "{title}" should have priority "{expected_priority}"')
def step_verify_task_priority(context, title, expected_priority):
    tasks = context.list_manager.list_tasks()
    task_str = next((task for task in tasks if title in task), None)
    assert task_str and expected_priority in task_str, f'Task "{title}" does not have the expected priority "{expected_priority}".'