# st="Print only the words that start with s in this sentence"
# for i in st.split():
#     if i[0]=='s':
#         print(i)
   
# for i in range(0,10):
#     if(i%2==0):
#         print(i)

# a=[i for i in range(0,50) if i%3==0]
# print(a)

# st='ptrint every word in this sentence that has a even num of letters'
# for i in st.split():
#     if(len(i)%2==0):
#         print(i+" is even")
        
#     print("even")
    
for i in range(1,100):
    if(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    elif (i%3==0 and i%5==0):
        print("fizzBuzz")
    else:
        print(i)