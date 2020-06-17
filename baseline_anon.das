// Dicom Anonymisation Script 
// Language reference: https://wiki.xnat.org/xnat-tools/dicomedit/dicomedit-6-2-language-reference

// Lorena Escudero (University of Cambridge), baseline version 1 - June 2020

// This script is intended to remove or set to Z/D any DICOM tags that are “baseline”,
// i.e. in Basic Profile but not kept in other profiles in Table E.1-1 of Suppl 142 
// ftp://medical.nema.org/medical/dicom/final/sup142_ft.pdf

// Note: If they are only “clean” in other profiles (not kept), the choice for Basic Profile is retained (e.g. remove, for Allergies) 

// Note: When multiple options are available, e.g. ‘X/Z – X unless Z is required to maintain IOD conformance’, first option is used

// Note: PatientName and PatientID are assumed to be de-identified already

//Changelog
// v1 - initial version, June 2020

// Baseline fields 
(0008,0050) := "" 	 // Accession Number^M
- (0018,4000)   // Acquisition Comments^M
- (0040,0555)   // Acquisition Context Sequence^M
- (0018,1400)   // Acquisition Device Processing Description^M
- (0018,9424)   // Acquisition Protocol Description^M
- (0040,4035)   // Actual Human Performers Sequence^M
- (0010,21B0)   // Additional Patient’s History^M
- (0038,0010)   // Admission ID^M
- (0008,1084)   // Admitting Diagnoses Code Sequence^M
- (0008,1080)   // Admitting Diagnoses Description^M
- (0010,2110)   // Allergies^M
- (4000,0010)   // Arbritrary^M
- (0040,A078)   // Author Observer Sequence^M
- (0010,1081)   // Branch of Service^M
- (0040,0280)   // Comments on Performed Procedure Step^M
- (0040,3001)   // Confidentiality Constraint on Patient Data Description^M
(0070,0084) := "" // Content Creator’s Name^M
- (0070,0086)   // Content Creator’s Identification Code Sequence^M
- (0040,A730)   // Content Sequence^M
(0018,0010)  := ""	  // Contrast Bolus Agent^M
- (0018,A003) 	// Contribution Description^M
- (0010,2150) 	// Country of Residence^M
- (0038,0300) 	// Current Patient Location^M
- (50X@,XXXX)	// Curve Data^M
- (0040,A07C) 	// Custodial Organisation Sequence^M
- (FFFC,FFFC)	// Data Set Trailing Padding^M
- (0008,2111) 	// Derivation Description^M
- (0400,0100) 	// Digital Signature UID^M
- (FFFA,FFFA) 	// Digital Signatures Sequence^M
- (0038,0040) 	// Discharge Diagnosis Description^M
- (4008,011A) 	// Distribution Address^M
- (4008,0119) 	// Distribution Name^M
(0040,2017) := ""  // Filler Order Number of Imaging Service Request^M
- (0020,9158)   // Frame Comments^M
- (0070,0001)	// Graphic Annotation Sequence - Note: Gives problems as "D" so removed^M
- (0040,4037)   // Human Performers Name^M
- (0040,4036)   // Human Performers Organisation^M
- (0088,0200)   // Icon Image Sequence^M
- (0008,4000)   // Identifying Comments^M
- (0020,4000)   // Image Comments^M
- (0028,4000)   // Image Presentation Comments^M
- (0040,2400)   // Imaging Service Request Comments^M
- (4008,0300)   // Impressions^M
- (0008,0081)   // Institution Address^M
- (0008,0082)   // Institution code Sequence^M
- (0008,0080)   // Institution Name^M
- (0008,1040)   // Institutional Department Name^M
- (0010,1050)   // Insurance Plan Identification^M
- (0040,1011)   // Intended Recipients of results Identification Sequence^M
- (4008,0111)   // Interpretation Approver Sequence^M
- (4008,010C)   // Interpretation Author^M
- (4008,0115)   // Interpretation Diagnosis Description^M
- (4008,0202)   // Interpretation ID Issuer^M
- (4008,0102)   // Interpretation Recorder^M
- (4008,010B)   // Interpretation Text^M
- (4008,010A)   // Interpretation Transcriber^M
- (0038,0011)   // Issuer of Admission ID^M
- (0010,0021)   // Issuer of Patient ID^M
- (0038,0061)   // Issuer of Service Episode ID^M
- (0400,0404)   // MAC^M
- (0010,2000)   // Medical Alerts^M
- (0010,1090)   // Medical Record Locator^M
- (0010,1080)   // Military Rank^M
- (0400,0550)   // Modified Attributes Sequence^M
- (0020,3406)   // Modified Image Description^M
- (0020,3401)   // Modifying Device ID^M
- (0020,3404)   // Modifying Device Manufacturer^M
- (0008,1060)   // Name of Physician(s) Reading Study^M
- (0040,1010)   // Name of Intended Recipient of Results^M
- (0010,2180)   // Occupation^M
- (0008,1072)   // Operators Identification Sequence^M
- (0008,1070)   // Operators Name^M
- (0400,0561)   // Original Attributes Sequence^M
- (0040,2010)   // Order Callback Phone Number^M
- (0040,2008)   // Order Entered By^M
- (0040,2009)   // Order Enterer Location^M
- (0010,1000)   // Other Patient IDs^M
- (0010,1002)   // Other Patient IDs Sequence^M
- (0010,1001)   // Other Patient Names^M
- (60X@,4000)   // Overlay Comments^M
- (60X@,3000)   // Overlay Data^M
- (0040,A07A)   // Participant Sequence^M
- (0010,1040)   // Patient Address^M
- (0010,4000)   // Patient Comments^M
- (0038,0500)   // Patient State^M
- (0040,1004)   // Patient Transport Arrangements^M
(0010,0030) := "" 	  // Patients Birth Date^M
- (0010,1005)   // Patients Birth Name^M
- (0010,0032)   // Patients Birth Time^M
- (0038,0400)   // Patients Institution Residence^M
- (0010,0050)   // Patients Insurance Plan Code Sequence^M
- (0010,1060)   // Patients Mothers Birth Name^M
- (0010,0101)   // Patients Primary Language Code Sequence^M
- (0010,0102)   // Patients Primary Language Modifier Code Sequence^M
- (0010,21F0)   // Patients Religious Preference^M
- (0010,2154)   // Patient’s Telephone Number^M
- (0040,0243)   // Performed Location^M
- (0040,0254)   // Performed Procedure Step Description^M
- (0040,0253)   // Performed Procedure Step ID^M
- (0008,1052)   // Performing Physicians Identification Sequence^M
- (0008,1050)   // Performing Physicians Name^M
- (0040,1102)   // Person Address^M
- (0040,1101)	 // Person Identification Code Sequence - Note: gives problems as "D" so removed^M
(0040,A123) := "Anon"	 // Person Name^M
- (0040,1103)   // Person Telephone Numbers^M
- (4008,0114)   // Physician Approving Interpretation^M
- (0008,1062)   // Physician Reading Study Identification Sequence^M
- (0008,1048)   // Physician(s) of Record^M
- (0008,1049)   // Physician(s) of Record Identification Sequence^M
(0040,2016) := "" // Place Order Number of Imaging Service Request^M
//- (ggg#,eeee)   // Private attributes^M
- (0040,0012)   // Pre-Medication^M
- (0018,1030)   // Protocol Name^M
- (0040,2001)   // Reason for Imaging Service Request^M
- (0032,1030)   // Reason for Study^M
- (0400,0402)   // Referenced Digital Signature Sequence^M
- (0038,0004)   // Referenced Patient Alias Sequence^M
- (0008,1120)   // Referenced Patient Sequence^M
- (0400,0403)   // Referenced SOP Instance MAC Sequence^M
- (0008,0092)   // Referring Physician’s Address^M
- (0008,0096)   // Referring Physician’s Identification Sequence^M
(0008,0090) := "" 	    // Referring Physician’s Name^M
- (0008,0094)   // Referring Physician’s Telephone Numbers^M
- (0010,2152)   // Region of Residence^M
- (0040,0275)   // Request Attributes Sequence^M
- (0032,1070)   // Requested Contrast Agent^M
- (0040,1400)   // Requested Procedure Comments^M
- (0032,1060)   // Requested Procedure Description^M
- (0040,1001)   // Requested Procedure ID^M
- (0040,1005)   // Requested Procedure Location^M
- (0032,1032)   // Requesting Physician^M
- (0032,1033)   // Requesting Service^M
- (0010,2299)   // Responsible Organisation^M
- (0010,2297)   // Responsible Person^M
- (4008,4000)   // Results Comments^M
- (4008,0118)   // Results Distribution List Sequence^M
- (4008,0042)   // Results ID Issuer^M
- (300E,0008)   	  // Reviewer Name^M
- (0040,4034) 	  // Scheduled Human Performers Sequence^M
- (0038,001E)	     // Scheduled Patient Institution Residence^M
- (0040,000B)  	     // Scheduled Performing Physician Identification Sequence^M
- (0040,0006) 	     // Scheduled Performing Physician Name^M
- (0040,0007) 	     // Scheduled Procedure Step Description^M
- (0008,103E) 	     // Series Description^M
- (0038,0062) 	     // Service Episode Description^M
- (0038,0060) 	     // Service Episode ID^M
- (0038,0050) 	     // Special Needs^M
- (0032,4000) 	     // Study Comments^M
- (0008,1030) 	     // Study Description^M
(0020,0010) := ""    // Study ID^M
- (0032,0012)   // Study ID Issuer^M
- (4000,4000)   // Text Comments^M
- (2030,0020)   // Text String^M
- (0088,0910)   	  // Topic Author^M
- (0088,0912)	     // Topic Key Words^M
- (0088,0906)	     	// Topic Subject^M
- (0088,0904)		   // Topic Title^M
- (0040,A088) 	   // Verifying Observer Identification Code Sequence - Note: gives problem as "" (Z) so removed^M
(0040,A075) := "Anon" 	   // Verifying Observer Name^M
- (0040,A073)	   // Verifying Observer Sequence - Note: Can give problems as "D", so removed^M
- (0040,A027)   // Verifying Organisation^M
- (0038,4000)   // Visit Comments^M

// Delete overlays - from Simon J Doran
-(6000,0010)
-(6000,0011)
-(6000,0040)
-(6000,0050)
-(6000,0100)
-(6000,0102)
-(6000,3000)
-(6001,0010)
-(6001,1001)

(0012,0062) := "YES" // Patient identity removed^M
(0012,0063) := "DicomEdit 6 anonymisation script" // Deidentification method^M


