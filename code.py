def check_freq(x):
    freq = {}
    for c in set(x):
       freq[c] = x.count(c)
    return freq
    
string = 'BOOKKEEPER'
output = string
freq_dict = check_freq(string)
for c in set(string):
    if(freq_dict[c] == 2):
        output = output.replace(c,'z')
    if(freq_dict[c] >= 2):
        output = output.replace(c,'x')
print(output)

#output: BzzzzxxPxR
