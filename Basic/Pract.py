import sys
deg_seq=[7,6,6,4,4,3,2,2]
seq=sorted(deg_seq,reverse=True)

print(seq)
if sum(seq)%2!=0:
    print(deg_seq,'is invalid degree sequence')
    sys.exit()
while True:
    first_ele=seq.pop(0)
    for i in range(first_ele):
        seq[i] -=1
    seq=sorted(seq,reverse=True)
    print('seq',seq)
    if -1 in seq:
        print('invalid sequence')
        sys.exit()
    if not(any(seq)):
        print(deg_seq,'is a valid degree sequence')
        sys.exit()


