
# ******************************
large = None
small = None

while True:
    word = input()
    if word == 'stop' or word == 'STOP':
        break
    if large is None or len(word) > len(large):
        large = word
    if small is None or len(word) < len(small):
        small = word

print(large, small)
# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
