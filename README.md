# python-challenge

Here is a description of two python scripts each called ``main.py`` contained in each of the two folders in this repository.  A description of the first is under the [PyBank](PyBank) heading and the second under [PyPoll](PyPoll).  

## PyBank

Expects to read a csv file named ``budget_data.csv`` in ``..Resources`` subfolder.  The input file should have the following format.

| Date   | Profit/Losses |
|--------|---------------|
| Jan-10 | 867884        |
| Feb-10 | 984655        |
| Mar-10 | 322013        |

Output is written to the screen and to the file [results.txt](PyBank/results.txt).  The file contents are below.

```text
Financial Analysis 
 ----------------------------
Total Months: 86
Total: $38,382,578
Average Change:  -2,315.12
Greatest Increase in Profits:  Feb-2012 ($1,926,159)
Greatest Decrease in Profits:  Sep-2013 ($-2,196,167)
```

In the above table, ``Total`` represents the sum of the values in the Profit/Losses column, ``Average Change`` is the average difference of ``Profit/Loss`` between consecutive months, and ``Greatest Increase in Profits`` and ``Greatest Decrease in Profits`` are the maximum and minimum of the differences of consecutive months Profit/Loss, respectively.

## PyPoll

Expects to read a csv file named ``election_data.csv`` in ``..Resources`` subfolder.  Each line identifies a voter, the county where they cast their vote, and their chosen candidate.  The input file should have the following format.

| Voter ID | County | Candidate |
|----------|--------|-----------|
| 12864552 | Marsh  | Khan      |
| 17775191 | Queen  | Correy    |
| 14003692 | Marsh  | Khan      |

The results of the election are written to the screen and to the file [results.txt](PyPoll/results.txt).  Some extra analysis is done county-by-county and that output is put into a table.

```text
Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231) votes.
Correy: 20.000% (704200) votes.
Li: 14.000% (492940) votes.
O'Tooley: 3.000% (105630) votes.
-------------------------
Khan
-------------------------

County-by-county Election Results
--------------------------------------------------------
          |  Correy  |    Khan   |    Li    | O'Tooley |
--------------------------------------------------------
|  Bamoo  | 20.006%  |  63.051%  | 13.950%  |  2.992%  |
|         | (69752)  |  (219834) | (48639)  | (10433)  |
--------------------------------------------------------
|  Marsh  | 19.992%  |  62.982%  | 14.018%  |  3.008%  |
|         | (453015) | (1427142) | (317651) | (68149)  |
--------------------------------------------------------
|  Queen  | 20.016%  |  63.037%  | 13.956%  |  2.991%  |
|         | (139554) |  (439494) | (97305)  | (20850)  |
--------------------------------------------------------
|  Raffah | 20.136%  |  62.948%  | 13.966%  |  2.950%  |
|         | (21055)  |  (65822)  | (14604)  |  (3085)  |
--------------------------------------------------------
| Trandee | 19.905%  |  63.029%  | 14.090%  |  2.976%  |
|         | (20824)  |  (65939)  | (14741)  |  (3113)  |
--------------------------------------------------------
```