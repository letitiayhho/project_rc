import sys
sys.path.append('/data/test_rc/')
import data
import os

test_rc_path = '/data/test_rc'




for filename in os.listdir(test_rc_path):
    file = open(os.path.join(test_rc_path, filename))
    
    while True:
        line = file.readline()
        token = data.tokenize(line)
        
    
    with open('tok_' + file, 'w') as w:
        w.write(

for file in files open(file):
    tokens = data.tokenize(file)
    print(tokens)

files = []
for i in os.listdir(path_to_folder):
    if i.endswith('.txt'):
        files.append(open(i))
# do what you want with all these open files
