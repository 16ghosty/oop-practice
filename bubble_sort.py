def Bubble_Sort(arr):
    for i in range(len(arr)-1):
        swap = False
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)
                swap = True
        if not swap:
            break
    return arr
        


if __name__ == "__main__":
    arr=[45,234,23,455,12,2,8,556,89,0,54,23,4,6,77,54]
    print(Bubble_Sort(arr))