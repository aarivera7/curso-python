import math


def run():
    # my_dict = {}

    # for i in range(1,101):
    #     if i%3 != 0:
    #         my_dict[i] = i**3
    
    # print(my_dict)


    # dict = {i: i**3 for i in range(1,101) if i%3 != 0}
    # print(dict)

    dict_r = {i: math.sqrt(i) for i in range(1,1000)}
    print(dict_r)

if __name__ == "__main__":
    run()