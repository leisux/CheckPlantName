# this script takes a list of plant names without authors and check them against the The Plant List
# it returns a list of the corresponding accepted name for the species in The Plant List including the author's name


def search_pl(genus, species):
    """
    take two strings (genus and species) as arguments and conduct a search on the plant list
    return a list of strings, which are the accepted species found in the plant list
    """

    # importing libraries BeautifulSoup and requests
    from bs4 import BeautifulSoup
    import requests

    # generate URL to search the plant list
    search_url = "http://www.theplantlist.org/tpl1.1/search?q="
    key1 = genus
    key2 = species
    search = search_url + key1 + "+" + key2

    # get the content from the URL generated and create soup object
    content = requests.get(search).content
    soup = BeautifulSoup(content, "lxml")

    # here the function look for Accepted names in two different type of page of The Plant List
    # page type 1: find all td elements in soup which have class name "name Accepted"
    accepted = soup.find_all("td" , class_ = "name Accepted")
    result = [ i.text for i in accepted]
    # page type2: find  the name of the species found
    #and select only results that are accepted named
    accepted2 = soup.find_all("h1")
    for i in accepted2:
        if "accepted" in i.text.encode('utf-8'):
            result.append(i.find("span", class_ = "name").text)

    # if it is a synonym extract the accepted name near the sentence "is a synonym of"
    if len(result) == 0:
        synonym = soup.find_all("span" , class_ = "subtitle")
        result = [i.text.replace("is a synonym\n of ", "") for i in synonym]
    return result

# ask for the name of the input csv file found in the same folder
# open and read input csv file with Genus name and species separated by a comma
# create a list of list object with each line is a list (species), which contain a list with genus and name strings

print "This program does the following:"
print "1) It takes an input file in csv format with a species'Genus and species name on each line "
print "for example: Zingiber, officinale"
print "2) It searches each plant name on The Plant List and retrieve the accepted name(s) for the species"
print "3) It generate an output csv file with the results for each species in each line"
print


fname = str(raw_input("enter the name of the input csv file (including .csv) -->"))

try:
    with open(fname , "r") as fn:
        species = []
        for line in fn:
            sp_name = line.split(",")
            sp_name[0] = sp_name[0].strip("\n").strip("\r")
            sp_name[1] = sp_name[1].strip("\n").strip("\r")
            species.append(sp_name)
    # create a list of list with the results of the search of accepted name on the plant list
    print "Checking plant names on The Plant List ..........."

    results = [search_pl(sp[0], sp[1]) for sp in species]
    print "Done"

    # next step aks the name of the output file and save output on a csv file add the .csv extension automatically
    outfile = str(raw_input("enter the name of the output file -->")) + ".csv"
    print "saving results..............."
    with open(outfile, "w") as outf:
        for sp in range(len(results)):
            outf.write(species[sp][0] + " " + species[sp][1])
            for x in range(len(results[sp])):
                outf.write(" " + "," + results[sp][x].encode('utf-8'))
            outf.write("\n")

    print "Done. You can find the output file " + outfile + " in the same folder of this script"
except:
    print "The file was not found!.....quitting the program "
