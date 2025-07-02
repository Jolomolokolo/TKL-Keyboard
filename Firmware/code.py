from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

# Define your row and column pins — update these for your actual PCB!
keyboard.col_pins = (26, 27, 28, 29, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)  # 14 columns (example)
keyboard.row_pins = (0, 1, 2, 3, 4, 5)  # 6 rows (example)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

from keymap import layers
keyboard.keymap = layers

if __name__ == '__main__':
    keyboard.go()
