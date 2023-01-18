"""
Create a class named Course that has instance variables title, instructor, price, lectures, users(list type), ratings, avg_rating.

Implement the methods __str__, new_user_enrolled, received_a_rating and show_details.

From the above class, inherit two classes VideoCourse and PdfCourse.

The class VideoCourse has instance variable length_video and

PdfCourse has instance variable pages.

"""

class Course:
    def __init__(self, title, instructor, price):
        self.title = title
        self.instructor = instructor
        self.price = price
        self.users = []
        self.ratings = []
        self.lectures = []
        self.avg_rating = 0

    #Create a function to add a user
    def new_user_enrolled(self, user):
        dummy_list = self.users
        dummy_list.append(user)
        self.users = dummy_list

    #Create a function to add a rating
    def received_a_rating(self, rating):
        dummy_list = self.ratings
        dummy_list.append(rating)
        self.ratings = dummy_list
        #Now we will need to update the average rating
        number_to_assign = sum(dummy_list) / len(dummy_list)
        self.avg_rating = number_to_assign

    #Create a function to add a lecture
    def add_a_lecture(self, lecture):
        dummy_list = self.lectures
        dummy_list.append(lecture)
        self.lectures = dummy_list

    def __str__(self):
        return ("The title of the class is " + str(self.title)
        + "\nThe instructor is " + str(self.instructor)
        + "\nThe price is £" + str(self.price)
        + "\nThe average rating is " + str(self.avg_rating))

    #Note to Paul -- I was not sure what you had in mind for this functions so this was a guess
    def show_details(self):
        print("Here are the users: ")
        for user in self.users:
            print(str(user))
            print("\n")

        print("*"*10)
        print("\nHere are the ratings: ")
        for rating in self.ratings:
            print(str(rating))
            print("\n")

        print("*"*10)
        print("\nHere are the lectures: ")
        for lecture in self.lectures:
            print(str(lecture))
            print("\n")

jeff = Course("Jeff", "Paul", 100)
print(jeff.__str__())

jeff.new_user_enrolled("Tom")
jeff.received_a_rating(10)
print(jeff.avg_rating)
jeff.add_a_lecture("History of Water")
jeff.show_details()

class VideoCourse(Course):
    def __init__(self, title, instructor, price, length_video):
        super().__init__(title, instructor, price)
        self.length_video = length_video

class PdfCourse(Course):
    def __init__(self, title, instructor, price, pages):
        super().__init__(title, instructor, price)
        self.pages = pages