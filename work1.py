e2f = dict (dog = 'chien', cat = 'chat', walrus = 'morse')
print (e2f)
print (e2f['walrus'])
f2e = {}
for english,french in e2f.items():
    f2e[french] = english

print (f2e)
print (f2e['chien'])

print (set(e2f.keys()))

life = {
    'animals':{
    'cats':['Henry','Grumpy','luce'],
    'octopy':{},
    'emus' : {}},
    'plants':{},
    'other':{}

}
print (life.keys())
print (life['animals'].keys())
print (life['animals']['cats'])
squares = {key: key*key for key in range(10)}
print (squares)
odd = { key for key in range(10) if key%2==1}
print (odd)
for thing in ('Got %s' % number for number in range(10)):
    print(thing)

keyzz = ('optimist','pessimist','troll')
valuezz = ('The glass is half full','The glass is half empty','How did you get a glass?')
slovar = dict(zip(keyzz,valuezz))
print (slovar)
