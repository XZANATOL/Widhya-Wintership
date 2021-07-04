if __name__ == '__main__':
    # Get Inputs
    x1, y1 = map(float, input("Enter X1 and Y1 coordinates [x1 y1] > ").split())
    x2, y2 = map(float, input("Enter X2 and Y2 coordinates [x2 y2] > ").split())

    D = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    print("Distance between both points is: " + str(D))