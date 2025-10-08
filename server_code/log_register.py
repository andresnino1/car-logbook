import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

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
def register_trip(date_string, odometer, usage_type, personal_km, work_km):
  date=datetime.strptime(date_string, "%d/%m/%Y").date() # Transform date string to data object
  usage_business = app_tables.usage_type.get(usage_type="Business") # search in usage_type database and get the row object that match Business
  usage_personal = app_tables.usage_type.get(usage_type="Personal") # search in usage_type database and get the row object that match Personal
  if usage_type=="Mix":
    app_tables.logbook.add_row(date_end=date, odometer_end=(odometer-personal_km),usage_type=usage_business,total_distance=work_km)
    app_tables.logbook.add_row(date_end=date, odometer_start=(odometer-personal_km),odometer_end=odometer, usage_type=usage_personal, total_distance=personal_km)
  elif usage_type=="Business":
    odometer_start = sum(row['total_distance'] for row in app_tables.logbook.search())
    app_tables.logbook.add_row(date_end=date,odometer_start=odometer_start,odometer_end=odometer,usage_type=usage_business, total_distance=work_km )
  elif usage_type=="Personal":
    odometer_start = sum(row['total_distance'] for row in app_tables.logbook.search())
    app_tables.logbook.add_row(date_end=date,odometer_start=odometer_start,odometer_end=odometer,usage_type=usage_personal, total_distance=personal_km )
  print("registere successfully")
  
@anvil.server.callable
def total_kms():
  total_kms = sum(row['total_distance'] for row in app_tables.logbook.search())
  return total_kms