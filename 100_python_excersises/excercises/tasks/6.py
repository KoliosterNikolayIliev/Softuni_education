# letters = [x for x in range(1, 21)]
# print(letters)

# myrange = range(10, 210, 10)
# print(list(myrange))

# letters = [x for x in range(10, 210, 10)]
# print(letters)

# letters = [str(x) for x in range(1, 21)]
# print(letters)
#
# my_range = range(1, 21)
# print(list(map(str, my_range)))

# a = ["1", 1, "1", 2]
# print(list(set(a)))
#
# a = ["1", 1, "1", 2]
# b = []
# [b.append(x) for x in a if x not in b]
# print(b)
#
# a = ["1", 1, "1", 2]
# from collections import OrderedDict
# print(list(OrderedDict.fromkeys(a)))

# mydict = {}
# mydict["a"], mydict["b"]=1, 2
#
# print(mydict)

# d = {"a": 1, "b": 2}
# print(d["b"])

# d = {"a": 1, "b": 2, "c": 3}
# print(d['a']+d['b'])
# d = {"a": 1, "b": 2}
# d["c"] = 3
# print(d)

# d = {"a": 1, "b": 2, "c": 3}
# print(sum(d.values()))

# d = {"a": 1, "b": 2, "c": 3}
# d2 = {k: v for k, v in d.items() if v <= 1}
# print(d2)
# from pprint import pprint
#
# d = {}
# d["a"] = list(range(1, 11))
# d["b"] = list(range(11, 21))
# d["c"] = list(range(21, 31))
# pprint(d)

# from pprint import pprint
#
# d = dict(a=list(range(1, 11)),
#          b=list(range(11, 21)),
#          c=list(range(21, 31))
#          )
# pprint(d["b"][2])

# d = dict(a=list(range(1, 11)),
#          b=list(range(11, 21)),
#          c=list(range(21, 31))
#          )
# for i in ["b", "c", "a"]:
#     print(f'{i} has value {d[i]}')

# [print(chr(x)) for x in range(97, 123)]
#
# import string
#
# for letter in string.ascii_lowercase:
#     print(letter)
# [print(x) for x in range(1,11)]
# def acceleration(v1, v2, t1, t2):
#     return (v2 - v1) / (t2 - t1)
#
#
# print(acceleration(0, 10, 0, 20))
# from math import pi
#
#
# def volume(h, r=10):
#     return (4 * pi * (r ** 3)) / 3 - (pi * (h ** 2) * (3 * r - h)) / 3
#
# print(volume(2))

# def foo(a=1, b=2):
#     return a + b
#
#
# x = foo() - 1
# print(x)

# def foo():
#     c = 1
#     return c
#
#
# print(foo())


# def word_counter(string):
#     a = string.split(' ')
#     return len(a)
#
#
# def filecheck():
#     file = 'C:\HOME\SKFUser\Desktop\\words1.txt'
#     with open(file, "r") as file:
#         result = word_counter(file.read())
#     return result
#
#
#
#
# print(filecheck())

# def count_words(filepath):
#     with open(filepath, 'r') as file:
#         string = file.read()
#         string2 = ''
#         for i in string:
#             if i == ',':
#                 i = ' '
#             string2 += i
#         string_list = string2.split(" ")
#         return len(string_list)
#
#
# print(count_words('C:\HOME\SKFUser\Desktop\\words2.txt'))
#
#
# def count_words(filepath):
#     with open(filepath, 'r') as file:
#         text = file.read()
#     text = text.replace(",", " ")
#     string_list = text.split(" ")
#     return len(string_list)
#
#
# print(count_words('C:\HOME\SKFUser\Desktop\\words2.txt'))
# import math
# print(math.sqrt(9))

# import math
# print(math.cos(1))

# import math
# print(math.pow(2, 3))

# def alphabet():
#     with open('C:\HOME\SKFUser\Desktop\\words3.txt', 'w') as file:
#         for x in range(97, 123):
#             file.write(chr(x) + '\n')
# alphabet()

# a = [1, 2, 3]
# b = (4, 5, 6)
# # c = []
# # for i in range(len(a)):
# #     c.append(a[i] + b[i])
# # [print(x) for x in c]
# [print(sum(x)) for x in zip(a, b)]

