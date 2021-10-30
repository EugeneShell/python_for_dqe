import datetime  # importing datetime module to handle with date
import os  # importing os module to handle with files
import CSV  # importing our CVS module to add functionality


class Post:  # creating parent class to further publications

    def __init__(self):
        self.text = input('Enter the publication text\nPrint here: ')


class News(Post):  # creating News class inherited on Post

    def __init__(self):
        super().__init__()  # calling parent class init features
        self.city = input('Enter the name of the city\n city: ')  # adding city attribute
        self.date = datetime.datetime.now()  # adding date attribute

    def __str__(self):  # formatting class output

        return (
            f'\nNews -------------------'
            f'\n{self.text}'
            f'\n{self.city}, {self.date.strftime("%d/%m/%Y %H.%M")}'
        )


class PrivateAd(Post):  # creating Private Ad class inherited on Post

    def __init__(self):
        super().__init__()  # calling parent class init features
        self.date = datetime.date.today()  # adding date attribute
        self.date_end_str = input('Enter the publication end date\nPrint date (in the format "dd.mm.yyyy"): ')
        self.date_end = datetime.datetime.strptime(self.date_end_str, '%d.%m.%Y').date()  # getting from user end date
        self.days_left = (self.date_end - self.date).days  # left days calculating

    def __str__(self):  # formatting class output

        return (
            f'\nPrivateAd --------------'
            f'\n{self.text}'
            f'\nActual until: {self.date_end.strftime("%d/%m/%Y")}, {self.days_left} days left'
        )


class Obituary(Post):  # creating Private Ad class inherited on Post

    def __init__(self):
        super().__init__()  # calling parent class init features
        self.burial_date = input(
            'Enter the burial date\nPrint date (in the format "dd.mm.yyyy"): ')  # adding burial date attribute
        self.burial_place = input('Enter the burial place\n burial place: ')  # adding burial place attribute
        self.city = input('Enter the name of the city\n city: ')  # adding city attribute
        self.date = datetime.datetime.now()  # adding date attribute

    def __str__(self):  # formatting class output

        return (
            f'\nObituary -------------'
            f'\n{self.city}, {self.date.strftime("%d/%m/%Y %H.%M")}'
            f'\n{self.text}'
            f'\nBurial Place and Date: {self.burial_place},{self.burial_date}'
            f'\nRest In Peace!'
        )


def menu():  # defining meny function

    print("--- Welcome to the newsfeed! ---")
    print("Menu:\n"
          "1 - News adding\n"
          "2 - Private ad adding\n"
          "3 - Obituary adding\n"
          "4 - Exit.")


def input_from_file():  # implementing function to adding data from file

    p = input("Input file path (if default, input 'default'): ")
    # according to the input, do record from file in default or exact directory to the target file
    if p == 'default':
        f1 = open('NewNewsFeed.txt', 'r')
        record = f1.read()
        f2 = open('NewsFeed.txt', 'a')
        f2.write('\n\n' + record)
        # close both files
        f1.close()
        f2.close()
        # delete file
        os.remove('NewNewsFeed.txt')
    else:
        f1 = open(p, 'r')
        record = f1.read()
        f2 = open('NewsFeed.txt', 'a')
        f2.write('\n\n' + record)
        # close both files
        f1.close()
        f2.close()
        # delete file
        os.remove(p)


def start():  # main start function implementing
    # adding choice of adding data
    ch = int(input("How would you prefer to add data\n 1) Extract from a file\n 2) Add manually\n"))
    if ch == 1:
        input_from_file()  # referencing to foo defined above
    elif ch == 2:

        menu()  # Calling a menu defined above
        choice = int(input("Your choice: "))  # Input user's choice

        while choice != 4:  # exit from app

            post = None

            if choice == 1:
                post = News()  # news posting
            elif choice == 2:
                post = PrivateAd()  # private ads posting
            elif choice == 3:
                post = Obituary()  # obituary posting
            else:
                print("Incorrect choice! Try again.")  # message about incorrect input value
            if post is not None:
                print(post)  # posting in console to check

            with open('NewsFeed.txt', 'a') as NewsFeed:  # appending to file
                print(post, file=NewsFeed)
            print("------------------------")
            print("                                                         ")
            menu()  # Main menu appears again while app is running
            choice = int(input("Your choice: "))

    CSV.Csvfile1.upd_f()  # after all adding words, letters and calcs to CSVs
    CSV.Csvfile2.upd_f()


start()


