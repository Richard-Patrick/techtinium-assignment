"""
Created on Fri Jun 12 19:10:32 2020

@author: Patrick


@Assignment: Techtinium


"""
# country based optimizer
def optimizer(capacity,hour,Machine_capacity,Machine_cost,region):
    machine=[]
    optimizer_info={}
    cost=0
    for i in Machine_capacity:
        if Machine_capacity[i] <= capacity:
            no_large = capacity // Machine_capacity[i]
            new_capacity = capacity % Machine_capacity[i]
            capacity = new_capacity
            machine.append((i,no_large))
            cost=cost+(Machine_cost[i]*no_large)
    optimizer_info["region"]=region
    optimizer_info["Total_cost"]= ('${}'.format(cost*hour))
    optimizer_info["Machines"]= machine
    return(optimizer_info)



# user input
capacity,hour =input().split(" ")
capacity,hour =int(capacity),int(hour)


# data of newyork
newyork_Machine_capacity = {'8XLarge': 160, '4XLarge': 80, '2XLarge': 40, 'XLarge': 20, 'Large': 10}
newyork_Machine_cost = {'8XLarge': 1400, '4XLarge': 774, '2XLarge': 450, 'XLarge': 230, 'Large': 120}

# data of india
Indian_Machinecapacity= {'8XLarge': 160, '2XLarge': 40, 'Large': 10}
India_Machinecost= {'8XLarge': 1300, '2XLarge': 413, 'Large': 140}
# data of newyork
china_Machinecapacity = {'8XLarge': 160, '4XLarge': 80, 'XLarge': 20, 'Large': 10}
china_Machinecost = {'8XLarge': 1180, '4XLarge': 670, 'XLarge': 200, 'Large': 110}

# optimizer
newyork=optimizer(capacity,hour,newyork_Machine_capacity,newyork_Machine_cost,"New York")
india=optimizer(capacity,hour,Indian_Machinecapacity,India_Machinecost,"India")
china=optimizer(capacity,hour,china_Machinecapacity,china_Machinecost,"China")

output=[newyork,india,china]
print(output)


