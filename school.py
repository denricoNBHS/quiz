def print_schedule(n, s):
    """ Prints a student's schedule 
    n -- the student's name, a string
    s -- the student's schedule, a list of strings.
    """

    title = "Schedule for {}".format(n)
    bar = '='*len(title)

    classes = ""
    for period, cls in enumerate(s):
        classes += "{}. {}\n".format(period + 1, cls)

    return "\n".join([bar, title, bar, classes]) 
