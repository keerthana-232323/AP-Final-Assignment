def do_tasks(arr) -> None:
    if not arr:
        return

    if len(arr) >= 4:
        print("Fourth item:", arr[3])
    else:
        print("The list has less than four items.")

    print(f"All items in the list except first two: {arr[2:]}")
    print(f"The list in reverse order: {arr[::-1]}")
    print(f"The sum of elements in the list: {sum(arr)}")
    print(f"Maximum element: {max(arr)} and Minimum element: {min(arr)}")

    if 0 in arr:
        print(f"Index of first 0 in the list: {arr.index(0)}")
    else:
        print("Index of first 0 in the list: -1")

    print(f"Sorted list in ascending order: {sorted(arr)}")
    print(f"Sorted list in descending order: {sorted(arr, reverse=True)}")


do_tasks([10, 20, 30, 20, 0, 20, 30, 40, 50, -20, 60, 60, -20])
