#!/usr/bin/env python

# Script written by Lorena Escudero (Department of Radiology, University of Cambridge) 
# to print command for DicomRemap per file in a project - June 2020

# Usage: anon_project.py input_DICOM_path output_anon_path 

import sys, os, glob

# ---------------------------------------------------------------------------------------------------------------------   

arguments = sys.argv[1:]

input_path  = arguments[0]
output_path = arguments[1]

# Find list of subjects

subjects = os.listdir(input_path)
for subject in subjects:
    #print (subject)
    # Walk to where the DICOM files are
    scans = os.listdir(input_path + os.sep + subject + os.sep + 'SCANS')
    if (len(scans)>1):
        print ('Check subject %s with %d scans' % (subject, len(scans)))
    else:
        for scan in scans:    
            files = os.listdir(input_path + os.sep + subject + os.sep + 'SCANS' + os.sep + scan + "/DICOM/")
            for file in files:
                if ( not file.endswith(".xml")):
                    #print(file)
                    input_file = input_path + os.sep + subject + os.sep + 'SCANS' + os.sep + scan + "/DICOM/" + file
                    output_file = output_path + os.sep + subject
                    print('DicomRemap -d baseline_anon.das -o %s %s' %(output_file, input_file))
    
