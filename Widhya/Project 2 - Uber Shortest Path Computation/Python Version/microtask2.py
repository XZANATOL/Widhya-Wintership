def distance_sum(arr, n):
    # sort the array
    arr.sort()

    # loop to find the distance of each independent axis
    res = 0
    sum = 0
    for i in range(n):
        res += arr[i] * i - sum
        sum += arr[i]

    return res


def totaldistancesum(x, y, n):
    return distance_sum(x, n) + distance_sum(y, n)


if __name__ == '__main__':
    n = int(input("Enter number of points > ")) # get array length
    print("") # for UI adjustment
    x = [float(input("Enter X point {} > ".format(_+1))) for _ in range(n)] # get x array
    print("") # for UI adjustment
    y = [float(input("Enter y Point {} > ".format(_ + 1))) for _ in range(n)] # get y array
    # print inputs & outputs
    print("\nEntered X coordinates list: {}".format(x))
    print("Entered y coordinates list: {}".format(y))
    print("Sum of Manhattan distance between all pairs of coordinates: {}".format(totaldistancesum(x,y,n)))