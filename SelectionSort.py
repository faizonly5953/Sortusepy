def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the remaining unsorted part
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"Langkah {i+1}: {arr}")

# Interactive input from the user
input_str = input("Masukkan List Angka, Pisahkan Dengan Spasi: ")
input_list = [int(x) for x in input_str.split()]

print(f"Input List: {input_list}")

selection_sort(input_list)
print(f"List Yang Sudah Tersort: {input_list}")
