#!/usr/bin/env python

# Script written by Lorena Escudero (Department of Radiology, University of Cambridge) 
# to check for DICOM fields with PHI in an XNAT project - April 2020 
#
# Usage: edit input_path and run from the server where the images are stored

import pydicom
import os, sys 
import fnmatch

# ---------------------------------------------------------------------------------------------------------------------

def check_reports(input_dicom):
    try:     
         data = pydicom.dcmread(input_dicom)
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
         if (fnmatch.fnmatch(data.ImageType[2].lower(), 'screen')):
             print ('ATTN! %s in file %s' % (data.ImageType, input_dicom))
    except:
        print('No metadata for %s' % input_dicom)

# ---------------------------------------------------------------------------------------------------------------------   

def check_phi(metadata, list_phi):
    for field in list_phi:
         try: 
            value = metadata[field]
            if (value != ''):
                print('   - Found %s = %s' %(field, value))
         except:
             pass

# ---------------------------------------------------------------------------------------------------------------------   

if __name__ == '__main__':

    list_phi = ['PatientID', 'PatientName','AccessionNumber', 'AcquisitionComments', 'AcquisitionContextSequence', 'AcquisitionDeviceProcessingDescription', 'AcquisitionProtocolDescription', 
    'ActualHumanPerformersSequence', 'AdditionalPatientHistory', 'AdmissionID', 'AdmittingDiagnosesCodeSequence', 'AdmittingDiagnosesDescription', 'Allergies',
    'Arbitrary', 'AuthorObserverSequence', 'Branch​OfService', 'CommentsOnThePerformedProcedureStep', 'ConfidentialityConstraintOnPatientDataDescription',
    'ContentCreatorName', 'ContentCreatorIdentificationCodeSequence', 'ContentSequence', 'ContrastBolusAgent', 'ContributionDescription', 'Country​Of​Residence', 
    'CurrentPatientLocation', 'CurveData', 'CustodialOrganizationSequence', 'DataSetTrailingPadding', 'DerivationDescription', 'DigitalSignatureUID',
    'DigitalSignaturesSequence', 'DischargeDiagnosisDescription', 'DistributionAddress', 'DistributionName', 'FillerOrderNumberImagingServiceRequest',
    'FrameComments', 'GraphicAnnotationSequence', 'HumanPerformerCodeSequence', 'HumanPerformerOrganization', 'IconImageSequence', 'IdentifyingComments', 
    'ImageComments', 'ImagePresentationComments', 'ImagingServiceRequestComments', 'Impressions', 'InstitutionAddress', 'InstitutionCodeSequence',
    'InstitutionName', 'InstitutionalDepartmentName', 'InsurancePlanIdentification', 'IntendedRecipientsOfResultsIdentificationSequence',
    'InterpretationApproverSequence', 'InterpretationAuthor', 'InterpretationDiagnosisDescription', 'InterpretationIDIssuer', 'InterpretationRecorder',
    'InterpretationText', 'InterpretationTranscriber', 'IssuerOfAdmissionID', 'IssuerOfPatientID', 'IssuerOfServiceEpisodeID', 'MAC', 'MedicalAlerts',
    'MedicalRecordLocator', 'MilitaryRank', 'ModifiedAttributesSequence', 'ModifiedImageDescription', 'ModifyingDeviceID', 'ModifyingDeviceManufacturer',
    'NameOfPhysiciansReadingStudy', 'NamesOfIntendedRecipientsOfResults', 'Occupation', 'OperatorIdentificationSequence', 'OperatorsName', 'OriginalAttributesSequence',
    'OrderCallbackPhoneNumber', 'OrderEnteredBy', 'OrderEntererLocation', 'OtherPatientIDs', 'OtherPatientIDsSequence', 'OtherPatientNames', 'OverlayComments',
    'OverlayData', 'ParticipantSequence', 'PatientAddress', 'PatientComments', 'PatientState', 'PatientTransportArrangements', 'PatientBirthDate', 'PatientBirthName',
    'PatientBirthTime', 'PatientInstitutionResidence', 'PatientInsurancePlanCodeSequence', 'PatientMotherBirthName', 'PatientPrimaryLanguageCodeSequence',
    'PatientPrimaryLanguageModifierCodeSequence', 'PatientReligiousPreference', 'PatientTelephoneNumbers', 'PerformedLocation', 'PerformedProcedureStepDescription',
    'PerformedProcedureStepID', 'PerformingPhysicianIdentificationSequence', 'PerformingPhysicianName', 'PersonAddress', 'PersonIdentificationCodeSequence',
    'PersonName', 'PersonTelephoneNumbers', 'PhysicianApprovingInterpretation', 'PhysiciansReadingStudyIdentificationSequence', 'PhysiciansOfRecord',
    'PhysiciansOfRecordIdentificationSequence', 'PlacerOrderNumberImagingServiceRequest', 'PreMedication', 'ProtocolName', 'ReasonForTheImagingServiceRequest',
    'ReasonForStudy', 'ReferencedDigitalSignatureSequence', 'ReferencedPatientAliasSequence', 'ReferencedPatientSequence', 'ReferencedSOPInstanceMACSequence', 
    'ReferringPhysicianAddress', 'ReferringPhysicianIdentificationSequence', 'ReferringPhysicianName', 'ReferringPhysicianTelephoneNumbers', 'RegionOfResidence', 
    'RequestAttributesSequence', 'RequestedContrastAgent', 'RequestedProcedureComments', 'RequestedProcedureDescription', 'RequestedProcedureID', 'RequestedProcedureLocation',
    'RequestingPhysician', 'RequestingService', 'ResponsibleOrganization', 'ResponsiblePerson', 'ResultsComments', 'ResultsDistributionListSequence', 
    'ResultsIDIssuer', 'ReviewerName', 'ScheduledHumanPerformersSequence', 'ScheduledPatientInstitutionResidence', 'ScheduledPerformingPhysicianIdentificationSequence', 
    'ScheduledPerformingPhysicianName', 'ScheduledProcedureStepDescription', 'SeriesDescription', 'ServiceEpisodeDescription', 'ServiceEpisodeID', 'SpecialNeeds',
    'StudyComments', 'StudyDescription', 'StudyID', 'StudyIDIssuer', 'TextComments', 'TextString', 'TopicAuthor', 'TopicKeywords', 'TopicSubject', 'TopicTitle', 
    'VerifyingObserverIdentificationCodeSequence', 'VerifyingObserverName', 'VerifyingObserverSequence', 'VerifyingOrganization', 'VisitComments']


    input_path = '/data/xnat/archive/PROJECT/arc001/'

    subjects = os.listdir(input_path)

    for subject in subjects:
        print('**************')
        print('Subject = %s' %(subject))
        subject_id = subject

        # Each subdirectory is a different scan i.e. session                                                                                         
        subject_path = input_path + os.sep + subject + os.sep + 'SCANS'
        scans = os.listdir(subject_path)

        for scan in scans:
            print('  *** Scan = %s' %(scan))
            scan_path = subject_path + os.sep + scan + os.sep+ 'DICOM'            
           
            n_dicom = 0
            dicom_file = ''
            
            for dirpaths, dirnames, filenames in os.walk(scan_path):
                    for filename in filenames:
                        if(not filename.endswith(".xml")):
                            n_dicom = n_dicom + 1
                            dicom_file = os.path.join(dirpaths, filename)
                            check_reports(dicom_file)
                            dicom_path = dirpaths
            if (n_dicom < 10):
                    print('ATTN!!! - check %s - it has %d files only' %(scan_path, n_dicom))

            metadata = pydicom.dcmread(dicom_file)
            check_phi(metadata, list_phi)
