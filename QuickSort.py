
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = []
    right = []
    equal = [pivot]

    for element in arr[1:]:
        if element < pivot:
            left.append(element)
        elif element > pivot:
            right.append(element)
        else:
            equal.append(element)

    print(f"Pivot: {pivot}")
    print(f"Left: {left}")
    print(f"Equal: {equal}")
    print(f"Right: {right}")

    left = quick_sort(left)
    right = quick_sort(right)

    return left + equal + right

# Interactive input from the user
input_str = input("Masukkan List Angka, Pisahkan Dengan Spasi: ")
input_list = [int(x) for x in input_str.split()]

print(f"Input List: {input_list}")

sorted_list = quick_sort(input_list)
print(f"Sorted List: {sorted_list}")
