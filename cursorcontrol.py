def terminal_reset():
    print("\u001b[0m", end="")

def cursor_up(n):
    print("\u001b[" + str(n) + "A", end = "") 

def cursor_down(n):
    print("\u001b[" + str(n) + "B", end = "")

def cursor_left(n):
    print("\u001b[" + str(n) +"D", end = "")
    
def cursor_right(n):
    print("\u001b[" + str(n) + "C", end = "")


def cursor(dir,n):
	dir =str.lower(dir)
	print("\u001b[" + str(n) , end = "")
	
	if(dir=="up") :
		print("A", end="")
	elif(dir=="down") :
		print("B", end="")
	elif(dir=="right") :
		print("C", end="")
	elif(dir=="left") :
		print("D", end="")


def set_colour(colour,fb):
    
    colour=str.lower(colour)
    fb=str.lower(fb)
    
    print("\u001b[",end="")
    
    if (fb=="text"):
        print("3" , end = "")
    elif (fb=="background"):
        print("4" , end = "")
    else:
        return
    
    if(colour=="black") :
        print("0", end="")
    elif(colour=="red") :
        print("1", end="")
    elif(colour=="green") :
        print("2", end="")
    elif(colour=="yellow") :
        print("3", end="")
    elif(colour=="blue") :
        print("4", end="")
    elif(colour=="magenta") :
        print("5", end="")
    elif(colour=="cyan") :
        print("6", end="")
    elif(colour=="white") :
        print("7", end="")
    
    print("m" , end = "")
    
    

def set_display_attrib(attrib):
    
    print("\u001b[",end="")
    
    if(attrib=="bright"):
        print("1m", end="")
    elif(attrib=="dim"):
        print("2m", end="")
    elif(attrib=="underscore"):
        print("4m", end="")
    elif(attrib=="blink"):
        print("5m", end="")
    elif(attrib=="reverse"):
        print("7m", end="")
    elif(attrib=="hidden"):
        print("8m", end="")
    else :
        print("0m")
    
    

def save_cursor_pos():
    print("\u001b[s",end="")

def restore_cursor_pos():
    print("\u001b[u",end="")

def enable_line_wrap():
    print("\u001b[7h",end="")

def disable_line_wrap():
    print("\u001b[7h",end="")

def set_cursor_column(col):
    print("\u001b[" + str(col) + "G", end = "")

    
def set_cursor_XY(x,y):
    print("\u001b[" + str(x) + ";" + str(y) + "H", end = "")
    
def cls():
    print("\u001b[2J",end="")

def clear_screen_down():
    print("\u001b[0J",end="")

def clear_screen_up():
    print("\u001b[1J",end="")

def clear_line():
    print("\u001b[2K",end="")

def clear_to_line_end():
    print("\u001b[0K",end="")

def clear__to_line_start():
    print("\u001b[1K",end="")

def scroll_down():
    print("\u001b[D",end="")

def scroll_up():
    print("\u001b[M",end="")

def scroll_between(start, end):
    print("\u001b[" + str(start) + ";" + str(end) + "r",end = "")

def scroll_normal():
    print("\u001b[r",end = "")






print("1234567890")
print("X")
print("X")
print("X")
print("X")
print("X")
print("X")
print("X")
print("X")
print("X")
cursor_up(4)
print("up4")
cursor_down(3)
print("down3")
cursor_right(12)
print("right12")
cursor_left(7)
print("left7")