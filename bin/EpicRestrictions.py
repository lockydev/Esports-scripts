import os
import json
import shutil

paths = [
  "C:\\ProgramData\\Epic\\UnrealEngineLauncher\\LauncherInstalled.dat", 
  "C:\\Users\\All Users\\Epic\\UnrealEngineLauncher\\LauncherInstalled.dat"
]

whitelist = [
  "602eb4abc8764c87b7f2607a1ef8c18e", # Valorant
  "Sugar", # Rocket League
  "64b0c77d07f644e6a2326a1fd7ab9926" # League of Legends
]



def findAndRestrict(file):
  f = open(file)
  lines = f.read()
  js = json.loads(lines)

  for app in js["InstallationList"]:
    if app["AppName"] not in whitelist:
      loc = app["InstallLocation"]
      print("BAD: " + app["InstallLocation"])
      
      print('icacls \"'+loc+'\" /t /inheritancelevel:r /c /deny Student:R')
      #shutil.rmtree(loc, ignore_errors=True)
      #os.mkdir(loc)
      newFile = open(loc+'\\restricted', 'w')
      newFile.close()
      # res = os.popen('icacls \"'+loc+'\" /t /c /deny Student:R')
    else:
      print("GOOD: " + app["InstallLocation"])

def logout():
  file = "C:\\Users\\"+os.getlogin()+"\\AppData\\Local\\EpicGamesLauncher\\Saved\\Config\\Windows\\GameUserSettings.ini"
  
  try:
    os.remove(file)
  except FileNotFoundError:
    print("Could not logout (probably doesn't exist)")
  newFile = open(file, 'w')
  newFile.close()

  

logout()
for path in paths:
  findAndRestrict(path)
