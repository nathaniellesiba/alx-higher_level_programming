#!/usr/bin/python3
def text_indentation(text):

if not isinstance(text, str):
raise TypeError("text must be a string")

punctuation = ['.', '?', ':']
start = 0
for i in range(len(text)):
if text[i] in punctuation:
print(text[start:i+1].strip())
print()
start = i+1
print(text[start:].strip())

