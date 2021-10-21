import ast

sentences = []

with open('books_hacking.catalog','r') as file:
    lines = file.readlines()
    for line in lines:
        line_list = line.replace("<","").split(">")
        sentences.append({"Ranking":line_list[0], "Title":line_list[1], "Caption":line_list[2], "Author":line_list[3], "Publication":line_list[4], "Rating":line_list[5], "Summary":line_list[6]})


rankings = []
titles = []
def searchKeyword(sentences,keyword="Linux"):
    summaryList = []
    for elements in sentences:
        if keyword in elements["Caption"]:
            summaryList.append(elements["Caption"])
    length = len(summaryList)

    return length
searchKeyword(sentences)

def showResults(sentences,keyword="Linux"):
    summaryList = []
    begin = 0
    end = 5
    i = 1
    for elements in sentences:
        if keyword in elements["Caption"]:
            summaryList.append(elements["Caption"])
    length = len(summaryList)

    while True:
        if (end > length):
            listLength = length-begin;
        else:
            listLength = end-begin


        print(f"Resultset {1} - {listLength}")
        while True:
            if end > length:
                end -= 1
                continue
            else:
                break
        for item in summaryList[begin:end]:
            print(str(i) + '.'+item)

            i += 1
        i = 1
        previous = end-begin
        if previous < 5:
            previous = 5
        else:
            pass

        print("What do you want to do next? ")
        print(f"1. Previous {previous} results")
        if (length - end) >= previous:
            print(f"2. Next {previous} results")
            previousCount = True
        else:
            print(f"2. Next {length-end} results")
            lastCount = True
        print("3. Export results")
        print("0. Exit paging")
        user_next = input("PLease enter your choice: ")
        if user_next == "1":
               if previous == end:
                   print("No previous to show")

               else:
                   end = end - (end - begin )
                   begin = end - previous
                   while True:
                       if begin < 0:
                           begin += 1
                       else:
                           break

        elif user_next == "2":
            if previousCount == True:
                begin += previous
                end += previous

            elif lastCount == True:
                begin += (length-end)
                end += (length-end)

        elif user_next == "3":
            print("Your results are exported.")
            with open('results.txt','w') as f:
                for item in summaryList[begin:end]:
                        f.write(item)
                        f.write('\n')

