import statistics

def start():
    print("Yo im legit retarded though")
def getuserinput():
    number = input("Enter some numbers yo seperated via commas: ")
    list =number.split(",")
    num_list=[]
    for i in list:
        num_list.append(float(i))
    print(num_list)
    return num_list
def avgyo(input):
    #total =0
    #for x in input:
        #total = total + x
    total = sum(input)
    length = len(input)
    average = total/length
    print(average)
    return 0
def minmax(input):
    minimum = min(input)
    maximum = max(input)
    #print(minimum)
    #print(maximum)
    newlist = []
    newlist.append(float(minimum))
    newlist.append(float(maximum))
    print(newlist)
    return newlist
def sort(input):
    input.sort()
    print(input)

def main():
    start()
    inp = getuserinput()
    avgyo(inp)
    minmax(inp)
    sort(inp)



if __name__ == '__main__':
    main()


