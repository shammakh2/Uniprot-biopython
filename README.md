<H1>CSC1034: Practical 2</H1>

This package allows analysis and display of proteins and their information from Uniprot .xml format.
It comes with a few key functions that allow dispensing and manipulation of data.

<h4> -Functionality </h4>

<h5>🚩1. Setting up Uniprot file location</h5>
To be able to parse data from your GNU zipped uniprot .xml file and analyse it, you need to specify the file location.
This can be done in 2 ways:
<h6>a. Saving file location</h6>
The`location` command allows you to pass in a file location which will be saved and you can follow up on it with other
commands without needing to type the file location repeatedly. The command is
    
    python uniplot.py location < enter file location >

***Note:** This command only stores one location.*
<h6>b. Temporary file location </h6>
If you want to temporarily switch to another file for processing, you can use the `--loco` command to pass a
file location argument. 

    python uniplot.py --loco <insert file_location> [Further processing options such as dump,list,etc.]  
    
***Note:** Temporary location takes priority*

<h5>🚩2. Complete Data output </h5>
One of the central features of this program is output of data. You can do this by using this command:

    python uniplot.py dump

<h5>🚩3. Output of protein name list </h2>
You can also output a list of names of the protein sequences and their origin which is done using the following command:

    python uniplot.py list
    
<h5>🚩4. Average length of the proteins</h5>
The following command can be used to find the average length of all the protein sequences in the database:

    python uniplot.py average

<h5>🚩5. Representing Data using charts </h5>
<h6>a. Display average as a graph</h6>
If you want to see the average protein length of different taxonomy levels, you can use the command below to have the
 data in form of a bar chart. To do so, use the command:
 
    python uniplot.py plot-taxa
    
This command will present the top-most level of taxonomy(i.e the Domain level) with average sequence length in form the 
of a graph; however, to display different levels the command above can be
 augmented with `--depth <Level of Taxonomy> ` so if you wanted to display the second level taxonomy the command may 
 look like:
 
    python uniplot.py plot-taxa --depth 2
    
***Note:** Depth 1 is  the highest level (and also the default) and higher values will give lower levels of taxonomy*


You can also get the average length of the protein sequence by the level of taxonomy as a pie chart, which will give the
 number of records and percentage in the database, with `--pie 1` like so:
 
    python uniplot.py plot-taxa --depth 2 --pie 1 (1 = True)
    
***Note:** the pie chart argument can be used with the depth argument in the command.*
    
<h6>b. Display the number of proteins for each taxonomic category</h6>
You can also display the number of records in taxonomic categories of different levels in the form of a pie chart.
Use the command and also pass a (optional) depth argument `--depth <level>` (default is 1)

    python uniplot.py pie --depth 1

***Note**: These processes will take longer for larger data files as a the program has to load the data* 🕝 🕒 🕞

<h4> -Improvements </h4>

* :sparkles: Better and more informative help menu ✔
* Detailed `README.md` ✔
* Storing file location for further processing ✔
* Bar graph and pie chart showing average length of protein sequence ✔
* Pie chart showing number of proteins per taxonomy ✔

    
    

