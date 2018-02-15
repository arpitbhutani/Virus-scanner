import os
import sys


if (len(sys.argv) != 3):
        print "<Usage>: python scan.py <signature_file> <directory_to_scan>"
        sys.exit()

sigfile = os.path.abspath(sys.argv[1])
path = os.path.abspath(sys.argv[2])
sigs = []

def scanvirus(filePath):
        with open(filePath, "rb") as file:
                lines = file.read()
                for sig in sigs:
                        if sig in lines:
                                print "Found match for signature: \'" + sig + "\' in File: " + filePath

with open(sigfile, "rb") as file:
        sigs = file.read().splitlines()

for root, dirs, files in os.walk(path):
        for file in files:
                filePath = os.path.join(root, file)
                if filePath != os.path.abspath(sys.argv[1]) and filePath != os.path.abspath(sys.argv[0]):
                        scanvirus(filePath)


