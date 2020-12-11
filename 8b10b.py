bit5dict={}
bit5dict['00000']= ['100111','011000']
bit5dict['00001']= ['011101','100010']
bit5dict['00010']= ['101101','010010']
bit5dict['00011']= ['110001','110001']
bit5dict['00100']= ['110101','001010']
bit5dict['00101']= ['101001','101001']
bit5dict['00110']= ['011001','011001']
bit5dict['00111']= ['111000','000111']
bit5dict['01000']= ['111001','000110']
bit5dict['01001']= ['100101','100101']
bit5dict['01010']= ['010101','010101']
bit5dict['01011']= ['110100','110100']
bit5dict['01100']= ['001101','001101']
bit5dict['01101']= ['101100','101100']
bit5dict['01110']= ['011100','011100']
bit5dict['01111']= ['010111','101000']
bit5dict['10000']= ['011011','100100']
bit5dict['10001']= ['100011','100011']
bit5dict['10010']= ['010011','010011']
bit5dict['10011']= ['110010','110010']
bit5dict['10100']= ['001011','001011']
bit5dict['10101']= ['101010','101010']
bit5dict['10110']= ['011010','011010']
bit5dict['10111']= ['111010','000101']
bit5dict['11000']= ['110011','001100']
bit5dict['11001']= ['100110','100110']
bit5dict['11010']= ['010110','010110']
bit5dict['11011']= ['110110','001001']
bit5dict['11100']= ['001110','001110']
bit5dict['11101']= ['101110','010001']
bit5dict['11110']= ['011110','100001']
bit5dict['11111']= ['101011','010100']

bit3dic={}
bit3dic['000']=['0100','1011']
bit3dic['001']=['1001','1001']
bit3dic['010']=['0101','0101']
bit3dic['011']=['0011','1100']
bit3dic['100']=['0010','1101']
bit3dic['101']=['1010','1010']
bit3dic['110']=['0110','0110']
bit3dic['111']=['0001','1110','1000','0111']


def encode(number,rdx,rdy):
    x = bit5dict[(number[3:8])]

    if(rdx==-1):
        x=x[0]
    else:
        x=x[1]
    nr = int(x, base=2)
    nr0,nr1=0,0
    for i in x:
        if i=='0':
            nr0+=1
        if i=='1':
            nr1+=1
    rdnoux = rdx
    if(nr1==nr0):
        rdnoux = rdx
    if(nr1!=nr0 and rdx==1):
        rdnoux = -1
    if(nr1!=nr0 and rdx==-1):
        rdnoux = 1

    y = bit3dic[(number[0:3])]

    if(rdy==-1):
        y=y[1]
    if(rdy==1):
        y=y[0]
    if(rdy==-1 and (nr==17 or nr==18 or nr==20)):
        y=y[3]
    if(rdy==1 and (nr==11 or nr==13 or nr==14)):
        y=y[2]
    nr0,nr1=0,0
    for i in y:
        if i=='0':
            nr0+=1
        if i=='1':
            nr1+=1
    rdnouy = rdy
    if(nr1==nr0):
        rdnouy = rdy
    if(nr1!=nr0 and rdy==1):
        rdnouy = -1
    if(nr1!=nr0 and rdy==-1):
        rdnouy = 1

    return rdnoux,rdnouy, x+y
    
rdx=-1
rdy=-1
rez=[]
for i in ['10100010','00010000','10000111']:
    rdx,rdy,vect=encode(i,rdx,rdy)
    rez.append(vect)

print(rez)