#!/usr/bin/env python
# coding: utf-8

# In[35]:


Asem_dirc = [": .byte",": .half", ": .word", ": .dword", ": .asciiz"]
incr = {": .byte":"1",": .half":"2",": .word":"4",": .dword":"8",": .asciiz":"1"}



def KMPSearch(minor,major): 
	l = len(minor) 
	L = len(major) 
	lcmin = [0]*l 
	j = 0 
	computeLPSArray(minor,l,lcmin) 
	i = 0
	while i < L: 
		if minor[j] == major[i]: 
			i += 1
			j += 1
		if j == l: 
			return 1
			j = lcmin[j-1] 

		elif i < L and minor[j] != major[i]: 
			if j != 0: 
				j = lcmin[j-1] 
			else: 
				i += 1

def computeLPSArray(minor,l,lcmin): 
	len = 0 
	lcmin[0] 
	i = 1
	while i < l: 
		if minor[i]== minor[len]: 
			len += 1
			lcmin[i] = len
			i += 1
		else:  
			if len != 0: 
				len = lcmin[len-1] 
			else: 
				lcmin[i] = 0
				i += 1




def KMPSearch2(minor, major): 
	ll=[]
	l = len(minor) 
	L = len(major) 
	lcmin = [0]*l
	j = 0  
	computeLPSArray(minor,l,lcmin) 
	i = 0 
	while i < L: 
		if minor[j] == major[i]: 
			i += 1
			j += 1

		if j == l: 
			ll.append ((i-j) )
			j = lcmin[j-1] 

		elif i < L and minor[j] != major[i]: 
			if j != 0: 
				j = lcmin[j-1] 
			else: 
				i += 1

	return  ll

def computeLPSArray(minor,l,lcmin): 
	len = 0 
	lcmin[0] 
	i = 1 
	while i<l: 
		if minor[i]== minor[len]: 
			len += 1
			lcmin[i] = len
			i += 1
		else: 
			if len != 0: 
				len = lcmin[len-1] 
			else: 
				lcmin[i] = 0
				i += 1

def KMPSearch3(minor,major): 
	l = len(minor) 
	L = len(major) 
	lcmin = [0]*l
	j = 0 
	computeLPSArray(minor,l,lcmin) 
	i = 0 
	while i < L: 
		if minor[j] == major[i]: 
			i += 1
			j += 1

		if j == l: 
			return (i-j) 
			j = lcmin[j-1] 

		elif i < L and minor[j] != major[i]: 
			
			if j != 0: 
				j = lcmin[j-1] 
			else: 
				i += 1

def computeLPSArray(minor,l,lcmin): 
	len = 0 
	lcmin[0]
	i = 1
	while i < l: 
		if minor[i]== minor[len]: 
			len += 1
			lcmin[i] = len
			i += 1
		else: 
			if len != 0: 
				len = lcmin[len-1] 
			else: 
				lcmin[i] = 0
				i += 1



def convert(s): 
  
     
    new = "" 
  
    
    for x in s: 
        new += str(x)  
  
    return new 




def onescomp(str):
    for i in range(len(str)):
        if(str[i]==1):
            str[i]=0
        else:
            str[i]=1
       
    return str
def foundfunct3(a,b):
    if(a==0):
        return R_funct3[R[b]]
    if(a==1):
        return I_funct3[I[b]]
    if(a==2):
        return S_funct3[S[b]]
    if(a==3):
        return SB_funct3[SB[b]]
    if(a==4):
        return U_funct3[U[b]]
    if(a==5):
        return UJ_funct3[UJ[b]]

def dec2bin2( a):
    binary = [0,0,0,0,0,0,0,0,0,0,0,0]
    index =11;
    while(a!=0):
        rem = a%2;
        binary[index] = rem
        index = index -1
        a = a//2
    return binary    
def dec2bin3( a):
    binary = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    index =19;
    while(a!=0):
        rem = a%2;
        binary[index] = rem
        index = index -1
        a = a//2
    return binary    
bin = dec2bin2(5)
def dec2bin32( a):
    binary = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    index =31;
    while(a!=0):
        rem = a%2;
        binary[index] = rem
        index = index -1
        a = a//2
    return binary 
def dec2bin64( a):
    binary = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    index =31;
    while(a!=0):
        rem = a%2;
        binary[index] = rem
        index = index -1
        a = a//2
    return binary 
def dec2bin16( a):
    binary = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    index =15;
    while(a!=0):
        rem = a%2;
        binary[index] = rem
        index = index -1
        a = a//2
    return binary 
