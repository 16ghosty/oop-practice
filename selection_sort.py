def Select_sort(arr):
    for i in range(len(arr)):
        midx = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[midx]:
                midx = j
            print(arr)
        arr[i], arr[midx] = arr[midx], arr[i]
        
    return arr  

if __name__ == "__main__":
    arr = [23,4,1,245,67,8856,323,452,1223,421,664,66789,9586]
    print(Select_sort(arr))