#
# def alphabet_double():
#     with open('C:\HOME\SKFUser\Desktop\\words3.txt', 'w') as file:
#         counter = 0
#         for x in range(97, 123):
#             if counter < 3:
#                 counter += 1
#             if counter<3:
#                 file.write(chr(x))
#             else:
#                 file.write(chr(x) + '\n')
#                 counter = 0
#
#
# alphabet_double()

# import string
#
# with open('C:\HOME\SKFUser\Desktop\\words3.txt', 'w') as file:
#
#     for l1, l2, l3 in zip(string.ascii_lowercase[0::3], string.ascii_lowercase[1::3],string.ascii_lowercase[2::3]):
#         file.write(l1 + l2 + l3 + '\n')

# import string
#
# for i in list(string.ascii_lowercase):
#     with open(f'C:\\HOME\\SKFUser\\Desktop\\new_folder\\{i}.txt', 'w') as file:
#         file.write(i)

# import string
#
# a = []
# for i in list(string.ascii_lowercase):
#     with open(f'C:\\HOME\\SKFUser\\Desktop\\new_folder\\{i}.txt', 'r') as file:
#         a.append(file.read())
#
# print(a)

# import glob
#
# letters = []
# file_list = glob.glob('C:\\HOME\\SKFUser\\Desktop\\new_folder/*.txt')
# for filename in file_list:
#     with open(filename, 'r') as file:
#         letters.append(file.read())
# print(letters)

# import string
#
# a = []
# for i in list(string.ascii_lowercase):
#     with open(f'C:\\HOME\\SKFUser\\Desktop\\new_folder\\{i}.txt', 'r') as file:
#         l = file.read()
#         if l in 'python':
#             a.append(l)
#
# print(a)

# for letter in "Hello":
#     if letter == "e":
#         print(letter)

# pa_ss = input("Please enter your password: ")

# age = int(input("What's your age? "))
# age_last_year = age - 1
# print("Last year you were %s." % age_last_year)

# print(type("Hey".replace("ey","i")[-1]))

# firstname = input("Enter first name: ")
# secondname = input("Enter second name: ")
# print("Your first name is %s and your second name is %s" % (firstname, secondname))

# d = {"employees":[{"firstName": "John", "lastName": "Doe"},
#                 {"firstName": "Anna", "lastName": "Smith"},
#                 {"firstName": "Peter", "lastName": "Jones"}],
# "owners":[{"firstName": "Jack", "lastName": "Petter"},
#           {"firstName": "Jessy", "lastName": "Petter"}]}
#
# d['employees'][1]['lastName']='Smooth'
# name = d['employees'][1]['lastName']
# print(d)

# d = {"employees":[{"firstName": "John", "lastName": "Doe"},
#                 {"firstName": "Anna", "lastName": "Smith"},
#                 {"firstName": "Peter", "lastName": "Jones"}],
# "owners":[{"firstName": "Jack", "lastName": "Petter"},
#           {"firstName": "Jessy", "lastName": "Petter"}]}
#
# d['employees'].append(dict())
# d['employees'][-1]['firstName'] = 'Albert'
# d['employees'][-1]['lastName'] = 'Bert'
# print(d)
# import json
#
# d = {"employees": [{"firstName": "John", "lastName": "Doe"},
#                    {"firstName": "Anna", "lastName": "Smith"},
#                    {"firstName": "Peter", "lastName": "Jones"}],
#      "owners": [{"firstName": "Jack", "lastName": "Petter"},
#                 {"firstName": "Jessy", "lastName": "Petter"}]}
#
# with open('C:\\HOME\\SKFUser\\Desktop\\names.json', 'w') as fp:
#     json.dump(d, fp, indent=4)

# import json
# from pprint import pprint
#
# with open('C:\\HOME\\SKFUser\\Desktop\\names.json', 'r') as fp:
#     pprint(json.load(fp))

# import json
#
#
# with open('C:\\HOME\\SKFUser\\Desktop\\names.json', 'r') as fp:
#     d = json.load(fp)
#     d['employees'].append(dict(firstName='Albert', lastName='Bert'))
# with open('C:\\HOME\\SKFUser\\Desktop\\names.json', 'w') as fp:
#     json.dump(d, fp, indent=4)

