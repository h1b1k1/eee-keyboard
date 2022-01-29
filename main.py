print("ASUS EEE keyboard")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.modules.layers import Layers #vrstvy

keyboard = KMKKeyboard()
keyboard.debug_enabled = True
keyboard.modules.append(Layers()) #vrstvy

keyboard.col_pins = (board.GP20,board.GP18,board.GP17,board.GP16,board.GP15,board.GP5,board.GP6,board.GP11)
keyboard.row_pins = (board.GP27,board.GP26,board.GP22,board.GP21,board.GP19,board.GP2,board.GP3,board.GP4,board.GP13,board.GP14,board.GP1,board.GP0,board.GP7,board.GP8,board.GP9,board.GP10)
keyboard.diode_orientation = DiodeOrientation.COLUMNS

keyboard.keymap = [
    [#qwerty
        KC.PAUSE,KC.UP,KC.SLASH,KC.LEFT,KC.SPACE,KC.GRAVE,KC.NO,KC.RGUI,
        KC.F10,KC.MINUS,KC.P,KC.SCOLON,KC.M,KC.F11,KC.N0,KC.COMMA,
        KC.F6,KC.U,KC.J,KC.N,KC.B,KC.F7,KC.N7,KC.NO,
        KC.F2,KC.N4,KC.E,KC.R,KC.G,KC.F3,KC.N3,KC.F,
        KC.NO,KC.Q,KC.S,KC.NO,KC.X,KC.NO,KC.TAB,KC.NO,
        KC.F8,KC.N9,KC.I,KC.O,KC.K,KC.F9,KC.N8,KC.L,
        KC.F4,KC.N6,KC.T,KC.Y,KC.H,KC.F5,KC.N5,KC.V,
        KC.ESCAPE,KC.N2,KC.W,KC.D,KC.C,KC.F1,KC.N1,KC.NO,
        KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.LCTRL,
        KC.F12,KC.LBRACKET,KC.RBRACKET,KC.QUOTE,KC.MO(1),KC.NO,KC.EQUAL,KC.DOT,
        KC.INSERT,KC.BSLASH,KC.LALT,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,
        KC.NO,KC.NO,KC.ENTER,KC.DOWN,KC.NO,KC.DELETE,KC.BSPC,KC.RIGHT,
        KC.NO,KC.CAPSLOCK,KC.A,KC.NO,KC.Z,KC.NO,KC.NO,KC.NO,
        KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.RALT,
        KC.NO,KC.LSHIFT,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.RSHIFT,
        KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.LGUI,
    ],
    [#FN
        KC.PAUSE,KC.PGUP,KC.SLASH,KC.HOME,KC.SPACE,KC.GRAVE,KC.NO,KC.RGUI,
        KC.F10,KC.MINUS,KC.PAST,KC.SCOLON,KC.M,KC.NUMLOCK,KC.PSLS,KC.COMMA,
        KC.F6,KC.KP_4,KC.KP_1,KC.N,KC.B,KC.MUTE,KC.N7,KC.NO,
        KC.F2,KC.N4,KC.E,KC.R,KC.G,KC.F3,KC.N3,KC.F,
        KC.NO,KC.Q,KC.S,KC.NO,KC.X,KC.NO,KC.TAB,KC.NO,
        KC.VOLD,KC.N9,KC.KP_5,KC.KP_6,KC.KP_2,KC.VOLU,KC.N8,KC.KP_3,
        KC.F4,KC.N6,KC.T,KC.Y,KC.H,KC.F5,KC.N5,KC.V,
        KC.ESCAPE,KC.N2,KC.W,KC.D,KC.C,KC.F1,KC.N1,KC.NO,
        KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.LCTRL,
        KC.F12,KC.LBRACKET,KC.RBRACKET,KC.QUOTE,KC.MO(1),KC.NO,KC.EQUAL,KC.DOT,
        KC.INSERT,KC.BSLASH,KC.LALT,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,
        KC.NO,KC.NO,KC.ENTER,KC.PGDN,KC.NO,KC.DELETE,KC.BSPC,KC.END,
        KC.NO,KC.CAPSLOCK,KC.A,KC.NO,KC.Z,KC.NO,KC.NO,KC.NO,
        KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.RALT,
        KC.NO,KC.LSHIFT,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.RSHIFT,
        KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.LGUI,
    ]
]

if __name__ == '__main__':
    keyboard.go()
