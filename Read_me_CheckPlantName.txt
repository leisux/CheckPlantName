************ CheckPLantName ********************************************************************
* code by Peter Giovannini :                 wwww.petergiovannini.com                            *
* License: GNU General Public License v3.0 : https://www.gnu.org/licenses/gpl-3.0.en.html        *                                                                      *"
* Source code shared on github:              https://github.com/petergpython                     *
**************************************************************************************************


This code runs on python 2.7

it assumes you have the following python libraries installed on your machine:
 a) requests
 b) BeautifulSoup


This code does the following:
1) It takes an input file in csv format with a species' Genus and species' name on each line separated by a comma.
 for example: Zingiber, officinale.
 If you want to search for the accepted names of all species in a Genus, on the input file put a line with the genus followed by a comma.
 for example: Zingiber,

2) It searches each plant name on the website www.ThePlantList.org and it retrieves the accepted name(s) for the species.

3) It generate an output csv file with the results for each species in each line."
  When the input is only a Genus name the output will be a list of all the accepted species in that genus.



 Notes:
!! the software works only if you are connected to internet as it needs to access www.ThePlantList.org   !!
!! the input file needs to be in the same folder where the program was launched

Known limitations:
some special characters (for example some type of accents) may not be correct in the generated output
