f = open("http_access_log","r+")
for line in f:
   print line.split(' - - ')[0]

for datetime in f:
   print datetime.strptime(' ] ')



