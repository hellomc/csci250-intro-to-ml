"""
@Author:    Michelle Adea

Analyzes stock information from NASDAQ to create a csv file,
to search the csv file for a specific stock, and to identify
the top 15 companies with the highest market cap.

'Input Args'
link_Nasdaq = "https://old.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download"
link_Nyse = "https://old.nasdaq.com/screening/companies-by-industry.aspx?exchange=NYSE&render=download"
link_Amex = "https://old.nasdaq.com/screening/companies-by-industry.aspx?exchange=AMEX&render=download"

'Output Args'
fileOut = "Adea_Assignment3_out.csv"
"""

from urllib import request
import sys

def displayMenu():
    """
    Prints out the Display Menu for the Stocks Data Analyzer.
    """
    print("****************************")
    print("Adea's Company List Data Analyzer")
    print("1) Export to merged/sorted (by stock symbol) CSV file")
    print("2) Search by stock symbol")
    print("3) Display 15 companies with the highest MarketCap value")
    print("4) Exit")
    print("****************************")

def optionIn():
    """
    Prompts user to input a choice between 1-4 and checks value.
    """
    while True:
        try:
            optionNum = input("Please choose one of the above options 1-4: ")
            if int(optionNum in range(1, 5)):
                break
            return optionNum
        except ValueError:
            print("Invalid Option. Enter 1-4!")

def process(option):
    """
    Checks the user input for the value and continues stock analysis.

    Parameters
    ----------
    option : string of a number from 1 to 4

    """
    all_stocks = {}

    if option == "1":
        exportStocks()
        #all_stocks = createDict()
    elif option == "2":
        all_stocks = createDict()
        searchStocks(all_stocks)
    elif option == "3":
        all_stocks = createDict()
        displayHighMarketCap(all_stocks)
    elif option == "4":
        sys.exit("End of Analyzer Program")

def readIn(filenameIn):
    """
    Reads in a file from the Internet and creates a list.
    """
    stocks = {}
    
    with request.urlopen(filenameIn) as fIn:
        header = fIn.readline()
        for line in fIn:
            line = line.decode("utf-8")
            newline = line.replace('","', '###')
            newline = line.replace('"', '')
            newSplit = newline.split("###")
            stocks[newSplit[0]] = [info for info in newSplit]
    
    #stocks = sorted(stocks.keys())
    
    return stocks

def exportStocks():
    """
    Prompts the user to name the file for the merged and sorted stocks,
    and to enter links for downloading the input files.

    Takes all the information from the input files and stores into a list
    that is sorted by the stock symbol and printed out to the output file.

    Returns
    -------
    newFile
        name of the file with complete information from multiple file inputs
    """
    list_allStocks = []
    
    newFile = input("Name your file: ")
    with open(newFile, "w+") as f:
        f.write('Symbol,Name,LastSale,MarketCap,ADR TSO,IPOyear,Sector,Industry,Summary Quote,\n')

    while True:
        try:
            option = input("Would you like to enter a link? Y/N\n")
            if option == "Y":
                link = input("Enter a link: ")
                dict_In = readIn(link)
                list_allStocks += dict_In
            elif option == "N":
                list_allStocks = sorted(list_allStocks)
                with open(newFile, "a+") as fOut:
                    for stock in list_allStocks:
                        fOut.write('%s' % stock)
                #with open(newFile, "r") as fOut:
                    #if fOut.mode == "r":
                        #text = fOut.read()
                        #print(text)
                print("%s%s" % ("All stock information can be found in: ", newFile))
                break
        except ValueError:
            print("Invalid Input. Y or N?\n")

def createDict():
    """
    Creates a dictionary from a given file.

    Returns
    -------
    dict_stocks
        dictionary with key-value pair of
        {stock symbol: (all other stock information)}

    """
    
    dict_stocks = {}

    inFile = input("Name your file: ")
    with open(inFile, "r") as f:
        header = f.readline()
        for line in f:
            line = line.replace(', ', '|')
            line = line.replace(',', '###')
            line = line.replace('|', ', ')
            newline = line.split('###')
            dict_stocks[newline[0]] = [item for item in newline]
    
    return dict_stocks

def searchStocks(mydict):
    """
    Prompts user to enter a stock symbol and performs search
    for that stock symbol in dictionary.

    Parameters
    ----------
    mydict : dictionary with key-value pair of
             {stock symbol: (all other stock information)}

    """

    stockSymbol = input("Search for this stock symbol: ")
    stockSymbol = stockSymbol.upper()
    
    if stockSymbol in mydict:
        stockInfo = mydict.get(stockSymbol)
        print("%-10s%-40s%-25s%-10s%-25s%-50s" % ("Symbol", "Name", "MarketCap", "IPOyear", "Sector", "Industry"))
        print("%-10s%-40s%-25s%-10s%-25s%-50s" % (stockInfo[0], stockInfo[1], stockInfo[3], stockInfo[5], stockInfo[6], stockInfo[7]))
    else:
        print("Stock Symbol Not Found")


def displayHighMarketCap(mydict):
    """
    Identifies the top 15 performing stocks based on MarketCap
    and displays to terminal.
    """

    highCapStock = {}
    highCapStock = sorted(mydict.items(), key = lambda x:float(x[1][3]), reverse=True)[0:15]
    
    print("%-7s%-10s%-40s%-25s%-10s%-25s%-50s" % ("Rank","Symbol", "Name", "MarketCap", "IPOyear", "Sector", "Industry"))
    rank = 1
    for key, value in highCapStock:
        print("%-7s%-10s%-40s%-25s%-10s%-25s%-50s" % (rank, value[0], value[1], value[3], value[5], value[6], value[7]))
        rank += 1

def stockAnalyzer():
    while True:
        try:
            displayMenu()
            choice = optionIn()
            process(choice)
        except ValueError:
            print("Invalid Input. Options are 1-4")

stockAnalyzer()