def dec2bin8( a):
    binary = [0,0,0,0,0,0,0,0]
    index =7;
    while(a!=0):
        rem = a%2;
        binary[index] = rem
        index = index -1
        a = a//2
    return binary 

def dec2bin( a):
    binary = [0,0,0,0,0]
    index = 0;
    while(a!=0):
        rem = a%2;
        binary[index] = rem
        index = index +1
        a = a//2
    return binary    
def dec2hex( a):
    hex = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"a",11:"b",12:"c",13:"d",14:"e",15:"f"}
    hexd = [0,0,0,0,0]
    index = 0;
    while(a!=0):
        rem = a%16;
        hexd[index] = hex.get(rem)
        index = index +1
        a = a//16
    return hexd    

def array2string(array):
    st = str(str(array[4])+str(array[3])+str(array[2])+str(array[1])+str(array[0]))
    return st;

def array2string2(array):
    st = str(str(array[0])+str(array[1])+str(array[2])+str(array[3])+str(array[4])+str(array[5])+str(array[6])+str(array[7])+str(array[8])+str(array[9])+str(array[10])+str(array[11]))
    return st;
def array2string3(array):
    st = str(str(array[0])+str(array[1])+str(array[2])+str(array[3])+str(array[4])+str(array[5])+str(array[6])+str(array[7])+str(array[8])+str(array[9])+str(array[10])+str(array[11])+str(array[12])+str(array[13])+str(array[14])+str(array[15])+str(array[16])+str(array[17])+str(array[18])+str(array[19]))
    return st;
def array2string32(array):
    st = str(str(array[0])+str(array[1])+str(array[2])+str(array[3])+str(array[4])+str(array[5])+str(array[6])+str(array[7])+str(array[8])+str(array[9])+str(array[10])+str(array[11])+str(array[12])+str(array[13])+str(array[14])+str(array[15])+str(array[16])+str(array[17])+str(array[18])+str(array[19])+str(array[20])+str(array[21])+str(array[22])+str(array[23])+str(array[24])+str(array[25])+str(array[26])+str(array[27])+str(array[28])+str(array[29])+str(array[30])+str(array[31]))
    return st;
def array2string16(array):
    st = str(str(array[0])+str(array[1])+str(array[2])+str(array[3])+str(array[4])+str(array[5])+str(array[6])+str(array[7])+str(array[8])+str(array[9])+str(array[10])+str(array[11])+str(array[12])+str(array[13])+str(array[14])+str(array[15]))
    return st;
def array2string8(array):
    st = str(str(array[0])+str(array[1])+str(array[2])+str(array[3])+str(array[4])+str(array[5])+str(array[6])+str(array[7]))
    return st;
def array2string64(array):
    st = str(str(array[0])+str(array[1])+str(array[2])+str(array[3])+str(array[4])+str(array[5])+str(array[6])+str(array[7])+str(array[8])+str(array[9])+str(array[10])+str(array[11])+str(array[12])+str(array[13])+str(array[14])+str(array[15])+str(array[16])+str(array[17])+str(array[18])+str(array[19])+str(array[20])+str(array[21])+str(array[22])+str(array[23])+str(array[24])+str(array[25])+str(array[26])+str(array[27])+str(array[28])+str(array[29])+str(array[30])+str(array[31])+str(array[32])+str(array[33])+str(array[34])+str(array[35])+str(array[36])+str(array[37])+str(array[38])+str(array[39])+str(array[40])+str(array[41])+str(array[42])+str(array[43])+str(array[44])+str(array[45])+str(array[46])+str(array[47])+str(array[48])+str(array[49])+str(array[50])+str(array[51])+str(array[52])+str(array[53])+str(array[54])+str(array[55])+str(array[56])+str(array[57])+str(array[58])+str(array[59])+str(array[60])+str(array[61]))
    return st;



# Array of formats
# Encoding R-0,I-1,S-2,SB-3,U-4,UJ-5
reg =[]
for i in range(32):
    reg.append("x"+str(i))
    

R = ["add", "and", "or", "sll", "slt", "sra", "srl", "sub", "xor", "mul", "div", "rem"]
I = ["addi", "andi", "ori", "lb", "ld", "lh", "lw", "jalr"]
S = ["sb", "sw", "sd", "sh"]
SB = ["beq", "bne", "bge", "blt"]
U = ["auipc", "lui"]
UJ = ["jal"]
formats = ["R","I","S","SB","U","UJ"]


