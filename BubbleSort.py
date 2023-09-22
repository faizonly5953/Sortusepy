def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to optimize the algorithm by detecting if any swaps were made in a pass
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap the elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        print(f"Pass {i+1}: {arr}")
        
        # If no swaps were made in a pass, the array is already sorted
        if not swapped:
            break

# Interactive input from the user
input_str = input("Masukkan List Angka, Pisahkan Dengan Spasi: ")
input_list = [int(x) for x in input_str.split()]

print(f"Input List: {input_list}")

bubble_sort(input_list)
print(f"List Yang Sudah Di Sort: {input_list}")
