alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def binarySearch(alphabet,target):
   top = "A"
   bottom =len(alphabet)-1
   found = False
while(top<=bottom) :
   middle = (top + bottom)//2
   midpoint = alphabet[middle]
if midpoint == target:
   target = True
else:
 if "target" < midpoint:
   bottom = middle-1
 print ("going left")
 if alphabet < target:
   top = midpoint+1
 print ("going right")
 if midpoint==target:
    print("type a letter here")


 else:
    top = middle+1
    target= false

alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
print(binarySearch(alphabet, "A"))
print(binarySearch(alphabet, "Z"))
