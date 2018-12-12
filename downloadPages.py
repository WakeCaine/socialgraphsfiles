import subprocess
import time
import os
from pathlib import Path

#cmd = "curl -X GET 4cca81b39bfd2f9a60833874dda397007d895883:x-oauth-basic 'https://api.github.com/search/repositories?q=game&per_page=100&page=1' > 4.json"
#results = subprocess.run(cmd, shell=True, universal_newlines=True, check=True)

#print(results.stdout)
continued = False

leap_years = ['2012', '2016']
each_month_days = ['31', '28', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31']
year_start = 2018
count = 1
for years in range(1):
    for j in range(10,12):
        days = int(each_month_days[j]) if (year_start not in leap_years) and (j+1) != 2 else 29
        for k in range(days):
            for l in range(10):
                month = str(j + 1) if (j + 1) > 9 else ("0" + str(j + 1))
                day = str(k + 1) if (k + 1) > 9 else ("0" + str(k + 1))
                cmd = "curl -u wakecaine1:d32914c5efad243710c300019ccdcab61a76e2a5 -X GET 'https://api.github.com/search/repositories?q=game+created:%s-%s-%s&per_page=100&page=%s' > %s_%s_%s_%s.json" % (year_start,month,day, l+1, year_start,month,day,l+1)
                print(cmd)
                results = subprocess.run(cmd, shell=True, universal_newlines=True, check=True)
                fileName = "%s_%s_%s_%s.json" % (year_start,month,day,l+1)
                file = Path() / fileName  # or Path('./doc.txt')
                size = file.stat().st_size
                count += 1
                #if count % 30 == 0:
                #    print("SLEEEPING!!!!!!!!!!")
                #    time.sleep(15)
                if size < 2000:
                    break
            print("Date: %s_%s_%s" % (year_start,j+1,k+1))
    continued = True
    year_start = year_start + (years + 1)


#https://api.github.com/search/repositories?q=game+created:<2009-09-01&per_page=100&page=1
