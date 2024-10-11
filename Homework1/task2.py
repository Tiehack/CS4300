#Functions that return different data types 
def getInteger():
    return 42

def getFloat():
    return 3.14159

def getString():
    return "Hello, DevEdu!"

def getBoolean():
    return True

#Main script
if __name__ == "__main__":
    print("Integer:", getInteger())
    print("Float:", getFloat())
    print("String:", getString())
    print("Boolean:", getBoolean())

#Asserts the test cases using pytest
def testGetInteger():
    assert isinstance(getInteger(), int)
    assert getInteger() == 42

def testGetFloat():
    assert isinstance(getFloat(), float)
    assert getFloat() == 3.14159

def testGetString():
    assert isinstance(getString(), str)
    assert getString() == "Hello, DevEdu!"

def testGetBoolean():
    assert isinstance(getBoolean(), bool)
    assert getBoolean() is True