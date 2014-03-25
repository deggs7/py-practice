
class Test(object):
    name = 'origin'

t = Test()

all = [ 'a',
       1,
       t,
       ['a', 'b', 'c'],
       ('x', 'y', 'z'),
       {
           'name': 'abc',
           'desc': 'xyc'
       }
      ]


def change(n):
    print id(n)
    if type(n) == str:
        n = 'b'
    elif type(n) == int:
        n = 2
    elif type(n) == list:
        n.append('d')
    elif type(n) == tuple:
        n = ('b', 'c', 'd')
    elif type(n) == dict:
        n['update'] = 'ok'
    elif type(n) == Test:
        n.name = 'okokok'
    print id(n)


for x in all:
    if type(x) == Test:
        print x.name
    else:
        print x
    change(x)
    print '-----------function------------'
    if type(x) == Test:
        print x.name
    else:
        print x
    print '==============================='
