def spy_game(arr):
    code=[0,0,7,'X']
    for i in arr:
        if i==code[0]:
            code.pop(0)
    #     if not code:
    #         return True
    # return False
    return len(code)==1
print(spy_game([1,2,0,0,89,5,7]))