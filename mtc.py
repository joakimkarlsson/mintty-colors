import os
import sys
import click
import os.path as op

try:
    import configparser

    def read_string(string):
        parser = configparser.ConfigParser()
        parser.read_string(string)
        return parser

except ImportError:
    import ConfigParser
    import io

    def read_string(string):
        parser = ConfigParser.ConfigParser()
        parser.readfp(io.BytesIO(string))
        return parser


@click.group()
def cli():
    pass


@cli.command(help='Set a color theme')
@click.argument('theme')
@click.pass_context
def set(ctx, theme):
    try:
        set_theme(theme)
    except ConfigParser.NoSectionError:
        click.echo('Don\'t know the theme {}.'.format(theme))
        click.echo('These are the ones I know about:')
        ctx.invoke(list)
        sys.exit(1)


@cli.command(help='List available color themes')
def list():
    parser = get_themes()
    for section in sorted(parser.sections()):
        click.echo(section)


#
# Escape sequences for the shell
#
# These are different if we're in tmux or not, so we need to check for that.
#
_TMUX = os.environ.get('TMUX')
ESC_BEGIN = '\033Ptmux;\033\033]' if _TMUX else '\033]'
ESC_END = '\a\033\\' if _TMUX else '\a'

COLOR_NAME_CODES = dict(
    foregroundcolour='10;',
    backgroundcolour='11;',
    cursorcolour='12;',
    black='4;0;',
    red='4;1;',
    green='4;2;',
    yellow='4;3;',
    blue='4;4;',
    magenta='4;5;',
    cyan='4;6;',
    white='4;7;',
    boldblack='4;8;',
    boldred='4;9;',
    boldgreen='4;10;',
    boldyellow='4;11;',
    boldblue='4;12;',
    boldmagenta='4;13;',
    boldcyan='4;14;',
    boldwhite='4;15;',
)


BUILTIN_THEMES = '''
[onedark]
ForegroundColour=171,178,191
BackgroundColour=30,33,39
CursorColour=97,175,239
BoldBlack=92,99,112
Black=92,99,112
BoldRed=224,108,117
Red=224,108,117
BoldGreen=152,195,121
Green=152,195,121
BoldYellow=209,154,102
Yellow=209,154,102
BoldBlue=97,175,239
Blue=97,175,239
BoldMagenta=198,120,221
Magenta=198,120,221
BoldCyan=86,182,194
Cyan=86,182,194
BoldWhite=171,178,191
White=171,178,191

[material-dark]
BackgroundColour=35,35,34
ForegroundColour=229,229,229
CursorColour=229,229,229
Black=33,33,33
BoldBlack=66,66,66
Red=183,20,31
BoldRed=232,59,63
Green=69,123,36
BoldGreen=122,186,58
Yellow=246,152,30
BoldYellow=255,234,46
Blue=19,78,178
BoldBlue=84,164,243
Magenta=86,0,136
BoldMagenta=170,77,188
Cyan=14,113,124
BoldCyan=38,187,209
White=239,239,239
BoldWhite=217,217,217

[material-light]
BackgroundColour=234,234,234
ForegroundColour=46,46,45
CursorColour=46,46,45
Black=33,33,33
BoldBlack=66,66,66
Red=183,20,31
BoldRed=232,59,63
Green=69,123,36
BoldGreen=122,186,58
Yellow=252,123,8
BoldYellow=253,142,9
Blue=19,78,178
BoldBlue=84,164,243
Magenta=86,0,136
BoldMagenta=170,77,188
Cyan=14,113,124
BoldCyan=38,187,209
White=239,239,239
BoldWhite=217,217,217

[solarized-light]
BackgroundColour=253,246,227
ForegroundColour=88,110,117
CursorColour=88,110,117
Black=0,43,54
BoldBlack=101,123,131
Red=220,50,47
BoldRed=220,50,47
Green=133,153,0
BoldGreen=133,153,0
Yellow=181,137,0
BoldYellow=181,137,0
Blue=38,139,210
BoldBlue=38,139,210
Magenta=108,113,196
BoldMagenta=108,113,196
Cyan=42,161,152
BoldCyan=42,161,152
White=147,161,161
BoldWhite=253,246,227

[solarized-dark]
BackgroundColour=0,43,54
ForegroundColour=147,161,161
CursorColour=147,161,161
Black=0,43,54
BoldBlack=101,123,131
Red=220,50,47
BoldRed=220,50,47
Green=133,153,0
BoldGreen=133,153,0
Yellow=181,137,0
BoldYellow=181,137,0
Blue=38,139,210
BoldBlue=38,139,210
Magenta=108,113,196
BoldMagenta=108,113,196
Cyan=42,161,152
BoldCyan=42,161,152
White=147,161,161
BoldWhite=253,246,227

[tomorrow-dark]
BackgroundColour=29,31,33
ForegroundColour=197,200,198
CursorColour=197,200,198
Black=29,31,33
BoldBlack=150,152,150
Red=204,102,102
BoldRed=204,102,102
Green=181,189,104
BoldGreen=181,189,104
Yellow=240,198,116
BoldYellow=240,198,116
Blue=129,162,190
BoldBlue=129,162,190
Magenta=178,148,187
BoldMagenta=178,148,187
Cyan=138,190,183
BoldCyan=138,190,183
White=197,200,198
BoldWhite=255,255,255

[tomorrow-light]
BackgroundColour=255,255,255
ForegroundColour=55,59,65
CursorColour=55,59,65
Black=29,31,33
BoldBlack=150,152,150
Red=204,102,102
BoldRed=204,102,102
Green=181,189,104
BoldGreen=181,189,104
Yellow=240,198,116
BoldYellow=240,198,116
Blue=129,162,190
BoldBlue=129,162,190
Magenta=178,148,187
BoldMagenta=178,148,187
Cyan=138,190,183
BoldCyan=138,190,183
White=197,200,198
BoldWhite=255,255,255
'''


_themes = None


def get_themes():
    global _themes

    if not _themes:
        parser = read_string(BUILTIN_THEMES)

        user_defined_colors_path = op.expanduser('~/.mintty-colors')
        if user_defined_colors_path:
            parser.read(user_defined_colors_path)

        _themes = parser

    return _themes


def set_theme(theme):
    parser = get_themes()
    for k, v in parser.items(theme):
        _set_color(k, v)


def _set_color(name, val):
    print('{begin}{color_name}{val}{end}'.format(
        begin=ESC_BEGIN,
        color_name=COLOR_NAME_CODES[name.lower()],
        val=val,
        end=ESC_END))


if __name__ == '__main__':
    cli()
