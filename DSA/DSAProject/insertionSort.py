def main():
    print(iSort([4,3,7,-9,4,0,2,1]))


def iSort(arr):
    for i in range(len(arr)):
        key = i
        for j in range(len(arr[0:i])):
            if arr[key] >= arr[key - 1] or range(len(arr[0:i])) == 1:
                break
            else:
                hold = arr[key - 1]
                arr[key - 1] = arr[key]
                arr[key] = hold
                key = key - 1

    return arr


if __name__ == '__main__':
    main()