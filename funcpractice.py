def max_num(num1, num2, num3):
    return max(num1, num2, num3) 

print(max_num(1, 2, 3))
# Output: 3

#==============================
def mult_list(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

print(mult_list([7,27,31]))
# Output: 5859

#==============================
def rev_string(string):
    return string[::-1]

print(rev_string("This is a Mirage"))
# Output: "egariM a si sihT"

#==============================
def num_within(x, range):
    if range[0] <= x <= range[1]:
        return True
    else:
        return False

print(num_within(31, (7, 27)))
# Output: False

#==============================
def pascal(n):
    for i in range(n):
        row = [1]*(i+1)
        for j in range(1, i):
            row[j] = prev_row[j-1] + prev_row[j]
        prev_row = row
        print(" ".join(str(x) for x in row))

pascal(5)