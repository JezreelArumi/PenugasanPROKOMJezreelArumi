# 2.7 Stripping Names
# The name has a tab and a newline at the start, and a tab and a newline
# at the end. The | marks make the whitespace around the name visible.
name = "\t\nAl Kinasih\t\n"

print("Original name:")
print(f"|{name}|")

print("\nlstrip():")
print(f"|{name.lstrip()}|")

print("\nrstrip():")
print(f"|{name.rstrip()}|")

print("\nstrip():")
print(f"|{name.strip()}|")