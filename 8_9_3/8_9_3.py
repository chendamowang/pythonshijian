import re, os
 
regex = re.compile(r'\w*abc\w*\n')
for filename in os.listdir('.'):
   if filename.endswith('.txt'):
       print filename + ":"
       content = open(filename).read()
       match = regex.findall(content)
       print match
       for i in match:
           print i,
       
