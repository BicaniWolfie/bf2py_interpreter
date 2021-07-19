
file_name = "helloworld.bf"
code_string = open(file_name, 'r').read();

def brainfuck(code):
    index_pointer = 0
    buffer = [0] * 3000
    text_buffer = ""
    
    for i in range (len(code)):
        if(code[i] == '>'):
            index_pointer += 1
        elif(code[i] == '<'):
            index_pointer -= 1
        elif(code[i] == '+'):
            buffer[index_pointer] += 1
        elif(code[i] == '-'):
            buffer[index_pointer] -= 1
        elif(code[i] == '.'):
            buffer[index_pointer] = chr(buffer[index_pointer])
        elif(code[i] == ','):
            buffer[index_pointer] = ord(buffer[index_pointer])
        elif(code[i] == '['):
            return
        elif(code[i] == ']'):
            return

    for i in range (len(buffer)):
        if buffer[i] != None:
            text_buffer + chr(buffer[i])
    print(text_buffer)
        
brainfuck(code_string)