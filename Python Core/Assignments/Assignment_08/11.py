

def rev(n,rev_no):
    while n > 0:
        digit = n % 10
        rev_no = rev_no * 10 + digit
        n = n // 10

    return rev_no


n = int(input('Enter the number to check rev: '))
rev_no = 0


print(rev(n,rev_no))