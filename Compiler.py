opcodes   = {"add"   : "000",
             "and"   : "001",
             "store" : "010",
             "load"  : "011",
             "shift" : "100",
             "beq"   : "101",
             "halt"  : "110",
             "tbd"   : "111"
             }

registers = {"$t1"  : "0000",
             "$t2"  : "0001",
             "$t3"  : "0010",
             "$t4"  : "0011",
             "$t5"  : "0100",
             "$t6"  : "0101",
             "$t7"  : "0110",
             "$t8"  : "0111",
             "$s1"  : "1000",
             "$s2"  : "1001",
             "$s3"  : "1010",             
             "$s4"  : "1011",
             "$s5"  : "1100",
             "$s6"  : "1101",
             "$zero"  : "1110",
             "$one"  : "1111"
             }


def get_binary():
    progIn = open("compilerIn.txt", "r")
    progOut = open("compilerOut.txt", "w")
    count = 0
    for line in progIn:
        count += 1
        inputLine = line.split()
        outputLine = []
        
        for x in range(len(inputLine)):
            inputLine[x] = inputLine[x].replace(",", "")
            
            if x == 0: 
                outputLine.append(opcodes.get(inputLine[x]))
                
                if not(opcodes.has_key(inputLine[x])): 
                    print "Error on line", count, ":", "\n    unknown instruction ", inputLine[x]; return                    
                
                if (inputLine[0] == "and")or(inputLine[0] == "add")or(inputLine[0] == "shift")or(inputLine[0] == "load")or(inputLine[0] == "store"):                    
                    if (len(inputLine) != 3):
                        print "Error on line", count, ":", "\n    wrong number of args for an and/add/shift instr"; return                        
                
                elif (inputLine[0] == "beq"):
                    if (len(inputLine) != 4):
                        print "Error on line", count, ":", "\n    wrong number of args for a beq instr"; return                        
            # first argument 
            elif x ==1:
                if (inputLine[0] == "and") or (inputLine[0] == "add") or (inputLine[0] == "shift"):
                                        
                    if not(registers.has_key(inputLine[x])):
                        print "Error on line", count, ":", "\n    second arg of an add/and/shift instr must be a register, got ", inputLine[x]; return
                                            
                    outputLine.append(registers.get(inputLine[x]))
                    
                elif (inputLine[0] == "load") or (inputLine[0] == "store") or (inputLine[0] == "beq"):
                    
                    if (inputLine[x][0] != "0") and (inputLine[x][0] != "1"):                       
                        print "Error on line", count, ":\n    second arg of a load/store/beg instr must be 1 or 0, got ", inputLine[x]; return                        
                    
                    outputLine.append(inputLine[x])#1 or a zero
            # second argument 
            elif x ==2:
                if (inputLine[0] == "and") or (inputLine[0] == "add") or (inputLine[0] == "shift"):
                    
                    if (inputLine[x][1] != "t"): 
                        print "Error on line", count, ":\n    second register of an add/and/shift instr must be a 't' register.  EG '$t1'"; return                        
                    
                    outputLine.append(registers.get(inputLine[x])[1:4])
                    
                elif (inputLine[0] == "load") or (inputLine[0] == "store"):
                    
                    # this is the flag for load/store
                    
                    if inputLine[1] == "0": 
                        pass# what to do if it was a zero
                    else:
                        pass# what to do if it was a one
                    
                    #append whatever it is for now
                    outputLine.append(inputLine[x])
                    
                elif (inputLine[0] == "beq"):
                    if not(registers.has_key(inputLine[x])):
                        print "Error on line", count, ":", "\n    second arg on a beq instr must be a register, got ", inputLine[x]; return
                    outputLine.append(registers.get(inputLine[x]))
                    
            # third argument, beq only   
            elif x == 3:
                
                #how to handle hardcoded labels?
                outputLine.append(inputLine[x])
                
        progOut.writelines(outputLine + ["\n"])
    
if __name__ == '__main__':
    get_binary()

            
        
        
        