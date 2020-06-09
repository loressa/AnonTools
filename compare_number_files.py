# Python script to compare two sets of DICOM files 

import os 

input_list = 'list_old_dirs.txt'

with open(input_list, 'r') as fp:
    line = fp.readline()
   
    while line:
        old_path = line.strip()
        new_path = old_path.replace('old','new')
            
        old_scans = os.listdir(old_path)
        new_scans = os.listdir(new_path)
        
        n_old = len(old_scans)
        n_new = len(new_scans)
        
        print('-----------------------------------------------------------')
        print('Number of files in old path %s is %d' %(old_path, n_old))
        print('Number of files in new path %s is %d' %(new_path, n_new))
        print('Difference %d' %(n_old - n_new))
        if (n_old != n_new):
            print('ATTN!!! Check %s and %s' %(old_path, new_path))
        
        line = fp.readline()
