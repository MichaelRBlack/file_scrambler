import os
import random

print("It's scramble time!")

rootdir = 'C:\\temp\\Music'

fileAssignmentIndex = 0
filesList = []

# Count how many files we're dealing with today
for root, dirs, files in os.walk(rootdir):
    for file in files:
        # print("root: "+root)
        # print(os.path.basename(root))
        filesList.append([root, file, os.path.join(root, file)])

print("File Count: ", len(filesList))
claimedNumbers = []

# While the size of the array is smaller than the number of files, 
# continue to generate a random number.
# when a random number is available, pick the next file in the list
while len(claimedNumbers) < len(filesList):
    r = random.randint(1, len(filesList))
    # print("Candidate: ", r)
    try:
        test = claimedNumbers[r]
        # print("Cache hit: "+str(r))
    except IndexError:
        # print("Assigning File"+str(r))
        claimedNumbers.insert(r, [r, filesList[fileAssignmentIndex]])
        fileAssignmentIndex += 1

i = 0
while i < len(claimedNumbers):
    rnd_num = claimedNumbers[i][0]
    old_file_name = claimedNumbers[i][1][1]
    old_file_path = claimedNumbers[i][1][0]
    old_full_path = claimedNumbers[i][1][2]
    # print("Random Number: "+str(rnd_num))
    # print("old_file_path: "+str(old_file_path))
    # print("old_file_name: "+str(old_file_name))
    # print(old_full_path)
    # print(rootdir+"/scrambled/{"+str(rnd_num)+"} "+old_file_name)
    os.rename(old_full_path, "C:\\temp\\scrambled\\{"+str(rnd_num)+"} "+old_file_name)
    i += 1

print("Have a nice day")