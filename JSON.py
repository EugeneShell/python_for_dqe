import datetime  # importing datetime module to handle with date
import functions
import json

class Post: #creating parent class to further publications

    def __init__(self):

        self.text = input('Enter the publication text\nPrint here: ')

class News(Post): #creating News class inherited on Post

    def __init__(self):

        super().__init__() #calling parent class init features
        self.city = input('Enter the name of the city\n city: ') #adding city attribute
        self.date = datetime.datetime.now() # adding date attribute

    def __str__(self): #formatting class output

        return (
            f'\nNews -------------------'
            f'\n{self.text}'
            f'\n{self.city}, {self.date.strftime("%d/%m/%Y %H.%M")}'
        )

class PrivateAd(Post): #creating Private Ad class inherited on Post

    def __init__(self):

        super().__init__() #calling parent class init features
        self.date = datetime.date.today() # adding date attribute
        self.date_end_str = input('Enter the publication end date\nPrint date (in the format "dd.mm.yyyy"): ')
        self.date_end = datetime.datetime.strptime(self.date_end_str, '%d.%m.%Y').date() #getting from user end date
        self.days_left = (self.date_end - self.date).days #left days calculating

    def __str__(self): #formatting class output

        return (
            f'\nPrivateAd --------------'
            f'\n{self.text}'
            f'\nActual until: {self.date_end.strftime("%d/%m/%Y")}, {self.days_left} days left'
        )

class Obituary(Post): #creating Private Ad class inherited on Post

    def __init__(self):

        super().__init__() #calling parent class init features
        self.burial_date = input('Enter the burial date\nPrint date (in the format "dd.mm.yyyy"): ')#adding burial date attribute
        self.burial_place = input('Enter the burial place\n burial place: ')#adding burial place attribute
        self.city = input('Enter the name of the city\n city: ')#adding city attribute
        self.date = datetime.datetime.now()#adding date attribute

    def __str__(self): #formatting class output

        return(
            f'\nObituary -------------'
            f'\n{self.city}, {self.date.strftime("%d/%m/%Y %H.%M")}'
            f'\n{self.text}'
            f'\nBurial Place and Date: {self.burial_place},{self.burial_date}'
            f'\nRest In Peace!'
        )

def menu(): #defining meny function

    print("--- Welcome to the newsfeed! ---")
    print("Menu:\n"
          "1 - News adding\n"
          "2 - Private ad adding\n"
          "3 - Obituary adding\n"
          "4 - Exit.")

def start(): #main start function implementing

    menu() # Calling a menu
    choice = int(input("Your choice: "))    # Input user's choice

    while choice != 4: # exit from app

        post = None

        if choice == 1:
            post = News()  #  news posting
        elif choice == 2:
            post =PrivateAd() # private ads posting
        elif choice == 3:
            post = Obituary() # obituary posting
        else:
            print("Incorrect choice! Try again.") # message about incorrect input value
        if post is not None:
            print(post) #posting in console to check

        with open('NewsFeed.json', 'a') as NewsFeed: # appending to file
            normal_text(post)
            print(post, file=NewsFeed)
        print("------------------------")
        print("                                                         ")
        menu() # Main menu appears again while app is running
        choice = int(input("Your choice: "))
start()
