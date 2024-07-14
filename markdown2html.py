#!/usr/bin/python3

import sys
import os
import hashlib

def print_usage_and_exit():
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

def print_missing_and_exit(filename):
    print(f"Missing {filename}", file=sys.stderr)
    sys.exit(1)

def convert_heading(line):
    heading_level = len(line.split(' ')[0])
    if heading_level > 6:
        return line
    return f"<h{heading_level}>{line[heading_level+1:].strip()}</h{heading_level}>"

def convert_unordered_list(lines):
    result = ["<ul>"]
    for line in lines:
        result.append(f"    <li>{line[1:].strip()}</li>")
    result.append("</ul>")
    return result

def convert_ordered_list(lines):
    result = ["<ol>"]
    for line in lines:
        result.append(f"    <li>{line[1:].strip()}</li>")
    result.append("</ol>")
    return result

def convert_paragraph(lines):
    result = ["<p>"]
    for line in lines:
        result.append(f"    {line}")
    result.append("</p>")
    return result

def convert_bold_and_emphasis(text):
    text = text.replace("**", "<b>", 1).replace("**", "</b>", 1)
    text = text.replace("__", "<em>", 1).replace("__", "</em>", 1)
    return text

def convert_custom_syntax(text):
    while '[[' in text and ']]' in text:
        start = text.index('[[')
        end = text.index(']]') + 2
        content = text[start+2:end-2]
        md5_content = hashlib.md5(content.encode()).hexdigest()
        text = text[:start] + md5_content + text[end:]

    while '((' in text and '))' in text:
        start = text.index('((')
        end = text.index('))') + 2
        content = text[start+2:end-2]
        modified_content = content.replace('c', '').replace('C', '')
        text = text[:start] + modified_content + text[end:]

    return text

def parse_markdown(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    html_lines = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('#'):
            html_lines.append(convert_heading(line))
        elif line.startswith('-'):
            ul_lines = []
            while i < len(lines) and lines[i].strip().startswith('-'):
                ul_lines.append(lines[i].strip())
                i += 1
            html_lines.extend(convert_unordered_list(ul_lines))
            continue
        elif line.startswith('*'):
            ol_lines = []
            while i < len(lines) and lines[i].strip().startswith
