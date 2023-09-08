"""Base class for sub windows in the application"""
from webbrowser import open_new

from customtkinter import CTkButton, CTkEntry, CTkFrame, CTkImage, CTkLabel, CTkOptionMenu, CTkProgressBar, CTkTextbox
from PIL import Image

from classes.gui.enums import Color
from utilities.config import get_color


class BaseFrame(CTkFrame):
  """Frame for sub windows in the application"""
  def __init__(self, master, title: str = ""):
    self.master = master
    super().__init__(master, fg_color="transparent")  # type: ignore[attr-defined]
    if title:
      self.master.title(title)  # type: ignore[attr-defined]
    self.__init_frame__()
    self.set_default_input()
    self.is_ready = True

  def __init_frame__(self):
    pass

  def __add_default__(self, widget_type, **parameters):
    """Add default parameters"""
    if widget_type == type(CTkLabel):
      if "text" not in parameters:
        parameters["text"] = ""
    return parameters

  def add_widget(self, widget_type: type, **parameters):
    """Add widget to the frame in specific cell and parameters"""
    parameters = self.__add_default__(widget_type, **parameters)
    if parameters:
      widget = widget_type(self, **parameters)
    else:
      widget = widget_type(self)
    return widget

  def add_image(self, path, **parameters):
    """Add image to the frame in a specific grid cell"""
    img = CTkImage(dark_image=Image.open(path), **parameters)
    img_widget = self.add_widget(CTkLabel, text="", image=img, justify="center")
    img_widget.image = img
    return img_widget

  def add_link(self, text, link):
    """Add text link to the frame in a specific grid cell"""
    lbl_link = self.add_widget(CTkLabel, text_color=get_color(Color.PRIMARY),
                               text=text, justify="center", cursor="hand2")
    lbl_link.bind("<Button-1>", lambda e: open_new(link))
    return lbl_link

  def add_label(self, text, **parameters):
    """"Add label to the frame in a specific grid cell"""
    lbl = self.add_widget(CTkLabel, text=text, **parameters)
    return lbl

  def add_entry(self, **parameters):
    """"Add entry to the frame in a specific grid cell"""
    entry = self.add_widget(CTkEntry, **parameters)
    return entry

  def add_button(self, text, click_func, **parameters):
    """"Add button to the frame in a specific grid cell"""
    if "command" not in parameters:
      parameters["command"] = click_func
    btn = self.add_widget(CTkButton, text=text, **parameters)
    return btn

  def add_progressbar(self):
    """"Add progress bar to the frame in a specific grid cell"""
    progbar = CTkProgressBar(self)
    progbar.set(0)
    return progbar

  def add_option(self, *value):
    """"Add option menu to the frame in a specific grid cell"""
    option = CTkOptionMenu(self, dynamic_resizing=False, values=value)
    return option

  def add_log(self):
    """"Add log output to the frame in a specific grid cell"""
    txt_log = self.add_widget(CTkTextbox)
    return txt_log

  def set_default_input(self):
    """default value for the input"""
