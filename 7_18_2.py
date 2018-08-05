import re

def mystrip(s, n=r'\s'):
    if n == r'\s':
        regex = re.compile(r'^%s*|%s*$' % (n, n))
    else:
        regex = re.compile(r'%s*' % n)
    
    s_strip = regex.sub(r'', s)
    return s_strip

print mystrip('    sdfsafa  sdfaf   ')
print mystrip(' adf')
print mystrip('aadfdf', 'a')
print mystrip('agggaagerwrccaa', 'a')
