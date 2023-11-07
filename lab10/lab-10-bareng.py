from main import get_my_data


# open file
with open('lab-10-bareng/preproinsulin-seq-clean.txt', 'r') as f:
    lines = f.readlines()
    # membaca baris per baris
    for line in lines:
        print(line)
    
    mydata = get_my_data()
        