import os,sys
import subprocess

def isscafile(check_filename):
  scafiletypes=[ "rb","erb","sql","php","phtml","ctp","pks","pkh","pkb","xml","config","Config","settings","properties","xaml","baml","asp","vbscript","js","ini","bas","vbs","frm","ctl","html","htm","xsd","wsdd","xmi","py","mxml","cbl","wadcfg","wadcfgx","appxmanifest","wsdl","plist","page","ts","conf","json","yaml","yml"]
  for scatype in scafiletypes:
      if (check_filename.endswith(scatype)):
          return "true"   
  return "false"
dir = "."
if len(sys.argv) > 1:
    dir = sys.argv[1]
    for root, directories, filenames in os.walk(dir):
      for directory in directories:
         print( os.path.join(root, directory))
      for filename in filenames:
        
        if isscafile(filename) == "true":
        #filename.endswith(".php") or filename.endswith(".js") or filename.endswith(".html") or filename.endswith(".htm") or filename.endswith(".sql"):
          # print filename
          fullpath = os.path.join(root,filename)
          print("Fortify SCA Translating File:(" + fullpath + ")")
          subprocess.run(["sourceanalyzer", "-b", "demophp ", fullpath])
    #print(fname)
    subprocess.run(["sourceanalyzer", "-b", "demophp", "-show-files"])
else:
  print("Usage: scatranslatedir <directory>")