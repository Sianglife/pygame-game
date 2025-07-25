import pygame_gui
import os

print("Module path:", pygame_gui.__file__)
font_path = os.path.join(os.path.dirname(
    pygame_gui.__file__), "data", "NotoSans-Regular.ttf")
print("Font exists:", os.path.exists(font_path))
