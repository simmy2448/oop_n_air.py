class flight:
    def __init__(self,flight_no,origin,destination,depart_time,arrival_time,price):
        self.flight_number= flight_no
        self.origin = origin
        self.destination = destination
        self.departure_time = depart_time
        self.arrival_time = arrival_time
        self.price = price
    def f_info(self):
        return f"Flight {self.flight_number}: from {self.origin} to {self.destination} at Rs.{self.price}"
class user:
    def __init__(self):
        pass

    def login(self):
        print("Login First")
        password=input("Enter Password: ")
        cpass=input("Confirm Password: ")

        if password ==cpass:
            print("Password Matched")
            self.book_flight()
        else:
            print("password Doesn't match")
            return 

class flight_reservation:
    def __init__(self):
        
        self.flights=[
            flight("001", "DELHI", "AMRITSAR", "10:00", "12:00", 4500),
            flight("002", "AMRITSAR", "DELHI", "13:00", "15:00", 4500),
            flight("003", "MUMBAI", "AMRITSAR", "09:00", "12:30", 5500),
            flight("004", "DELHI", "CANADA", "20:00", "08:00", 75000),
            flight("005", "DELHI", "USA", "21:00", "09:00", 80000),
            flight("006", "DELHI", "UK", "22:00", "07:00", 70000),
            flight("007", "DELHI", "SINGAPORE", "11:00", "19:00", 35000),
            flight("008", "DELHI", "HONGKONG", "18:00", "01:00", 40000)]
        self.bookings=[]
        self.user=user()

    def menu(self):
        print("__________________  welcome  to  ABC AIrline __________________  ")
        print(" MENU >>>")
        print("Enter 1 to book a flight")
        print("Enter 2 to cancel a flight")
        print("ENter 3 to View avaiable flights")
        choice=int(input("Enter Your Choice "))
        return choice
        

    def view_flights(self):
        print("Available Flights")
        for flight in self.flights:
            print(flight.f_info())


    def book_flight(self):
        print("Welcome to book flight page")
        self.view_flights()

        flight_no=input("Enter the flight number you want to book: ")
        selected_flight=None
        for flight in self.flights:
            if flight.flight_number==flight_no:
                selected_flight=flight
                break
        if not selected_flight:
            print("invalid flight number!")
            return
        
        name = input("Enter your full name: ")
        age = input("Enter your age: ")
        passport = input("Enter your passport number: ")
        contact = input("Enter your contact number: ")
        booking = {
        'name': name,
        'age': age,
        'passport': passport,
        'contact': contact,
        'flight': selected_flight}
        
        self.bookings.append(booking)     
        print(f"flight {flight} is booked successfully!")
        print("Booking Confirmation Detail:")
        print(f"passenger: {name}, age:{age},passport:{passport}")
        print(selected_flight.f_info())
        print(f"Contact: {contact}")

    def cancel_flight(self):
        if not self.bookings:
            print("there is no booking to cancel.")
            return
        passport = input("enter your passport number to cancel booking: ")

        for booking in self.bookings:
            if booking['passport']== passport:
                self.bookings.remove(booking)
                print("booking cancelled successfully.")
                return
    print("booking is not found with your given passport number.")

    def run(self):
        while True:
            choice=self.menu()
            if choice==1:
                if self.user.login():
                    self.book_flight()
            elif choice== 2:
                self.cancel_flight()
            elif choice==3:
                self.view_flights()
            else:
                print("invalid choice")

            repeat=input("do you want to continue? (yes/no): ").lower()
            if repeat =="no":
                print("thank you for using ABC airlines. Have a nice day!")
                break

reservation= flight_reservation()
reservation.run()



    
    
