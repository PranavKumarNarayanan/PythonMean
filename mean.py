#Program to find the mean of grouped data by Pranav Kumar S
lower_limit=[]
upper_limit=[]
freq=[]
z=int(input('Please type the number of observations: '))
print('Please type the Upper Limit, Lower Limit, and the Frequency:')

for j in range(z):
    lower_limit.append(int(input('Lower Limit: ')))
    upper_limit.append(int(input('Upper Limit: ')))
    freq.append(int(input('Frequency: ')))
xi=[]

for l in range(z):
    xi.append((upper_limit[l]+lower_limit[l])/2)
fixi=[]

for k in range(z):
    fixi.append(freq[k]*xi[k])

sig_fixi=[]
sig_freq=[]
sig_freq=0
sig_fixi = 0

#Finding sum of fixi
for ele in range(0, len(fixi)):
	sig_fixi = sig_fixi + fixi[ele]
#Finding sum of frequency
for ele in range(0, len(freq)):
	sig_freq = sig_freq + freq[ele]
mean=sig_fixi/sig_freq
print('The mean of the given data is', mean)