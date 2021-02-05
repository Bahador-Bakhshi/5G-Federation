import numpy as np
import math

time_interval = 10
rate = 2
arrivals = [0]
# print(rate)
while arrivals[-1] < time_interval:
    print("arrivals -1: ",arrivals[-1])
    t = np.random.exponential(scale=float(1)/float(rate))
    print("t:", t)
    arrivals += [arrivals[-1] + t]
    print("arrivals[]: ", arrivals, "\n")
if arrivals[-1] > time_interval:
    arrivals = arrivals[:-1]

arrivals = arrivals[1:]


print("absolute value:", math.ceil(abs(-0.005)))

# def merge(a, b):
#     result = []
#     for i in a:
#         for j in b:
#             elem = (i,j)
#             result.append(elem)
#     return result
#
#
#
# Q = np.zeros(shape = (1,2), dtype =np.float)
#
#
# cpu = np.arange(20)
# mem = np.arange(30)
# # print(cpu)
# capacity = np.concatenate((cpu,mem))
# new_capacity = merge(cpu,mem)
# print(capacity)
# cpu = cpu.reshape(len(cpu),1)
# print(cpu)
# mem = mem.reshape(len(mem),1)
#
# # print(cpu)
# # print(mem)
#
# # capacity = np.concatenate(cpu,mem, axis=0)
#
# print(len(capacity))
# print(new_capacity)
#
# array_capacity = np.asarray(new_capacity)
# print(array_capacity)
# # array_capacity = array_capacity.reshape(len(array_capacity),1)
# print(array_capacity[150])


