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


  # # ================ DropDown Machine Type Show Function ==================

  # def dropdown_machine_type_show(self, **event_args):
  #   """This method is called when the DropDown is shown on the screen"""
  #   self.dropdown_machine_type.items = [(r["model"],r) for r in app_tables.machine_type.search()]
  #   self.dropdown_machine_type.include_placeholder=True
  #   self.dropdown_machine_type.placeholder="Select a Machine Model"



  def dropdown_usage_type_show(self, **event_args):
    """This method is called when the component is shown on the screen."""
    self.dropdown_usage_type.items = [(r["usage_type"],r) for r in app_tables.usage_type.search()]
    self.dropdown_usage_type.include_placeholder=True
    self.dropdown_usage_type.placeholder="Select Usage Type"



