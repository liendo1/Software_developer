contact = {'Alice': {'home': '123'}, 'Bob': {'work': '06 321 654 87'}, 'Charlie': {'home': '06 876 543 21', 'work': '088 019 8888'}}


numSearch = '06 321 654 87'
numSearch = numSearch.replace(' ','')
if ' ' in numSearch:
    for names, values in contact.items():
        if numSearch == values.values():
            print(f"Found: '{names}'", end='')
            for info, phnumber in values.items():
                print(f", {info}: '{phnumber}'", end='')
elif not ' ' in numSearch:
    for names, values in contact.items():
        for info, phnumber in values.items():
            if numSearch == phnumber.replace(' ', ''):
                print(f"Found: '{names}'", end='')
                for info, phnumber in values.items():
                    print(f", {info}: '{phnumber}'", end='')







#if not ' ' in name:
   # print('not tin spacio')
#else:
  #  print('tin spacio')