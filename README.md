# Big Data Federation, Inc.

## Q 1
### Investing Historical data extractor
A little command-line app to download historical data in CSV format from,
• https://www.investing.com/commodities/gold-historical-data
• https://www.investing.com/commodities/silver-historical-data


### Setup

```
git clone git@github.com:sriharshams/bigdatafederation.git
cd commodity-price-analysis
npm install
```

### Usage
To run the script,  use one of the following:
```
npm start -- <args>
node main.js <args>
```


### Available commands


      Commands:

        get [name|id]  get historical data
        help [cmd]     display help for [cmd]

      Options:

        -h, --help     output usage information
        -V, --version  output the version number


### get

Download historical data from [investing.com](http://www.investing.com/). By default, the result is printed to the console. Use `-f` if you want the csv te be saved directly into a file.

      Options:

        -h, --help             output usage information
        -V, --version          output the version number
        -i --id [id]           id of the commodity to fetch
        -s --startdate [date]  start date in MM/dd/yyyy format.
        -e --enddate [date]    end date in MM/dd/yyyy format.
        -f --file [file]       result file. If none, the result will be printed to the console.
        -v --verbose           enable verbose mode.


### Commodities

The program supports commodities from US for Gold and Silver.

### Run Q1 to get the data from investing.com
#### get gold commodity data
node main.js get -i 8830
#### get silver commodity data
node main.js get -i 8836

##### Past 10 year data of gold & silver is downloaded for answering Q2 / Q3 using below commands
##### get gold commodity data for past 10 yrs and save it in historical-gold.csv
node main.js get -i 8830 -s 03/01/2008 -e 03/01/2018 -v -f historical-gold.csv
##### get silver commodity data for past 10 yrs and save it in historical-silver.csv
node main.js get -i 8836 -s 03/01/2008 -e 03/01/2018 -v -f historical-silver.csv


## Q2
### Run following command to find mean, variance of gold / silver from saved file historical-gold.csv / historical-silver.csv
python getCommodityPrice.py 2017-05-01 2017-05-03 gold

## Q3
### Install

This project requires **Python 2.7**(if you complete this project in Python 3.x, you will have to update the code in various places including all relevant print statements) and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)

You will also need to have software installed to run and execute a [Jupyter Notebook](http://ipython.org/notebook.html)

If you do not have Python installed yet, it is highly recommended that you install the [Anaconda](http://continuum.io/downloads) distribution of Python, which already has the above packages and more included. Make sure that you select the Python 2.7 installer and not the Python 3.x installer.

### Code

Code is provided in the `commodities_data_query.ipynb` notebook file. Also be required to use the included `historical-gold.csv`, `historical-silver.csv` dataset file.

### Run

In a terminal or command window, navigate to the top-level project directory `commodity-price-analysis/` (that contains this README) and run one of the following commands:

```bash
ipython notebook commodities_data_query.ipynb
```  
or
```bash
jupyter notebook commodities_data_query.ipynb
```

This will open the Jupyter Notebook software and project file in your browser.
