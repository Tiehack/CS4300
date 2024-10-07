def calculateDiscount(price, discountPercent):
        if discountPercent < 0 or discountPercent > 100:
            print("Discount must be between 0 and 100!")
        
        finalPrice = price * (1 - discountPrice / 100)
        return finalPrice

def testInt():
    assert calculateDiscount(100, 20) == 80
    assert calculateDiscount(50, 50) == 25

def testFloat():
    assert calculateDiscount(100.0, 15.5) == 84.5
    assert calculateDiscount(75.99, 10.5) == 67.98955

def testMixed():
    assert calculateDiscount(200, 12.5) == 175.0
    assert calculateDiscount(300.75, 25) == 225.5625

