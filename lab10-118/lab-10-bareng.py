from helper import get_my_data

# open file
with open('lab-10-bareng/preproinsulin-seq-clean.txt', 'r') as f:
    lines = f.readlines()
    # membaca baris per baris
    line = lines[0]
    print(line)
    
    # 1-24 = 0-24
    pertama = line[0:24]
    print(pertama)
    # 25 - 54 
    kedua = line[24:54]
    print(kedua)
    # 55-89
    ketiga = line[54:89]
    print(ketiga)
    # 90 - 110
    keempat = line[89:110]
    print(keempat)
    

print("\n",len(pertama), len(kedua), len(ketiga), len(keempat))