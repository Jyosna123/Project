import tourism as ts
import invalid_place_exception as ie
tourism=ts.Tourism()
n=int(input("Enter the number of registrations:\n"))
for i in range(n):
  print("Enter the registration details",str(i+1),":")
  passenger_name,place,no_of_days,no_of_tickets=input().split(":")
  status=tourism.validate_place_name(place)
  if status==True:
    tourism.add_passenger_details(passenger_name,place,int(no_of_days),int(no_of_tickets))
  else:
    print(status)
    continue 
s=input("Enter the place that needs to be searched:\n").strip()
p1=tourism.view_passenger_details(s)
if len(p1)!=0:
  for i in p1:
    print("Passenger Name ",i.get_passenger_name())
    print("Number od Days",i.get_no_of_days())
    print("Number of Tickets ",i.get_no_of_tickets())
    print("Bill Amount ",float(i.get_bill_amount()))
else:
  print("No Passengers found")