task_time = [int(x) for x in input().split(" ")]

command = input()

while command != "End":
    tokens = command.split(" ")
    cmd = tokens[0]
    if cmd == "Complete":
        index = int(tokens[1])
        if 0 <= index < len(task_time):
            task_time[index] = 0

    elif cmd == "Change":
        index = int(tokens[1])
        new_time = int(tokens[2])
        if 0 <= index < len(task_time):
            task_time[index] = new_time

    elif cmd == "Drop":
        index = int(tokens[1])
        if 0 <= index < len(task_time):
            task_time[index] = -1

    elif cmd == "Count":
        if tokens[1] == "Completed":
            compl_tasks = [x for x in task_time if x == 0]
            print(len(compl_tasks))

        elif tokens[1] == "Incomplete":
            incompl_tasks = [x for x in task_time if x > 0]
            print(len(incompl_tasks))

        elif tokens[1] == "Dropped":
            dropped_tasks = [x for x in task_time if x == -1]
            print(len(dropped_tasks))

    command = input()

list_incompl_tasks = [str(x) for x in task_time if x > 0]
print(" ".join(list_incompl_tasks))
