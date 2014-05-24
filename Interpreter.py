from array import array;
import sys;
#This will input the program as string
#Then read the whole program and if any character found instead of the 8 commands give an error along with character.
program = input();
error = 1;#initialized to false
opening = 0;
closing = 0;
for index in range(0, len(program)):
    if(program[index] != '.' and program[index] != "," and program[index] != '>' and program[index] != '<' and program[index] != '-' and program[index] != '+' and program[index] != '[' and program[index] != ']'):
        #print(program[index]);
        #print("Error found ar character number: %d" % index);
        error = 0;

    if(program[index] == ']'):
        closing = closing + 1;

    if(program[index] == '['):
        opening = opening + 1;

if(opening != closing):
    error = 0;
    #print ("Unequal number of opening and closing brackets for looping");

#no error in program so continue;

if error == 1:
    print("No error found in program. Interpreting your code");


#this is the algorithm for interpreting.
#1. Cound the numbers of total command supplied by the user.
#2. Then Strat executing from the beggining till the end.
#3. Whenever a srating square bracket comes get its index and also the ending square bracket index. Then execute that part seperately by
#passing it to a function. Now recurion will occur of an other brackets are found. Executing the commands inside the brackets till
#the current value of the pointer pointing is 0.


#, is used for input;
#. is used for output; input and output is only ascii characters.
#< is used to move the pointer left
#> is used to move the poiner right
#+ is used to increment the value the pointer is pointing to
#- is used to decremenet the value the pointer is pointing to


class execution:
    infinite_array = array("i");#will hold decimals (integers);
    pointer = 0;#pointing to a particular operation.
    program = "";
    number_of_commands = len(program);
    iii = 0;#execution will start from command at 0 index of the string.
    input_stream = "";#stream holding the user inputs.

    def __init__(self, program):
        self.program = program;
        self.number_of_commands = len(self.program);

    #functions for command , . + - < >
    def execution_comma(self):
        #take the input
        if(len(self.input_stream) == 0):
            self.input_stream = input();
            x = list(self.input_stream)[0];#when we pass a string to list it takes out single chars and then puts them in form of list of characters.
            self.input_stream = self.input_stream[1:];#remove the first character
            y = ord(x);#takes an character and returns its ascii code i.e., decimal equivalent.
            self.infinite_array.insert(int(self.pointer + 1), y);
        else:
            x = list(self.input_stream)[0];
            self.input_stream = self.input_stream[1:];#remove the first character
            y = ord(x);
            self.infinite_array.insert(int(self.pointer + 1), y);

        #print("Input taken");

    def execution_fullstop(self):
        #print("The output is below");
        if(self.infinite_array[self.pointer] >= 0 and self.infinite_array[self.pointer] <= 255):
            #print();
            sys.stdout.write(str(chr(self.infinite_array[self.pointer])));
            sys.stdout.flush();


    def execution_lessthan(self):
        self.pointer = self.pointer - 1;
        #print("Less than executed %i" % self.pointer);

    def execution_greaterthan(self):
        self.pointer = self.pointer + 1;
        #print("Graeter than executed %i" % self.pointer);

    def execution_increment(self):
        self.infinite_array[self.pointer] = self.infinite_array[self.pointer] + 1;
        #print("Increment executed %i" % self.pointer);

    def execution_decrement(self):
        self.infinite_array[self.pointer] = self.infinite_array[self.pointer] - 1;
        #print("Decrement executed %i" % self.infinite_array[self.pointer]);

    def execution_loop(self, start, end):
        print("Execution started");
        s = start;
        e = end;
        z = 0;
        #now execute from start index to end index

        while(self.infinite_array[self.pointer] != 0):
            #print("%i" % z);
            s = start;
            z = z + 1;
            while s < e:
                if(self.program[s] == '.'):
                    self.execution_fullstop();
                    s = s + 1;
                    continue;

                if(self.program[s] == ','):
                    self.execution_comma();
                    s = s + 1;
                    continue;

                if(self.program[s] == '+'):
                    self.execution_increment();
                    s = s + 1;
                    continue;

                if(self.program[s] == '-'):
                    self.execution_decrement();
                    s = s + 1;
                    continue;

                if(self.program[s] == '>'):
                    self.execution_greaterthan();
                    s = s + 1;
                    continue;

                if(self.program[s] == '<'):
                    self.execution_lessthan();
                    s = s + 1;
                    continue;

                if(self.program[s] == '['):
                    ss = s + 1;
                    ee= self.number_of_commands;
                    temp = 0;
                    #find the range first
                    for g in range(ss, ee):
                        if(self.program[g] == '['):
                            temp = temp + 1;
                        else:
                            if(self.program[g] == ']'):
                                if(temp > 0):
                                    temp = temp - 1;
                                else:
                                    ee = g;
                    z = ee - s;
                    s = ss + 1 + z;
                    self.execution_loop(ss,ee);

                else:
                    s = s + 1;


    def start(self):
            while self.iii < self.number_of_commands:
                if(self.program[self.iii] == '.'):
                    self.execution_fullstop();
                    self.iii = self.iii + 1;
                    continue;

                if(self.program[self.iii] == ','):
                    self.execution_comma();
                    self.iii = self.iii + 1;
                    continue;

                if(self.program[self.iii] == '-'):
                    self.execution_decrement();
                    self.iii = self.iii + 1;
                    continue;

                if(self.program[self.iii] == '+'):
                    self.execution_increment();
                    self.iii = self.iii + 1;
                    continue;

                if(self.program[self.iii] == '<'):
                    self.execution_lessthan();
                    self.iii = self.iii + 1;
                    continue;

                if(self.program[self.iii] == '>'):
                    self.execution_greaterthan();
                    self.iii = self.iii + 1;
                    continue;

                if(self.program[self.iii] == "["):
                    #what this will do is find the range between the closing and opening brackets.
                    #then it will ask the self.iii variable to continue from the closing bracket.
                    #then it will call a recursive function that will execute the commands between the range and also see if any
                    #new loop is present. Similar algorithm for every loop found (range finding) and then it will call the functions recursively.
                    #a loop stops when the pointer is pointer to a array element whose value is '0'

                    #first find the range.
                    #then pass the range to the recursive function.
                    #then increment the value of self.iii
                    #the recursive function is responsible for executing the loop.
                    start = self.iii + 1;
                    end = self.number_of_commands;
                    temp = 0;

                    #start a loop to search for the ending of the loop ie. ending index
                    for x in range(self.iii + 1, self.number_of_commands):
                        if(self.program[x] == '['):
                            temp = temp + 1;
                        else:
                            if(self.program[x] == ']'):
                                if(temp > 0):
                                    temp = temp - 1;
                                else:
                                    end = x;

                    #we got the start and end.
                    self.execution_loop(start, end);

                    #get the difference and give it for further looping.
                    z = end - self.iii;
                    self.iii = self.iii + 1 + z;

p = execution(program);
p.start();