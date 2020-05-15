from timeit import default_timer as timer

n = 100000000

def func(a):
    k = False
    result = 0
    for i in range(n):
        k = not k
        if k:
            result += 1
        else:
            result -= 1
    print(result)

def f_plus(val):
    return val + 1

def f_minus(val):
    return val - 1

def func2(a):
    k = False
    #calc_dic = {False: f_plus, True: f_minus}
    calc_dic = {False: 1, True: -1}
    result = 0
    for i in range(n):
        k = not k
        result += calc_dic[k]
    print(result)

def func3(a):
    k = False
    result = 0
    for i in range(n):
        k = not k
        result += 1
    print(result)

if __name__ == "__main__":

    a = []
    b = []
    c = []
    start = timer()
    func(a)
    print("without GPU:", timer() - start)

    start = timer()
    func2(b)
    print("with GPU 1:", timer() - start)

    start = timer()
    func3(b)
    print("with GPU 2:", timer() - start)