R_funct3 = {"add":"000","sub":"000","sll":"001","slt":"010","sltu":"011","xor":"100","srl":"101","sra":"101","or":"110","and":"111","mul":"000","div":"100","rem":"110"}
I_funct3 = {"addi":"000","andi":"111","ori":"110","lb":"000","ld":"011","lh":"001","lw":"010","jalr":"000"}
S_funct3 = {"sb":"000","sh":"001","sw":"010","sd":"011"}
SB_funct3 = {"beq":"000","bne":"001","blt":"100","bge":"101"}
U_funct3 = {"auipc":"000","lui":"000"}
UJ_funct3 = {"jal":"000"}
R_funct7 = {"add":"0000000","sub":"0100000","sll":"0000000","slt":"0000000","xor":"0000000","srl":"0000000","sra":"0100000","or":"0000000","and":"0000000","mul":"0000001","div":"0000001","rem":"0000001"}

I_opcode = {"addi":"0010011","andi":"0010011","ori":"0010011","lb":"0000011","ld":"0000011","lh":"0000011","lw":"0000011","jalr":"1100111"}

def I_opfind(string):
    a,b=formatfound(string)
   
    
    return I_opcode[I[b]]
    




def formatfound(string):
    string = string.split(" ")[0]
    for i in range (len(I)):    
        if(KMPSearch(I[i],string )==1):
            return 1,i
    for i in range (len(R)):
        if(KMPSearch(R[i],string )==1):
            return 0,i
    
    for i in range (len(S)):    
        if(KMPSearch(S[i],string )==1):
            return 2,i
    for i in range (len(SB)):    
        if(KMPSearch(SB[i],string )==1):
            return 3,i
    for i in range (len(U)):    
        if(KMPSearch(U[i],string )==1):
            return 4,i
    for i in range (len(UJ)):
        if(KMPSearch(UJ[i],string )==1):
            return 5,i


def foundfunct7(b):
   
    return R_funct7[R[b]]
    



def Rformat(funt3,reg1,reg2,reg3,b):
    reg_1 = array2string(dec2bin(int(reg1)))
    reg_2 = array2string(dec2bin(int(reg2)))
    reg_3 = array2string(dec2bin(int(reg3)))
    
    output = str(foundfunct7(b))+str(reg_1)+str(reg_2)+str(funt3)+str(reg_3)+"0110011"
    return output
    
    


def Sformat(funt3,reg1,reg2,immd):
    reg_1 = array2string(dec2bin(int(reg1)))
    reg_2 = array2string(dec2bin(int(reg2)))
    
    immd_1 = convert(dec2bin2(int(immd))[0:7])
    immd_2 = convert(dec2bin2(int(immd))[7:12])
    
    output = str(immd_1)+str(reg_2)+str(reg_1)+funt3+str(immd_2)+"0100011"
    
    return output



def Iformat(funt3,reg1,reg2,immd,string):

    if(immd<0):
        
        immd = -1*immd
        immd_= onescomp(dec2bin2(int(immd)))
        immd_ = array2string2(immd_)
        ll = (int(immd_,2)+1 ) 
        immd = ll
        
      
    reg_1 = array2string(dec2bin(int(reg1)))
    reg_2 = array2string(dec2bin(int(reg2)))
    immd_ = array2string2(dec2bin2(int(immd)))
    
    output = str(immd_)+str(reg_1)+str(funt3)+str(reg_2)+I_opfind(string)
    
    return output

def SBformat(funt3,reg1,reg2,aas,string,po2,iids):
    hhf = string.replace("\n","").split(",")
    pat = hhf[2]
    po=0
    pat = pat+':'
    p = re.compile('[\w]*[:]') 
    cnt=0
    cnt1 = 0
    
    po=0
    po1 = 0
    for i in (range(len(aas))):
        if(i>iids):
            
            
            if(i==po2):
                po = po+1
                po1 = po1 +1
                break
            else:
                if(len(p.findall(list1[i]))==0):
                    po = po+1
                po1 = po1 +1
    
    flag = 0
    for i in (range(len(aas))):
        if(i>iids):
            
               
            if(KMPSearch(pat, aas[i])):
                flag = 1    
                cnt = cnt+1
                break
            else:
                if(len(p.findall(list1[i]))==0):
                    cnt = cnt+1
    
    cnt  = cnt - po 
    if(flag==0):
        print("Error: "+str(pat)+" not Defined")
        return 
    #print(pat)
    immd = cnt*2
    if(immd<0):
        immd = -1*immd
        immd_= onescomp(dec2bin2(int(immd)))
        immd_ = array2string2(immd_)
        ll = (int(immd_,2)+1 ) 
        immd = ll
    
    d1 = convert((dec2bin2(int(immd))[2:8]))
    d2 = ((dec2bin2(int(immd))[0]))
    d3 = convert((dec2bin2(int(immd))[8:12]))
    d4 = ((dec2bin2(int(immd))[1]))
    reg_1 = array2string(dec2bin(int(reg1)))
    reg_2 = array2string(dec2bin(int(reg2)))
    
    output = str(d2)+str(d1)+str(reg_1)+str(reg_2)+str(funt3)+str(d3)+str(d4)+"1100011"
    
    return output   

    

    
    
