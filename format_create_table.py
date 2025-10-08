#!/usr/bin/env python

import re
import sys

def format_create(sql: str) -> str:
    sql = sql.lower() \
        .replace("`", "") \
        .replace("\t", " ") \
        .replace("\\n", "\n")

    # get max fieldname len
    lines = []
    fieldnames = []
    max_fieldname_len = 0
    for line in sql.splitlines():
        if line.startswith('table'):
            continue
        parts = line.split(' ')
        # remove tablename column
        if parts[1] == 'create' and parts[2] == 'table':
            parts = parts[1:]
        # handle leading spaces
        if parts[0] == '' and parts[1] == '':
            fieldname = parts[2]
            fieldnames.append(fieldnames)
            max_fieldname_len = max(max_fieldname_len, len(fieldname))
        lines.append(parts)

    # create output
    key_found = 0
    constraint_found = 0
    lines2 = []
    for parts in lines:
        if parts[0] == '' and parts[1] == '':
            fn = parts[2]
            # add blank line before keys
            if (fn == 'primary' or fn == 'key') and not key_found:
                lines2.append('')
                key_found = 1
            # add blank line before constraints
            if fn == 'constraint' and not constraint_found:
                lines2.append('')
                constraint_found = 1
            parts[2] = parts[2].ljust(max_fieldname_len)
        # add blank line before closing ')'
        if parts[0] == ')':
            lines2.append('')
        lines2.append(' '.join(parts))
    # add semicolon at the end
    lines2.append(';')

    return '\n'.join(lines2)

if __name__ == "__main__":
    raw = sys.stdin.read()
    print(format_create(raw))
