import sys

max_pol=0
for i in range(999, 100-1,-1):
    for j in range(999, 100-1,-1):
        value=str(i*j)
        len_value=len(value)
        #print(value)
        if len_value%2==0:
            if value[:len_value//2:] == value[len_value//2:len_value:][::-1]:
                if max_pol < int(value):
                    max_pol=int(value)
                print(value, i, j)

        else:
            if value[:len_value//2:] == value[len_value//2+1:len_value:][::-1]:
                if max_pol < int(value):
                    max_pol=int(value)
                print(value, i, j)

        
print(max_pol)
