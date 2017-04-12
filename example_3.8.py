#3.8 exercise
print("\n exercise 3.8\n")
places=['norway','sweden','iceland','austria','switzerland']
print("these".title()+" are the places"+" i".title()+" want to visit\n"+str(places))
print("\nAfter sorted:\n")

print(sorted(places))

print("\nStill in orginial order\n"+str(places)+"\n")


sorted(places,reverse=True)
print("sorted and revered in alphabetic order \n"+str(places)+"\n")

print("My list is still in orginal order: \n"+str(places)+"\n")
places.reverse()
print("list has been changed to reverse order via reverse()\n"+str(places)+"\n")
places.reverse()
print("Now again list is been changed to reverse order via reverse() \n"+str(places)+"\n")

places.sort(reverse=True)
print("list is sorted via sort() \n"+str(places))
