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
        if parts[0] == '' and parts[1] == '':
            fieldname = parts[2]
            fieldnames.append(fieldnames)
            max_fieldname_len = max(max_fieldname_len, len(fieldname))
        lines.append(parts)
    #lines = []
    #fieldnames = []
    #max_fieldname_len = 0
    lines2 = []
    for parts in lines:
        if parts[0] == '' and parts[1] == '':
            parts[2] = parts[2].ljust(max_fieldname_len)
        lines2.append(' '.join(parts))
            
    return '\n'.join(lines2)

    #print(max_fieldname_len)
    #return "\n".join(lines)

    #return sql
    # Normalize case of main keywords
    # keywords = [
    #     "create table", "primary key", "unique key", "key",
    #     "constraint", "foreign key", "references",
    #     "engine=", "default charset="
    # ]
    # for kw in keywords:
    #     sql = re.sub(kw, kw.lower(), sql, flags=re.I)

    # Split commas into newlines (but not inside parentheses like decimal(12,4))
    #sql = re.sub(r",\s+([A-Za-z])", ",\n\\1", sql)

    # lines = []
    # inside = False
    # for line in sql.splitlines():
    #     line = line.rstrip()
    #     # if line.lower().startswith("create table"):
    #     #     lines.append(line)
    #     #     inside = True
    #     #     continue
    #     # if inside:
    #     #     if line.startswith(")"):
    #     #         inside = False
    #     #         lines.append(")")
    #     #         continue
    #     #     if line:
    #     #         lines.append("   " + line)  # indent 3 spaces
    #     # else:
    #     #     lines.append(line)

    # # Ensure closing semicolon
    # if not lines[-1].strip().endswith(";"):
    #     lines[-1] = lines[-1] + "\n;"

    #return "\n".join(lines)

if __name__ == "__main__":
    raw = sys.stdin.read()
    print(format_create(raw))
