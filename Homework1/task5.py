# List of favorite books with titles and authors
favorite_books = [
    ("The Catcher in the Rye", "J.D. Salinger"),
    ("To Kill a Mockingbird", "Harper Lee"),
    ("1984", "George Orwell"),
    ("Pride and Prejudice", "Jane Austen"),
    ("The Great Gatsby", "F. Scott Fitzgerald")
]

# Function to return the first three books using list slicing
def get_first_three_books():
    return favorite_books[:3]

# Dictionary representing a basic student database
student_database = {
    "Alice": 1001,
    "Bob": 1002,
    "Charlie": 1003,
    "David": 1004,
    "Eva": 1005
}

# Function to get student ID by name
def get_student_id(name):
    return student_database.get(name)

# Test cases using pytest

def test_get_first_three_books():
    expected_books = [
        ("The Catcher in the Rye", "J.D. Salinger"),
        ("To Kill a Mockingbird", "Harper Lee"),
        ("1984", "George Orwell")
    ]
    assert get_first_three_books() == expected_books

def test_get_student_id():
    assert get_student_id("Alice") == 1001
    assert get_student_id("Charlie") == 1003
    assert get_student_id("Eva") == 1005
    assert get_student_id("Unknown") is None  # Test case for non-existent student