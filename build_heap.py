# python3


def build_heap(data, n, i):
    # swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    # smallest = -1
    # for i in range((n//2)-1, -1, -1):

        # smallest = i+1  # garantē ka uzsāks while ciklu
        # while smallest != i:   # cikls turpinās līdz mazākā vērtība ir priekšā
    smallest = i
    l = 2 * i + 1   # kreisais
    r = 2 * i + 2   # labais

    if l < n and data[l] < data[smallest]:
        smallest = l
    
    if r < n and data[r] < data[smallest]:
        smallest = r
    
    if smallest != i:
        swaps.append([i,smallest])
        (data[i], data[smallest]) = (data[smallest], data[i])
        build_heap(data,n,smallest)

def heapS(data,n):
    for i in range((n//2)-1,-1,-1):
        build_heap(data,n,i)
    # for i in range(n-1, -1, -1):
        # Move current root to end #
    #     data[0], data[i] = data[i], data[0]
    #     build_heap(data, i, 0)
    
swaps = []
def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    text = input()
    data = []
    n = 0
    if text == "I": # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))

    elif text == "F": # input from file
        text = "tests/04"
        with open(text) as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
            

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    heapS(data, n)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    # fails = open("atbilde","w")
    if swaps == 0:
        print(0)
        # fails.write(0)
    else:
        print(len(swaps),end ="")
        # fails.write(str(len(swaps))+"\n")
        for i, j in swaps:
            print(i, j,end="")
            # fails.write(str(i) +" "+ str(j)+"\n")
    # fails.close()
    # output all swaps

    # print("sorted: ")
    # print(data)


if __name__ == "__main__":
    main()
