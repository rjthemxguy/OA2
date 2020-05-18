import fileImport as f
import claimImport as c
import constants as con
from os import system
from colorama import Fore, Back, Style
import globals as g
import oaFileImport as o
import SummaryModule as s

extract = f.fileClass()

extract.openInput("051520_042420through051220_ins2.csv")
extract.fixAddress("addressFixed1.csv")
claims = extract.get()


currentAccession = claims.iloc[con.FIRST_ROW, con.ACCESSION_NUMBER]
claim = c.claimClass()
oaFile = o.oaFileClass()
summary = s.summaryClass()
claimList = []

singleRecord = True



for i in range(len(claims)):



    if claims.iloc[i, con.ACCESSION_NUMBER] == currentAccession:
        claim.addRow(claims.loc[i])


    else:
        claimList.append(claim)
        currentAccession = claims.iloc[i, con.ACCESSION_NUMBER]
        claim = c.claimClass()
        claim.addRow(claims.loc[i])
        singleRecord = False

        # last record, put it in list
        if i == len(claims) - 1:
           claimList.append(claim)

if singleRecord == True:
    claimList.append(claim)



summary.writeMast()

for claim in claimList:

    # claim.setMedicare()
    claim.checkForLab("LP2")
    claim.checkForLab("LP")
    claim.getDiagCodes()
    claim.loadPrices()
    #claim.setDaigCodes()
    oaFile.writeTestBlock(claim.rowList, claim.diagCodeList)
    summary.writeClaim(claim,claim.diagCodeList)

oaFile.closeOAFile()
summary.writePDF()