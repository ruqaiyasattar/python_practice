#3.10
print("\n Exercise 3.10")
river=['indus','jhelum','chenab','sutlej','kabul']
print("\n"+str(river))
print("Length od list "+str(len(river))+"\n")

river.reverse()
print("value in reverse order:\n"+str(river))

river.reverse()
print("\nhere is the original list \n"+str(river))


print("Here is the sorted list \n"+str(sorted(river)))
river.reverse()
river.sort()

print("sorting by sort() function\n"+str(river))

vanish='kabul'
river.remove(vanish)
print("remove() function \n"+str(river))
print("'"+vanish+"'"+" item in list is removed by using remove()\n")

rivers=river.pop()
print(rivers+" is removed from list by pop() function\n")

del river[0]
print("item at zero index is deleted by using del function \n"+str(river)+"\n")

river.insert(0,'new item')
print("new item at zero index is added by using insert()\n"+str(river))