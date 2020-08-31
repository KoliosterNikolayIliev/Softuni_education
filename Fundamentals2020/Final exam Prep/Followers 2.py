followers = {}

while True:
    command = input()
    if command == "Log out":
        break

    command = command.split(": ")
    cmd = command[0]
    username = command[1]

    if cmd == "New follower":
        likes = 0
        comments = 0
        if username not in followers.keys():
            followers[username] = [likes, comments]
    elif cmd == "Like":
        likes = int(command[2])

        if username not in followers:
            comments = 0
            followers[username] = [likes, comments]
        else:
            followers[username][0] += likes
    elif cmd == "Comment":
        if username not in followers:
            likes = 0
            comments = 0
            followers[username] = [likes, comments]
            followers[username][1] += 1
        else:
            followers[username][1] += 1

    elif cmd == "Blocked":
        if username not in followers:
            print(f"{username} doesn't exist.")
        else:
            del(followers[username])

followers = dict(sorted(followers.items(), key=lambda x: (-(x[1][0]), x[0])))
print(f"{len(followers)} followers")
for i in followers.keys():
    print(f"{i}: {sum(followers[i])}")


