#List of all favorite books 
books = [
    ("Harry Potter", "J.K. Rowling"),
    ("The Hunger Games", "Suzanne Collins"),
    ("Diary of a Wimpy Kid", "Jeff Kinney"),
    ("The Great Gatsby", "F. Scott Fitzgerald"),
    ('Marvel Comics', "Stan Lee")
]

#Slices the list and gets first three books 
def getFirstThreeBooks():
    return books[:3]

#Dictionary representing a student database
studentDatabase = {
    "Nick": 63,
    "Dirceu": 64,
    "Albert": 65,
    "Autumn": 66,
    "Katie": 67
}

#Function to get student ID by name
def getStudentID(name):
    return studentDatabase.get(name)

#Test cases using pytest
def testGetFirstThreeBooks():
    expectedBooks = [
        ("Harry Potter", "J.K. Rowling"),
        ("The Hunger Games", "Suzanne Collins"),
        ("Diary of a Wimpy Kid", "Jeff Kinney"),
    ]
    assert get_first_three_books() == expected_books

def testGetStudentID():
    assert getStudentID("Nick") == 63
    assert getStudentID("Dirceu") == 64
    assert getStudentID("Albert") == 65
    assert getStudentID("Autumn") == 66
    assert getStudentID("Katie") == 67