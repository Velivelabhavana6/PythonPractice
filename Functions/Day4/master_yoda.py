def master_yoda(text):
       s=text.split()
       s.reverse()
       return ' '.join(s)
   
print(master_yoda("i am home"))