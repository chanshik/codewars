import random


def interpret(code):
    step = [
        # Row, Col
        (0, -1), (0, 1), (-1, 0), (1, 0)
    ]
    DIR_LEFT = 0
    DIR_RIGHT = 1
    DIR_UP = 2
    DIR_DOWN = 3
    BOARD_WIDTH = 80
    BOARD_HEIGHT = 25

    def move_next(f):
        f['ip'][0] += step[f['dir']][0]
        f['ip'][1] += step[f['dir']][1]

        if f['ip'][0] < 0:
            f['ip'][0] = len(f['code']) - 1
        elif f['ip'][0] >= len(f['code']):
            f['ip'][0] = 0

        if f['ip'][1] < 0:
            f['ip'][1] = len(f['code'][f['ip'][0]]) - 1
        elif f['ip'][1] >= len(f['code'][f['ip'][0]]):
            f['ip'][1] = 0

        return f['code'][f['ip'][0]][f['ip'][1]]


    def change_dir(f, op):
        dir_table = {
            '>': DIR_RIGHT,
            '<': DIR_LEFT,
            '^': DIR_UP,
            'v': DIR_DOWN,
        }
        f['dir'] = dir_table[op]


    def number(f, op):
        f['stk'].append(int(op))


    def plus(f, op):
        a = f['stk'].pop()
        b = f['stk'].pop()
        f['stk'].append(a + b)


    def minus(f, op):
        a = f['stk'].pop()
        b = f['stk'].pop()
        f['stk'].append(b - a)


    def mul(f, op):
        a = f['stk'].pop()
        b = f['stk'].pop()
        f['stk'].append(a * b)


    def div(f, op):
        a = f['stk'].pop()
        b = f['stk'].pop()
        f['stk'].append(b / a)


    def modulo(f, op):
        a = f['stk'].pop()
        b = f['stk'].pop()
        if a == 0:
            f['stk'].append(0)
        else:
            f['stk'].append(b % a)


    def logical_not(f, op):
        a = f['stk'].pop()
        if a == 0:
            f['stk'].append(1)
        else:
            f['stk'].append(0)


    def greater_than(f, op):
        a = f['stk'].pop()
        b = f['stk'].pop()
        if b > a:
            f['stk'].append(1)
        else:
            f['stk'].append(0)


    def if_right(f, op):
        a = f['stk'].pop()
        if a == 0:
            change_dir(f, '>')
        else:
            change_dir(f, '<')


    def if_down(f, op):
        a = f['stk'].pop()
        if a == 0:
            change_dir(f, 'v')
        else:
            change_dir(f, '^')


    def start_string(f, op):
        op = move_next(f)
        while op != '"':
            f['stk'].append(ord(op))

            op = move_next(f)


    def duplicate(f, op):
        if len(f['stk']) == 0:
            f['stk'].append(0)
        else:
            a = f['stk'].pop()
            f['stk'].append(a)
            f['stk'].append(a)


    def swap(f, op):
        if len(f['stk']) == 1:
            f['stk'].append(0)
        else:
            a = f['stk'].pop()
            b = f['stk'].pop()

            f['stk'].append(a)
            f['stk'].append(b)


    def discard(f, op):
        f['stk'].pop()


    def print_int(f, op):
        a = f['stk'].pop()

        f['out'].append(str(a))


    def print_ascii(f, op):
        a = f['stk'].pop()
        if isinstance(a, int):
            f['out'].append(chr(a))
        else:
            f['out'].append(a)


    def trampoline(f, op):
        move_next(f)


    def put(f, op):
        y = f['stk'].pop()
        x = f['stk'].pop()
        v = f['stk'].pop()

        f['code'][y][x] = int(v)


    def get(f, op):
        y = f['stk'].pop()
        x = f['stk'].pop()
        v = f['code'][y][x]

        if isinstance(v, int):
            f['stk'].append(v)
        else:
            f['stk'].append(ord(v))

    def change_dir_random(f, op):
        dirs = ["<", "^", ">", "v"]

        change_dir(f, dirs[random.randint(0, 3)])

    op_table = {
        '>': change_dir,
        '<': change_dir,
        '^': change_dir,
        'v': change_dir,
        '+': plus,
        '-': minus,
        '*': mul,
        '/': div,
        '%': modulo,
        '!': logical_not,
        '`': greater_than,
        '"': start_string,
        ':': duplicate,
        '\\': swap,
        '$': discard,
        '.': print_int,
        ',': print_ascii,
        '#': trampoline,
        'p': put,
        'g': get,
        '_': if_right,
        '|': if_down,
        '?': change_dir_random,
    }
    for n in range(10):
        op_table[chr(n + ord('0'))] = number

    code_map = [list(line) for line in code.split("\n")]
    f = {
        "code": code_map,
        "ip": [0, 0],
        "stk": list(),
        "out": list(),
        "dir": DIR_RIGHT,
    }

    op = code_map[0][0]
    while op != '@':
        if op == ' ':
            op = move_next(f)
            continue

        # if op not in op_table:
        #     print("Not yet implemented or invalid operation: %s" % op)
        #     return ""

        op_func = op_table[op]
        op_func(f, op)

        op = move_next(f)

    return "".join(f['out'])

from unittest import TestCase


class TestBefungeInterpret(TestCase):
    def test_interpret(self):
        """
        ['08>:1-:v v *_$.@ ',
         ' ^ _$>\:^']
'08>:1-:v v *_$.@ '
' ^ _$>\:^'

08>:1-:v v *_$.@
  ^    _$>\:^

08>:1-:v v *_$.@
  ^    _$>\:^
        """
        self.assertEquals(
            interpret('01->1# +# :# 0# g# ,# :# 5# 8# *# 4# +# -# _@'),
            '01->1# +# :# 0# g# ,# :# 5# 8# *# 4# +# -# _@')
        self.assertEquals(interpret("08>:1-:v v *_$.@\n  ^    _$>\\:^"), "40320")
        self.assertEquals(interpret('>987v>.v\nv456<  :\n>321 ^ _@'), '123456789')
        self.assertEquals(interpret(""">              v
v  ,,,,,"Hello"<
>48*,          v
v,,,,,,"World!"<
>25*,@"""), "Hello World!\n")

        self.assertEquals(interpret("""2>:3g" "-!v\\  g30          <
 |!`" ":+1_:.:03p>03g+:" "`|
 @               ^  p3\\" ":<
2 2345678901234567890123456789012345678"""), '23571113171923293137')
