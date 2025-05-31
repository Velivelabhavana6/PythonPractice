def paper_doll(text):
    result=''
    for char in text:
        result=result+char*3
    return result

print(paper_doll)