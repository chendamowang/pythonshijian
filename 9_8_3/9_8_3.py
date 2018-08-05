import shutil, os, re

regex = re.compile(r'''
    (^spam)
    (\d+)
    ''',re.VERBOSE)
#sp_list= []
i = 1
workdir = os.path.abspath('.')
for filename in os.listdir('.'):
    n = regex.search(filename)
    
    if n != None:

        
        firstpart = n.group(1)
        secondpart = n.group(2)
        if int(secondpart) != i:
            oldfilename = os.path.join(workdir, filename)
            newfilename = os.path.join(workdir, 'spam'+'%03d'% i+'.txt')
            shutil.move(oldfilename, newfilename)
        
        i += 1
        
        #sp_list.append(secondpart)

#new_list = [x+1 for x in range(len(sp_list))]
#print new_list

#for i in range(len(sp_list)):
    #oldfilename = os.path.join(workdir, 'spam'+sp_list[i]+'.txt')
    #newfilename = os.path.join(workdir, 'spam'+'%03d'% new_list[i]+'.txt')
    #shutil.move(oldfilename, newfilename)
