#example 3.4
print("Guest invitation example\n")
invitation=['daniel','john','michele']

print("whole list is :"+str(invitation))
print("I would like to invite you Mr "+invitation[0]+" for dinner"+"\n"+"I would like to invite you Mr "+invitation[1]+" for dinner"+"\n"+"I would like to invite you Mr "+invitation[2]+" for dinner")
print("Mr "+invitation[0]+" has busy schedule so he can't attend tonights' dinner invitation\n")
print("So i have modified invitation list")

invitation.insert(0,'david')
print(invitation)
print("I would like to invite you Mr "+invitation[0]+" for dinner"+"\n"+"I would like to invite you Mr "+invitation[1]+" for dinner"+"\n"+"I would like to invite you Mr "+invitation[2]+" for dinner"+"\nI would like to invite you Mr "+invitation[-1]+" for dinner")
print("\nAttention!".upper()+" Everyone "+"i have found bigger table for dinner".upper()+"\n")

invitation.insert(0,'charlie')
invitation.insert(int(len(invitation)/2),'ayaan')
invitation.append('hafeez')

print("I would like to invite you Mr "+invitation[0]+" for dinner"+"\n"+"I would like to invite you Mr "+invitation[1]+" for dinner"+"\n"+"I would like to invite you Mr "+invitation[2]+" for dinner"+"\nI would like to invite you Mr "+invitation[3]+" for dinner"+"\nI would like to invite you Mr "+invitation[4]+" for dinner"+"\nI would like to invite you Mr "+invitation[5]+" for dinner"+"\nI would like to invite you Mr "+invitation[-1]+" for dinner")
print("\nattention all".upper()+" i can only invite two guest to dinner\n")

last=invitation.pop(-1)
print("sorry ".title()+"mr ".title()+last+" I can't invite you in tonights' dinner")

sec_last=invitation.pop(-1)
print("sorry ".title()+"mr ".title()+sec_last+" I can't invite you in tonights' dinner")

third_last=invitation.pop(-1)
print("sorry ".title()+"mr ".title()+third_last+" I can't invite you in tonights' dinner")

four_last=invitation.pop(-1)
print("sorry ".title()+"mr ".title()+four_last+" I can't invite you in tonights' dinner")

fifth_last=invitation.pop(-1)
print("sorry ".title()+"mr ".title()+fifth_last+" I can't invite you in tonights' dinner")


#3.5 example
print("\nExample 3.5\n")
print("i have invited ".title()+str(len(invitation))+" guests")


del invitation[-1]
del invitation[-1]
print("\nhere is the empty list  \n".upper()+str(invitation))
