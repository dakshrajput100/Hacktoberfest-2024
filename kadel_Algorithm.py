def bubble_sort(arr):
    n = len(arr)  
    for i in range(n - 1): 
        swapped = False 
        for j in range(n - i - 1):  
           
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
                swapped = True   
        if not swapped:
            break  

def print_array(arr):
    for num in arr:  
        print(num, end=' ')  
    print()  

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]  
    bubble_sort(arr)  
    print("Sorted array:")  
    print_array(arr)  
