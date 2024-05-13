def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def main():
    num_sequence = input("Enter a sequence  numbers: ")
    num_array = [int(num) for num in num_sequence.split(",")]
    search_number = int(input("Enter the number : "))
    count = num_array.count(search_number)
    if count > 0:
        print(f"{search_number} is present  {count} times.")
    else:
        print(f"{search_number} is not found .")
    merge_sort(num_array)
    print("Sorted array:", num_array)
if __name__ == "__main__":
    main()
