import os

def startupMain():
  print("Manual Startup Enabled.")
  input("Follow Instructions in README.md, then press enter to continue\n")


  bot_id = input("What is the bot's ID? ")
  token = input("What is the bot's token? ")
  status = input("What do you want the bots status to be? ")
  with open('config.py', 'a') as f:
    f.write(f'\nAPPLICATION_ID = "{bot_id}"\nTOKEN = "{token}"\nSTATUS = "{status}"')
  print("Manual Config Completed!")
  os.remove("botStartup.py")
  quit("Run main.py again to run the bot")
