def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    #write your logic here
    bill_amount=0
if(food_type=="N" and quantity_ordered>=1):
    if(distance_in_kms==0 or distance_in_kms<0):
        bill_amount=-1
    elif(distance_in_kms>=7):
        bill_amount=150*quantity_ordered+(distance_in_kms-6)*6+9
    elif(distance_in_kms>3 and distance_in_kms<=6):
        bill_amount=150*quantity_ordered+(distance_in_kms-3)*3
    elif(distance_in_kms!=0 or distance_in_kms<=3):
        bill_amount=150*quantity_ordered+distance_in_kms*0
    elif(food_type=="V" and quantity_ordered>=1):
        if(distance_in_kms==0 or distance_in_kms<0):
            bill_amount=-1
        elif(distance_in_kms>=7):
            bill_amount=120*quantity_ordered+(distance_in_kms-6)*6+9
        elif(distance_in_kms>3 and distance_in_kms<=6):
            bill_amount=120*quantity_ordered+(distance_in_kms-3)*3
        elif(distance_in_kms!=0 or distance_in_kms<=3):
            bill_amount=120*quantity_ordered+distance_in_kms*0
else:
           bill_amount=-1
return bill_amount
#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,-10)
print(bill_amount)

   
