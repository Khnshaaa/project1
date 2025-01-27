#A recipe you are reading states how many grams 
# you need for the ingredient. Unfortunately, your store only 
# sells items in ounces. Create a function to convert grams
# to ounces. ounces = 28.3495231 * grams

def grams_ounces(grams):
    ounces = grams / 28.3495231
    return ounces
grams = 100
print(f"{grams} grams is equal to {grams_ounces(grams):.2f} ounces.")
