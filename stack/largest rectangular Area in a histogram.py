def max_Area_Histogram(histogram):
    stack = []
    max_area = 0
    index = 0
    while index < len(histogram):
        if stack == [] or histogram[stack[-1]] < histogram[index]:
            stack.append(index)
            index+=1
        else:
            top_of_stack = stack.pop()
            area = (histogram[top_of_stack]*((index - 1 - stack[-1]) if stack else index))

            max_area = max(max_area, area)

    while stack:
        top_of_stack = stack.pop()
        area = (histogram[top_of_stack]*((index - 1 - stack[-1]) if stack else index))

        max_area = max(max_area, area)


    return max_area

h = [6, 2, 5, 4, 5, 1, 6]
print("Maximum area is",
       max_Area_Histogram(h))