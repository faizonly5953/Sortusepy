def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Langkah  {i}: {arr}")

# Interactive input from the user
input_str = input("Masukkan List Angka, Pisahkan Dengan Spasi: ")
input_list = [int(x) for x in input_str.split()]

print(f"Input List: {input_list}")

insertion_sort(input_list)
print(f"List Yang Sudah Tersort: {input_list}")
