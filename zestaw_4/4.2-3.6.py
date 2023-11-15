def draw_rectangle(height, width):

    rectangle = ""

    for i in range(0, height):
        rectangle+= "+"
        rectangle+= "---+" *width
        rectangle+= "\n"

        rectangle+= "|"
        rectangle+= "   |" * width
        rectangle+= "\n"

    rectangle+= "+"
    rectangle+= "---+" * width
    rectangle+= "\n"

    print(rectangle)

draw_rectangle(3, 7)
