# Railway Reservation System
class Pdetails:

    def setName(self, n):
        self.name = n

    def getName(self):
        return self.name

    def setAge(self, a):
        self.age = a

    def getAge(self):
        return self.age


class Ticket(Pdetails):

    def setFare(self,n):
        self.price = n

    def getFare(self):
        return self.price

    def setNumber(self, n):
        self.number = n

    def getNumber(self):
        return self.number

    def setTravel(self, s, d):
        self.source = s
        self.destination = d

    def getTravel(self):
        return self.source, self.destination


t1 = Ticket()
nam = input("Enter Name: ")
ag = int(input("Enter Age: "))
num = int(input("Enter Ticket Number: "))
s = input("Enter Source: ")
d = input("Enter destination: ")
f = input("Enter Fare: ")

t1.setName(nam)
t1.setAge(ag)
t1.setFare(f)
t1.setNumber(num)
t1.setTravel(s, d)
print("........")
print(f'Name : {t1.getName()}')
print(f'Age: {t1.getAge()}')
print(f'Ticket Number: {t1.getNumber()}')
print(f'Fare :{t1.getFare()}')
print(f'from {t1.getTravel()[0]} to {t1.getTravel()[1]}')