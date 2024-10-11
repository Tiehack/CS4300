import numpy as np

#Creates a list and adds a constant value to each element
def addConstantToArray(arr, constant):
    return np.add(arr, constant)

#Function to perform matrix multiplication
def matrixMultiply(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

#Function to calculate the mean of an array
def calculateMean(arr):
    return np.mean(arr)

#Main script to demonstrate functionality
if __name__ == "__main__":
    arr = np.array([1, 2, 3, 4, 5])
    print("Original array:", arr)
    print("Array after adding 10:", addConstantToArray(arr, 10))

    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    print("Matrix multiplication result:", matrixMultiply(matrix1, matrix2))

    print("Mean of array:", calculateMean(arr))

#All of the matrix test cases using pytest
def testAddConstantToArray():
    arr = np.array([1, 2, 3])
    result = addConstantToArray(arr, 10)
    expected = np.array([11, 12, 13])
    assert np.array_equal(result, expected)

def testMatrixMultiply():
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    result = matrixMultiply(matrix1, matrix2)
    expected = np.array([[19, 22], [43, 50]])
    assert np.array_equal(result, expected)

def testCalculateMean():
    arr = np.array([1, 2, 3, 4, 5])
    result = calculateMean(arr)
    expected = 3.0
    assert result == expected