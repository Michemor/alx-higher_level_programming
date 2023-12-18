#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    divides integers contained at the same position
    in both lists
    """
    added_list = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
            added_list.append(div)
        except ZeroDivisionError:
            print("division by zero")
            added_list.append(0)
        except TypeError:
            print("wrong type")
            added_list.append(0)
        except IndexError:
            print("out of range")
            added_list.append(0)
        finally:
            continue
    return (added_list)
