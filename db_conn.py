class Connection:
  def __init__(self, name, password):
    self.name = name
    self.password = password
    

def get_conn():
  return Connection(
    "test",
    "1234"
  )
  
