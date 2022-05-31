import string
class Student:
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, name):
        self.name = name
          
        def check_name ():
            while True:
                if any(chr.isdigit() for chr in self.name):
                    self.name =  input('You entered a number. Enter text alone: ')
                
                else:
                    return self.name 
                    break

        name = check_name()
            
            

    def change_age(self, age):
 
        self.age = age
        
        def check_age ():

            def exp1():
                for i in self.age:
                    if i in string.punctuation:
                        return True

            def exp2():
                if any(chr.isalpha() for chr in self.age):
                    return True
            while True:
                if exp1() or exp2():
                    self.age =  input('You entered text/punctuation/decimal. Enter whole number alone: ')
                else:
                    return self.age
                    break

        

        age = check_age()


    def add_track(self, tracks):
        self.tracks = self.tracks + [''.join(tracks)]
        return self.tracks

        
    def get_score(self):
        self.score = float(self.score)
        return (self.score)

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
Isioma = Student(name="Isioma", age=22, tracks=["FE"],score=99)
Jane = Student(name="Janet", age=24, tracks=["FE"],score=50)

#First block. Doesn't Accept user input.

print('')
print ('First student\'s name is', Bob.name)
print ('First student\'s age is', Bob.age)
print ('First student\'s list of tracks is', Bob.tracks)
print('First score is', Bob.get_score())

Bob.change_name("Peter")
Bob.change_age('23')
Bob.add_track(["UI/UX"])

print('')
print ('Changed student\'s name is', Bob.name)
print ('Changed student\'s age is', Bob.age)
print ('Changed student\'s list of tracks is', Bob.tracks)
print('Score was unchanged and is', Bob.get_score())

#second block. Accepts User input

print('')
print ('Current student\'s name is', Bob.name)
print ('Current student\'s age is', Bob.age)
print ('Current student\'s list of tracks is', Bob.tracks)
print('Current score is', Bob.get_score())

while True:
    print('')
    Bob.change_name(input('Enter new name: '))
    Bob.change_age(input('Enter new age: '))
    Bob.add_track([input('Enter new track: ')])

    print('')
    print ('New student\'s name is', Bob.name)
    print ('New student\'s age is', Bob.age)
    print ('New student\'s list of tracks is', Bob.tracks)
    print('Student score was unchanged and is', Bob.get_score())

    leave = (input('Exit Editor? Y or N: '))
    if leave == 'Y':
        break
    else:
        continue








  


