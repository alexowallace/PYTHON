marks = {
    "harry" : 100,
    "ashok" : 99,
    "rohan" : 34,
    0 :70
}

marks ={} #empty dict
print(marks , type(marks))
print(marks["ashok"])
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"harry":80, "ashuka" :75})
print(marks)

print(marks.get("harry"))
a = marks.clear()
print(a)
print(marks , type(marks))

a = marks.pop("ashok",'99')
print(a)
print(marks , type(marks))

a = marks.popitem()
print(a)
print(marks , type(marks))

words= {
    "namaskar" : "hello",
    "tata" : "bye",
    "bihani " : "morning"
    
}

word = input("enter the word you want meaning of")
print(words[word])



d ={}

name = input("enter friends name: ")
lang= input("enter lang name:")
d.update({name:lang})

name = input("enter friends name: ")
lang= input("enter lang name:")
d.update({name:lang})

name = input("enter friends name: ")
lang= input("enter lang name:")
d.update({name:lang})

name = input("enter friends name: ")
lang= input("enter lang name:")
d.update({name:lang})

print(d)