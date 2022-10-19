n= 5
r=2
nfct = 1
rfct=1
nrfct=1
for x in range(1, n+1):
    nfct=nfct*x

for x in range(1, (n-r)+1):
    nrfct=nrfct*x

for x in range(1, r+1):
    rfct = rfct * x

# ncr = n! / (n-r)! * r!
ncr = nfct / nrfct * rfct
print(ncr)