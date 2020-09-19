#!/usr/bin/env python3


import argparse
import typing
import dis
import ast

from types import CodeType

import struct

from io import BytesIO
from dataclasses import dataclass
from collections import defaultdict

from lark import Lark, Transformer, v_args
from funcy import collecting


# ----- WRITE CODE HERE -----

bytecode_parser = Lark(grammar, parser='lalr', transformer=VisitTree())

ast_parser = Lark(grammar, parser='lalr')


def main(args):
    with open(args.file, 'r') as fin:
        text = ''.join(
            line for line in fin
            if line.strip() and not line.startswith('#')
        )

    if args.ast:
        program_ast = ast_parser.parse(text)
        print(program_ast)

    program_ir = bytecode_parser.parse(text)
    if args.ir:
        print(program_ir)

    codeobj = create_codeobj(program_ir)
    if args.bytecode:
        dis.dis(codeobj)

    do_exec = not (args.ast or args.ir or args.bytecode)
    if do_exec:
        return exec(codeobj)



def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='input file')
    parser.add_argument('--ast', action='store_true', help='show ast')
    parser.add_argument('--ir', action='store_true', help='show IR')
    parser.add_argument('--bytecode', action='store_true', help='show bytecode')
    return parser.parse_args()


if __name__ == '__main__':
    main(parse_args())
