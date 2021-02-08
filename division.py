numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
output = []
for i in range(len(numbers)):
    if(numbers[i]%2 == 0):
        output.append(i+1)
print("The positions of numbers divisible by 2 are: {}".format(output))