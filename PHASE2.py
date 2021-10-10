def twos_comp(val, bits):
    
    if ((val and (1 << (bits - 1))) != 0): # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val
#=====================fetch==================
def fetch(pc,list):
  return list[pc]

#==========================DECODE===================

def decode_op(arr,Reg):
    global RA,RB
    global B_SEL,rd,imm,ALU_op,Y_SEL,return_addr
    subArr=arr[25:] 
    fun3=arr[17:20]
    fun7=arr[0:7]
    if(subArr=="0110011"):                #R
      B_SEL=0
      Y_SEL[0]=0
      Y_SEL[1]=0
      Y_SEL[2]=0
      ops={"000":"00001","001":"00100","010":"00101","100":"01001","101":"00111","101":"00110","110":"00011","111":"00010"}
      

      if(fun7=="0100000"):
        if(fun3=="000"):	
	  ALU_op="01000"
	  
          rd=int(str(arr[20:25]),2)
          rs1=int(str(arr[12:17]),2)
          rs2=int(str(arr[7:12]),2)
          RA=Reg[rs1]
          RB=Reg[rs2]
          B_SEL=0
          A_sel=0
          InA=RA
          imm=0
	

	if(fun3=="101"):					#edited
	  ALU_op="00110"
	  
          rd=int(str(arr[20:25]),2)
          rs1=int(str(arr[12:17]),2)
          rs2=int(str(arr[7:12]),2)
          RA=Reg[rs1]
          RB=Reg[rs2]
          B_SEL=0
          A_sel=0
          InA=RA
          imm=0
	  



      elif(fun7=="0000001"):
        if(fun3=="000"):         #mul
          ALU_op="01010"
          rd=int(str(arr[20:25]),2)
          rs1=int(str(arr[12:17]),2)
          rs2=int(str(arr[7:12]),2)
          RA=Reg[rs1]
          RB=Reg[rs2]
          B_SEL=0
          A_sel=0
          InA=RA
          imm=0
        elif(fun3=="100"):        #div
          ALU_op="01011"
          rd=int(str(arr[20:25]),2)
          rs1=int(str(arr[12:17]),2)
          rs2=int(str(arr[7:12]),2)
          RA=Reg[rs1]
          RB=Reg[rs2]
          B_SEL=0
          A_sel=0
          InA=RA
          imm=0
        elif(fun3=="110"):        #rem
          ALU_op="01100"
          rd=int(str(arr[20:25]),2)
          rs1=int(str(arr[12:17]),2)
          rs2=int(str(arr[7:12]),2)
          RA=Reg[rs1]
          RB=Reg[rs2]
          B_SEL=0
          A_sel=0
          InA=RA
          imm=0
      else:
        ALU_op=ops.get(fun3)
        rd=int(str(arr[20:25]),2)
        rs1=int(str(arr[12:17]),2)
        rs2=int(str(arr[7:12]),2)
        RA=Reg[rs1]
        RB=Reg[rs2]
        B_SEL=0
        A_sel=0
        InA=RA
        imm=0
      


    elif(subArr=="0000011"):   #I
      B_SEL=1
      Y_SEL[0]=0
      Y_SEL[1]=0
      Y_SEL[2]=1             
      ops={"000":"10000" ,"001":"10010","010":"10011","011":"10001"}
      ALU_op=ops.get(fun3)
      if(arr[0]=='1'):
	binary_string = str(arr[0:12])
	imm = twos_comp(int(binary_string,2), len(binary_string))
      else:
	imm=int(str(arr[0:12]),2)
      rs1=int(str(arr[12:17]),2)
      rd=int(str(arr[20:25]),2)
      RA=Reg[rs1]
      B_SEL=1
      A_sel=0
      InA=RA

    elif(subArr=="0010011"):                 #I
      B_SEL=1
      Y_SEL[0]=0
      Y_SEL[1]=0
      Y_SEL[2]=1
      ops={"000":"01101" ,"110":"01111","111":"01110"}
      ALU_op=ops.get(fun3)
      if(arr[0]=='1'):
	binary_string = str(arr[0:12])
	imm = twos_comp(int(binary_string,2), len(binary_string))
      else:
        imm=int(str(arr[0:12]),2)
      rs1=int(str(arr[12:17]),2)
      rd=int(str(arr[20:25]),2)
      RA=Reg[rs1]
      B_SEL=1
      A_sel=0
      InA=RA

    elif(subArr=="1100111"):                 #I #jalr
      B_SEL=1
      Y_SEL[0]=0
      Y_SEL[1]=0
      Y_SEL[2]=1
      ALU_op="10100"
      if(arr[0]=='1'):
	binary_string = str(arr[0:12])
	imm = twos_comp(int(binary_string,2), len(binary_string))
      else:
        imm=int(str(arr[0:12]),2)
      rs1=int(str(arr[12:17]),2)
      rd=int(str(arr[20:25]),2)
      RA=Reg[rs1]
      B_SEL=1
      A_sel=0
      InA=RA
       
  

    elif(subArr=="0010111"):                 #auipc
      B_SEL=1
      Y_SEL[0]=0
      Y_SEL[1]=1
      Y_SEL[2]=0
      ALU_op="11101"
      rd=int(str(arr[20:25]),2)
      imm=int(str(arr[0:20])+"000000000000",2)
    
      RA=0
      RB=0
      A_sel=1
      InA=RA
                                                                #check
    
    elif(subArr=="0110111"):                  #lui
      B_SEL=1
      Y_SEL[0]=0
      Y_SEL[1]=1
      Y_SEL[2]=1
      ALU_op="11110"
            
      rd=int(str(arr[20:25]),2)
      imm=int(str(arr[0:20])+"000000000000",2)
      RA=0
      RB=0
      B_SEL=1
      A_sel=0
      InA=RA

    elif(subArr=="1101111"):                 #UJ
      B_SEL=0
      Y_SEL[0]=1
      Y_SEL[1]=0
      Y_SEL[2]=0
      ALU_op="11111"
      rd=int(str(arr[20:25]),2)

    
      
      #imm=int(str(arr[0])+str(arr[12:20])+str(arr[11])+str(arr[1:11]))+"0",2)
      binary_string = str((arr[0])+str(arr[12:20])+str(arr[11])+str(arr[1:11])+"0")
      if(arr[0]=='1'):
	imm = twos_comp(int(binary_string,2), len(binary_string))
      else:
        imm=int(binary_string,2)
      RA=0
      RB=0
      B_SEL=0
      A_sel=0
      InA=RA


    elif(subArr=="0100011"):                 #S         #fun3 for sd 011 
      B_SEL=1
      Y_SEL[0]=1
      Y_SEL[1]=0
      Y_SEL[2]=1
      ops={"000":"10101" ,"001":"10111","010":"11000","011":"10110"}
      ALU_op=ops.get(fun3)
      rd=0
      rs1=int(str(arr[12:17]),2)
      rs2=int(str(arr[7:12]),2)
      imm=int(str(arr[0:7])+str(arr[20:25]),2)
      RA=Reg[rs1]
      RB=Reg[rs2]
      B_SEL=1
      A_sel=0
      InA=RA



    elif(subArr=="1100011"):                 #SB
      B_SEL=0
      Y_SEL[0]=1
      Y_SEL[1]=1
      Y_SEL[2]=0
      ops={"000":"11001" ,"001":"11010","100":"11100","101":"11011"}
      ALU_op=ops.get(fun3)
      rd=0
      rs1=int(str(arr[12:17]),2)
      rs2=int(str(arr[7:12]),2)
      imm=int(str(arr[0])+str(arr[24])+str(arr[1:7])+str(arr[20:24])+"0",2)
      RA=Reg[rs1]
      RB=Reg[rs2]
      A_sel=0                                   #check
      InA=RA

    InA=RA

    



    
    
    return InA,B_SEL,RB,rd,imm,return_addr,ALU_op,subArr,fun3,Y_SEL

