largest=0
for i in range (100,1000):
    for j in range (100,1000):
        product = i*j
        str1 = str(product)
        if str1 == str1[::-1]:
            if product > largest:
                largest = product
print(largest)