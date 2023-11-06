var_to_be_removed = ["ORIGIN", "1", "61", "//"]
filename = "preproinsulin-seq.txt"

new_sequence = []
with open(filename, 'r') as f:
    lines = f.readlines()
    print("input string: ", lines)
    for line in lines:
        remove_newline = line.replace("\n", " ")
        split_line = remove_newline.split(" ")
        
        for c in split_line:
            if not c in var_to_be_removed and c != "":
                new_sequence.append(c)

new_sequence = "".join(new_sequence)
print(f'\nnew sequence is = {new_sequence} \nlength = {len(new_sequence)}')

file_seq_clean='preproinsulin-seq-clean.txt'
with open(file_seq_clean, 'w') as f:
    f.write(new_sequence)

file_isinsulin_seq_clean = 'Isinsulin-seq-clean.txt'
file_binsulin_seq_clean = 'binsulin-seq-clean.txt'
file_cinsulin_seq_clean = 'cinsulin-seq-clean.txt'
file_ainsulin_seq_clean = 'ainsulin-seq-clean.txt'

# dictionary of file and bit to save

dict_filename_and_sequence = [
        {
            'filename': file_isinsulin_seq_clean,
            'seq_start': 1,
            'seq_end': 24,
        },
        {
            'filename': file_binsulin_seq_clean,
            'seq_start': 25,
            'seq_end': 54,
        },
        {
            'filename': file_cinsulin_seq_clean,
            'seq_start': 55,
            'seq_end': 89,
        },
        {
            'filename': file_ainsulin_seq_clean,
            'seq_start': 90,
            'seq_end': 110,
        }
    ]


print("\n=> process to write some sequence to files")
for data in dict_filename_and_sequence:
    fname = data['filename']
    ss = data['seq_start']
    es = data['seq_end']
    with open('result/'+fname, 'w') as f:
        new_line = new_sequence[ss-1:es]
        print(f'get idx {ss}-{es} = [{new_line}] write to [{fname}]')
        f.write(new_line)
        
        
print("--- writing done ---")
# validate the result is as expected
validate_new_seq = ""
for data in dict_filename_and_sequence:
    with open('result/'+data['filename'], 'r') as f:
        line = f.readline()
        validate_new_seq += line
        
print("is valid? => ", end = "")
if new_sequence == validate_new_seq:
    print("VALID")
else:
    print("INVALID")