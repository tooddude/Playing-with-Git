import re
import shutil
import datetime
import os
from datetime import date, timedelta

# curent date
# add this to the end of the next statement to go back a day 
#now = datetime.datetime.now() -timedelta(days=1)
now = raw_input("Enter Newsletter drop date (YYYYMMDD): ") 
#now = datetime.datetime.now() 


strToday = 'NL_' + now
print now
print strToday
t = now[0:4] + '_' + now[4:6] +  '_' + now[6:8]
print t
strToday_YYYY_MM_DD =  now[0:4] + '_' + now[4:6] +  '_' + now[6:8]
strToday_YYYYspMMspDD = now[0:4] + ' ' + now[4:6] +  ' ' + now[6:8]
strToday_YYYYMMDD = now 

# variables
outFileDir = 'E:\\Database\\BNJ\\11-005\\' + strToday + '\\'
templateDir = 'E:\\Database\\BNJ\\11-005\\Template\\'
automationDir = 'E:\\Database\\BNJ\\11-005\\Automation\\'

#outFile = inFileDir + 'Qwest_10_136_Step_1_processing.yxmd'
# create the new directories
if not os.path.exists(outFileDir):
  os.makedirs(outFileDir)

# ***** YXMD FILE FOR PROCESSING IN DB STUDIO
# get all files from the template dir
for subdir, dirs, files in os.walk(templateDir):
   for file in files :
      print file
      # open the template file
      fileRead = open(templateDir + file,'r')
      # change the date in the template file
      memFile = re.sub('2011_03_30', strToday_YYYY_MM_DD, fileRead.read())
      memFile = re.sub('20110330', strToday_YYYYMMDD, memFile)
      memFile = re.sub('2011 03 30', strToday_YYYYspMMspDD, memFile)
      
      # write the changed file to the date file to the date directory
      fileWrite = open(outFileDir + file,'w')
      fileWrite.write(memFile)
      fileWrite.close()
