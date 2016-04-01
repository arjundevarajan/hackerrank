nums = map(int,raw_input().split()); n = nums[0]; m = nums[1]; array = map(int,raw_input().split()); Aset = set(map(int,raw_input().split())); Bset = set(map(int,raw_input().split()))
happiness = 0
for i in array:
    if (i in Aset and i not in Bset):
        happiness+=1
    if (i in Bset and i not in Aset):
        happiness-=1
print happiness