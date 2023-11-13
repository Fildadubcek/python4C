class Student:
    def __init__(self, jmeno, prijmeni, hodnoceni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.hodnoceni = hodnoceni

    def info(self):
        print(f"Jméno: {self.jmeno}, příjmení: {self.prijmeni}, hodnocení: {self.hodnoceni}")

    def znamka(self):
        if self.hodnoceni > 90:
            print("Výborně")
        elif self.hodnoceni > 70:
            print("Dobře")
        elif self.hodnoceni > 50:
            print("Prospěl")
        else:
            print("Neprospěl")
        
student1 = Student("Jan", "Novák", 80)
student1.info()
student1.znamka()