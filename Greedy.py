


#Greedy methods implemented

class Greedy:

    #1.Gas fuel problem
    #假设有一个汽车从A点x0行驶到B点xn，中间各个加油站的里程位置构成一个数组gas_station[x0,x1...,xn]，汽车在加满油的情况下能够行驶的
    #最大距离为max_distance，要求在从A到B的过程中使用最少的加油站并返回使用加油站的数目
    def min_fuel(self,gas_station,max_distance):
        x = 0
        num = 0
        while(x!=len(gas_station)-1):
            now_index = x
            while(x < len(gas_station)-1)and(gas_station[x+1]-gas_station[now_index] <= max_distance):
                x = x + 1
            if (now_index == x):
                return False
            if x<(len(gas_station)-1):
                num = num+1
        return num

    #2.Celebration party
    #聚会分配老师问题，有不同孩子的年龄组成数组ages=[x0,...,xn],需要给他们进行分组，要求每个组内的年龄
    #差距不超过max_age_dis，要求返回各个分组
    def distrubute_groups(self,ages,max_age_dis):
        ages.sort()
        i = 0
        groups = []
        while i<=len(ages)-1:
            list = [ages[i],ages[i]+max_age_dis]
            group = self.find_children(list,ages)
            groups.append(group)
            while i<=len(ages)-1 and ages[i]<=list[1]:
                i = i+1
        return groups

    def find_children(self,list,ages):
        group = []
        for age in ages:
            if age>=list[0] and age<=list[1]:
                group.append(age)
        return group



if __name__ == '__main__':
    gas_station = [0, 100, 200, 300]
    max_distance = 200
    greedy = Greedy()
    # num = greedy.min_fuel(gas_station, max_distance)
    # print(num)
    ages = [1.1,1.2,1.5,2,3,5,5.5,6]
    max_age_dis = 1
    groups = greedy.distrubute_groups(ages,max_age_dis)
    print(groups)