loc = ['s1','s2','s3','s4','s5','s6']
dist = [1500,1000,2400,3400,2100,4000]

source = input("Enter source : ")
dest = input("enter destination : ")

i_source = loc.index(source)
i_dest = loc.index(dest)

i = i_source
total_distance = 0

while (i != i_dest):
    total_distance += dist[i]
    print(i)
    if (i == len(loc) - 1):
        i = 0
    else :
        i += 1
print(total_distance)
cost_km = int(input("Enter cost per km : "))
cost = (total_distance/1000) * cost_km
print("Total cost : ",cost)