def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    sorted_list = sorted(list_of_integers)
    return sorted_list[-1]
