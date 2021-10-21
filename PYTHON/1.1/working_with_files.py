#variable
readOtherFile = False




def countLines():
    with open(fileName, 'r') as books:
        line_count = 0
        for book in books:
            line_count = line_count + 1
        print(line_count - 1)

def highestRankingNum(sentences):
    rankings = []
    for elements in sentences:
        rankings.append(elements["Rating"])
    max_ranking_num = max(rankings)
    return max_ranking_num

def highestRankingTitle(sentences,max_ranking_num):
    for elements in sentences:
        if elements['Rating'] == max_ranking_num:
            max_ranking_name = elements["Title"]
            return max_ranking_name

def lowestRankingNum(sentences):
    rankings = []
    for elements in sentences:
        rankings.append(elements["Rating"])
    min_ranking_num = min(rankings)
    return min_ranking_num

def averageRankingNum(sentences):
    rankingsString = []
    rankingsInt = []
    for elements in sentences:
        rankingsString.append(elements["Rating"])
        for i in rankingsString:
            i = float(i)
            rankingsInt.append(i)
    average = round(sum(rankingsInt) / len(rankingsInt), 2)
    return average

def searchKeyword(sentences,keyword):
    summaryList = []
    for elements in sentences:
        if keyword in elements["Caption"]:
            summaryList.append(elements["Caption"])
    length = len(summaryList)
    return length


def showResults(sentences, keyword):
    summaryList = []
    begin = 0
    end = 5
    i = 1
    #check for all the sentences that are the same under Caption
    for elements in sentences:
        if keyword in elements["Caption"]:
            summaryList.append(elements["Caption"])
    length = len(summaryList)
    while True:
        if end > length:
            listLength = length - begin
        else:
            listLength = end - begin
        print(f"Resultset {1} - {listLength}")
        while True:
            # check that the end is not bigger than the length of the list to avoid out of range error
            if end > length:
                end -= 1
                continue
            else:
                break
        #print the summary list books between the begin and end range
        for item in summaryList[begin:end]:
            print(str(i) + '.' + item)
            i += 1
        i = 1
        #put the right range when chosing to see the previous books
        previous = end - begin
        if previous < 5:
            previous = 5
        else:
            pass

        print("What do you want to do next? ")
        print(f"1. Previous {previous} results")
        if length - end >= previous:
            print(f"2. Next {previous} results")
            previousCount = True
        else:
            print(f"2. Next {length - end} results")
            lastCount = True
        print("3. Export results")
        print("0. Exit paging")
        user_next = input("PLease enter your choice: ")
        if user_next == "1":
            if previous == end:
                print("No previous to show")
            else:
                #this makes sure that the right previous books can be shown
                end = end - (end - begin)
                begin = end - previous
                while True:
                    if begin < 0:
                        begin += 1
                    else:
                        break

        elif user_next == "2":
            #if the last books are shown and the user choose next this message will be promt
            if length - end == 0:
                print("No more books to show!")
            else:
                #update the variables when next is clicked
                if previousCount == True:
                    begin += previous
                    end += previous

                elif lastCount == True:
                    begin += (length - end)
                    end += (length - end)
        #export the books to a text file
        elif user_next == "3":
            print("Your results are exported.")
            with open('results.txt', 'w') as f:
                for item in summaryList[begin:end]:
                        f.write(item)
                        f.write('\n')
        #stopn the game
        elif user_next == "0":
            break
        else:
            print("Invalid input")
            continue
print("*** Welcome to the book collection ***")
while True:
    sentences =[]
    fileName = input("Enter the name of the file containing your book (type 'exit' to quit the application):").lower()
    try:
        if fileName == "exit":
            break
        else:
            f = open(fileName, 'r')
            lines = f.readlines()
            f.close()
            for line in lines:
                line_list = line.replace("<","").split(">")
                sentences.append({"Ranking":line_list[0],"Title":line_list[1],"Caption":line_list[2],"Author":line_list[3],
                                  "Publication":line_list[4],"Rating":line_list[5],"Summary":line_list[6]})
            sentences.pop(0)
            print("Reading contents....")
            countLines()
            print(f"Book with the highest rating ({highestRankingNum(sentences)}) is '{highestRankingTitle(sentences,highestRankingNum(sentences))}'.")
            print(f"The lowest rating is '{lowestRankingNum(sentences)}'")
            print(f"The average rating is {averageRankingNum(sentences)}.")
            print("What do you want to do next?")
            print("1. search through the catalog")
            print("2. Read another file")
            while True:
                if readOtherFile == False:
                    user = input("Please enter your choice: ")
                else:
                    break
                if user == "1":
                    while True:
                        lookUpKeyword = input("search keyword: ")
                        if searchKeyword(sentences,lookUpKeyword) == 0 or lookUpKeyword.isdigit():
                            print("Input is invalid try again!")
                            continue
                        else:
                            print(f"Found {searchKeyword(sentences, lookUpKeyword)} books.")
                            showResults(sentences,lookUpKeyword)
                            readOtherFile = True
                            sentences.clear()
                            break
                elif user == "2":
                    f.close()
                    break
            continue
    except FileNotFoundError:
        fileName = input("File does not exist. Please try again (type 'exit' to quit the application):")