# import json
#
# with open('C:\\HOME\\SKFUser\\Desktop\\names.json', 'r+') as file:
#     d = json.load(file)
#     d['employees'].append(dict(firstName='Albert', lastName='Bert'))
#     file.seek(0)
#     json.dump(d, file, indent=4, sort_keys=True)
#     file.truncate()

# a = [1, 2, 3]
# for i in enumerate(a):
#     print(f'Item {i[1]} has index {i[0]}')

# from time import sleep
#
# counter = 0
# while True:
#     if counter == 4:
#         print("End of the Loop")
#         break
#     counter+=1
#     print('Hi')
#     sleep(counter)
#
# d = dict(weather = "clima", earth = "terra", rain = "chuva")
# word = input('Enter word:').lower()
# try:
#     print(d[word])
# except KeyError:
#     print('That word doesn\'t exist!')
# from pprint import pprint
#
# import requests
#
# r = requests.get('http://www.pythonhow.com/data/universe.txt', headers = {'user-agent': 'customUserAgent'})
#
# pprint(r.text)


# import requests
#
# r = requests.get('http://www.pythonhow.com/data/universe.txt', headers={'user-agent': 'customUserAgent'})
#
# data = r.text
# output = data.count('a')
# print(output)

# import webbrowser
#
# query = input("Input your query: ")
# webbrowser.open(f"https://google.com/search?q={query}")

# import webbrowser
#
# query = input("Input your query: ")
# webbrowser.open("https://google.com/search?q=%s" % query)

# import pandas
# from pandas import concat
#
# data_1 = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
# data_2 = pandas.read_csv("http://www.pythonhow.com/data/sampledata_x_2.txt")
# data_3 = concat((data_1, data_2))
# data_3.to_csv("sampledata_x_3.txt", index=False)

# import pandas
# import matplotlib.pyplot as plt
#
#
# data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
# data.plot(x='x', y='y', kind='scatter')
# plt.show()
# import calendar
#
# from datetime import date
# today = date.today()
# month = calendar.month_name[today.month]
# day = calendar.day_name[today.day]
#
# print(f'Today is {day}, {month} {today.day}, {today.year}')

# from datetime import datetime
#
# print(datetime.now().strftime("Today is %A, %B %d, %Y"))

# import datetime
# a = int(input('Please enter your age:'))
# current_year = datetime.datetime.now().year
# print(f'We think you were born back in {current_year-a}')

# import string
# import random
#
# LETTERS = string.ascii_letters
# NUMBERS = string.digits
# PUNCTUATION = string.punctuation
#
#
# def password_generator():
#     length = 6
#     printable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'
#     printable = list(printable)
#     random.shuffle(printable)
#     random_password = random.choices(printable, k=length)
#     random_password = ''.join(random_password)
#     return random_password

# print(password_generator())


# def password_checker():
#     import string
#     length = 5
#     LETTERS = string.ascii_letters.upper()
#     NUMBERS = string.digits
#     a = input('Please enter new password:')
#     counter_l = 0
#     counter_n = 0
#     for symbol in a:
#         counter_l += LETTERS.count(symbol)
#         counter_n += NUMBERS.count(symbol)
#     if counter_l != 0 and counter_n != 0 and len(a) >= length:
#         return 'Password is fine'
#     print('Password is not fine')
#     return password_checker()
#
#
# print(password_checker())
#
# while True:
#     psw = input("Enter new password: ")
#     if any(i.isdigit() for i in psw) and any(i.isupper() for i in psw) and len(psw) >= 5:
#         print("Password is fine")
#         break
#     else:
#         print("Password is not fine")

# def password_checker():
#     import string
#     length = 5
#     LETTERS = string.ascii_letters.upper()
#     NUMBERS = string.digits
#     a = input('Please enter new password:')
#     counter_l = 0
#     counter_n = 0
#     for symbol in a:
#         counter_l += LETTERS.count(symbol)
#         counter_n += NUMBERS.count(symbol)
#     ok = True
#     if counter_l == 0:
#         ok = False
#         print('You need at least one uppercase letter')
#     if counter_n == 0:
#         ok = False
#         print('You need at least one number')
#     if len(a) < length:
#         ok = False
#         print('You need at least 5 characters')
#     if ok:
#         return 'Password is fine'
#     return password_checker()
#
#
# print(password_checker())

