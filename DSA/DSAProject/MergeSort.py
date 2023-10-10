def main():


def mergesort(arr):
    if 


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

# print(merge([1,2,9,10,100], [4,5,6,17,20,24,26,27,28,34,35,36]))

def splt(arr):
    n = len(arr)
    hlf = n/2 if n%2==0 else (n+1)/2
    hlf = int(hlf)
    a = arr[:hlf]
    b = arr[hlf:]

    return a,b








