import os

TMUX = os.environ.get('TMUX')
ESC_BEGIN = '\033Ptmux;\033\033]' if TMUX else '\033]'
ESC_END = '\a\033\\' if TMUX else '\a'

COLOR_NAME_CODES = dict(
    ForegroundColour='10;',
    BackgroundColour='11;',
    CursorColour='12;',
    Black='4;0;',
    Red='4;1;',
    Green='4;2;',
    Yellow='4;3;',
    Blue='4;4;',
    Magenta='4;5;',
    Cyan='4;6;',
    White='4;7;',
    BoldBlack='4;8;',
    BoldRed='4;9;',
    BoldGreen='4;10;',
    BoldYellow='4;11;',
    BoldBlue='4;12;',
    BoldMagenta='4;13;',
    BoldCyan='4;14;',
    BoldWhite='4;15;',
)


def set_color(name, val):
    print('{begin}{color_name}{val}{end}'.format(
        begin=ESC_BEGIN,
        color_name=COLOR_NAME_CODES[name],
        val=val,
        end=ESC_END))


set_color('ForegroundColour', '#000000')
set_color('BackgroundColour', '#C0C0C0')
set_color('CursorColour', '#00FF00')
set_color('Black', '#000000')
set_color('Red', '#BF0000')
set_color('Green', '#00BF00')
set_color('Yellow', '#BFBF00')
set_color('Blue', '#0000BF')
set_color('Magenta', '#BF00BF')
set_color('Cyan', '#00BFBF')
set_color('White', '#BFBFBF')
set_color('BoldBlack', '#404040')
set_color('BoldRed', '#FF4040')
set_color('BoldGreen', '#40FF40')
set_color('BoldYellow', '#FFFF40')
set_color('BoldBlue', '#6060FF')
set_color('BoldMagenta', '#FF40FF')
set_color('BoldCyan', '#40FFFF')
set_color('BoldWhite', '#FFFFFF')
