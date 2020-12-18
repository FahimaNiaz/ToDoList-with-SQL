import PySimpleGUI as sg
from dbops import insert_into_tasks_table,select_statement, mark_task_as_complete,update_task

sg.theme('DarkTeal')

tasklist=select_statement()
todolist=[]


layout = [
     [sg.Text("Enter the task", font=("Arial", 14)), sg.InputText("", font=("Arial", 14), size=(20,1),key="taskname"),
     sg.Button("Add", font=("Arial", 14), key="add_save")],
    [sg.Listbox(tasklist, size=(40, 10), font=("Arial", 14), key='todolist', text_color= "black"), sg.Button("Edit", font=("Arial", 14)),
     sg.Button("Delete", font=("Arial", 14),key='delete')],
]


def delete_tasks(values):
    mark_task_as_complete(values['todolist'][0])
    update_UI()

def add_task(values):
    if window.FindElement('add_save').GetText()== 'Add':
        insert_into_tasks_table(values['taskname'])
    else:
        old_task = values['todolist'][0]
        new_task = values['taskname']
        update_task(old_task, new_task)
    update_UI()

   
def update_UI():    
    tasks=select_statement()
    window.FindElement('add_save').Update("Add")
    window.FindElement('taskname').Update('')
    window.FindElement('todolist').Update(values=tasks)
    window.FindElement('taskname').Update(value="")


def edit_tasks(values):
    window.FindElement('taskname').Update(value = values['todolist'][0])
    window.FindElement('add_save').Update("Save")
    window.FindElement('taskname').Update('')


if __name__ == '__main__':
    window = sg.Window("To-Do List with SQL", layout)

while True:
    event, values = window.Read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'add_save':
        add_task(values)
    elif event =='Edit':
        edit_tasks(values)
    if event == 'delete':
        delete_tasks(values)
      
window.Close()



