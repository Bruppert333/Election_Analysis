# Election Analysis

## Project Overview
The purpose of this election analysis is to extract data from the election_results.csv file. The CSV file holds over 300,000 lines of data and our job is to break it down to see the following:
* The total votes casted
* What counties the votes came from
* The percentage and votes casted per county
* What county had the largest turnout
* The candidates that ran in the election 
* The percentage and votes the candidates received
* The winner of the election

## Resources
Data source: election_results.csv <br/>
Progam: Python 3.7 and Visual Studio Code

## Election-Audit Results
* How many voters were cast in this congressional election? 
    * 369,711
* Provide a breakdown of the number of votes and the percentage of toal votes for each county in the precinct.
    * Jefferson: 10.5% (38,855)
    * Denver: 82.8% (306,055)
    * Arapahoe: 6.7% (24,801)
* Which county had the largest number of votes?
    * Denver
* Provide a breakdown of the number of votes and the percentage of the toal votes each candidate received.
    * Charles Casper Stockham: 23.0% (85,213)
    * Diana Degette: 73.8% (272,892)
    * Raymon Anthony Doane: 3.1% (11,606)
* Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
    * The winner of the election was Diana Degette who received 272,892 votes which is 73.8% of the total votes casted. <br/>
Deliverable 1. <br/>
![deliverable_1](Resources/deliverable_1.png)

Deliverable 2. <br/>
![deliverable_2](Resources/deliverable_2.png) <br/>
I was able to post the results in the terminal by using the print() command. To get the results into the text file you need to use the .write command. <br/>
![example_print](Resources/example_print.png) 

## Election Audit Summary
This script can be used for any election because it will list out the total votes, who the votes were for, and what county the vote came from. It is a repetitive script when it comes to how to get county votes and candidate votes. An example of modifying the script would be if the order of the data was different. For example, if the county was listed after the candidate we would simply change the row[] number to accomdidate that difference. 

