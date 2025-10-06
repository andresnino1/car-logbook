from ._anvil_designer import LogbookTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import m3.components as m3

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
# FALTA EVALUAR cuando usage type se seleciona como personal
# o como work y se debe guardar el valor completo del odometro en esas variales
 # cuando se oprima el boton de SEND 

  # When odometer value change the personal km and work km is empty
  def text_box_odometer_change(self, **event_args):
    self.text_box_personal_km.text = ""
    self.text_box_work_km.text = ""
    
  # Show usage type items in dropdown
  def dropdown_usage_type_show(self, **event_args):
    self.dropdown_usage_type.items = [(r["usage_type"],r) for r in app_tables.usage_type.search()]
    self.dropdown_usage_type.include_placeholder=True
    self.dropdown_usage_type.placeholder="Select Usage Type"

  # Evaluate when dropdown is select Mix Usage Type1
  def dropdown_usage_type_change(self, **event_args):
    usage_type_obj = self.dropdown_usage_type.selected_value
    usage_type = usage_type_obj['usage_type']
    if usage_type == 'Mix':
      self.column_panel_usage_type.visible=True
    else:
      self.column_panel_usage_type.visible=False
  
  # evaluate when personal kms changes and calculate work kmts
  def text_box_personal_km_change(self, **event_args):
    odometer = abs(self.text_box_odometer.text)
    personal_km = abs(self.text_box_personal_km.text)
    if personal_km > odometer:
      alert("Check Odometer Value", title="Wrong Value")
      self.text_box_personal_km.text=""
      self.text_box_work_km.text=""
    else:
      self.text_box_work_km.text = odometer - personal_km

  # evaluate when Work kms change and calculate personal kms
  def text_box_work_km_change(self, **event_args):
    odometer = abs(self.text_box_odometer.text)
    work_km = abs(self.text_box_work_km.text)
    if work_km > odometer:
      alert("Check Odometer Value", title="Wrong Value")
      self.text_box_personal_km.text=""
      self.text_box_work_km.text=""
    else:
      self.text_box_personal_km.text = odometer - work_km

  # Send Button - add register to database
  def button_send_click(self, **event_args):
    """This method is called when the component is clicked."""
    date=self.date_picker_trip.date
    odometer = self.text_box_odometer.text
    usage_type_obj = self.dropdown_usage_type.selected_value
    personal_km = self.text_box_personal_km.text
    work_km = self.text_box_work_km.text
    
    if date is None:
      alert("Choose a Date")
    
    elif odometer == "":
      alert("Enter Odometer Value")

    elif usage_type_obj is None:
      alert("Select Usage Type")
      
    elif personal_km == "":
      alert("Enter Personal Kms Value")
      
    elif work_km == "":
      alert("Enter Work Kms Value")

    else:
      date_format = date.strftime("%d/%m/%Y")
      print(date_format, odometer,personal_km,work_km)

  def total_km_value_show(self, **event_args):
    """This method is called when the component is shown on the screen."""
    total_kms=anvil.server.call('total_kms')
    self.total_km_value.text = total_kms

 

