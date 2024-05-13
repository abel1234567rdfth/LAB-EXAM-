def delete_element(arr, index):
    if index < 0 or index >= len(arr):
        print("Invalid index.")
        return arr
    else:
        return arr[:index] + arr[index + 1:]
array = [3, 7, 1, 9, 4]
index = 2
modified_array = delete_element(array, index)
print("Modified:", modified_array)
