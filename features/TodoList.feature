Feature: To Do List Manager


  Scenario: Add a task to the to-do
    Given the to-do list is empty
    Then the to-do list should contain "Buy groceries"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task: |
      | Buy groceries |
      | Pay bills |
    When the user lists all tasks
    Then the output should contain:
      | Tasks:         |
      | Buy groceries |
      | Pay bills     |

  Scenario: Mark a task as completed
      Given the to-do list contains tasks:
      | Task | Status |
      | Buy groceries | Pending |
      When the user marks task "Buy groceries" as completed
      Then the to-do list should show task "Buy groceries" as completed

   Scenario: Clear the entire to-do list
      Given the to-do list contains tasks:
        | Task          |
        | Buy groceries |
        | Pay bills     |
      When the user clears the to-do list
      Then the to-do list should be empty

  Scenario: Edit a task
      Given the to-do list contains a task with title "Buy groceries" and description "Buy milk"
      When the user updates the task "Buy groceries" to have a new description "Buy bread and eggs"
      Then the task "Buy groceries" should have description "Buy bread and eggs"

  Scenario: Set and verify task priority
    Given the to-do list contains a task with title "Complete assignment" and priority "Medium"
    When the user updates the task "Complete assignment" to have a new priority "High"
    Then the task "Complete assignment" should have priority "High"

  
