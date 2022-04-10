import sys
from PIL import Image

stdin = ""

def main(src):
    try:
        filesrc = Image.open(src)
        
        w, h = filesrc.size
        pixel_map = filesrc.load()
        
        for x in range(w):
            for y in range(h):
                r, g, b, p = filesrc.getpixel((x, y))
                
                print(r, g, b)
    except Exception as e:
        print("An error occurred. Please specify a valid image file.")
        e.__trace_back__.print_exception()

def get_inst(r, g, b):
    pass

def interpret(code):
    cells = [0] * 1000
    ptr = 0
    stdin_ptr = 0
    
    read = 0
    
    ######
    
    min_value = 0
    max_value = 255
    
    min_cell = 0
    max_cell = 999
    
    ######
    
    while read < len(code):
        c = code[read]
        
        if c == '>':
            ptr = ptr + 1
            
            if ptr > max_cell:
                ptr = min_cell
        elif c == '<':
            ptr = ptr - 1
            
            if ptr < min_cell:
                ptr = max_cell
        elif c == '+':
            cells[ptr] = cells[ptr] + 1
            
            if cells[ptr] > max_value:
                cells[ptr] = min_value
        elif c == '-':
            cells[ptr] = cells[ptr] - 1
            
            if cells[ptr] < min_value:
                cells[ptr] = max_value
        
        elif c == '.':
            if (print_char):
                print(chr(cells[ptr]), end="")
            else:
                print(cells[ptr], end="") # não coloca mais espaço
        
        elif c == ',':
            #cells[ptr] = int(input("Requested Input: "))
            if stdin_ptr > len(stdin):
                print("Exceeded.")
            
            cells[ptr] = int(stdin[stdin_ptr])
            stdin_ptr = stdin_ptr + 1
        
        elif c == ']':
            if cells[ptr] != 0:
                count = 0
                
                for j in reversed(range(read - 1)):
                    ch = code[j]
                    
                    if ch == ']':
                        count = count + 1
                    
                    elif ch == '[':
                        if count != 0:
                            count = count - 1
                            
                            continue
                        
                        read = j
                        
                        break
        
        read = read + 1

if __name__ == "__main__":
    main(sys.argv[1])
