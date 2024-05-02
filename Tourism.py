import Invalid_place_exception as ie
import Passenger as ps
class Tourism:
  def __init__(self):
    self.passenger_list=[]
  def get_passenger_list(self):
    return self.__passenger_list
  def set_passenger_list(self,passenger_list):
    self.__passenger_list=passenger_list 
  def validate_place_name(self,place):
    try:
      places=["Beach","Pilgrimage","Heritage","Hill Station","Water Falls","Adventures"]
      if place in places:
        return True 
      else:
        raise ie.InvalidPlaceException("Invalid Place Name\n")
    except ie.InvalidPlaceException as e:
      return e.message 
  def add_passenger_details(self,passenger_name,place,no_of_days,no_of_tickets):
    passenger=ps.Passenger()
    passenger.set_passenger_name(passenger_name)
    passenger.set_place(place)
    passenger.set_no_of_days(no_of_days)
    passenger.set_no_of_tickets(no_of_tickets)
    passenger.calculate_bill_amount(place)
    self.passenger_list.append(passenger)
  def view_passenger_details(self,place):
    passengers=[]
    for i in self.passenger_list:
      if i.get_place()==place:
        passengers.append(i)
    return passengers