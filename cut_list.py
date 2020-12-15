import math


global_counter = 0


def cut_me(givemelisthere: list, cutsize: int) -> list:
    global global_counter
    listholder = []
    try:
        equalsizecuts = math.floor(len(givemelisthere)/cutsize)
        if len(givemelisthere) % cutsize == 0:
            offset = 0
        else:
            offset = 1
        listholder = []
        ## creating holder for equal lists
        for i in range(equalsizecuts + offset):
            listholder.append([])
        print(listholder)
        global global_counter
        for i in range(equalsizecuts + 1):
            for j in range(len(givemelisthere)):
                listholder[i].append(givemelisthere[global_counter])
                global_counter += 1
                if global_counter > 0 and global_counter % cutsize == 0:
                    break
    except IndexError:
        print("Gentle warning: lists are of unequal sizes")
    except ZeroDivisionError:
        print("You cannot cut list into 0 length sizes.")
    return listholder

if __name__ == '__main__':
    mylist=[i for i in range(21)]
    print(mylist)
    cutlist = cut_me(mylist, 5)
    print("list is", cutlist)
# cut_list
