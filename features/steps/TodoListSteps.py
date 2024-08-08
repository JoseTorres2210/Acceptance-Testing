from behave import given, when, then

# Define a list to represent the to-do list
to_do_list = []

# Define a variable to capture the output of listing tasks
output = ""

# Given the to-do list is empty
@given('the to-do list is empty')
def step_impl(context):
    global to_do_list
    to_do_list = []

# When the user adds a task "{task}"
@when('the user adds a task "{task}"')
def step_impl(context, task):
    global to_do_list
    to_do_list.append({'Task': task, 'Status': 'Pending'})

# Then the to-do list should contain "{task}"
@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    task_exists = any(item['Task'] == task for item in to_do_list)
    assert task_exists, f'Task "{task}" not found in the to-do list'

# Given the to-do list contains tasks:
@given('the to-do list contains tasks:')
def step_impl(context):
    global to_do_list
    to_do_list = [{'Task': row['Task'], 'Status': row.get('Status', 'Pending')} for row in context.table]

# When the user lists all tasks
@when('the user lists all tasks')
def step_impl(context):
    global output
    output = "Tasks:\n" + "\n".join(f"- {task['Task']}" for task in to_do_list)

# Then the output should contain:
@then('the output should contain:')
def step_impl(context):
    expected_output = context.text.strip()
    assert output.strip() == expected_output, f"Expected output:\n{expected_output}\nActual output:\n{output}"

# When the user marks task "{task}" as completed
@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    for item in to_do_list:
        if item['Task'] == task:
            item['Status'] = 'Completed'
            break

# Then the to-do list should show task "{task}" as completed
@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    task_found = next((item for item in to_do_list if item['Task'] == task), None)
    assert task_found is not None, f'Task "{task}" not found in the to-do list'
    assert task_found['Status'] == 'Completed', f'Task "{task}" is not marked as completed'

# When the user clears the to-do list
@when('the user clears the to-do list')
def step_impl(context):
    global to_do_list
    to_do_list = []

# Then the to-do list should be empty
@then('the to-do list should be empty')
def step_impl(context):
    assert len(to_do_list) == 0, "The to-do list is not empty"