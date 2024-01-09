class Person:
    def __init__(self,name,age,gender,occupation,color):
        self.name=name
        self.age=age
        self.gender=gender
        self__occupation=occupation
        self.color=color

    def pozdrav(self):
        print(f"Ahoj volam sa {self.name} a mam {self.age} rokov a farbu oci {self.color}")

    def miesto(self):
        print(f"{self.name} ma bydlisko {self.occupation}")
    def vek_plus(self,a):
        b=self.age+a
        print("Moj pridany vek je",b)
    def vek(self):
        print(f"Moj skutocny vek je {self.age}")


patrik=Person("Patrik",30,"muz","Bratislava","modra")
patrik.pozdrav()


jan=Person("Jan",48,"muz","Bratislava","modra")
jan.name="peter"
print(jan.name)
jan.pozdrav()
jan.vek_plus(10)

jan.vek()
print(jan.color)

