from ._anvil_designer import LogbookTemplate
from anvil import *
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


  # Show usage type items in dropdown
  def dropdown_usage_type_show(self, **event_args):
    """This method is called when the component is shown on the screen."""
    self.dropdown_usage_type.items = [(r["usage_type"],r) for r in app_tables.usage_type.search()]
    self.dropdown_usage_type.include_placeholder=True
    self.dropdown_usage_type.placeholder="Select Usage Type"

  # Evaluate when dropdown is select Mix Usage Type1
  def dropdown_usage_type_change(self, **event_args):
    """This method is called when an item is selected"""
    usage_type_obj = self.dropdown_usage_type.selected_value
    usage_type = usage_type_obj['usage_type']
    if usage_type == 'Mix':
      self.column_panel_usage_type.visible=True
    else:
      self.column_panel_usage_type.visible=False

  def text_box_personal_km_change(self, **event_args):
    """This method is called when the text in this component is edited."""
    odometer = abs(self.text_box_odometer.text)
    personal_km = abs(self.text_box_personal_km.text)
    if personal_km > odometer:
      alert("Check Odometer Value", title="Wrong Value")
    else:
      self.text_box_work_km.text = odometer - personal_km

  # When odometer value change the personal km and work km is empty
  def text_box_odometer_change(self, **event_args):
    """This method is called when the text in this component is edited."""
    self.text_box_personal_km.text = ""
    self.text_box_work_km.text = ""