def Uformat(reg1,imm,b):
    reg_1 = array2string(dec2bin(int(reg1)))
    op=U[b]
    immd_ = array2string3(dec2bin3(int(imm)))
  
    if(op=="auipc"):
           output = str(immd_)+str(reg_1)+"0010111"
    else:
        output = str(immd_)+str(reg_1)+"0110111"
    
    return output
def UJformat(reg1,aas,string,po2,iids):
    hhf = string.replace("\n","").split(",")
    pat = hhf[1]
    po=0
    pat = pat+':'
    p = re.compile('[\w]*[:]') 
    cnt=0
    cnt1 = 0
    
    po=0
    po1 = 0
    for i in (range(len(aas))):
        if(i>iids):
            
            
            if(i==po2):
                po = po+1
                po1 = po1 +1
                break
            else:
                if(len(p.findall(list1[i]))==0):
                    po = po+1
                po1 = po1 +1
    
    flag = 0
    for i in (range(len(aas))):
        if(i>iids):
            
               
            if(KMPSearch(pat, aas[i])):
                flag = 1 
                cnt = cnt+1
                break
            else:
                if(len(p.findall(list1[i]))==0):
                    cnt = cnt+1
    if(flag==0):
        print("Error: "+str(pat)+" not Defined")
        return
 
    cnt  = cnt - po 
    
    
    immd = cnt*2
   
    if(immd<0):
        immd = -1*immd
        immd_= onescomp(dec2bin3(int(immd)))
        
        immd_ = array2string3(immd_)
        ll = (int(immd_,2)+1 ) 
        immd = ll
    d4 = convert((dec2bin3(int(immd))[1:9]))
    d2 = convert((dec2bin3(int(immd))[10:20]))
    d1 = ((dec2bin3(int(immd))[0]))
    d3 = ((dec2bin3(int(immd))[9]))
    reg_1 = array2string(dec2bin(int(reg1)))
    
   
    output = str(d1)+str(d2)+str(d3)+str(d4)+str(reg_1)+"1101111"
    return output




# Array of formats

def regno(string, op,aas,po,iids):
    passorder = []
    p = re.compile('[x]\d+') 
    jfj=  p.findall(string)
    for z in range(len(jfj)):
        passorder.append(int(jfj[z].replace("x","")))
    
    funct3pass = str(R_funct3.get(str(op)))
    a,b=formatfound(string)
    var=formats[a]
    
    funct3pass = foundfunct3(a,b)
    
    if(var=="R"):                                                         #let vari contain the format
        ss = string
        ss = ss.split(",")
        ss1 =int( ss[0].split(" ")[1].replace("x",""))
        ss2 = int( ss[1].replace("x",""))
        ss3 = int(ss[2].replace("x",""))
        return(Rformat(funct3pass,ss3,ss2,ss1,b))
    if(var=="SB"):
        if(len(passorder)==3):
            print("Error:Expecting one immediate value")
            return
        if(len(passorder)==1):
            h1=(passorder[0])
            h2=h1
        else:
            h1=(passorder[0])
            h2=(passorder[1])
        
        return( SBformat(funct3pass,h2,h1,aas,string,po,iids))
    if(var=="S"):
        if(len(passorder)==3):
            print("Error:Expecting one immediate value")
            return
        if(len(passorder)==1):
            h1=(passorder[0])
            h2=h1
        else:
            h1=(passorder[0])
            h2=(passorder[1])
        imm=immediate_found(string)
    
        return( Sformat(funct3pass,h2,h1,imm))   
        
  
    
    if(var=="I"):
        if(len(passorder)==3):
            print("Error:Expecting one immediate value")
            return
        if(len(passorder)==1):
            h1=(passorder[0])
            h2=h1
        else:
            h1=(passorder[0])
            h2=(passorder[1])
        imm=immediate_found(string)
        return(Iformat(funct3pass,h2,h1,imm,string))    #let imm gets the immediate value
    if(var=="U"):
        ss = string.split(",")
        imm =int(ss[1],16)
        if(imm<0):
            imm = -1*imm
            immd_= onescomp(dec2bin2(int(imm)))
            immd_ = array2string2(immd_)
            ll = (int(immd_,2)+1 ) 
            imm = ll
        
       
        return(Uformat((passorder[0]),imm,b))
    if(var=="UJ"):
        
        
        return(UJformat((passorder[0]),aas,string,po,iids))
        
