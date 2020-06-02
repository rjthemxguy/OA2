import csv
import globals as g
import pandas as pd
import DBModule as db



if g.mode == "I":
    import constants as con

else:
    import constantsMed as con

import os


class fileClass:
    def __init__(self):

        self.filePath = "input/"
        self.inputFileName = ""


    def __numIn(self, s):
        return any(i.isdigit() for i in s)

    def setPath(self, path):
        self.filePath = path

    def openInput(self, inputFileName):
        with open(self.filePath + inputFileName, 'r') as file:
            fileData = file.read()

            fileData = fileData.replace('"', '')

            with open('scratch/readIns.csv', 'w') as file:
                file.write(fileData)

                file.close()


    def alignAccession(self):
        with open('scratch/cleaned.csv', 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            with open('scratch/aligned.csv', "w", newline='') as result:
                writer = csv.writer(result)

                for row in csvreader:

                    if "SUITE" in row[335]:
                        row[334] = row[334] + row[335]
                        del row[335]

                    if row[con.ACCESSION_NUMBER] == "":
                        del row[con.ACCESSION_NUMBER]

                    if row[con.ACCESSION_NUMBER] == "":
                        del row[con.ACCESSION_NUMBER]

                    if row[con.ACCESSION_NUMBER] == "":
                        del row[con.ACCESSION_NUMBER]

                    writer.writerow(row)

                result.close()

    def alignAccessionMedi(self):
        with open('scratch/cleaned.csv', 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            with open('scratch/aligned.csv', "w", newline='') as result:
                writer = csv.writer(result)

                for row in csvreader:

                    if self.__numIn(row[24]):
                        row[23] = row[23] + row[24]
                        del row[24]

                    if self.__numIn(row[30]):
                        row[29] = row[29] + row[30]
                        del row[30]

                    if "APT" in row[24]:
                        row[23] = row[23] + row[24]
                        del row[24]

                    if "APT" in row[30]:
                        row[29] = row[29] + row[30]
                        del row[30]

                    if row[68] != "":
                        row[67] = row[68]
                        row[68] = ""

                    if row[75] == "":
                        del row[75]

                    if row[74] != "":
                        row[83] = row[82]
                        row[82] = row[81]
                        row[81] = row[80]
                        row[80] = row[79]
                        row[79] = row[78]
                        row[78] = row[77]
                        row[77] = row[76]
                        row[76] = row[75]
                        row[75] = row[74]
                        row[74] = ""

                    if row[90] != "":
                        row[95] = row[94]
                        row[94] = row[93]
                        row[93] = row[92]
                        row[92] = row[91]
                        row[91] = row[90]
                        row[90] = ""

                    row[20] = row[19]
                    row[19] = row[18]
                    row[18] = row[17]
                    row[17] = row[16]
                    row[16] = row[15]
                    row[15] = row[9]
                    row[9] = ""

                    row[28] = row[27]
                    row[27] = row[26]
                    row[26] = row[25]
                    row[25] = row[24]
                    row[24] = row[23]
                    row[23] = ""

                    row[68] = row[67]
                    row[67] = row[66]
                    row[66] = row[65]
                    row[65] = row[64]
                    row[64] = ""

                    row[83] = row[82]
                    row[82] = row[81]
                    row[81] = row[80]
                    row[80] = row[79]
                    row[79] = row[78]
                    row[78] = row[77]
                    row[77] = row[76]
                    row[76] = row[75]
                    row[75] = row[74]
                    row[74] = ""

                    row[96] = row[95]
                    row[95] = row[94]
                    row[94] = row[93]
                    row[93] = row[92]
                    row[92] = row[91]
                    row[91] = ""

                    if row[con.ACCESSION_NUMBER] == "":
                        if row[con.ACCESSION_NUMBER - 1] != "":
                            row[con.ACCESSION_NUMBER] = row[con.ACCESSION_NUMBER - 1]
                            row[con.ACCESSION_NUMBER - 1] = ""

                        if row[con.ACCESSION_NUMBER] == "":
                            if row[con.ACCESSION_NUMBER - 2] != "":
                                row[con.ACCESSION_NUMBER] = row[con.ACCESSION_NUMBER - 2]
                                row[con.ACCESSION_NUMBER - 2] = ""

                        try:
                            if row[con.ACCESSION_NUMBER + 1] != "":
                                row[con.ACCESSION_NUMBER] = row[con.ACCESSION_NUMBER + 1]
                                row[con.ACCESSION_NUMBER + 1] = ""
                        except:
                            pass

                        try:
                            if row[con.ACCESSION_NUMBER + 2] != "":
                                row[con.ACCESSION_NUMBER] = row[con.ACCESSION_NUMBER + 2]
                                row[con.ACCESSION_NUMBER + 2] = ""
                        except:
                            pass


                    writer.writerow(row)

                result.close()

    def parseForMed(self, issue, fileName):
        with open('scratch/' + fileName, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            with open('scratch/parsed1.csv', "w", newline='') as result:
                writer = csv.writer(result)

                for row in csvreader:
                    if "PALMETTO" not in row[1]:
                        writer.writerow(row)

                result.close()

    def parseForBlankIns(self, issue, fileName):
        with open('scratch/parsed1.csv', 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            with open('scratch/parsed2.csv', "w", newline='') as result:
                writer = csv.writer(result)

                for row in csvreader:
                    if len(row[1]) == 0:
                        row[1] = "Insurance Info Missing"
                    writer.writerow(row)

                result.close()

    def parseForBadSubID(self, issue, fileName):
        with open('scratch/parsed2.csv', 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            with open('scratch/parsed3.csv', "w", newline='') as result:
                writer = csv.writer(result)

                for row in csvreader:
                    if self.__numIn(row[15]) == True:
                        writer.writerow(row)

                result.close()

    def parseForBadAddress(self, issue, fileName):
        with open('scratch/parsed3.csv', 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            with open('scratch/parsed4.csv', "w", newline='') as result:
                writer = csv.writer(result)

                for row in csvreader:
                    if "SUITE" in row[con.SUITE_FIX_1]:
                        row[con.SUITE_FIX_1 - 1] = row[con.SUITE_FIX_1 - 1] + row[con.SUITE_FIX_1]
                        del row[con.SUITE_FIX_1]

                    writer.writerow(row)
                result.close()

    def parseForRan(self, _accession):
        database = db.database_class()

        with open('scratch/parsed4.csv', 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            with open('scratch/addressFixed.csv', "w", newline='') as result:
                writer = csv.writer(result)

                for row in csvreader:
                    if database.didRun(row[con.ACCESSION_NUMBER])  == False:
                         writer.writerow(row)
                    else:
                        print("Accession " + row[con.ACCESSION_NUMBER] + " Ran")




    def fixAddress(self, fileName):

        with open('scratch/' + fileName, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            with open('scratch/addressFixed.csv', "w", newline='') as result:
                writer = csv.writer(result)

                for row in csvreader:

                    if self.__numIn(row[con.NUM_FIX_1]) == True:
                        row[con.NUM_FIX_1 - 1] = row[con.NUM_FIX_1 - 1] + row[con.NUM_FIX_1]
                        del row[con.NUM_FIX_1]

                    if self.__numIn(row[con.NUM_FIX_2]) == True:
                        row[con.NUM_FIX_2 - 1] = row[con.NUM_FIX_2 - 1] + row[con.NUM_FIX_2]
                        del row[con.NUM_FIX_2]

                    if self.__numIn(row[con.NUM_FIX_3]) == True:
                        row[con.NUM_FIX_3 - 1] = row[con.NUM_FIX_3 - 1] + row[con.NUM_FIX_3]
                        del row[con.NUM_FIX_3]

                    if "SUITE" in row[con.SUITE_FIX_1]:
                        row[con.SUITE_FIX_1 - 1] = row[con.SUITE_FIX_1 - 1] + row[con.SUITE_FIX_1]
                        del row[con.SUITE_FIX_1]

                    if "SUITE" in row[con.SUITE_FIX_2]:
                        row[con.SUITE_FIX_2 - 1] = row[con.SUITE_FIX_2 - 1] + row[con.SUITE_FIX_2]
                        del row[con.SUITE_FIX_2]

                    if "MD" in row[con.MD_FIX]:
                        del row[con.MD_FIX]

                    if "MD" in row[con.MD_FIX2]:
                        del row[con.MD_FIX2]

                    writer.writerow(row)

                result.close()

    def get(self):

        self.dataset = pd.read_csv("input/" + g.fileToOpen, header=None)
        return (self.dataset)

        print("There is no Accessions number to run")
        exit(200)


