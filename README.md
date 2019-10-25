<H1>CSC1034: Practical 2</H1>


This package allows analysis and display of proteins and information about them from Uniprot database in xml format.
It comes with a few key functions that allow dispensing and manipulation of data.

<h5>1. Complete Data output </h5>
One of the central features of this program is output of data. You can do this by using this command:

    pipenv run python uniplot.py dump

<h5>2. Output of protein name list </h2>
You can also output a list of names of the protein sequences and their origin which is done using the following command:

    pipenv run python uniplot.py list
    
<h5>3. Average length of the proteins</h5>
The following command can be used to find the average length of all the protein sequences in the database

    pipenv run python uniplot.py average

<h5>4. Representing Data using charts </h5>
If you want to see the average protein length of different taxanomy levels, you can use the command below to have the data in form of a barchart
 

***Note**: These processes will take longer for larger data files as a the program has to load the data*
