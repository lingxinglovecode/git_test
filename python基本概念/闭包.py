



#外函数返回内函数的引用
def out_fuc():
    out_params = 1
    def in_fuc():
        print(out_params)
        return True
    return in_fuc
b = out_fuc()
b()


#内函数对外函数的临时变量进行调用
def out_fuc():
    out_params = 1
    def in_fuc():
        # out_params = out_params + 1
        print(out_params)
        return True
    return in_fuc
b = out_fuc()
b()
a=2





def out_fuc():
    out_params_1 = 1
    out_params_2 = [1]
    def in_fuc():
        nonlocal out_params_1
        out_params_1 = out_params_1+1
        out_params_2[0] = out_params_2[0]+1
        print(out_params_1)
        print(out_params_2[0])
        return True
    return in_fuc()
b = out_fuc()
a=2