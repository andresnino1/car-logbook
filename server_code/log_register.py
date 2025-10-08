import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
@anvil.server.callable
def register_trip(date, odometer, usage_type, personal, work):
  if usage_type=="Mix":
    app_tables.logbook.add_row(date_end=date, odometer_end=odometer,usage_type=usage_type,total_distance=odometer)
    
  app_tables.logbook.add_row(date_end=date,odometer_end=odometer,usage_type=usage_type, )
  pass
  
@anvil.server.callable
def total_kms():
  total_kms = sum(row['total_distance'] for row in app_tables.logbook.search())
  return total_kms