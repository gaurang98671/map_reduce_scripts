import sys
import ast

s = "('a', 'b')"
s = ast.literal_eval(s)
print(s)
