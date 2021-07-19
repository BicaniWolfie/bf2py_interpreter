import bisect

file_name = "helloworld.bf"
code_string = open(file_name, 'r').read()
print("Converting: " + code_string)
# ++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.


# Defining Variables for the loop
while_start = []
while_end = []

for i in range(len(code_string)):
    if(code_string[i] == '['):
        while_start.append(i)
    elif(code_string[i] == ']'):
        while_end.append(i)

e = while_start.copy();
f = while_end.copy();
# while_sort = []

while_sort = [14,33,43,45,8,48]

# for i in range(len(e) - 1):
    
#     a = bisect.bisect_left(e, f[i]) - 1

#     while_sort.append(e[a])
#     while_sort.append(f[i])
#     e.remove(e[a])
#     f.remove(f[i])

# while_sort.append(e[0])
# while_sort.append(f[0])
# e.remove(e[0])
# f.remove(f[0])

print(while_sort)

print("List of [: " + str(while_start))
print("List of ]: " + str(while_end))

index_pointer = 0
b = 0
buffer = [0] * len(code_string)
char_buffer = [''] * len(code_string)
text_buffer = ""
skip_step = True

while (b <= len(code_string)):
    
    if(skip_step == False):
        b += 1
    else:
        skip_step = False
    # A definition of instructions for each of the 8 symbols in "Brainfuck"
    # print(b)
    if code_string[b] == '[':
        if(buffer[index_pointer] == 0):
            a = while_sort.index(b)
            print(str(b) + " is a while start going to to position " + str(while_sort[a + 1]))
            print("Value Index: " + str(index_pointer) + " Index Value: " + str(buffer[index_pointer]))
            b = while_sort[a + 1]
            # skip_step = True
    elif code_string[b] == ']':
        if(buffer[index_pointer] != 0):
            a = while_sort.index(b)
            print(str(b) + " is a while end going to position " + str(while_sort[a - 1]))
            print("Value Index: " + str(index_pointer) + " Index Value: " + str(buffer[index_pointer]))
            b = while_sort[a - 1]
            # skip_step = True
    elif(code_string[b] == '>'):
        # print(">")
        index_pointer += 1
    elif(code_string[b] == '<'):
        # print("<")
        index_pointer -= 1
    elif(code_string[b] == '+'):
        # print("+")
        buffer[index_pointer] += 1
    elif(code_string[b] == '-'):
        # print("-")
        buffer[index_pointer] -= 1
    elif(code_string[b] == '.'):
        char_buffer[index_pointer] = chr(ord('@') + buffer[index_pointer])
        buffer[index_pointer] = 0
        print("Updated Char Buffer: "  + str(char_buffer))
    elif(code_string[b] == ','):
        buffer[index_pointer] = ord(char_buffer[index_pointer])


## Decoding of the buffer into a temporary text buffer, which gets printed into the console
for i in range (len(char_buffer)):
    if char_buffer[i] != '':
        text_buffer += str(char_buffer[i])
print(text_buffer)