immq = []
import re 
def immediate_found(string):
    p = re.compile('[,][-/+]?[\d]+') 
    ff = str(p.findall(string))
    ff  = ff.replace(",","")
    ff = (ff.replace("'",""))
    ff = ff.replace("[","")
    ff = ff.replace("]","")
    
    ff = int(ff)
    return ff


    



g = open("oo.mc.txt","w+")
p = re.compile('[+|-]?\d+') 


def assebly_dirc(string,PC,aas,po,iids):
    
    
    import re 
    

    for i in range(len(Asem_dirc)):
       
        if(KMPSearch(Asem_dirc[i],string)==1):
            
            if(i!=4):
                p = re.compile('[+|-]?\d+') 
                num87 = p.findall(string)
                
                for j in range(len(num87)):
                    g.write(str(hex(PC[0]))+" "+str(hex(int(num87[j])))+"\n")
                    PC[0] = PC[0] + int(incr[str(Asem_dirc[i])])
            elif(i==4):
                saa = string.split(" ")[2]
                p = re.compile('\w') 
                daa = p.findall(saa)
                for j in range(len(daa)):
                    g.write(str(hex(PC[0]))+" "+str(hex(ord(daa[i])-ord('a')+10))+"\n")
                    PC[0] = PC[0] + int(incr[str(Asem_dirc[i])])
                
                
            return
    
    a,b=formatfound(string)
    op=formats[a]
    
  
    g.write(str(hex(PC[0]))+" "+str(hex(int(regno(string, op,aas,po,iids),base = 2)))+"\n")
    #print(regno(string, op,aas,po,iids))
    PC[0] = PC[0] + 4
def assebly_dirc1(string,PC,aas,po):
    
    
    import re 
    

    for i in range(len(Asem_dirc)):
    
        if(KMPSearch(Asem_dirc[i],string)==1):
            
            
            if(i!=4):
                p = re.compile('[+|-]?\d+')
                string = string.split(":")[1]
                num87 = p.findall(string)
               
                for j in range(len(num87)):
                    immd = int(num87[j])
                    if(immd<0):
                        immd = -1*immd
                        if(str(Asem_dirc[i])==": .byte"):
                            immd_= onescomp(dec2bin8(int(immd)))

                            immd_ = array2string8(immd_)
                        if(str(Asem_dirc[i])==": .half"):
                            immd_= onescomp(dec2bin16(int(immd)))

                            immd_ = array2string16(immd_)
                        if(str(Asem_dirc[i])==": .word"):
                        
                            immd_= onescomp(dec2bin32(int(immd)))

                            immd_ = array2string32(immd_)
                        if(str(Asem_dirc[i])==": .dword"):
                            immd_= onescomp(dec2bin64(int(immd)))

                            immd_ = array2string64(immd_)
                            
                        ll = (int(immd_,2)+1 ) 
                        immd = ll
                   
                    g.write(str(hex(PC[0]))+" "+str(hex(int(immd)))+"\n")
                    PC[0] = PC[0] + int(incr[str(Asem_dirc[i])])
            elif(i==4):
               
                saa = string.split(" ")[2]
                p = re.compile('\w') 
                daa = p.findall(saa)
                for j in range(len(daa)):
                  
                    g.write(str(hex(PC[0]))+" "+str(hex(ord(daa[j])-ord('a')+10))+"\n")
                    PC[0] = PC[0] + int(incr[str(Asem_dirc[i])])
                
                
            return
    
    
          
             
f= open("text.mc.txt","r+")
g = open("oo.mc.txt","w+")
list1=f.readlines()
PC= []
PC.append(268435456)
p = re.compile('[\w]*[:]') 
ap = 0
for i in range(len(list1)):
    if(i!=0):
        if(KMPSearch(".text", list1[i])): 
            ap =i
            break
            
        if(len(p.findall(list1[i]))!=0):
            
            
            if(len(list1[i])==1): break

            assebly_dirc1(list1[i],PC,list1,i)
PC[0]=0
for i in range(len(list1)):
    if(i>ap):
        if(len(p.findall(list1[i]))==0):
          
            if(len(list1[i])==1): break

            assebly_dirc(list1[i],PC,list1,i,ap)
        
#print(d1,d2,d3,d4,reg_1)
#output = str(d2)+str(d4)+str(d1)+str(reg_1)+"1101111"
#0000 0000 11111111 000 1 11111111 00001 1101111           
            




g = open("oo.mc.txt","w+")







