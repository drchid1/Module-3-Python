# Module 3 - Python Challenge - Assigment Submission

Author : **Murali Chidambaram Veerabahu**

## Introduction

This assigment has two exercise called "PyBank" and "PyPoll". The task is to use python program to pull out the descriptive statistics from the respective CSV files and summarise the data in an simple output to the terminal and a text file. In class we learned the use of the OS module and CSV module in python. In my reaserch for this assigment I came accross slicker solutions using the Pandas module. I have used the Pandas module functions togther with fundamental coding concepts such as Loops and Conditionals.

Each project folder contains the python program named as **main.py**. The **Resources** folder contains the source data CSV file and the **Analysis** folder holds the final output file.

## PyBank

Most of the calculations were using standard python functions and the Pandas module. The Change in Profit/Losses was a more challenging calculation. The change was calculated and stored in new list. The new list was used to calculate the average change. The output file was printed to the terminal and writted to a text file.

## PyPoll

The *value_counts()* was used for its ability to count unique items to summarise the candiate's votes. This was stored in a list called *candidate_list*. This list was looped through to find the percentage votes. In the same loop a dictionary was created to store all the values of the summary data for each candidate. The loop also had a conditional to indentify the winning candidate.

The dictionary was used to output the summary and the final outout included the winning candidate.  For a change compared to the previous project a text file was created for the output and this was then opened to display the results in the terminal.

## Marking requirements

### Correctly Reads in the CSV (10 points)

*Reads in the CSVs for both PyBank and PyPoll using Python (5 points)*
*Successfully stores the header row (5 points)*

The CSV files was read using the Pandas Module and not the CSV module and hence header row was not stored as the data was in a dataframe. If the CSV module was used, like how we did in class the **Next** function: `headers = next(csv_reader)` would need to be used.

### Results Printed out to correctly to terminal (40 points)

*Results correctly display for PyBank:*
*Total Months (5 points)*
*Total (5 points)*
*Average Change (5 points)*
*Greatest Increase (5 points)*
*Greatest Decrease (5 points)*

*Results correctly display for PyPoll:*
*Total Votes (5 points)*
*Each candidate’s total votes and percent of votes (5 points)*
*Winner (5 points)*

The results have been printed to the terminal as per the assigment requirements and formatting.

### Code Runs Error Free (10 points)

*Error Free (5 points)*
*Producing consistent results (5 points)*

The code was initially developed in a Jupyter notebook to check each step of the code and if the data output was accurate. The code was then written in VS Code and executed to ensure it was working.

### Exports results to text file (30 points)

*The text file contains for PyBank:*
*Total Months (2.5 points)*
*Total (2.5 points)*
*Average Change (5 points)*
*Greatest Increase (5 points)*
*Greatest Decrease (5 points)*

*The text file contains for Pypoll:*
*Total Votes (2.5 points)*
*Each candidate’s total votes and percent of votes (2.5 points)*
*Winner (5 points)*

The output to the file was the same as the results on the terminal display.

### Code is cleaned and commented (10 points)

*Has additional tests and debugging removed (5 points)*
*Commented (5 points)*

As mentioned before the code was checked at each stage on a Jupyter notebook and debugged. It was also checked and debugged as a python file. The code has been indented, spaced and commented for an easier read.

~END~
