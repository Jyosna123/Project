class InvalidPlaceException(Exception):
  message=""
  def __init__(self,message):
    self.message=message