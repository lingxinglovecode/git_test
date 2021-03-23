


#Greedy methods implemented

#Gas fuel problem
#假设有一个汽车从A点x0行驶到B点xn，中间各个加油站的里程位置构成一个数组gas_station[x0,x1...,xn]，汽车在加满油的情况下能够行驶的
#最大距离为max_distance，要求在从A到B的过程中使用最少的加油站并返回使用加油站的数目
def min_fuel(gas_station,max_distance):
    x = 0
    num = 0
    while(x!=len(gas_station)-1):
        now_index = x
        while(gas_station[x+1]-gas_station[now_index] <= max_distance) and ((x+1) < len(gas_station)-1):
            x = x + 1
        if (now_index == x):
            return False
        num = num+1
    return num

gas_station = [0,100,200,300]
max_distance = 100
num=min_fuel(gas_station,max_distance)
print(num)