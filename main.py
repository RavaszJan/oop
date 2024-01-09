class Person:
    def __init__(self,name,age,gender,occupation):
        self.name=name
        self.age=age
        self.gender=gender
        self._occupation=occupation


    def pozdrav(self):
        print(f"Ahoj volam sa {self.name} a mam {self.age} rokov ")

    def miesto(self):
        print(f"{self.name} ma bydlisko {self._occupation}")
    def vek_plus(self,a):
        b=self.age+a
        print("Moj pridany vek je",b)
    def vek(self):
        print(f"Moj skutocny vek je {self.age}")


class Student(Person):
    def __init__(self,name,age,gender,_occupation,score):
        super().__init__(name,age,gender,_occupation)
        self.score=score

    def jeGenius(self):
        if self.score>90:
            print(f"{self.name} je genius a {self.gender}")
        else:
            print(f"{self.name} nie je genius a {self.gender}")

patrik=Student("Patrik",30,"muz","Bratislava",70)
patrik.jeGenius()



jan=Person("Jan",48,"muz","Bratislava")
jan.name="peter"
print(jan.name)
jan.miesto()
jan.vek_plus(10)

jan.vek()

