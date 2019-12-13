a = 'some_string'
id(a)
id('some' + '_' + 'string')


a = 'wtf'
b = 'wtf'
a is b
# ?

a = 'wtf!'
b = 'wtf!'
a is b
# ?

a, b = 'wtf!', 'wtf!'
a is b
# ?


'a' * 20 is 'aaaaaaaaaaaaaaaaaaaa'
'a' * 21 is 'aaaaaaaaaaaaaaaaaaaaa'  # python2/python3
