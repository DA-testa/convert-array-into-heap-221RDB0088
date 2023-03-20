def main():
    text = input("enter 'I' or  'F'")
    if "F" in text:
        file_name = input("file name: ")
        if "a" not in file_name:
            path = './tests/'+file_name
            with open(path, 'r',encoding = 'utf-8') as file:
                n = int(file.readline())
                data = list(map(int,file.readline().split()))

        elif "I" in text:
            n = int(input())
            data = list(map(int,input().split()))

        assert data is not None and len(data) == n

        swaps = build_heap(data)

        assert len(swaps) <= n*4

        print(len(swaps))
        for i, j in swaps:
            print(i,j)

if __name__ == "__main__":
    main()