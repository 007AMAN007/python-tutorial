currentTasks = []
print("Your tasks to do:")
print(currentTasks)
i=0
while i<10:
  print("Enter 1 to display task(s), Enter 2 to add task, Enter 3 to delete task, Enter 0 to exit")
  option = raw_input()

  print("You have entered: "+option)

  if option == 2 or option == '2':
    task = raw_input("Enter task: ")
    currentTasks.append(task)
    print("Your tasks to do:")
    print(currentTasks)
    
  elif option == 3 or option == '3':
    task = raw_input("Enter task name to delete: ")
    currentTasks.remove(task)
    print("Your tasks to do:")
    print(currentTasks)

  elif option == 0 or option == '0':
    exit()

  elif option == 1 or option == '1':
    print("Your tasks to do:")
    print(currentTasks)
    
  else:
    print("Option not matched")
i+=1