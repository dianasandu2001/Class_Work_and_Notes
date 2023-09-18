scores = [78,89,64,23,100,99,75,57,86,56]
for score in scores:
    if score >= 90:
        print("A")
    elif score > 80:
        print("B")
    elif score > 70:
        print("C")
    elif score > 60:
        print("D")
    else:
        print("F")
