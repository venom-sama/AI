def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

def print_array(arr):
    print("Array:", arr)

def main():
    arr = []
    while True:
        print("\nSelection Sort Menu:")
        print("1. Enter Array")
        print("2. Sort Array")
        print("3. Print Array")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            arr = list(map(int, input("Enter the array elements separated by space: ").split()))
        elif choice == "2":
            if not arr:
                print("Please enter an array first.")
            else:
                selection_sort(arr)
                print("Array sorted using Selection Sort.")
        elif choice == "3":
            if not arr:
                print("Array is empty. Please enter an array first.")
            else:
                print_array(arr)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
