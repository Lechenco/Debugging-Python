import sys
import readline

def remove_html_markup(s):
    tag   = False
    quote = False
    out   = ""
    
    for c in s:
        
        if c == '<' and not quote:
            tag = True
        elif c == '>' and not quote:
            tag = False
        elif (c == '"' or c == "'") and tag:
            quote = not quote
        elif not tag:
            out += c
        
    return out

stepping = False
breakpoints = {9: True, 14: True}
watchpoints = {'c': True}

def debug(command, my_locals):
    global stepping
    global breakpoints
    
    if command.find(' ') > 0:
        arg = command.split(' ')[1]
    else:
        arg = None

    if command.startswith('s'):     # step
        stepping = True
        return True
    elif command.startswith('c'):   # continue
        stepping = False
        return True
    elif command.startswith('p'):    #print
        if len(command) < 2:
            print(my_locals)
        else:
            var = command[2:]
            try:
                varvalue = my_locals[var]
                print var, ' = ', varvalue
            except KeyError:
                print "No such variable:", var

    elif command.startswith('b'):    # breakpoint
        try:
            line = int(command[2:])
            breakpoints[line] = True
        except ValueError:
            print "You must supply a line number"
        
    elif command.startswith('w'):   #watchpoint
        try:
            var = command[2:]
            watchpoints[var] = my_locals[var]
        except KeyError:
            print "You must supply a variable name"

    elif command.startswith('q'):   # quit
        sys.exit(0)
    else:
        print("No such command", repr(command))
        
    return False

commands = ["p", "s", "p s", "p fo", "q"]

def input_command():
    command = raw_input("(my-spyder) ")
    #global commands
    #command = commands.pop(0)
    return command

def traceit(frame, event, trace_arg):
    global stepping

    if event == 'line':
        if stepping or breakpoints.has_key(frame.f_lineno):
            resume = False
            while not resume:
                print(event, frame.f_lineno, frame.f_code.co_name, frame.f_locals)
                command = input_command()
                resume = debug(command, frame.f_locals)
    return traceit

sys.settrace(traceit)

print(remove_html_markup("xyz"))

sys.settrace(None)