#==========EXECUTE================

def execute(op,ra,rb,PC,RB):
  global RM,rz
  RM=0
  if (op == "00001"):  #add                           
      rz= ra+rb
      print("RZ CHANGED TO: "+str(RZ))
     
  elif (op == "00010"):  #and            
      rz= ra&rb
      print("RZ CHANGED TO: "+str(RZ))
  elif (op == "00011"): #or
      rz= ra|rb
      print("RZ CHANGED TO: "+str(RZ))
  elif (op == "00100"): #sll
      rz= ra<<rb
      print("RZ CHANGED TO: "+str(RZ))
  elif (op == "00101"): #slt
     if(ra<rb):
       rz= 1
       print("RZ CHANGED TO: "+str(RZ))
     else:
       rz= 0
       print("RZ CHANGED TO: "+str(RZ))
  elif (op == "00110"): #sra
     rc=ra>>31
     rd=1<<31
     if(rc==1):
       for i in range(int(str(rb),2)):
         ra=ra>>1
         ra=ra+rd
       rz=ra
       print("RZ CHANGED TO: "+str(RZ))
     else:
       rz= ra>>rb                 #just
       print("RZ CHANGED TO: "+str(RZ))
      
  elif (op == "00111"): #srl
      rz= ra>>rb
      print("RZ CHANGED TO: "+str(RZ))
  elif (op == "01000"): #sub
      rz= ra-rb     
      print("RZ CHANGED TO: "+str(RZ))    
  elif (op == "01001"): #xor
      rz= ra^rb     
      print("RZ CHANGED TO: "+str(RZ))       
  elif (op == "01010"): #mul
      rz= ra*rb       
      print("RZ CHANGED TO: "+str(RZ))    
  elif (op == "01011"):  #div    
      rz= ra/rb      
      print("RZ CHANGED TO: "+str(RZ))
  elif (op == "01100"): #rem
      rz= ra%rb            
      print("RZ CHANGED TO: "+str(RZ))
  elif (op == "01101"): #addi
      
   
      rz= ra+rb
      print("RZ CHANGED TO: "+str(RZ))
  elif (op == "01110"): #andi
      rz= ra&rb
      print("RZ CHANGED TO: "+str(RZ))
  elif (op == "01111"): #ori
      rz= ra|rb
      print("RZ CHANGED TO: "+str(RZ))
  elif (op == "10000"): # lb
      RM =RB
      print("RM CHANGED TO: "+str(RM))
      rz= ra+rb
  elif (op == "10001"): #ld
      RM =RB
      print("RM CHANGED TO: "+str(RM))
      rz= ra+rb
  elif (op == "10010"): #lh
      RM = RB
      print("RM CHANGED TO: "+str(RM))
      rz= ra+rb
  elif (op == "10011"): #lw
      RM = RB
      print("RM CHANGED TO: "+str(RM))
      rz= ra+rb
  elif (op == "10100"): #jalr
      PC=ra+rb
      print("PC CHANGED TO: "+str(PC))	      
  elif (op == "10101"): #sb
      RM = RB
      print("RM CHANGED TO: "+str(RM))
      rz=ra+rb
  elif (op == "10110"): #sd
      RM = RB
      print("RM CHANGED TO: "+str(RM))
      rz= ra+rb
  elif (op == "10111"): #sh
      RM = RB
      print("RM CHANGED TO: "+str(RM))
      rz= ra+rb
  elif (op == "11000"): #sw
      RM = RB
      print("RM CHANGED TO: "+str(RM))
      rz= ra+rb
  elif (op == "11001"):#beq
      
      if(ra==rb):
        PC=PC+imm-4
        print("PC CHANGED TO: "+str(PC))	
	rz= ra+rb
        
      else:
        
        rz= ra+rb
                                
  elif (op == "11010"):#bne
      if(ra!=rb):
        PC=PC+imm-4
	print("PC CHANGED TO: "+str(PC))	
	rz= ra+rb
        
      else:
        rz= ra+rb
  elif (op == "11011"):#bge
      if(ra>=rb):
        PC=PC+imm-4
	print("PC CHANGED TO: "+str(PC))	
	rz= ra+rb
        
      else:
        rz= ra+rb
  elif (op == "11100"):#blt
      if(ra<rb):
        PC=PC+imm-4
	print("PC CHANGED TO: "+str(PC))	
	rz= ra+rb
        
      else:
        rz= ra+rb
  elif (op == "11101"):#auipc
        rz= rb+PC-4
  elif (op == "11110"):#lui
      rz= ra+rb
  elif (op == "11111"):#jal
      rz=ra+rb
      PC=PC+imm-4
      print("PC CHANGED TO: "+str(PC))	
     
      
      
  return rz,RM,PC

