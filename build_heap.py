def build_heap(data):
    swaps = []

    n = len(data)
    # TODO: Creat heap and heap sort

    for i in range(n // 2, -1, -1):
        heap_sort(data, i, swaps)
    return swaps


def heap_sort(data, i, swaps):
    
    n = len(data)

    parent = i
    kreis =2*i+1

    if kreis <= (n-1) and data[kreis] < data[parent]:
        parent = kreis

    labais =2*i+2  
    if labais <= (n-1) and data[labais] < data[parent]:

        parent = labais
    if i != parent:
        data[i], data[parent] = data[parent], data[i]
        swaps.append((i, parent))
        heap_sort(data, parent, swaps)




def main():   
    
    # TODO : add input and corresponding checks
    print("F vai I")
    inp = input()
    
    #ja F
    if "F" in inp :
        fails =input()

        if "a" not in fails:
            path = './tests/' + fails
            with open(path, 'r') as testfile:
                n = int(testfile.readline().strip())
                n1 = testfile.readline().strip()
            data = list(map(int, n1.split()))
            assert len(data) == n

            swaps = build_heap(data)

         # TODO: output how many swap


            print(len(swaps))
            for i, j in swaps:
                print(i, j)

   
    # ja I
    elif "I" in inp :
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n

        #call for access
        swaps = build_heap(data)

         # TODO: output how many swaps were made

        print(len(swaps))
        for i, j in swaps:
            print(i, j)
    else:
        print("error")
        return



if __name__ == "__main__":
    main()