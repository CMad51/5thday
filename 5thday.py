# hoval_avval
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
minimum=min(ages)
#print(minimum)
maximum=max(ages)
ages.append(minimum)
ages.append(maximum)
ages.sort()
numbers=len (ages)
if numbers % 2 ==1:
 mediane =(ages[int(numbers-1)/2])
elif numbers % 2== 0:
 mediane=((ages[int(numbers/2)])+(ages[int(numbers/2)-1]))/2
else:
 None

print(int(mediane))


