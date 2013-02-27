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
             "$store"  : "0100",
             "$beq1"  : "0101",
             "$beq2"  : "0110",
             "$beq3"  : "0111",
             "$s1"  : "1000", 
             "$47"  : "1001", 
             "$flag"  : "1010", 
             "$four"  : "1011",
             "$load"  : "1100",
             "$negone"  : "1101",
             "$zero": "1110",
             "$one" : "1111"
             }


def get_binary():
    progIn = open("compilerIn.txt", "r+")
    progOut = open("compilerOut.txt", "w")
    count = 0
    labels = {}
    data = progIn.readlines()
    for x in range(len(data)):
        count += 1
        inputLine = data[x].split()
        if inputLine[0][0:5] == "Label":
            # add {Labels# : count(base 2)} to the labels dictionary .  b's show up for some reason so i replace them
            labels[inputLine[0].replace(":", "")] = bin(count).replace("b", "0").zfill(5)
            data[x] = " ".join(inputLine[1:len(inputLine)]) + "\n"
            
    print data, "!!!", labels
    

    count=0
    for line in data:
        count += 1
        inputLine = line.split()
        outputLine = []
        
        for x in range(len(inputLine)):
            inputLine[x] = inputLine[x].replace(",", "")
            
            #get the opcodes
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
                    
                    # store flag is 1 for storing to stack and 0 for storing to mem[10]
                    
                    if inputLine[1] == "0": 
                        pass# what to do if it was a zero
                    else:
                        pass# what to do if it was a one
                    
                    #append whatever it is for now
                    outputLine.append(inputLine[x])
                    
                elif (inputLine[0] == "beq"):
                    if (inputLine[x][0] != "0") and (inputLine[x][0] != "1"):                       
                        print "Error on line", count, ":\n    second arg of a load/store/beg instr must be 1 or 0, got ", inputLine[x]; return   
                        
                    outputLine.append(inputLine[x])                    
                    
            # third argument, beq only   
            elif x == 3:
                if not(labels.has_key(inputLine[x])):                       
                    print "Error on line", count, ":\n    unknown label: ", inputLine[x]; return 
                outputLine.append(labels.get(inputLine[x]))
                
        progOut.writelines(outputLine + ["\n"])
    
if __name__ == '__main__':
    get_binary()

            
        
        
        