# while True:
#     notes = []
#     psw = input("Enter password: ")
#     if not any(i.isdigit() for i in psw):
#         notes.append("You need at least one number")
#     if not any(i.isupper() for i in psw):
#         notes.append("You need at least one uppercase letter")
#     if len(psw) < 5:
#         notes.append("You need at least 5 characters")
#     if len(notes) == 0:
#         print("Password is fine")
#         break
#     else:
#         print("Please check the following: ")
#         for note in notes:
#             print(note)

# def password_checker():
#     import string
#     length = 5
#     LETTERS = string.ascii_letters.upper()
#     NUMBERS = string.digits
#     errors = []
#     u = input('Please enter new Username:')
#     b = check_username(u)
#     if b is False:
#         print('Username exists')
#         return password_checker()
#     print('Username is fine')
#     a = input('Please enter new password:')
#     counter_l = 0
#     counter_n = 0
#     for symbol in a:
#         counter_l += LETTERS.count(symbol)
#         counter_n += NUMBERS.count(symbol)
#
#     if counter_l == 0:
#         errors.append('You need at least one uppercase letter')
#     if counter_n == 0:
#         errors.append('You need at least one number')
#     if len(a) < length:
#         errors.append('You need at least 5 characters')
#     if len(errors) == 0:
#         return 'Password is fine'
#     print("Please check the following: ")
#     for error in errors:
#         print(error)
#     return password_checker()
#
#
# def check_username(username):
#     names_d = []
#     with open('users.txt', 'r') as file:
#         names = file.readlines()
#     for i in names:
#         names_d.append(i.strip('\n'))
#     if username in names_d:
#         return True
#     return False


# print(password_checker())

# import ephem
# jupiter = ephem.Jupiter()
# jupiter.compute('1230/1/1')
# distance_au_units = jupiter.sun_distance
# distance_km = distance_au_units * 149597870.691
# print(distance_km)

# from screeninfo import get_monitors
# for m in get_monitors():
#     w = m.width
#     h = m.height
#     print(f'Width: {w},  Height: {h}')


# import pyglet
#
# window = pyglet.window.Window()
#
# label = pyglet.text.Label('Hello, world',
#                           font_name='Times New Roman',
#                           font_size=36,
#                           x=window.width // 2, y=window.height // 2,
#                           anchor_x='center', anchor_y='center')
#
#
# @window.event
# def on_draw():
#     window.clear()
#     label.draw()
#
#
# pyglet.app.run()


# def stripList():
#     with open('countries_raw.txt', 'r') as file:
#         list_raw = file.readlines()
#     with open('countries.txt', 'w') as file:
#         [file.write(x) for x in list_raw if x.lower() != 'top of page\n' and len(x.strip()) != 1 and x != '\n']
#
#
# stripList()


# def only_country_list(list):
#     with open('countries.txt', 'r') as file:
#         ll = file.readlines()
#         ll = [x.strip('\n') for x in ll]
#         l = sorted([x for x in list if x in ll])
#     return l
#
#
#
# print(only_country_list(["Portugal", "Germany", "Munster", "Spain"]))

# def country_list(list):
#     with open('countries_missing.txt', '+r') as file:
#         ll = file.readlines()
#         ll = [x.strip('\n') for x in ll]
#         l = sorted(ll + list)
#     with open('countries_full.txt', 'w') as file2:
#         [file2.write(x + '\n') for x in l]
#
#
# country_list(["Portugal", "Germany", "Spain"])

# import pandas as pd
# df = pd.read_csv ('countries_by_area.txt')
# density = df['population_2013']/df['area_sqkm']
# df['Density'] = density
# df.sort_values("Density", axis = 0, ascending = False,
#                  inplace = True, na_position ='last')
# ll = df['country'].tolist()
# for x in range(5):
#     print(ll[x])

# import pandas
#
# data = pandas.read_csv("countries_by_area.txt")
# data["density"] = data["population_2013"] / data["area_sqkm"]
# data = data.sort_values(by="density", ascending=False)
#
# for index, row in data[:5].iterrows():
#     print(row["country"])

