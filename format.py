#!/usr/bin/env python3
# SPDX-License-Identifier: 0BSD

import argparse


def tokenize(contents):
    tokens = []
    partial = ""
    for ch in contents:
        if ch.isspace() or ch in ("(", ")", ";", ",", "."):
            tokens.append(partial)
            tokens.append(ch)
            partial = ""
        else:
            partial += ch
    return [token for token in tokens if not token.isspace() and len(token) > 0]


def render(tokens, indent):
    contents = ""
    prior_token = None
    indent_level = 0
    needs_newline = False
    for token in tokens:
        if token in (")", "END"):
            indent_level -= 1
            needs_newline = True
        elif prior_token in (None, ".") or token in (",", ";", "."):
            pass
        else:
            contents += " "
        if needs_newline:
            prior_token = None
            contents += "\n" + indent * indent_level
            needs_newline = False
        contents += token
        prior_token = token
        if token in ("(", "BEGIN"):
            indent_level += 1
            needs_newline = True
        elif token in (",", ";"):
            needs_newline = True
        if token == ";" and indent_level == 0:
            contents += "\n"
    return contents.rstrip() + "\n"


def format(filename, spaces, in_place):
    with open(filename, "r") as file:
        old_contents = file.read()
    tokens = tokenize(old_contents)
    indent = " " * spaces if spaces is not None else "\t"
    new_contents = render(tokens, indent)
    if in_place:
        if new_contents != old_contents:
            with open(filename, "w") as file:
                file.write(new_contents)
    else:
        print(new_contents, end="")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--spaces",
        metavar="n",
        type=int,
        help="indent using 'n' spaces (if omitted, indent using tabs)",
    )
    parser.add_argument(
        "--in-place",
        "-i",
        action="store_true",
        help="modify files in place",
    )
    parser.add_argument(
        "filename",
        nargs="+",
        help="a file to format",
    )
    return parser.parse_args()


if __name__ == "__main__":
    ns = parse_args()
    for filename in ns.filename:
        format(filename, ns.spaces, ns.in_place)
