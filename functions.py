import mysql.connector
import time
from os import system, name


def Clear():

  # for windows
  if name == 'nt':
    _ = system('cls')

  # for mac and linux(here, os.name is 'posix')
  else:
    _ = system('clear')


def get_options(available_options, subheading):
  while True:
    print()
    print('   *** STUDENT REPORT ***')
    print()
    print('        ', subheading)
    print()

    for option in available_options:
      print(option[0].lower() + ' - ' + option)

    print()

    user_option = input("Enter Option : ").lower()

    alias_options = []

    for i in available_options:
      alias_options.append(i[0].lower())

    if user_option in alias_options:
      return user_option
    else:
      print("Invalid Option Selected")
      input("Press Enter to try again ... ")
      Clear()


def get_menu_options():
  main_menu_options = ('s', 'h', 'x')

  while True:
    print()
    print('STUDENT REPORT')
    print()
    print('s = START')
    print('h = HELP')
    print('x = EXIT')

    print()
    user_input = input("Enter an option : ")

    if user_input in main_menu_options:
      return user_input
    else:
      print()
      print(" Invalid Option Selected ! ")
      input(" Press Enter to retry .. ")
      Clear()


def Connect():
  try:
    global connection
    global cursor
    print()
    print()
    print('Connecting...')
    connection = mysql.connector.connect(host='hostname',
                                         user='username',
                                         password='password',
                                         database='databasename')
    Clear()
    if connection.is_connected():
      cursor = connection.cursor()
      print()
      print()
      print("Connected Succesfully")
      time.sleep(1)
    else:
      print()
      print()
      print("Unable To Connect Now . Try again later")
      input("Press Enter to retry...")
  except Exception as e:
    print()
    print()
    print(e)
    print("Unable To Connect Now . Try again later")
    input("Press Enter to retry...")


def Help():
  print()
  print("Help")
  print()
  input("Press Enter to Go Back...")


def Exit():
  print("See you Soon ..")
  time.sleep(2)
  exit()


def Add_record():
  #cursor = connection.cursor()
  cursor.execute('show tables')
  rec = cursor.fetchall()
  for i in rec:
    print(i)


def Show_record():
  #cursor = connection.cursor()
  cursor.execute('show tables')
  rec = cursor.fetchall()
  for i in rec:
    print(i)
  input('Press Enter to go back .. ')
