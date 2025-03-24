import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def manage_todo():
    todos = []
    print("Simple To-Do List App")
    logger.info("To-Do List App started")
    
    while True:
        action = input("Enter 'add', 'list', or 'exit': ").lower()
        if action == "add":
            task = input("Enter task: ")
            todos.append(task)
            logger.info("Task added: %s", task)
            print(f"Added: {task}")
        elif action == "list":
            if not todos:
                print("No tasks yet!")
                logger.warning("Task list is empty")
            else:
                print("Your tasks:")
                for i, task in enumerate(todos, 1):
                    print(f"{i}. {task}")
                logger.info("Task list displayed, count: %d", len(todos))
        elif action == "exit":
            print("Goodbye!")
            logger.info("To-Do List App exited")
            break
        else:
            print("Invalid option!")
            logger.error("Invalid input: %s", action)

if __name__ == "__main__":
    manage_todo()