# Python module for fetching URLs
from urllib import request

class Stock:
  index = 0

  def __init__(self, symbol, name, lastSale, marketCap, ipoYear, sector, industry):
    self.symbol = symbol
    self.name = name
    self.lastSale = lastSale
    self.marketCap = marketCap
    self.ipoYear = ipoYear
    self.sector = sector
    self.industry = industry
  
  def display(self):
    return("%-8s*****%-10s*****%-10s*****%-10s*****%-10s*****%-10s*****%-10s" % (self.symbol, self.name, self.lastSale, self.marketCap, self.ipoYear, self.sector, self.industry))

# Define a function that reads in a file from the Internet and produces a csv file
def readIn(filenameIn, filenameOut):
    fIn = request.urlopen(filenameIn)
    fOut = open(filenameOut, "a+")
    # read in one line at a time from file and write to new file
    for line in fIn:
        # line is a placeholder
        line = fIn.readline()
        # text uses utf-8 encoding
        decoded = line.decode("utf-8")
        # original delimiter is '","' replace with "###"
        decoded = decoded.replace('", "', "###")
        # splitText produces a list of items in decoded
        splitText = decoded.split("###")
        # only want certain fields from splitText
        splitTextNew = splitText[:4] + splitText[5:8]
        # splitText looks like ['"TXG', '10x Genomics, Inc.', '62', '5818678920', 'n/a', '2019', 'Capital Goods', 'Biotechnology: Laboratory Analytical Instruments', 'https://old.nasdaq.com/symbol/txg",\r\n']
        #checking info
        print(splitTextNew[:4] + splitText[5:8])
        # print items from splitTextNew to csvfile
        for ii in splitTextNew:
            fOut.write(ii + ', ')
    fOut.close()
    return fOut

# Concatenate the files together, and sort the information
link_Nasdaq = "https://old.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download"
link_Nyse = "https://old.nasdaq.com/screening/companies-by-industry.aspx?exchange=NYSE&render=download"
link_Amex = "https://old.nasdaq.com/screening/companies-by-industry.aspx?exchange=AMEX&render=download"
fileOut = "All_Stocks.csv"

# Create menu
def displayMenu():
    print("****************************")
    print("Adea's Company List Data Analyzer")
    print("1) Export to merged/sorted (by stock symbol) CSV file")
    print("2) Search by stock symbol")
    print("3) Display 15 companies with the highest MarketCap value")
    print("4) Exit")
    print("****************************")

def optionIn():
    while True:
        try:
            optionNum = input("Please choose one of the above options 1-4: ")
            if int(optionNum in range(1, 5)):
                break
        except ValueError:
            print("Invalid Option. Enter 1-4!")
        return optionNum

def process(option):
    if option == "1":
        #operation exportStocks
        print(exportStocks())
    #elif option == "2":
        #operation searchStocks
    #elif option == "3":
        #operation displayHighMarketCap
    #elif option == "4":
        #sys.exit include sys library

def exportStocks():
  # name your csv file
  newFile = input("Name your file: ")
  f = open(newFile, "w+")
  f.write('"Symbol","Name","LastSale","MarketCap","IPOyear","Sector","Industry"\n')
  f.close()
  while True:
    try:
        # checks if user has input data
        option = input("Would you like to enter a link? Y/N\n")
        if option == "Y":
            # prompts user to input link for input data
            link = input("Enter a link: ")
            #process with readIn function
            readIn(link, newFile)
        elif option == "N":
            # opens up the file in read mode and prints all text
            f = open(newFile, "r")
            if f.mode == "r":
                text = f.read()
                print(text) # open up new file
            f.close()
            break
    except ValueError:
        print("Invalid Input. Y or N?\n")
        
  
  # append to file the additional information read in
"""
def searchStocks():

def displayHighMarketCap():
"""

displayMenu()
choice = optionIn()
process(choice)
