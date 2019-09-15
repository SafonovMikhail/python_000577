tasks = [9,8,7,6,5,4,3,2,1]
print("tasks: ", tasks)
latest_task_accomplished = tasks.pop(1)
print("latest_task_accomplished = tasks.pop(1): ", latest_task_accomplished)
tasks_accomplished = tasks
print("tasks:", tasks)
print(len(tasks))
print("tasks_accomplished: ", tasks_accomplished)
tasks_accomplished.append(tasks.pop(0)) # странная конструкция, сдвиг
print("tasks_accomplished: ", tasks_accomplished)
print("tasks: ", tasks)
print(len(tasks))
print("tasks_accomplished.insert(1, tasks.pop(1)): ")
tasks_accomplished.insert(1, tasks.pop(1))
print("tasks_accomplished: ", tasks_accomplished)
print("len(tasks_accomplished): ",len(tasks_accomplished))
# A time-saver: To pop the last element in a list, skip the index number.
# Leave the parentheses empty. Write:
print("latest_task_accomplished = tasks.pop()")
latest_task_accomplished = tasks.pop()
print("latest_task_accomplished: ", latest_task_accomplished)
latest_task_accomplished = tasks.pop()
latest_task_accomplished.insert(5, tasks.pop())
print("latest_task_accomplished:", latest_task_accomplished)

