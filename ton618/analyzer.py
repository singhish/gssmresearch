import os

# Part 1: Processing Potential Lines
"""
Here, I open a .txt file containing all potential
absorption features I observed by eye along the
spectrum of Ton 618. I convert the resulting strings
into floats to facilitate data analysis.
"""
lines = open("potential_absorption_features.txt", "r").readlines()[0].split("\r")

for i in range(len(lines)):
    lines[i] = float(lines[i])

# Part 2: Processing All Redshifts
"""
I create a list of the files for all redshifted 
wavelengths at the redshift of each absorbers along 
the sightline to Ton 618. From here, I transpose every
line from each file into a 1D list of floats and the 
ion corresponding to each line in a 1D list of strings. 
I then take note of the intervals of the indices
corresponding to each redshift using the commented-out
print statement for Part 3 of the script.
"""
os.chdir("ton618redshifts")
wavelength_files = [
    open("1-0_3630.txt", "r"), open("2-1_2252.txt", "r"), open("3-1_3582.txt", "r"), open("4-1_4290.txt", "r"),
    open("5-1_6251.txt", "r"), open("6-1_6266.txt", "r"), open("7-1_6315.txt", "r"), open("8-1_7942.txt", "r"),
    open("9-1_7945.txt", "r"), open("10-1_7947.txt", "r"), open("11-1_7950.txt", "r"), open("12-1_7951.txt", "r"),
    open("13-1_7956.txt", "r"), open("14-1_7962.txt", "r"), open("15-1_8865.txt", "r"), open("16-1_8871.txt", "r"),
    open("17-1_8963.txt", "r"), open("18-1_8975.txt", "r"), open("19-2_1103.txt", "r"), open("20-2_1197.txt", "r")
]
os.chdir("..")
chemical_data = []
wavelengths = []

for i in range(len(wavelength_files)):
    wavelengths.extend(wavelength_files[i].readlines())

for i in range(len(wavelengths)):
    temp_data = wavelengths[i].rstrip("\n").split("      ")
    chemical_data.append(temp_data[0])
    wavelengths[i] = float(temp_data[1])
#    print i, chemical_data[i], wavelengths[i]
    
# Part 3: Finding Likely Lines
"""
I compare each potential absorption feature to every 
redshifted wavelength in the 1D list. If a potential 
absorption is within a defined tolerance (tol) of 
a redshifted wavelength, it, its redshift, and the
redshifted wavelength are placed into an list and
appended to a list of candidate absorption features.
tol is set to an arbitrarily value small enough to
compensate for wider absorption feature. Each
candidate absorption feature is later visually 
cross-checked in IRAF. The redshift of each candidate 
feature is identified using the intervals identified 
in Part 2.
"""
tol = 1
candidates = []
for i in range(len(lines)):
    for j in range(len(wavelengths)):
        z = 0
        if abs(lines[i] - wavelengths[j]) < tol:
            if j <= 164: z = 0.3630 
            elif j <= 327: z = 1.2252
            elif j <= 490: z = 1.3582
            elif j <= 653: z = 1.4290
            elif j <= 816: z = 1.6251
            elif j <= 979: z = 1.6266
            elif j <= 1142: z = 1.6315
            elif j <= 1305: z = 1.7942
            elif j <= 1468: z = 1.7945
            elif j <= 1631: z = 1.7947
            elif j <= 1794: z = 1.7950
            elif j <= 1957: z = 1.7951
            elif j <= 2120: z = 1.7956
            elif j <= 2283: z = 1.7962
            elif j <= 2446: z = 1.8865
            elif j <= 2609: z = 1.8871
            elif j <= 2772: z = 1.8963
            elif j <= 2935: z = 1.8975
            elif j <= 3098: z = 2.1103
            else: z = 2.1197
            candidates.append([lines[i], wavelengths[j], z, chemical_data[j]])

# Part 4: Printing Candidate Absorption Features Across All Redshifts
"""
I sort the candidates list for readability, and then
print each element of candidates.
"""
candidates = sorted(candidates)
print "[ line , wav , z , ion ] tol=", tol
for i in range(len(candidates)):
    print candidates[i]