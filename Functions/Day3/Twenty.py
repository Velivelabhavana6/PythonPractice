def makes_Twenty(n1,n2):
    n3=n1+n2
    if n3==20:
        return True
    elif n1==20 or n2==20:
        return True
    else:
        return False

print(makes_Twenty(12,8))