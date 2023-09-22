def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    print(f"Pisahkan Antara: {arr} Menjadi {left_half} Dan {right_half}")

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    print(f"Gabungkan: {left} Dan {right} Menjadi {result}")

    return result

# Interactive input from the user
input_str = input("Masukkan List Angka, Pisahkan Menggunakan Spasi: ")
input_list = [int(x) for x in input_str.split()]

print(f"Input List: {input_list}")

sorted_list = merge_sort(input_list)
print(f"List Yang Sudah Tersort: {sorted_list}")
