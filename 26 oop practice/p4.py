class train :
    def __init__(self,name,fare,seats) :
        self.name = name
        self.fare = fare 
        self.seats = seats
    def getStatus(self):
        print(f"available seats are: {self.seats}")
    def getFare(self):
        print(f"price of ticket per person is: {self.fare} Rs")
    def bookticket(self):
        if(self.seats>0):
            print(f"your tickeet is booked with seat number {self.seats}")
            self.seats = self.seats - 1
        else :
            print("Sorry, not enough seats are available")
    

rajdhani = train("rajdhani express",100,1)
rajdhani.getStatus()
rajdhani.getFare()
rajdhani.bookticket()
rajdhani.getStatus()
rajdhani.bookticket()
