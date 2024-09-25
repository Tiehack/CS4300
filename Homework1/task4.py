def calculateDiscount(price, discountPercent):
        if discountPercent < 0 or discountPercent > 100:
            print("Discount must be between 0 and 100!")
        
        finalPrice = price * (1 - discountPrice / 100)
        return finalPrice

