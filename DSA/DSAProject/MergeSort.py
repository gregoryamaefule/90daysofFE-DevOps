def main():
    print(mergesort([1,9819,-1,-3]))
    # print(mergesort([4,7,8,9,3,2,1]))


def mergesort(arr):
    if len(arr) == 1:
        return arr
    else:
        a,b = splt(arr)

        return merge(mergesort(a),mergesort(b))


def merge(arr1, arr2=[]):
    resArr = []
    k = 0
    j = 0
    for i in range(len(arr1) + len(arr2)):
        if k > len(arr1) - 1 and j <= len(arr2) - 1:
            resArr.extend(arr2[j:])
            break
        elif j > len(arr2) - 1 and k <= len(arr1) - 1:
            resArr.extend(arr1[k:])
            break

        if k > len(arr1) - 1 or j > len(arr2) - 1:
            break

        if arr1[k] < arr2[j]:
            resArr.append(arr1[k])
            k += 1
        elif arr1[k] > arr2[j]:
            resArr.append(arr2[j])
            j += 1

    return resArr


def splt(arr):
    n = len(arr)
    hlf = n/2 if n%2==0 else (n+1)/2
    hlf = int(hlf)
    a = arr[:hlf]
    b = arr[hlf:]

    return a,b

if __name__ == '__main__':
    main()





