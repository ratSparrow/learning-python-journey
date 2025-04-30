done = True
# done 

print (type(done) == bool)

if done:
    print("Yes")
else:
    print("No")


book_read_1 = True
book_read_2 = False

print(any ([book_read_1, book_read_2])) #Any function   returns True if any of the values are True
print(all ([book_read_1, book_read_2])) #All function returns True if all of the values are True