def build_histogram(lists):
    for data in lists:
        brick = ""
        no_of_times = data
        while no_of_times > 0:
            if no_of_times % 2 == 0:
                brick += "* "
            else:
                brick += "*."
            no_of_times -= 1
        print(brick)


# Call Method directly
build_histogram([3, 6, 7, 9, 7])
