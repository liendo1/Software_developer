def addBooksToList(sentences):
    rankingsList = []
    for elements in sentences:
        rankingsList.append(elements["Rating"])
    rankingsList = list(map(float, rankingsList))
    return rankingsList


def highestRankingNumber(rankingsList):
    max_ranking_num = max(rankingsList)
    return max_ranking_num

def highestRankingTitle(sentences, max_ranking_num):
    max_ranking_num = str(max_ranking_num)
    for elements in sentences:
        if elements['Rating'] == max_ranking_num:
            max_ranking_name = elements["Title"]
            return max_ranking_name

def lowestRankingNumber(rankingsList):
    min_ranking_num = min(rankingsList)
    return min_ranking_num

def averageRankingNumber(rankingsList):
    average = round(sum(rankingsList) / len(rankingsList),2)
    return average

def searchKeyWord(sentences,keyword):
    summaryList = []
    for elements in sentences:
        if keyword in elements["Summary"]:
            summaryList.append(elements["Summary"])
    length = len(summaryList)
    return length

def showResults(sentences, keyword):
    summaryList = []
    for elements in sentences:
        if keyword in elements["Summary"]:
            summaryList.append(elements["Summary"])
    print(f"Found {len(summaryList)} books.")
    indexStart = 0
    pageSize = 5
    indexEnd = indexStart + pageSize
    number = 1
    nextOption = len(summaryList) - indexEnd
    if nextOption > 5 :
        nextOption = 5
    else:
        nextOption = len(summaryList) - indexEnd
    while True:

        print(f"Resultset {indexStart+1} - {indexEnd}")
        for book in summaryList[indexStart:indexEnd]:
            print(f"{number}. {book}")
            number += 1
        print("What do you want to do next?")
        print("1. Previous 5 results")
        print(f"2. Next {nextOption} results")
        print("3. Export results")
        print("0. Exit paging")
        navigateChoice = input("Please enter your choice: ")
        if navigateChoice == "1":
            if indexStart == 0 or (indexStart - pageSize) < 0:
                print("No previous information to show")
                continue
            else:
                indexEnd = indexEnd - (indexEnd - indexStart)
                indexStart = indexStart - pageSize
                number = indexStart+1
                continue
        elif navigateChoice == "2":
            if indexEnd == len(summaryList):
                print("No next information to show")
                continue
            elif indexEnd + pageSize > len(summaryList):
                if (len(summaryList) - (indexEnd + pageSize)) < 0:
                    indexStart = indexStart + pageSize
                    indexEnd = len(summaryList)
                    number = indexStart+1
                    continue
            else:
                indexStart = indexStart + pageSize
                indexEnd = indexEnd + indexStart
                number = indexStart+1
                continue
        elif navigateChoice == "3":
            print("Your results are exported.")
            with open('results.txt', 'w') as f:
                for item in summaryList[indexStart:indexEnd]:
                    for phrases in sentences:
                        if item == phrases["Summary"]:
                            f.write(f"<{phrases['Ranking']}><{phrases['Title']}><{phrases['Caption']}><{phrases['Author']}><{phrases['Publication']}><{phrases['Rating']}><{phrases['Summary']}>")
                            f.write('\n')
        elif navigateChoice == "0":
            break
def main():
    Start = True
    print("*** Welcome to the book collection *** ")
    while Start == True:
        sentences = []
        fileName = input("Enter the name of the file containing your book (type 'exit' to quit the application): ").lower()
        #fileName ="hack.catalog"
        try:
            if fileName == "exit":
                break
            else:
                f = open(fileName,'r')
                lines = f.readlines()
                f.close()
                for line in lines:
                    line_list = line.replace("<","").split(">")
                    sentences.append({"Ranking":line_list[0],"Title":line_list[1],"Caption":line_list[2],"Author":line_list[3],"Publication":line_list[4],"Rating":line_list[5],"Summary":line_list[6]})
                print("Reading contents.....")
                print(f"Read {len(sentences)} books.")
                print(f"Book with the highest rating ({highestRankingNumber(addBooksToList(sentences))}) is is '{highestRankingTitle(sentences,highestRankingNumber(addBooksToList(sentences)))}'.")
                print(f"The lowest rating is '{lowestRankingNumber(addBooksToList(sentences))}'")
                print(f"The average rating is {averageRankingNumber(addBooksToList(sentences))}.")
                while True:
                    print(f"What do you want to do next?")
                    print("1. Search through the catalog")
                    print("2. Read another file")
                    user = input("Please enter your choice: ")
                    if user == "1":
                        while True:
                            lookUpKeyword = input("Search keyword: ")
                            if searchKeyWord(sentences,lookUpKeyword) == 0 or lookUpKeyword.isdigit():
                                print("Input is invalid try again")
                                continue
                            else:
                                showResults(sentences,lookUpKeyword)
                                break
                    elif user == "2":
                        break
        except FileNotFoundError:
            continue


if __name__== "__main__":
    main()