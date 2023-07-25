class Geoff:

    def __init__(age,company,school):
        self.__age = age
        self.__school = school
        self.company = company

    def print():
        print(f"Hi, I'm geoff. \n I'm {self.__age}" +
              f"I graduated from {self.__school}.\n" +
              f"I work for {self.company}")
    
    def setAge(age):
        self.__age = age
    def getAge():
        return self.__age

    def chat(conversation):
        return "I don't know that"
    
    def sayHi(name):
        return f"Hi,{name}! I am Geoff"

    def setSchool(school):
        self.__school = school
    def getSchool():
        return self.__school


if __name__ == "__main__":

    geoff = Geoff(31,"Deagu Univ.","Epsilon delta co.LTD.")

    geoff.print()
