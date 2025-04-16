class InvalidInputException(Exception):
    """An exception is raised when the colours are not R or G."""
    pass


def change(s):
    try:
        for c in s:
            if c != "R" and c != "G":
                raise InvalidInputException ("Colour is not R or G.")
    except InvalidInputException as err:
        print(f"InvalidInputException: {err}")
    else:
        s_list = list(s)
        r_count = s_list.count("R")
        g_count = s_list.count("G")
        change_count = 0
        if r_count > g_count:
            for i in range(len(s_list)):
                if s_list[i] == "G":
                    change_count += 1
        else:
            for i in range(len(s_list)):
                if s_list[i] == "R":
                    change_count += 1

        return change_count


colours = input("Enter colours (only R and G): ").upper()
print(f"Minimum number of changes: {change(colours)}")