#==============Memorycall===================
def checkKey(dict, key): 
    global c 
    if key in dict.keys(): 
	  c=1 
    else: 
	  c=0 
  

def memdata_store(n_byte,dec,addr):
  global data,c
  checkKey(data,addr)
  if(c==1):
		del data[addr]
  bin_data_0b=str(bin(dec))
  j=len(bin_data_0b)
  bin_data=bin_data_0b[2:j]
  j=j-2
  for k in range(0,8*n_byte-j):
    bin_data="0"+bin_data
  for i in range(0, n_byte):
      str_addr=addr+i
      dictn={str_addr:bin_data[8*(n_byte-i-1):8*(n_byte-i)]}
      data.update(dictn)


def memdata_load(n_byte,addr):
  global data
  str_data=""
  for i in range(0,n_byte):
   
    str_data=data[addr+i]+str_data
    out=int(str(str_data),2)
  return out


def datamem(bin_data_0b, addr):
  global data
  j=len(bin_data_0b)
  bin_data=bin_data_0b[2:j]
  j=j-2
  for k in range(0,8-j):
    bin_data="0"+bin_data
  dictn={addr:bin_data[0:8]}
  data.update(dictn)
  


def memcall(ALU_op,rz,rm):
		global ry
		if(ALU_op=='10000'):
			ry=memdata_load(1,rz)
		elif(ALU_op=='10001'):
			ry=memdata_load(8,rz)
		elif(ALU_op=='10010'):
			ry=memdata_load(2,rz)
		elif(ALU_op=='10011'):
			ry=memdata_load(4,rz)
		elif(ALU_op=='10101'):
			ry=0
			memdata_store(1,rm,rz)
		elif(ALU_op=='10110'):
			ry=0
			memdata_store(8,rm,rz)
		elif(ALU_op=='10111'):
			ry=0
			memdata_store(2,rm,rz)
		elif(ALU_op=='11000'):
			ry=0
			memdata_store(4,rm,rz)
		return ry


