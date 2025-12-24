import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.handlers.sequences import send_string
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

# =====================
# MATRIX CONFIGURATION
# =====================
keyboard.row_pins = (
    board.GP2,  
    board.GP26, 
    board.GP27,   
)

keyboard.col_pins = (
    board.GP28, 
    board.GP29, 
    board.GP6,  
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# =====================
# BRAILLE STATE
# =====================
braille_mask = 0

DOTS = {
    "L1": 0b000001,  # dot 1
    "L2": 0b000010,  # dot 2
    "L3": 0b000100,  # dot 3
    "R1": 0b001000,  # dot 4
    "R2": 0b010000,  # dot 5
    "R3": 0b100000,  # dot 6
}

BRAILLE_TABLE = {
    0b000001: "a",
    0b000011: "b",
    0b001001: "c",
    0b011001: "d",
    0b010001: "e",
    0b001011: "f",
    0b011011: "g",
    0b010011: "h",
    0b001010: "i",
    0b011010: "j",
    0b000101: "k",
    0b000111: "l",
    0b001101: "m",
    0b011101: "n",
    0b010101: "o",
    0b001111: "p",
    0b011111: "q",
    0b010111: "r",
    0b001110: "s",
    0b011110: "t",
    0b100101: "u",
    0b100111: "v",
    0b111010: "w",
    0b101101: "x",
    0b111101: "y",
    0b110101: "z",
}

# =====================
# BRAILLE HANDLER
# =====================
def braille_dot(dot_bit):
    def handler(key, keyboard, *args):
        global braille_mask

        if key.is_pressed:
            braille_mask |= dot_bit
        else:
            if braille_mask != 0:
                char = BRAILLE_TABLE.get(braille_mask, "")
                if char:
                    send_string(keyboard, char)
                braille_mask = 0

    return handler

# -------------------
# ROTARY ENCODER
# -------------------

encoder = EncoderHandler()
keyboard.modules.append(encoder)
#Turn up and Turn down Volume
encoder.pins = (
    (board.GP7, board.GP0),  
)

encoder.map = (
    (KC.VOLD, KC.VOLU), 
)
# Mute volume
keyboard.matrix = KeysScanner(
    pins=(board.GP4,),        
    value_when_pressed=False )

# =====================
# CUSTOM KEYS
# =====================
L1 = KC.NO.clone()
L1.on_press = braille_dot(DOTS["L1"])
L1.on_release = braille_dot(DOTS["L1"])

L2 = KC.NO.clone()
L2.on_press = braille_dot(DOTS["L2"])
L2.on_release = braille_dot(DOTS["L2"])

L3 = KC.NO.clone()
L3.on_press = braille_dot(DOTS["L3"])
L3.on_release = braille_dot(DOTS["L3"])

R1 = KC.NO.clone()
R1.on_press = braille_dot(DOTS["R1"])
R1.on_release = braille_dot(DOTS["R1"])

R2 = KC.NO.clone()
R2.on_press = braille_dot(DOTS["R2"])
R2.on_release = braille_dot(DOTS["R2"])

R3 = KC.NO.clone()
R3.on_press = braille_dot(DOTS["R3"])
R3.on_release = braille_dot(DOTS["R3"])

# =====================
# KEYMAP (MATCHES YOUR MATRIX)
# =====================
keyboard.keymap = [
    [
        KC.MUTE,
        R1,    KC.BSPC,  L1,
        R2,    KC.ENTER,  L2,
        R3,    KC.SPACE, L3,
    ]
]

if __name__ == "__main__":
    keyboard.go()

