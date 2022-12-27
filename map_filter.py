import functools
import statistics


data=[x for x in range(-100,100,3)]
def iseven(i):
    return i%2==0
evens=list(filter(iseven, data))
print(evens)
evens1=[]
for i in data:
    if i%2==0:
        evens1.append(i)
print(evens1)
print(list(filter(lambda x: x %2 ,data)))
list=[x for x in range (1,20)if not x%3==0]
print(list)
data1=[1.3,2.1,3.2,0.4,0.9,0.5,1.1,2.7]
#print(dir(statistics))
##help(statistics.geometric_mean)
g_mean=statistics.geometric_mean(data1)
print(f"{g_mean=}")
#print(f"filter output:{list(filter(lambda x:x> g_mean,data1))}")
data5=[10,20,30,40,50]
map_out= list(map(lambda x:2*x,data5))
print(f"data5:{data5}")
#print(f"map_out:{map_out}")
sum_out= functools.reduce(lambda x,y: x+y ,map_out)
print(f"sum_out:{sum_out}")
print(f"avg:{sum_out/len(data5)}")
