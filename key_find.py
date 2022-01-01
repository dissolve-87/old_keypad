key=[]
val=[]
num = {2:{1:"a",2:"b",3:"c"},3:{1:"d",2:"e",3:"f"},4:{1:"g",2:"h",3:"i"},5:{1:"j",2:"k",3:"l"},6:{1:"m",2:"n",3:"o"},7:{1:"p",2:"q",3:"r",4:"s"},8:{1:"t",2:"u",3:"v"},9:{1:"w",2:"x",3:"y",4:"z"},0:{1:"0",2:"Space"}}
with open("data.txt","r") as file:
    try:
        for line in file:
            key.append(int(line.rstrip()[0]))
            val.append(int(line.rstrip()[2]))
    except:
        print("Please Enter Correct input")
        exit(0)
for f, b in zip(key, val):
    print(f"[{f}] key [{b}] times  = [{num[f][b]}]")
