import re


def test(password):
    isok = True
    testregex1 = re.compile(r'.{8,}')
    testregex2 = re.compile(r'[a-z]+[A-Z]+|[A-Z]+[a-z]+')
    testregex3 = re.compile(r'[0-9]+')
    if testregex1.search(password) == None:
        isok = False
    if testregex2.search(password) == None:
        isok = False
    if testregex3.search(password) == None:
        isok = False
    if isok == True:
        print 'ok'
    else:
        print 'low'

if __name__ == '__main__':
    test('AAAAAAAAAaaaa')
    test('aAaAA1')
    test('aaaaaaaaaaaaaaaaaaaa133')
    test('sdfSFSFdf234')
    test('13aFFFFFFFFFFF24')
