def BinarySearch(sorted_arr, target):
    low = 0 
    high = len(sorted_arr)-1
    
    while low<=high:
        mid = (low+high)//2
        if sorted_arr[mid]==target:
            return mid
        elif sorted_arr[mid]<target:
            low = mid + 1
        else :
            high = mid - 1
    
    return -1

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,23,45,53,67,86,99,202,300,520]
    print(BinarySearch(arr,202))