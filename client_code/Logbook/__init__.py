from ._anvil_designer import LogbookTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import m3.components as m3

personal_km = ""
work_km = ""

class Logbook(LogbookTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.column_panel_usage_type.visible=False


  # # ================ DropDown Machine Type Show Function ==================

  # def dropdown_machine_type_show(self, **event_args):
  #   """This method is called when the DropDown is shown on the screen"""
  #   self.dropdown_machine_type.items = [(r["model"],r) for r in app_tables.machine_type.search()]
  #   self.dropdown_machine_type.include_placeholder=True
  #   self.dropdown_machine_type.placeholder="Select a Machine Model"

# ========= TODO ================
# cuando registre el odometro refrescar el valor suma total en total kms

  # Calculate Total Kms calling Server and show value in the main card
  def total_km_value_show(self, **event_args):
    global total_kms
    total_kms=anvil.server.call('total_kms')
    self.total_km_value.text = total_kms

  # When odometer value change the personal km and work km is empty
  def text_box_odometer_change(self, **event_args):
    global personal_km
    global work_km
    personal_km = ""
    work_km = ""
    self.text_box_odometer.border_color="black"
    self.text_box_personal_km.text = personal_km
    self.text_box_work_km.text = work_km
    odometer = self.text_box_odometer.text
    total_km = self.
    if odometer == "":
      self.text_box_odometer.border_color="red"
    elif odometer < 0:
      alert("Enter Just Positive Values")
    # elif odometer < total_km :
    #   alert("Check Odometer Value")
    #   # self.dropdown_usage_type.placeholder="Select Usage Type"

      
    
    
  # Show usage type items in dropdown
  def dropdown_usage_type_show(self, **event_args):
    self.dropdown_usage_type.items = [(r["usage_type"],r) for r in app_tables.usage_type.search()]
    self.dropdown_usage_type.include_placeholder=True
    self.dropdown_usage_type.placeholder="Select Usage Type"

  # Evaluate when dropdown is select Mix Usage Type1
  def dropdown_usage_type_change(self, **event_args):
    global personal_km
    global work_km
    usage_type_obj = self.dropdown_usage_type.selected_value
    usage_type = usage_type_obj['usage_type']
    if usage_type == 'Mix':
      self.column_panel_usage_type.visible=True
    if usage_type == "Personal":
      personal_km = self.text_box_odometer.text
      work_km = 0
      self.column_panel_usage_type.visible=False
    if usage_type == "Business":
      personal_km = 0
      work_km = self.text_box_odometer.text
      self.column_panel_usage_type.visible=False
  
  # evaluate when personal kms changes and calculate work kmts
  def text_box_personal_km_change(self, **event_args):
    global personal_km
    global work_km
    self.text_box_personal_km.border_color="black"
    odometer = self.text_box_odometer.text
    personal_km = self.text_box_personal_km.text
    self.text_box_work_km.text = ""
    if personal_km == "":
      self.text_box_personal_km.border_color="red"
    elif personal_km > odometer:
      alert("Check Odometer Value", title="Wrong Value")
      self.text_box_personal_km.text=""
      self.text_box_work_km.text=""
      personal_km = ""
      work_km = ""
    elif personal_km < 0:
      alert("Enter Just Positive Values")
      self.text_box_personal_km.text=""
      self.text_box_work_km.text=""
      personal_km = ""
      work_km = ""
    else:
      work_km = odometer - personal_km
      self.text_box_work_km.text = work_km
      

  # evaluate when Work kms change and calculate personal kms
  def text_box_work_km_change(self, **event_args):
    global personal_km
    global work_km
    self.text_box_work_km.border_color="black"
    odometer = self.text_box_odometer.text
    work_km = self.text_box_work_km.text
    self.text_box_personal_km.text = ""

    if work_km == "":
      self.text_box_work_km.border_color="red"
    elif work_km > odometer:
      alert("Check Odometer Value", title="Wrong Value")
      self.text_box_personal_km.text=""
      self.text_box_work_km.text=""
      personal_km = ""
      work_km = ""
    elif work_km < 0:
      alert("Enter Just Positive Values")
      self.text_box_personal_km.text=""
      self.text_box_work_km.text=""
      personal_km = ""
      work_km = ""
    else:
      personal_km = odometer - work_km
      self.text_box_personal_km.text = personal_km

  # Send Button - add register to database
  def button_send_click(self, **event_args):
    """This method is called when the component is clicked."""
    date=self.date_picker_trip.date
    odometer = self.text_box_odometer.text
    total_km = self.total_km_value.text
    usage_type_obj = self.dropdown_usage_type.selected_value
    global personal_km
    global work_km 
    
    if date is None:
      alert("Choose a Date")
    
    elif odometer == "":
      alert("Enter Odometer Value")

    elif odometer < total_km:
      alert("Check Odometer Value")

    elif usage_type_obj is None:
      alert("Select Usage Type")
      
    elif personal_km == "":
      alert("Enter Personal Kms Value")
      
    elif work_km == "":
      alert("Enter Work Kms Value")

    else:
      date_format = date.strftime("%d/%m/%Y")
      usage_type=usage_type_obj["usage_type"]
      anvil.server.call('register_trip',date_format,odometer,usage_type, personal_km,work_km)
      alert("Kmts Registered Successfully", title="Trip Registered")
      personal_km = 0
      work_km = 0
      odometer = 0
      self.text_box_odometer.text=""
      self.text_box_personal_km.text=""
      self.text_box_work_km.text=""
      self.total_km_value_show()

 
  

 

