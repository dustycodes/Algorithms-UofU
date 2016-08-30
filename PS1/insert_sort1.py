comp = 0
def compare():
    global comp
    comp += 1
    return True

def sort_numbers(s):
    for i in range(1, len(s)):
        val = s[i]
        j = i - 1
        while (j >= 0) and compare() and (s[j] > val):
            s[j+1] = s[j]
            j = j - 1
        s[j+1] = val
        if s[2] == 7:
            return

s = [0, 7, 8, 5, 6, 3, 4, 1, 2]
sort_numbers(s)
print(comp)