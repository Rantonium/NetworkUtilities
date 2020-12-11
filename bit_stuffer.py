import sys

bitstring=sys.argv[1]
data=list(bitstring)
nrOnes = int(sys.argv[2])  
  
i=0
c=0

while(i<len(data)):
  print(data[i],end=" ")
  if(data[i]=='1'):
      c+=1
  else: 
      c=0
  
  if c==(nrOnes-1):
    data.insert(i+1,'0')
    c=0
    i+=1
  i+=1

x='0'+'1'*nrOnes+'0'+(''.join(data))+'0'+'1'*nrOnes+'0'
print("\n"+x)
