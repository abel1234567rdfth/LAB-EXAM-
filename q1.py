def main():
    num_sequence = input("Enter a sequence  numbers  ")
    num_array = [int(num) for num in num_sequence.split(",")]
    search_number = int(input("Enter the number to search : "))
    count = num_array.count(search_number)
    if count > 0:
        print(f"{search_number} is present  {count} times.")
    else:
        print(f"{search_number} is not found.")
if __name__ == "__main__":
    main()
