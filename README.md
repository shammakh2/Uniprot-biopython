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
If you want to see the average protein length of different taxonomy levels, you can use the command below to have the
 data in form of a barchart. To do so, use the command:
 
    pipenv run python uniplot.py plot-taxa
    
This command will present the top-most level of taxonomy(i.e the Domain level) and the count of records in each in the
 form of a graph; however, to display by different levels the command above can be
 augmented with `--depth <Level of Taxonomy> ` so if you wanted to display the second level taxonomy the command may 
 look like
 
    pipenv run python uniplot.py plot-taxa --depth 2
    
 ***Note:** Depth 1 is  the highest level and higher values will give lower levels of taxonomy


To see the number of records by the level of taxonomy you can display the data as a pie chart which will give the
 number of records and percentage in the database with `--pie 1` like so
 
 ***Note:** the pie chart argument can be used with the depth argument in the command.*
 
    pipenv run python uniplot.py plot-taxa --depth 2 --pie 1 (1 = True)


***Note**: These processes will take longer for larger data files as a the program has to load the data*
