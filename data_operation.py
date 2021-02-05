def get_data(file,mode,seperate):
    cin=open(file,mode,encoding='utf8')
    data=[]
    
    while True:
        n=[1]
        n*=seperate
        n[0]=cin.readline().strip('\n')
        if not n[0]:
            break
        
        else:
            for i in range(1,seperate):
                n[i]=cin.readline().strip('\n')
            data.append(n)
            
    cin.close()
    return data

def write_data(file,mode,data):
    cout=open(file,mode,encoding='utf8')
    
    for line in data:
            for item in line:
                cout.write(item+'\n')
                
    cout.close()