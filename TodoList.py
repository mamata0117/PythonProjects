tasks_lists=[]
while True:
    print('Enter what you want to do:\n')
    option=int(input('1.Add a task \n 2.View tasks \n3.Remove task\n 4.Exit \n' )) 
    match option:
        case 1:
            work=input('Enter the task you want to perform :\n')
            tasks_lists.append(work)
            # append is used to add an element to the end of the list
            print('Task added successfully')
        case 2:
            if len(tasks_lists)==0:
                print('No task to display')
            else:
                print('Tasks:')
                for i,task in enumerate(tasks_lists):
                    print(f"{i+1}. {task}")
# enumerate is used to get the index and value of the list
        case 3:
          if len(tasks_lists)==0:
              print("No task to remove")
          elif tasks_lists<0 or tasks_lists>=len(tasks_lists):
              print("Invalid task number")
          else:
              task_num=int(input('Enter the task number you want to remove:\n'))
              tasks_lists.pop(task_num-1)
              # pop is used to remove an element from the list
              print('Task removed successfully')    
        case 4:
            print('Exiting the program...')
            break
        case _:
            print('Invalid option')