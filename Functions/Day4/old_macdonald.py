def old_macdonald(name):
    # s=""
    # for i in range(len(name)):
    #     if(i==0 or i==3):
    #         s=s+name[i].upper()
    #     else:
    #         s=s+name[i]
    # return s
    first=name[:3]
    second=name[3:]
    return first.capitalize()+second.capitalize()

print(old_macdonald('macdonald'))