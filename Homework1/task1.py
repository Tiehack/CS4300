#Function to print the message
def printMessage():
    print("Hello, DevEdu!")

#Main script
if __name__ == "__main__":
    printMessage()

#Test function using pytest
def testMessage(capsys):
    #Capture the output using capsys
    printMessage()

    #Capture the printed output
    captured = capsys.readouterr()

    #Verifies the output
    assert captured.out.strip() == "Hello, DevEdu!"