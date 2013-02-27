

def addInstr(arg1, arg2, arg3):
    return arg1*arg2
    print "add"

def andInstr(arg1, arg2, arg3):
    print "and"

def storeInstr(arg1, arg2, arg3):
    print "store"

def loadInstr(arg1, arg2, arg3):
    print "load"

def shiftInstr(arg1, arg2, arg3):
    print "shift"

def beqInstr(arg1, arg2, arg3):
    print "beq"

def haltInstr(arg1, arg2, arg3):
    print "halt"

def tbdInstr(arg1, arg2, arg3):
    print "tbd"

opcodes   = {"000": addInstr,
             "001": andInstr,
             "010": storeInstr,
             "011": loadInstr,
             "100": shiftInstr,
             "101": beqInstr,
             "110": haltInstr,
             "111": tbdInstr,
             }

def exe():
    prog = open("compilerOut.txt", "r")
    count = 0
    for line in prog:
        count += 1
        
        op = line[0:3]
        func = opcodes.get(op)
        
        arg1, arg2, arg3 = None, None, None        
        
        if (opcodes.get(op) == addInstr) or (opcodes.get(op) == shiftInstr) or (opcodes.get(op) == andInstr):
            arg1 = line[3:7]
            arg2 = line[7:10]
            
        elif (opcodes.get(op) == storeInstr) or (opcodes.get(op) == loadInstr):
            arg1 = line[3]
            arg2 = line[4:10]
            
        elif (opcodes.get(op) == beqInstr):
            arg1 = line[3]
            arg2 = line[4:8]
            arg3 = line[8:10]
            
        if func:
            try:
                func(arg1, arg2, arg3)
            except Exception as inst:
                print "Error executing ", func.__name__, " on line", count," :", inst
                return
        else:
            print "Error on line ", count, " unknown function call: ", op
        
        
        
    
    pass
if __name__ == '__main__':
    exe()