# import sqlite3
#
# con = sqlite3.connect("database.db")
# cur = con.cursor()
# cur.execute("SELECT country FROM countries WHERE area >=2000000")
# rows = cur.fetchall()
# con.close()
# for i in rows:
#     print(i[0])

# import sqlite3
#
# import pandas as pd
#
# con = sqlite3.connect("database.db")
# cur = con.cursor()
# df = pd.read_sql_query("SELECT * from countries", con)
#
# con.close()
# df.to_csv('countries_n.csv',index=False)

# import sqlite3
#
# import pandas
#
# con = sqlite3.connect("database.db")
# cur = con.cursor()
# cur.execute("SELECT country FROM countries WHERE area >=2000000")
# rows = cur.fetchall()
# con.close()
#
# df = pandas.DataFrame.from_records(rows)
# df.columns = ['Rank', 'Country', 'Area', 'Population']
# df.to_csv('countries_big_area.csv', index=False)
#
# def test1(a, *args):
#
#     l=args
#     print(l)
#     return [*args]
#
# print(test1(1, [1,2,3,4,5,6,7,8,9]))
# Unsuccessful
import csv
import sqlite3

# con = sqlite3.connect("database.db")
# cur = con.cursor()
# with open("ten_more_countries.txt", "r") as file:
#     rows = csv.reader(file)
#     print(list(rows))
#     for row in rows:
#         cur.execute("INSERT INTO countries VALUES (NULL,?,?,NULL)", (row["Country"],row["Area"]))
# con.commit()
# con.close()


# import sqlite3
# import pandas
#
# data = pandas.read_csv("ten_more_countries.txt")
#
# conn = sqlite3.connect("database.db")
# cur = conn.cursor()
# for index, row in data.iterrows():
#     print(row["Country"], row["Area"])
#     cur.execute("INSERT INTO countries VALUES (NULL,?,?,NULL)", (row["Country"], row["Area"]))
# conn.commit()
# conn.close()

# from glob import glob
#
# print(len(glob("exrcise_92/*.py", recursive=False)))

# from glob import glob
#
# print(len(glob("exercise_93/**/*.py",recursive=True)))

# urls = []
# with open("urls.txt", "r") as file:
#     for url in file.readlines():
#         # url = url.strip('\n')
#         url = url.replace("s", "", 1)
#         url = url.replace("/", "//", 1)
#         urls.append(url)
#     print(urls)
#
# with open("corrected_urls.txt", "w") as file:
#     for url in urls:
#         file.write(url)

# planets = input("Please enter value:").split(",")
#
# with open("Planets.txt", "a+") as file:
#     for planet in planets:
#         file.write(planet+"\n")
#

# from tkinter import *
# window=Tk()
#
# btn=Button(window, text="Add Line", fg='blue')
# btn.place(x=300, y=37)
# btn2=Button(window, text="Save changes", fg='blue')
# btn2.place(x=380, y=37)
# btn3=Button(window, text="Save and close", fg='blue')
# btn3.place(x=480, y=37)
# txtfld=Entry(window, text="This is Entry Widget", bd=5)
# txtfld.place(x=100, y=37)
#
# window.title('Hello Python')
# window.geometry("600x100+10+20")
# window.mainloop()
#
#
# file = open("Data.txt", "a+")
# while True:
#     data = input("Please enter value:")
#     if data == "CLOSE":
#         break
#     elif data == "SAVE":
#         file.close()
#         file = open("Data.txt", "a+")
#         continue
#     else:
#         file.write(data + "\n")

#Thinker progrm

# from tkinter import *
#
# window = Tk()
#
# file = open("user_gui.txt", "a+")
#
#
# def add():
#     file.write(user_value.get() + "\n")
#     entry.delete(0, END)
#
#
# def save():
#     global file
#     file.close()
#     file = open("user_gui.txt", "a+")
#
#
# def close():
#     file.close()
#     window.destroy()
#
#
# user_value = StringVar()
# entry = Entry(window, textvariable=user_value)
# entry.grid(row=0, column=0)
#
# button_add = Button(window, text="Add line", command=add)
# button_add.grid(row=0, column=1)
#
# button_save = Button(window, text="Save changes", command=save)
# button_save.grid(row=0, column=2)
#
# button_close = Button(window, text="Save and Close", command=close)
# button_close.grid(row=0, column=3)
#
# window.mainloop()


