def sum_of_digit(n,a=0):
    a=a+(n%10)
    if n==0:
        return a
    else:
        return sum_of_digit((n//10),a)
    
    
print(f"sum of the digit is {sum_of_digit(n)}")
