import math 
cases = int(input().rstrip())

for i in range(cases):
    line = int(input().rstrip())
    
    print(line, end = " ") #Prints the number back out
    
    #Yin vs Yang
    
    if line%2==0:
        print("Yang", end = " ")
    else:
        print("Yin", end = " ")
        
    #figuring out Element
    Elements = ["Wood","Fire", "Earth", "Metal", "Water"]
    Element = line - 4
    Element = Element%10
    Element = math.floor(Element/2)
    print(Elements[Element], end = " ")
    #Animal 
    Animals = ["Rat","Ox", "Tiger", "Rabbit", "Dragon","Snake","Horse", "Goat", "Monkey", "Rooster","Dog","Pig"]
    Year = line - 4
    Year = Year%12
    print(Animals[Year])
    