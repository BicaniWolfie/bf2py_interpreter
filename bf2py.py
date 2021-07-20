# Initial Variables
debug = False
file_name = "Test Files/hw2.bf"
code_string = open(file_name, 'r').read()

if debug == True:
    print("Coverting: " + code_string)

# Creation of a sorted list of positions "while_sort", in an alternating pattern as follows:
# [starting while-bracket, ending while-bracket, starting while-bracket, ending while-bracket, ...]
while_sorted = []

# Creation of a temporary array used for the operation of sorting the list
e = []

for i in range(len(code_string)):
    if(code_string[i] == '['):
        e.append(i)
    if(code_string[i] == ']'):
        while_sorted.append(e[-1])
        while_sorted.append(i)
        e.pop();

if debug == True:
    print("Sorted List: " + str(while_sorted))

# This is the main interpreter of the code. Variables for this loop will be defined as follows:
index_pointer = 0
b = -1
buffer = [0] * len(code_string)
char_buffer = []
text_buffer = ""

while (b < len(code_string)):
    
    # Program increments the current position in the code by 1
    b += 1
    
    # The loop breaks if it has reached the end of the code 
    if b == len(code_string):
        break

    # A definition of the instructions for each of the 8 symbols used by "Brainfuck"
    # First the loop checks for any potential while-loops in Brainfuck
    if code_string[b] == '[':
        if(buffer[index_pointer] == 0):
            a = while_sorted.index(b)
            b = while_sorted[a + 1]
            if debug == True:
                print(str(b) + " is a while start going to to position " + str(while_sorted[a + 1]))
                print("Value Index: " + str(index_pointer) + " Index Value: " + str(buffer[index_pointer]))
    elif code_string[b] == ']':
        if(buffer[index_pointer] != 0):
            a = while_sorted.index(b)
            b = while_sorted[a - 1]
            if debug == True:
                print(str(b) + " is a while end going to position " + str(while_sorted[a - 1]))
                print("Value Index: " + str(index_pointer) + " Index Value: " + str(buffer[index_pointer]))
    
    # Next comes instructions for each of the other 6 operations
    elif(code_string[b] == '>'):
        if debug == True:
            print(">")
        index_pointer += 1
    elif(code_string[b] == '<'):
        if debug == True:
            print("<")
        index_pointer -= 1
    elif(code_string[b] == '+'):
        if debug == True:
            print("+")
        buffer[index_pointer] += 1
    elif(code_string[b] == '-'):
        if debug == True:
            print("-")
        buffer[index_pointer] -= 1
    elif(code_string[b] == '.'):
        char_buffer.append(chr(buffer[index_pointer]))
        if debug == True:
            print("Updated Char Buffer: "  + str(char_buffer))
    elif(code_string[b] == ','):
        buffer[index_pointer] = ord(char_buffer[index_pointer])
        if debug == True:
            print("Updated Char Buffer: "  + str(char_buffer))

## Decoding of the buffer into a temporary text buffer, which gets printed into the console
for i in range (len(char_buffer)):
    if char_buffer[i] != '':
        text_buffer += str(char_buffer[i])
print(text_buffer)