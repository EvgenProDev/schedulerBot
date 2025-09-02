Task Manager Telegram Bot

AUTHORS: Evgenii Prokopik

FILES: bot.py, tasks.json

DESCRIPTION:
The program implements a task manager, which can be used through the Telegram bot.
The program provides an interface for user to be able to interact with the list of their tasks and manage it as needed.
This program utilizes the python-telegram-bot Telegram API to access the user's information allow them to do the I/O operations.

The program supports the following commands:

/start: Displays a welcome message and the list of available commands.
/add <task>: Adds a new task to the task list.
/delete <task number>: Deletes a specific task by its number in the list.
/list: List all tasks currently saved in the user's task list.
/clear: Remove all tasks from user's list.
/help: Display the list of available commands.
/stop: Stop the bot from responding to new commands.

