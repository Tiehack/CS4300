import os

#Counts words in the given text files 
def wordCountInFile(filePath):
    with open(filePath, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)

#Creates a list to hold readable files 
textFiles = ['sample1.txt', 'sample2.txt']

#Test cases for reading files 
def generationTest(metafunc):
    if "textFile" in metafunc.fixturenames:
        metafunc.parametrize("textFile", textFiles)

#Creates test cases based on file names 
def testWord(textFile):
    fileWordCount = {
        "sample1.txt": 8,
        "sample2.txt": 7
    }

    assert wordCountInFile(textFile) == fileWordCount[textFile]