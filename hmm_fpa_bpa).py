# -*- coding: utf-8 -*-
"""HMM_FPA_BPA (1).ipynb


<h1> <center> HIDDEN MARKOV MODEL</center></h1>,

<h2><center>USER INPUT</center></h2>
"""

def getInput():
    #getting input states
    hidStates = int(input("Enter number of Hidden states(S) : "))
    emmiStates = int(input("Enter number of Emmission States(E) : "))
    #creating a dictionary and hashing values to string names(for easy access)...
    hash_bag = {}
    print("=========================================\n\n\n\n\n")
    #getting puts of hidden states and hashing them to respective strings...
    print("Enter the values for Hidden State")
    for i in range(1,hidStates+1):
        for j in range(1,hidStates+1):
            stry = 'S' + str(i)+"S"+str(j)+" (a"+str(i)+str(j)+")"
            x = float(input("Enter the value of "+stry + ": "))
            hash_bag['a'+str(i)+str(j)] = x
    print("=========================================== \n\n\n\n")
    print("Enter the values of emmission State")
    #getting puts of emmision states and hashing them to respective strings...
    emmi_value = {}
    for i in range(1,hidStates+1):
        for j in range(1,emmiStates+1):
            stry = 'S' + str(i)+'E' + str(j)+" (e"+str(i)+str(j)+")"
            x = float(input("Enter the value of "+ stry + ": "))
            hash_bag['e'+str(i)+str(j)] = x
    #print("The values are : ", hash_bag)
    print("============================\n\n")
    print("Enter the pie value for the hidden states - \n")
    for i in range(1,hidStates+1):
        x = float(input("Enter the pie value S "+str(i)+" : "))
        hash_bag['pi'+str(i)] = x

    return hash_bag

"""<h2><center> FORWARD PROPAGATION"""

def FPA():

    #getting number of grams ...
    words = int(input("Enter the grams in order : "))
    grams = []

    for i in range(words):
        temp = int(input("Enter K : "))
        grams.append(temp)
    print("Enter the intialise Alpha value : ")

    for i in range(1,3):
        key = 'IN'+str(i)+str(1)
        value = int(input("Enter the "+key+" : "))
        dic[key] = value

    for T in range(1,words+1):
        for I in range(1,3):
            adder = 0
            for J in range(1,3):
                j = float(dic['a'+str(I)+str(J)]*dic['e'+str(I)+str(grams[0])]*dic['IN'+str(J)+str(T)])
                adder = adder+j
                dic['IN'+str(I)+str(T+1)] = adder
        grams.pop(0)
    result = 0
    for i in range(1,2+1):
      result = result + dic['IN'+str(i)+str(4)]
    return dic,result

"""## <center>  BACKWARD PROPAGATION


"""

def BPA():

    #getting number of grams ...
    words = int(input("Enter the grams in order : "))
    grams = []
    rev_grams = []
    for i in range(words):
        temp = int(input("Enter K : "))
        grams.append(temp)
    rev_grams = grams[::-1]
    print("Enter the intialise Beta value : ")
    for i in range(1,3):
        key = 'IN'+str(i)+str(words+1)
        value = int(input("Enter the "+key+" : "))
        dic[key] = value
    for T in reversed(range(words+1)):
        if T == 0:
            break
        else:
            for I in range(1,3):
                adder = 0
                for J in range(1,3):
                    j = float(dic['a'+str(I)+str(J)]*dic['e'+str(I)+str(rev_grams[0])]*dic['IN'+str(J)+str(T+1)])
                    adder = adder+j
                    dic['IN'+str(I)+str(T)] = adder
            rev_grams.pop(0)
    result = 0
    for i in range(1,2+1):
      result = result +(dic['pi'+str(i)]*dic['IN'+str(i)+str(1)])
    return dic,result

"""<h2><center> FINAL RESULT DERIVATION"""

#Driver code ....
print("===============================USER INPUT==========================\n\n\n")
dic = getInput()



print("===============================FPA=================================\n\n\n")
hash_bagy , result = FPA()
print("The generated hash : ")
print(hash_bagy)
print("The result is : ",result)
print("===============================BPA=================================\n\n\n")
has_bagy, result = BPA()
print("The generated hash : ")
print(has_bagy)
print("The result is : ",result)