#================register update=============

def reg_update(Reg,rd,RY):
  if(subArr=="0110011" or subArr=="0000011" or subArr=="0010011" or subArr=="1100111" or subArr=="0010111" or subArr=="0110111" or subArr=="1101111"):
  	Reg[rd]=RY
  	Reg[0]=0
	print("UPDATED REGISTER FILE: ")
        print(Reg)
  	return Reg

  else:
	 Reg[0]=0
	 return Reg  




#======================initial_values===========
arr="01011111111111111010111110100011"
Reg=[0,0,2147483632,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print("INITIAL REGISTER FILE: ")
print(Reg)
PC=0
print("INITIAL REGISTER FILE: 0")
IR="NULL"
clock=0

#registers
RB=12
RY=0
RA=0
RZ=0
InA=0
InB=0
RM=0
#variables
rs1=0
rs2=0
rz=0
rd=0
subArr=0
ry=0
data={}

#controls
B_SEL=0
Y_SEL=[0,0,0]
ALU_op=[0,0,0,0,0]


#intermediate variables
imm=57
return_addr=85775

#==================start of program=============


#list2=["00000000011100000000000110010011","00000000100000000000001000010011","00000010010000011000001010110011","end"]


f= open("/home/mahidhar/Desktop/check.mc","r+")
list1=f.readlines()

list2=[]
for i in range(len(list1)):
  if(list1[i][0:4]=="0x0 "):
    n=i
    break
  else:
    n=0

if list1[0][0:10]=="0x10000000" :
  
  for l in range(n):    
      str1 = str(list1[l][2:10])
      str2 = str(list1[l][13:])
     
      n1 = int(str1,16) 
      n2 = int(str2,16) 
      n2 = bin(n2)
      datamem(n2,n1)
  for i in range(n,len(list1)): 
    for j in range(len(list1[i])):
        if(list1[i][j]==" "):
            j=j+1;
            a=j+10;
           
            str3=str(list1[i][j:])
           
            n3 = int(str3,16)

            n3 = bin(n3)
            n3 = str(n3[2:])
            list2.append(str(n3))
            break
else:
   
   for i in range(len(list1)): 
      for j in range(len(list1[i])):
          if(list1[i][j]==" "):
            j=j+1;
            str3=str(list1[i][j:])
            n3 = int(str3,16)
            n3 = bin(n3)
            n3 = str(n3[2:])
            list2.append(str(n3))
            break

for i in range(len(list2)):
    if(len(list2[i])!=32): 
         d=32-len(list2[i])
         for j in range(d):
            list2[i]="0"+str(list2[i])

list2.append("end")

      
      










stmt=1
while(list2[PC/4]!="end"):
      
      stmt=stmt+1
      arr=fetch(PC/4,list2)
      IR=arr
      print("IR CHANGED TO: "+ IR)
      print("CURRENT PC: "+str(PC))
      PC=PC+4
      return_addr=PC
    
      InA,B_SEL,RB,rd,imm,return_addr,ALU_op,subArr,fun3,Y_SEL=decode_op(arr,Reg);



#======================MUXB=======================
      if(B_SEL==0):
       InB=RB
      else:
       InB=imm
   
       
      

    



      RZ,RM,PC=execute(ALU_op,InA,InB,PC,RB)
      ry=memcall(ALU_op,RZ,RM)
	 
      #====================MUX-Y======================
     
      if(Y_SEL[0]==0 and Y_SEL[1]==0 and Y_SEL[2]==0 ):         #for R type
        RY=RZ
      elif(Y_SEL[0]==0 and Y_SEL[1]==0 and Y_SEL[2]==1):        #for I type
        if(subArr=="0000011"):    #load
          RY=ry
									#check
        if(subArr=="0010011"):    #addi,ori,etc
          RY=RZ
	    
        if(subArr=="1100111"):    #jalr
          RY=return_addr
      elif(Y_SEL[0]==0 and Y_SEL[1]==1 and Y_SEL[2]==0):        #for auipc
        RY=RZ                                            
      elif(Y_SEL[0]==0 and Y_SEL[1]==1 and Y_SEL[2]==1):        #for lui
        RY=RZ    
      elif(Y_SEL[0]==1 and Y_SEL[1]==0 and Y_SEL[2]==0):        #for UJ type
        RY=return_addr
      elif(Y_SEL[0]==1 and Y_SEL[1]==0 and Y_SEL[2]==1):        #for S type
        RY="null"
      elif(Y_SEL[0]==1 and Y_SEL[1]==1 and Y_SEL[2]==0):        #for SB type
        RY="null"
      
	 

      
      

      Reg=reg_update(Reg,rd,RY)
print("FINAL REGISTER FILE: ")
print(Reg)
print("FINAL DATA: ")
print(data)
