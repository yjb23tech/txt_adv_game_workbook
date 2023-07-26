print("Aim is to print the multiples of 2 using nested for loops")

print(" ") 

#We can control the zero based index boundaries of the range() function 
#Lower boundary can be brought forward i.e. in this instance, from 0 to 2 
#Upper boundary can be controlled; the real upper is one less than the one set i.e. although it is set as 3, because of the zero indexing, in reality is 2 
#So the range for loop (a) is actually a single index value of 2 i.e. this outer loop only runs once and the value of 'a' is only ever '2'  

#Within the single instance of loop (a) running however loop (b) runs many times 
#Lower boundary has been brought forward i.e. in this instance from 0 to 1
#Upper boundary is actually 10
#Loop therefore if range(11) was used would run 11 times (from 0 to 10) however because of lower boundary adjustment to range(1,11) loop runs 10 times i.e. from 1 to 10 

for a in range(2, 3):
    for b in range(1, 11):
        print(f"==> {(a*b)}")

print(" ")
