class Geoff:

    def __init__(age,company,school):
        self.age = age
        self.school = school
        self.company = company

    def print():
        print(f"Hi, I'm geoff. \n I'm {self.age}" +
              f"I graduated from {self.school}.\n" +
              f"I work for {self.company}")


if __name__ == "__main__":

    geoff = Geoff(31,"Deagu Univ.","Epsilon delta co.LTD.")

    geoff.print()