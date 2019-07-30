
#Compare Two FPRs
import pandas as pd
import logging

import os,sys
import subprocess
if len(sys.argv) > 2:
   fprone = sys.argv[1]
   fprtwo = sys.argv[2]

   with open("fprcompare.file1", "w") as file:
      subprocess.run(["FPRUtility.bat","-listIssues", "-project", fprone, "-search","-information","-queryAll", "-categoryIssueCounts","-outputFormat", "CSV"], stdout=file)

   with open("fprcompare.file2", "w") as file2:
      subprocess.run(["FPRUtility.bat","-listIssues", "-project", fprtwo, "-search","-information","-queryAll", "-categoryIssueCounts","-outputFormat", "CSV"],stdout=file2)

   #fprutility -listIssues -project webgoat.fpr -search -information -queryAll -categoryIssueCounts -outputFormat CSV > demofprutility.csv
   #fprutility -listIssues -project webgoat2.fpr -search -information -queryAll -categoryIssueCounts -outputFormat CSV > demofprutility2.csv

   log = logging.getLogger(__name__)
   first_dict=pd.read_csv('fprcompare.file1', header=0)
   first_dict=first_dict.applymap(str).groupby('path')['category'].apply(list).to_dict()
  
   second_dict=pd.read_csv('fprcompare.file2', header=0)
   second_dict=second_dict.applymap(str).groupby('path')['category'].apply(list).to_dict()

   fprdiff1 = { k :first_dict[k] for k in set(first_dict) - set(second_dict) }

   print("===============================================================")
   print("FPR Diff(" + fprone + ")")
   print("===============================================================")
   for path1 in fprdiff1.keys():
     print(path1)
   print("Total Diff: (" + str(len(fprdiff1.keys())) + ")" )
   print("===============================================================")

   fprdiff2 = { k : second_dict[k] for k in set(second_dict) - set(first_dict) }

   print("===============================================================")
   print("FPR Diff(" + fprtwo + ")")
   print("===============================================================")
   for path2 in fprdiff2.keys():
     print(path2)
   print("Total Diff: (" + str(len(fprdiff2.keys())) + ")" )
   print("===============================================================")
else:
    print("usage: fprcompare.py <FPR file > <FPR file>")
