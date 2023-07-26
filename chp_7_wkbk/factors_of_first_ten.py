print("\nPrint out the factors for the first ten integers on the number line\n")

for a in range(1,11):
    factors = [] 
    for b in range(1, a + 1):
        if ((a % b) == 0):
            factors.append(b)
        else:
            print(f"{b} is NOT a factor of {a}")

    print(f"These are the factors of {a}: {factors}")
    print(" ")


