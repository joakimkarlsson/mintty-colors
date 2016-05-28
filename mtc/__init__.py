import os

TMUX = os.environ.get('TMUX')
ESC_BEGIN = '\033Ptmux;\033\033]' if TMUX else '\033]'
ESC_END = '\a\033\\' if TMUX else '\a'

print('{}10;#000000{}'.format(ESC_BEGIN, ESC_END))  # Foreground
print('{}11;#C0C0C0{}'.format(ESC_BEGIN, ESC_END))  # Background
print('{}12;#00FF00{}'.format(ESC_BEGIN, ESC_END))  # Cursor
print('{}4;0;#000000{}'.format(ESC_BEGIN, ESC_END))  # black
print('{}4;1;#BF0000{}'.format(ESC_BEGIN, ESC_END))  # red
print('{}4;2;#00BF00{}'.format(ESC_BEGIN, ESC_END))  # green
print('{}4;3;#BFBF00{}'.format(ESC_BEGIN, ESC_END))  # yellow
print('{}4;4;#0000BF{}'.format(ESC_BEGIN, ESC_END))  # blue
print('{}4;5;#BF00BF{}'.format(ESC_BEGIN, ESC_END))  # magenta
print('{}4;6;#00BFBF{}'.format(ESC_BEGIN, ESC_END))  # cyan
print('{}4;7;#BFBFBF{}'.format(ESC_BEGIN, ESC_END))  # white
print('{}4;8;#404040{}'.format(ESC_BEGIN, ESC_END))  # bold black
print('{}4;9;#FF4040{}'.format(ESC_BEGIN, ESC_END))  # bold red
print('{}4;10;#40FF40{}'.format(ESC_BEGIN, ESC_END))  # bold green
print('{}4;11;#FFFF40{}'.format(ESC_BEGIN, ESC_END))  # bold yellow
print('{}4;12;#6060FF{}'.format(ESC_BEGIN, ESC_END))  # bold blue
print('{}4;13;#FF40FF{}'.format(ESC_BEGIN, ESC_END))  # bold magenta
print('{}4;14;#40FFFF{}'.format(ESC_BEGIN, ESC_END))  # bold cyan
print('{}4;15;#FFFFFF{}'.format(ESC_BEGIN, ESC_END))  # bold white
