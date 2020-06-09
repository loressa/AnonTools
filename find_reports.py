import os
import pydicom as pydcm 

inputList = 'list_dirs.txt'
with open(inputList, 'r') as fp:
    line    = fp.readline()
    while line:
        files = os.listdir(line.strip())
        for file in files:
            input_dicom = line.strip() + os.sep + file
            try:
                data = pydcm.dcmread(input_dicom)
                #print(data.ImageType)
                if (data.ImageType[0].lower() == 'derived'):
                    print ('ATTN! %s in file %s' % (data.ImageType, input_dicom))
                if (data.ImageType[2].lower() == 'localizer'):
                    print ('ATTN! %s in file %s' % (data.ImageType, input_dicom))
                if ((data.ImageType[2].lower() == 'report') or (data.ImageType[2].lower() == 'reports')):
                    print ('ATTN! %s in file %s' % (data.ImageType, input_dicom))
                if ((data.ImageType[2].lower() == 'presentation') or (data.ImageType[2].lower() == 'presentations')):
                    print ('ATTN! %s in file %s' % (data.ImageType, input_dicom))
                if (data.ImageType[2].lower() == 'other'):
                    print ('ATTN! %s in file %s' % (data.ImageType, input_dicom))
            except:
                  print('No metadata for %s' % input_dicom)

        line    = fp.readline()
                  
