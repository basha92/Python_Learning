#this program prints patient name with IDs
patient_id = ['Patient 1', 'Patient 2', 'Patient 3']
patients = ["John","Alice","David"]
#To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
for id, name in zip(patient_id, patients):
    print('{0} : {1}'.format(id, name))