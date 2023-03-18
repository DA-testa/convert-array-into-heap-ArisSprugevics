# python3


def build_heap(data, n):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for i in range((n//2)-1, -1, -1):

        smallest = i+1  # garantē ka uzsāks while ciklu
        while smallest != i:   # cikls turpinās līdz mazākā vērtība ir priekšā
            smallest = i
            l = 2 * i + 1   # kreisais
            r = 2 * i + 2   # labais

            if l < n and data[l] < data[smallest]:
                smallest = l
            
            if r < n and data[r] < data[smallest]:
                smallest = r
            
            if smallest != i:
                swaps.append[i,smallest]
                data[i], data[smallest] = data[smallest], data[i]

    for i in range(n-1,-1,-1):
        data[0], data[i] = data[i], data[0] # pārvieto root uz beigām
        smallest = i+1
        n=i
        i = 0

        while smallest != i:   # cikls turpinās līdz mazākā vērtība ir priekšā
            smallest = i

            l = 2 * i + 1   # kreisais
            r = 2 * i + 2   # labais

            if l < n and data[l] < data[smallest]:
                smallest = l
            
            if r < n and data[r] < data[smallest]:
                smallest = r
            
            if smallest != i:
                swaps.append[i,smallest]
                data[i], data[smallest] = data[smallest], data[i]
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    text = input()

    if text == "I": # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))

    elif text == "F": # input from file
        text = input()
        with open(text) as f:
            n = int(f.readline())
            data = list(map(int, f.readlines().split()))
    else:
        print("unknown command")
    

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data, n)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    print(len(swaps))

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
