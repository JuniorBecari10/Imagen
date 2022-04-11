import sys
from PIL import Image

# Codes

# 0 0 0        | +
# 255 0 0      | -
# 0 255 0      | >
# 0 0 255      | <
# 255 255 0    | .
# 0 255 255    | ,
# 255 0 255    | [
# 255 255 255  | ]

stdin = ""

def main(src):
    try:
        filesrc = Image.open(src)
        code = ""
        
        w, h = filesrc.size
        pixel_map = filesrc.load()
        
        for y in range(h):
            for x in range(w):
                r, g, b, a = filesrc.getpixel((x, y))
                
                code += get_instruction(r, g, b, a)
        
        #print(code)
        interpret(code)
    except Exception as e:
        print("An error occurred. Please specify a valid image file.")
        #e.__traceback__.print_exception()

def get_instruction(r, g, b, a):
    if a == 0:
        return ""
    
    if r == 0 and g == 0 and b == 0:
        return "+"
    if r == 255 and g == 0 and b == 0:
        return "-"
    if r == 0 and g == 255 and b == 0:
        return ">"
    if r == 0 and g == 0 and b == 255:
        return "<"
    if r == 255 and g == 255 and b == 0:
        return "."
    if r == 0 and g == 255 and b == 255:
        return ","
    if r == 255 and g == 0 and b == 255:
        return "["
    if r == 255 and g == 255 and b == 255:
        return "]"
    
    return ""

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
            print((cells[ptr]), end="")
        
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
    if (len(sys.argv) != 2):
        print("Usage: python imagen.py/imagen.exe source.png")
        exit()
    
    main(sys.argv[1])
