import json
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import sys
#from telegram.ext.filters import filters
#from telegramext import Updater, CallbackContext

# Set your Telegram bot token here
TOKEN = 'YOUR_TOKEN'

# JSON file where tasks will be stored
TASKS_FILE = 'tasks.json'

'''
# Load existing tasks from the JSON file (if it exists)
def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return an empty list if the file does not exist or is empty


# Save tasks to the JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


# Command handler for '/start' command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Welcome! Send me a task, and I will save it for you.\n"
        "You can also view your tasks by typing /tasks."
    )


# Command handler for '/tasks' command to show saved tasks
def show_tasks(update: Update, context: CallbackContext) -> None:
    tasks = load_tasks()
    if tasks:
        task_list = "\n".join([f"{i + 1}. {task}" for i, task in enumerate(tasks)])
        update.message.reply_text(f"Your tasks:\n{task_list}")
    else:
        update.message.reply_text("You have no tasks yet.")


# Function to handle new tasks sent by the user
def add_task(update: Update, context: CallbackContext) -> None:
    task = update.message.text
    if task.startswith('/'):
        return  # Ignore commands

    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

    update.message.reply_text(f"Task added: {task}")

'''

#returns all the tasks from json file
def getTasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)

    except:
        return {}

#saves tasks on json file
def saveTasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

#prints the welcome message on the start of bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    newMessage = (
                "Welcome to taskManegerWPG_bot! \n"
                 + "type '/stop' - to stop the bot \n"
                  + "type '/add <yourTask>' - to add new task \n"
                  + "type '/delete <taskNumber>' - to delete a task \n"
                  + "type '/list' - to list all your tasks \n"
                  + "type '/help' - to view the list of available commands \n"
                  + "type '/clear' - to remove all tasks from your list"
                  )
    await update.message.reply_text(newMessage)


#stops the bot from responding to the new user's commands
async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    newMessage = ("Shutting down... \n"
                  + "You can press 'Stop' button to stop this bot from running"
                  )
    await update.message.reply_text(newMessage)

    if context.application:
        await context.application.stop()

#adds new task
async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    userID = str(update.message.from_user.id)
    newTask = " ".join(context.args)

    if not newTask:
        await update.message.reply_text("Please provide a task!")
        return

    tasks = getTasks()

    if userID not in tasks:
        tasks[userID] = []

    tasks[userID].append(newTask)
    saveTasks(tasks)

    await update.message.reply_text(f"Task added: {newTask}")



#deletes a specified task
async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    userID = str(update.message.from_user.id)
    tasks = getTasks()

    if userID not in tasks or not tasks[userID]:
        await update.message.reply_text("You do not currently have any tasks in your list")
        return

    else:
        try:
            taskIndex = int(context.args[0])-1

            if 0 <= taskIndex <= len(tasks[userID]):
                removedTask = tasks[userID].pop(taskIndex)
                saveTasks(tasks)
                await update.message.reply_text(f"Removed task: {removedTask}")
            else:
                await update.message.reply_text(f"Invalid task number: {taskIndex+1}")


        except:
            await update.message.reply_text("Something went wrong when deleting a task")


async def clearAll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    userID = str(update.message.from_user.id)

    tasks = getTasks()

    if userID not in tasks:
        await update.message.reply_text("No tasks to be deleted")



    else:

        if len(tasks[userID]) > 0:
            del tasks[userID]
            saveTasks(tasks)
            await update.message.reply_text("All tasks cleared")

        else:
            await update.message.reply_text("No active tasks to delete")

#lists al the current user's tasks
async def listTasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    userID = str(update.message.from_user.id)
    tasks = getTasks()

    if userID in tasks and tasks[userID]:
        tasksList = ""
        for num, text in enumerate(tasks[userID]):
            #tasksList = tasksList.join([f"{num}. {text}"])
            #tasksList = tasksList + "\n"
            tasksList += f"{num+1}. {text}" + "\n"
            #await update.message.reply_text(text)
        #task_list = "\n".join([f"{i + 1}. {t}" for i, t in enumerate(tasks[userID])])
        await update.message.reply_text(f"Your tasks:\n{tasksList}")

    else:
        await update.message.reply_text("You have no tasks yet.")


#prints the list of available commands
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    newMessage = (
            "LIST OF AVAILABLE COMMANDS: \n"
            + "type '/stop' - to stop the bot \n"
            + "type '/add <yourTask>' - to add new task \n"
            + "type '/delete <taskNumber>' - to delete a task \n"
            + "type '/list' - to list all your tasks \n"
            + "type '/help' - to view the list of available commands \n"
            + "type '/clear' - to remove all tasks from your list"
    )
    await update.message.reply_text(newMessage)

#prints the user's message (if not a command)
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #newMessage = update.message.text
    newMessage = "you sent smth!"
    await update.message.reply_text(newMessage)



# Main function to set up the bot
def main():

    '''
    # Create an Updater object and pass the bot token
    updater = Updater(TOKEN)

    # Register handlers
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("tasks", show_tasks))
    dispatcher.add_handler(MessageHandler(filters.text & ~filters.command, add_task))

    # Start polling to listen for messages
    updater.start_polling()

    # Run the bot until it is interrupted (Ctrl+C)
    updater.idle()
    '''


    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("stop", stop))
    application.add_handler(CommandHandler("add", add))
    application.add_handler(CommandHandler("delete", delete))
    application.add_handler(CommandHandler("list", listTasks))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("clear", clearAll))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling()


if __name__ == '__main__':
    main()
