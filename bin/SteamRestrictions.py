import os
import shutil
import VDF

steamapps = "C:\\Program Files (x86)\\Steam\\config\\steamapps.vrmanifest"


whitelist = {
  "VRChat",
  "Overwatch",
  # Steam stuff
  'Steam Controller Configs', 
  'Steamworks Shared',
}



def findAndRestrict(path):
  path = path + "\\steamapps\\common"
  dirs = set(os.listdir(path))
  dirs.difference(whitelist) 

  for app in dirs:
    loc = path + "\\" + app
    print("BAD: " + loc)
    
    print('icacls \"'+loc+'\" /t /inheritancelevel:r /c /deny Student:R')
    #shutil.rmtree(loc, ignore_errors=True)
    #os.mkdir(loc)
    newFile = open(loc+'\\restricted.txt', 'w')
    newFile.close()
    # res = os.popen('icacls \"'+loc+'\" /t /c /deny Student:R')

def logout():
  file = "C:\\Program Files (x86)\\Steam\\config\\loginusers.vdf"
  
  try:
    os.remove(file)
  except FileNotFoundError:
    print("Could not logout (probably doesn't exist)")

  newFile = open(file, 'w')
  newFile.close()

  

logout()

file = "C:\\Program Files (x86)\\Steam\\config\\libraryfolders.vdf" 
vd = VDF.PyVDF()
res = vd.read(file) 
paths = [res['libraryfolders'][item]['path'].replace("\\\\", "\\") for item in res['libraryfolders']]
for path in paths:
  findAndRestrict(path)
