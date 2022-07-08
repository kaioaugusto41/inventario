import os
hostname = "10.180.1.32" #example
response = os.system("ping -n 2 " + hostname)

#and then check the response...
if response == 0:
  print(hostname, 'is up!')
else:
  print(hostname, 'is down!')