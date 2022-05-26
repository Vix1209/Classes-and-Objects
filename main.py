class Student:
    def __init__(self, name, age, track, score):
        self.name = name 
        self.age =  int(age)
        self.track = track
        self.score = float(score) 
        # print (f'{self.name}, {self.age}, {self.track}, {self.score}')
        
        
    def change_name(self, name2):
        self.name = name2
        print (f'{self.name}, {self.age}, {self.track}, {self.score}')

            
    def change_age(self, age2):
        self.age = age2
        print (f'{self.name}, {self.age}, {self.track}, {self.score}')


    def add_track(self, track2):
        self.track = track2 
        print (f'{self.name}, {self.age}, {self.track}, {self.score}')

    
    def get_score(self, score2):
        self.score = score2
        return self.score
    
        
Bob = Student("John", 26, ["FE","BE"], 20.90)

Bob.change_name('Peter')

Bob.change_age(34)

Bob.add_track("UI/UX")

print(Bob.get_score(float(input('Input new score: '))))
