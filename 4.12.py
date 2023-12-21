class Student:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek
        self.predmety = []
        self.znamky = []

    def pridej_predmet(self, predmet):
        self.predmety.append(predmet)

    def ziskej_prumer(self):
        if not self.znamky:
            return 0
        return sum(self.znamky) / len(self.znamky)

    def pridej_znamku(self, znamka):
        self.znamky.append(znamka)

    def informace(self):
        print(f"Jméno: {self.jmeno}")
        print(f"Věk: {self.vek}")
        print(f"Seznam předmětů: {', '.join(self.predmety)}")
        print(f"Průměr: {self.ziskej_prumer()}")

class Teacher:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek
        self.predmety = []
        self.ziaci = []

    def pridat_studenta(self, student):
        self.ziaci.append(student)

    def odebrat_studenta(self, student):
        if student in self.ziaci:
            self.ziaci.remove(student)

    def informace(self):
        print(f"Jméno učitele: {self.jmeno}")
        print(f"Věk učitele: {self.vek}")
        print(f"Seznam předmětů: {', '.join(self.predmety)}")

# Ukázkové použití tříd
student1 = Student("Jan Novák", 15)
student1.pridej_predmet("Matematika")
student1.pridej_predmet("Čeština")
student1.pridej_znamku(90)
student1.pridej_znamku(85)

teacher1 = Teacher("Mgr. Karel Vomáčka", 35)
teacher1.pridat_studenta(student1)

student1.informace()
teacher1.informace()
