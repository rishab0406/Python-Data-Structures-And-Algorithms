def selection_sort(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if i!= min_index:
            arr[i],arr[min_index] = arr[min_index] , arr[i]
    print(elements)


if __name__ =="__main__":
    elements=[47,9,1,98,33,82,7,69,42]
    selection_sort(elements)
