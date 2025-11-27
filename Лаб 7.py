# Task 1
hashes = ("abc123", "ffd222", "9af010", "ffd222", "x0x0x0")
print(hashes.count("ffd222"))

# Task 2
users = ("guest", "moderator", "admin", "root")
print(users.index("admin"))

# Task 3
key_params = ("AES", 256, "CBC")
algorithm, key_size, mode = key_params
print("Algorithm:", algorithm)
print("Key size:", key_size)
print("Mode:", mode)

# Task 4
log = ("login", "download", "upload", "logout")
print(log[-1])

# Task 5
ips = ("192.168.0.1", "10.0.0.2", "172.16.0.3")
user_ip = input("Введите IP: ")
if user_ip in ips:
    print("Найдено")
else:
    print("Нет в списке")

# Task 6
name = input("Name: ")
role = input("Role: ")
status = input("Status: ")
user_data = (name, role, status)
print(user_data)

# Task 7
access = ("read", "write", "execute")
new_value = input("New value: ")
new_access = (access[0], new_value, access[2])
print(new_access)

# Task 8
attempts = ("success", "fail", "fail", "success", "fail", "fail")
print("Task 8 success:", attempts.count("success"))
print("Task 8 fail:", attempts.count("fail"))

# Task 9
admins = ("root", "admin")
users = ("alex", "bob")
all_users = admins + users
print(all_users)

# Task 10
logs = ("login", "upload", "download", "logout")
start, *middle, end = logs
print("Task 10 start:", start)
print("Task 10 middle:", tuple(middle))
print("Task 10 end:", end)