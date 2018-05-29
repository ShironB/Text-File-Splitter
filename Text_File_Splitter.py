'''
Script Description
=====================
The script takes all files in input folder and split each one of them to several files. Max splited file size
will be 50MB. The splitted files can be found in output folder.


Flow
========
1. Check for files in input folder.
2. Found Files --> Check Size --> Bigger than 50MB --> Read 5 lines and write to new file
3. New File is reached 50 MB --> Close file --> Start New One


TASKS
========
1. Add Logging, Lose Shell Prints
2. Implementing better EOF check
'''


import datetime
import os
import time


# CHANGE FOLDERS BASED ON YOUR NEEDS
inputFolder = "input"
outputFolder = "output"

# CHANGE VARS BASED ON YOUR NEEDS
maxSize = 51200000


currentTime = time.time()
currentFile = -1

# SEARCHING FILES IN FOLDER
for currentFile in os.listdir(inputFolder):
    # CHECKING THAT THE FILE IS BIGGER THEN 50. ELSE DISMISS
    fullSrcPath = inputFolder + '/' + currentFile
    fileSize = os.path.getsize(fullSrcPath)

    # NO NEED TO DO SOMETHING IF IT SMALLER THAN 50 MB
    if fileSize > maxSize:
        # OPEN THE SOgURCE FILE
        outputFileCounter = 0
        fInput = open(fullSrcPath, 'r')
        print "Opened The File:  " + fullSrcPath

        # OPEN THE DESTINATION FILE
        newLine = fInput.readline()
        while newLine != "":
            outputFileName = currentFile[0:len(currentFile)-4] + "_" + str(outputFileCounter) + ".txt"
            fullDstPath = outputFolder + '/' + outputFileName
            fOutput = open(fullDstPath, 'w')
            print "Created New File:  " + fullDstPath

            # INIT COUNTERS AND TEMP VARS
            i = 0
            lineStack = ""

            # READING BATCH OF 5 LINES AND WRITING THEM TO THE NEW FILE
            while (os.path.getsize(fullDstPath) < maxSize):
                if newLine != "":  # NOT EOF.
                    lineStack = lineStack + newLine
                    i += 1
                    newLine = fInput.readline()
                    if i == 5:  # REACHED 5 LINES IN MEMORY
                        fOutput.write(lineStack)
                        lineStack = ""
                        i = 0
                else:  # DID REACH END OF FILE
                    fOutput.write(lineStack)
                    print "END OF FILE"
                    break

            fOutput.close()
            outputFileCounter += 1

    else:
        print "The File" + str(currentFile) + "Is Small Enough. Splitting Is Unnecessary"

# IF THERE ARE NO FILES IN INPUT FOLDER
if currentFile == -1:
    print "No Files In Input Folder."

