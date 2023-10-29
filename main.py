from functions import Clear,Connect,Help,Exit,get_options,Add_record,Show_record

# Main Program
connected=False

while True:

  main_menu_options = ('START', 'HELP', 'EXIT')
  user_input = get_options(main_menu_options, 'MAIN MENU')

  if user_input == 's':
    Clear()
    if connected == False:
      Connect()
      connected = True
    Clear()

    while True:

      start_menu_options = ('ADD RECORDS', 'SHOW RECORDS', 'BACK')
      user_input = get_options(start_menu_options,'')

      if user_input == 'a':
        Clear()
        Add_record()
        Clear()

      elif user_input == 's':
        Clear()
        Show_record()
        Clear()

      elif user_input == 'b':
        Clear()
        break

  elif user_input == 'h':
    Clear()
    Help()
    Clear()

  elif user_input == 'e':
    Clear()
    Exit()
