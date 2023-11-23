import os

def splice_sentences(file_path):
    with open(file_path,'r') as f:
        data = f.read()
    new_data = ''
    last_index = -2
    for index, ch in enumerate(data):
        if (ch == '\n' and (data[index-1] != '.' and data[index-1] != '!' and data[index-1] != '?')):
            new_data += ' '
        else:
            new_data += ch
    base = os.path.splitext(file_path)[0]
    output_path = base + '_spliced.txt'

    with open(output_path,'w') as f:
        f.write(new_data)
    return None


splice_sentences('/Users/tempaccount/Downloads/afterhours_s5_ep32_segment_a.txt')


