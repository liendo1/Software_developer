contact = {
    'Alice': {'home': '06 123 456 78'},
    'Bob': {'work': '06 321 654 87'},
    'Charlie': {'home': '06 876 543 21', 'work': '088 019 8888'}
}
number = '068765432'
lista = []
for key in contact:
    for secondarykey in contact[key]:
        if contact[key][secondarykey].replace(' ', '') == number.replace(' ',''):
            name = key
            type = secondarykey
            number = contact[key][secondarykey]
            print(name,end=', ')
            lista.append(name)

if len(lista) == 0:
    print(f'nothing found for {number}')

else:
    for names in contact:
       if name == names:
            for info in contact[names]:
                print(info, contact[names][info],end=' ')



