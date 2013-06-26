'''
Created on 26 Jun 2013

@author: Will Usher

Reads the OSeMOSYS .csv file into a python data structure


'''

import csv
import matplotlib.pyplot as plt
import itertools

def readfile(filename,tablename):
    
    with open(filename,'rb') as csvfile:
        datareader = csv.reader(csvfile,dialect='excel')
        
        for row in datareader:
    #       Identify capacity table
            if row[0] == tablename:
    #        Return list of headers
                startline = datareader.line_num
                title = row[0]
                headers = datareader.next()
                data = []
                print title
                print headers
                for row in datareader:
                    if row[0] == '':
                        endline = datareader.line_num
                        break
                    print row
                    data.append(row)
        print 'Started at ' + str(startline) + ' and finished at ' + str(endline)
        return reshape_data(headers,data)

def reshape_data(headers, data):
    '''Reshapes chart data received in list of headers and data rows
    Input: 
        headers:     1-by-x list of headers
        data:        y-by-x list of data rows
    Output:
        reshaped:    y+1-by-x list of lists of data with headers in [0]
    '''
    reshaped = [['Year']]
    for column in headers:
        if (column != ''):
            reshaped.append([column])
    
    for row in data:
        for i,column in enumerate(row):
            if (column != ''):
                reshaped[i].append(float(column))
                
    return reshaped

def plot_stacked_bar(data,tablename):
    
    p = []
    headerlist = []
    colors = itertools.cycle(['y', 'g', 'r', 'c', 'm', 'b', 'k'])
    xaxis = data[0][1:]
    
    for i,row in enumerate(data[1:]):
    #       Get the value of the previous entry to fill in the bottom parameter
        if (i >= 1):
            bottom = data[i][1:]
        else:
            bottom = 0
    #       Add the plot to the list of plots
        p.append( plt.bar(xaxis,row[1:],bottom=bottom,color=colors.next()))
        headerlist.append(row[0])
        
    #   Build legend
    plt.legend( (p), (headerlist) )
    plt.title(tablename)
    plt.show()

def main():
    
    filename = 'SelectedResults_Zv39.csv'
    tablename = 'TotalAnnualCapacity (Capacity Units)'
    
    plottabledata = readfile(filename,tablename)
    print 'Finished reading in file'
    
    plot_stacked_bar(plottabledata,tablename)
    
    #===========================================================================
    # Plot the chart
    #===========================================================================
    
    
main()

# plt.legend( (p1[0], p2[0]), ('Men', 'Women') )
