
possible = []

def isValid(num) :
    doubles = {}   
    for j in range(1, len(num)) :        # start at 2nd char
        if int(num[j-1]) <= int(num[j]) : # if previous char is less or equal to current char
            if num[j-1] == num[j] :  # if previous and current char matches
                if num[j] in doubles :
                    doubles[num[j]] += 1 # increment matching count
                else :
                    doubles[num[j]] = 2
        else :                    
            return False # previous char was the same or lwoer than current

    for key, val in doubles.items() : # if matching char count == 2 then True
        if val == 2 :
            return True

    return False

for i in range(240298,784956) :    
    number = str(i) # convert to string
    if isValid(number) :       
        possible.append(number)


print(len(possible))