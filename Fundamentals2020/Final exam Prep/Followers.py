followers = {}

while True:

    commandif = input()
    if commandif == "Log out":
        break
    command = commandif.split(": ")

    cmd = command[0]
    username = command[1]

    if cmd == "New follower":

        if username not in followers.keys():
            likes = 0
            comments = 0
            followers[username] = [likes, comments]

    elif cmd == "Like":
        if username not in followers.keys():
            likes = int(command[2])
            comments = 0
            followers[username] = [likes, comments]
        else:
            comments = 0
            newlikes = int(command[2])
            likes = followers[username][0]
            followers[username] = [(likes + newlikes), comments]

    elif cmd == "Comment":
        if username not in followers.keys():
            comments = 1
            likes = 0
            followers[username] = [likes, comments]
        else:
            likes = followers[username][0]
            comments = followers[username][1]
            followers[username] = [likes, (comments + 1)]

    elif cmd == "Blocked":
        if username in followers.keys():
            followers.pop(username)
        else:
            print(f"{username} doesn't exist.")



followers = dict(sorted(followers.items(), key=lambda x: (-(x[1][0]), x[0])))
print(f"{len(followers.keys())} followers")
for i in followers.keys():
    print(f"{i}: {sum(followers[i])}")

