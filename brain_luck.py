"""
Inspired from real-world Brainf**k, we want to create an interpreter of that language
which will support the following instructions
(the machine memory or 'data' should behave like a potentially infinite array of bytes, initialized to 0):

> increment the data pointer (to point to the next cell to the right).
< decrement the data pointer (to point to the next cell to the left).
+ increment (increase by one, truncate overflow: 255 + 1 = 0) the byte at the data pointer.
- decrement (decrease by one, treat as unsigned byte: 0 - 1 = 255 ) the byte at the data pointer.
. output the byte at the data pointer.
, accept one byte of input, storing its value in the byte at the data pointer.
[ if the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command,
  jump it forward to the command after the matching ] command.
] if the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command,
  jump it back to the command after the matching [ command.
The function will take in input...

the program code, a string with the sequence of machine instructions,
the program input, a string, eventually empty, that will be interpreted as an array of bytes
using each character's ASCII code and will be consumed by the , instruction
... and will return ...

the output of the interpreted code (always as a string), produced by the . instruction.
"""


def brain_luck(code, input):
    frame = {
        "code": code,
        "ip": 0,
        "out": "",
        "data": [0] * 8,
        "dp": 0,
        "read": input,
        "rp": 0,
        "depth": 0
    }

    def move_right():
        frame["dp"] += 1
        frame["ip"] += 1

        if len(frame["data"]) == frame["dp"]:
            frame["data"] += [0] * len(frame["data"])

    def move_left():
        frame["dp"] -= 1
        frame["ip"] += 1

    def read_one_byte():
        if len(frame["data"]) == frame["dp"]:
            frame["data"] += [0] * len(frame["data"])

        if frame["read"][frame["rp"]] != 0:
            frame["data"][frame["dp"]] = ord(frame["read"][frame["rp"]])

        frame["ip"] += 1
        frame["rp"] += 1

    def if_then():
        if frame["data"][frame["dp"]] == 0:
            ip = frame["ip"] + 1
            cur_depth = frame["depth"]

            while ip < len(frame["code"]):
                if frame["code"][ip] == "[":
                    cur_depth += 1
                elif frame["code"][ip] == "]":
                    if frame["depth"] == cur_depth:
                        ip += 1
                        break

                    cur_depth -= 1

                ip += 1


            frame["ip"] = ip
        else:
            frame["ip"] += 1
            frame["depth"] += 1

    def loop():
        if frame["data"][frame["dp"]] != 0:
            ip = frame["ip"] - 1
            cur_depth = frame["depth"]

            while ip >= 0:
                if frame["code"][ip] == "]":
                    cur_depth += 1
                elif frame["code"][ip] == "[":
                    if frame["depth"] == cur_depth:
                        ip += 1
                        break

                    cur_depth -= 1

                ip -= 1

            frame["ip"] = ip
        else:
            frame["ip"] += 1
            frame["depth"] -= 1

    def inc():
        dp = frame["dp"]
        val = 0
        try:
            val = frame["data"][dp] + 1
        except:
            from pprint import pprint
            pprint(frame)

        if val > 255:
            val = 0

        frame["data"][dp] = val
        frame["ip"] += 1

    def dec():
        dp = frame["dp"]
        val = frame["data"][dp] - 1

        if val < 0:
            val = 255

        frame["data"][dp] = val
        frame["ip"] += 1

    def output():
        dp = frame["dp"]
        val = frame["data"][dp]

        frame["out"] += chr(val)
        frame["ip"] += 1

    op_table = {
        ",": read_one_byte,
        "[": if_then,
        "]": loop,
        "+": inc,
        "-": dec,
        ".": output,
        ">": move_right,
        "<": move_left,
    }

    len_code = len(code)
    while frame["ip"] < len(frame["code"]):
        ip = frame["ip"]
        if frame["code"][frame["ip"]] == 0 or frame["code"][frame["ip"]] == 255:
            break

        op = frame["code"][frame["ip"]]
        if op not in op_table:
            break

        op_table[op]()

        # print(frame["code"])
        # print("%s^  ip: %d, dp: %d, data: %d, depth: %d" % (
        #     " " * frame["ip"], frame["ip"], frame["dp"], frame["data"][frame["dp"]], frame["depth"]))

    return frame["out"]

from unittest import TestCase


class TestBrainLuck(TestCase):
    def test_brain_luck(self):
        # Echo until byte(0) encountered
        self.assertEquals(
            brain_luck(',[.[-],]', 'Codewars' + chr(0)),
            'Codewars'
        )

        # Echo until byte(255) encountered
        self.assertEquals(
            brain_luck(',+[-.,+]', 'Codewars' + chr(255)),
            'Codewars'
        )

        # Two numbers multiplier
        self.assertEquals(
            brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)),
            chr(72)
        )

        self.assertEquals(
            brain_luck(
                ',>+>>>>++++++++++++++++++++++++++++++++++++++++++++>++++++++++++++++++++++++++++++++<<<<<<[>[>>>>>>+>+<<<<<<<-]>>>>>>>[<<<<<<<+>>>>>>>-]<[>++++++++++[-<-[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]>[<<[>>>+<<<-]>>[-]]<<]>>>[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]>[<<+>>[-]]<<<<<<<]>>>>>[++++++++++++++++++++++++++++++++++++++++++++++++.[-]]++++++++++<[->-<]>++++++++++++++++++++++++++++++++++++++++++++++++.[-]<<<<<<<<<<<<[>>>+>+<<<<-]>>>>[<<<<+>>>>-]<-[>>.>.<<<[-]]<<[>>+>+<<<-]>>>[<<<+>>>-]<<[<+>-]>[<+>-]<<<-]',
                '\n'),
             '1, 1, 2, 3, 5, 8, 13, 21, 34, 55'
        )