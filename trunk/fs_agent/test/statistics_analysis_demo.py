# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2016-12-13
# desc: this algorithm was reference neopi.py
# thanks for @Neohapsis <https://github.com/Neohapsis/>


import sys
import os
import re
import csv
import zlib
import time
import math
from collections import defaultdict

#define the smallest file size to filter. 
SMALLEST = 60


class LanguageIC:
    """Class that calculates a file's Index of Coincidence as
    as well as a a subset of files average Index of Coincidence.
    """
    def __init__(self):
        """Initialize results arrays as well as character counters."""
        self.char_count =  defaultdict(int)
        self.total_char_count = 0
        self.results = []
        self.ic_total_results = ""

    def calculate_char_count(self,data):
        """Method to calculate character counts for a particular data file."""
        if not data:
            return 0
        for x in range(256):
            char = chr(x)
            charcount = data.count(char)
            self.char_count[char] += charcount
            self.total_char_count += charcount
        return

    def calculate_IC(self):
        """Calculate the Index of Coincidence for the self variables"""
        total = 0
        for val in self.char_count.values():

            if val == 0:
                continue
            total += val * (val-1)

        try:
            ic_total = float(total)/(self.total_char_count * (self.total_char_count - 1))
        except:
            ic_total = 0
        self.ic_total_results = ic_total
        return

    def calculate(self,data,filename):
        """Calculate the Index of Coincidence for a file and append to self.ic_results array"""
        if not data:
            return 0
        char_count = 0
        total_char_count = 0

        for x in range(256):
            char = chr(x)
            charcount = data.count(char)
            char_count += charcount * (charcount - 1)
            total_char_count += charcount

        ic = float(char_count)/(total_char_count * (total_char_count - 1))
        self.results.append({"filename":filename, "value":ic})
        # Call method to calculate_char_count and append to total_char_count
        self.calculate_char_count(data)
        return ic


class Entropy:
    """Class that calculates a file's Entropy."""

    def __init__(self):
        """Instantiate the entropy_results array."""
        self.results = []

    def calculate(self,data,filename):
        """Calculate the entropy for 'data' and append result to entropy_results array."""

        if not data:
            return 0
        entropy = 0
        self.stripped_data =data.replace(' ', '')
        for x in range(256):
            p_x = float(self.stripped_data.count(chr(x)))/len(self.stripped_data)
            if p_x > 0:
                entropy += - p_x * math.log(p_x, 2)
        self.results.append({"filename":filename, "value":entropy})
        return entropy


class LongestWord:
    """Class that determines the longest word for a particular file."""
    def __init__(self):
        """Instantiate the longestword_results array."""
        self.results = []

    def calculate(self,data,filename):
        """Find the longest word in a string and append to longestword_results array"""
        if not data:
            return "", 0
        longest = 0
        longest_word = ""
        words = re.split("[\s,\n,\r]", data)
        if words:
            for word in words:
                length = len(word)
                if length > longest:
                    longest = length
                    longest_word = word
        self.results.append({"filename":filename, "value":longest})
        return longest


class Compression:
    """Generator finds compression ratio"""

    def __init__(self):
        """Instantiate the results array."""
        self.results = []

    def calculate(self, data, filename):
        if not data:
            return "", 0
        compressed = zlib.compress(data)
        ratio = float(len(compressed)) / float(len(data))
        self.results.append({"filename":filename, "value":ratio})
        return ratio



class SearchFile:
    
    def search_file_path(self, web_dir, ext_list):
        for root, dirs, files in os.walk(web_dir):
            for file in files:
                filename = os.path.join(root, file)
                #file_ext = file.split(".")[1]
                #print '>>>', file_ext
                #sys.exit(0)

                SMALLEST = 60
                if (re.search('(\.php|\.asp|\.py)$', filename)) and (os.path.getsize(filename) > SMALLEST):
                    try:
                        data = open(root + "/" + file, 'rb').read()
                    except:
                        data = False
                        print "Could not read file :: %s/%s" % (root, file)
                    yield data, filename



if __name__ == "__main__":
    """Parse all the options"""

    timeStart = time.clock()

    web_dir = "/tmp/wx"
    ext_list = ['php','asp']
    out_file = "./out2.csv"

    # Error on an invalid path
    if os.path.exists(web_dir) == False:
        parser.error("Invalid path")
   
    tests = []
    tests.append(LanguageIC())
    tests.append(Entropy())
    tests.append(LongestWord())
    tests.append(Compression())

    # Instantiate the Generator Class used for searching, opening, and reading files
    locator = SearchFile()

    # CSV file output array
    csv_array = []
    csv_header = ["filename"]

    # Grab the file and calculate each test against file
    fileCount = 0
    fileIgnoreCount = 0
    for data, filename in locator.search_file_path(web_dir, ext_list):
        if data:
            # a row array for the CSV
            csv_row = []
            csv_row.append(filename)

            for test in tests:
                calculated_value = test.calculate(data, filename)
                # Make the header row if it hasn't been fully populated, +1 here to account for filename column
                if len(csv_header) < len(tests) + 1:
                    csv_header.append(test.__class__.__name__)
                csv_row.append(calculated_value)
                fileCount = fileCount + 1
            csv_array.append(csv_row)

    csv_array.insert(0,csv_header)
    fileOutput = csv.writer(open(out_file, "wb"))
    fileOutput.writerows(csv_array)

    timeFinish = time.clock()

    # Print some stats
    print "\n[[ Total files scanned: %i ]]" % (fileCount)
    print "[[ Total files ignored: %i ]]" % (fileIgnoreCount)
    print "[[ Scan Time: %f seconds ]]" % (timeFinish - timeStart)




