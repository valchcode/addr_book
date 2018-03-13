def vvod(text):
    if text=='S':
        nameaddrs = input('\nВведите имя контакта --> ')
        searchname (nameaddrs)
    elif text=='A':
        addname = input('\nВведите имя контакта --> ')
        addphone = input('\nВведите телефон контакта --> ')
        addaddrs = input('\nВведите адрес контакта --> ')
        addrs[addname] = [addphone, addaddrs]
        add2file = open('addrbook.txt', 'a+')
        mylist = [addname, addphone, addaddrs, '\n']
        delimiter = '---'
        mylist = (delimiter.join(mylist))
        mylist = mylist [:-4] + mylist [-1:]
        add2file.write(mylist)
        add2file.close
        print ("\n Контакт добавлен в адресную книгу")
    elif text=='P':
        for name, address in addrs.items():
            print('\nИмя: {0}, тел. и адрес: {1}'.format(name, address))
    elif text=='DEL':
        #addrs
        nameaddrs = input('\nВведите имя удаляемого контакта --> ')
        if nameaddrs in addrs:
            addrs.pop(nameaddrs)
            print ("\n Контакт удален из адресной книги")
            with open ('addrbook.txt','w') as i:
                for key, val in addrs.items():
                    i.write('{}---{}\n'.format(key,'---'.join(val)))
        else:
            print ("\n Такого контакта нет")    
    elif text=='EXIT':
        return
    else:
        print ("\n Неправильный ввод, попробуйте еще раз")
    print ("\n поиск контакта - 'S'\n добавление контакта - 'A'\n показать все контакты - 'P'\n удаление контакта - 'DEL'\n выход - 'EXIT'\n")
    text = input('Введите что-нибудь --> ')
    vvod(text)
    
def searchname (nameaddrs):
    if nameaddrs in addrs:
        print ("\nТел. и адрес:", addrs[nameaddrs])
    else:
        print ("\n Такого контакта нет")
        
addrs = dict()
for line in open('addrbook.txt'):
    line = line.split('\n') # из строки получаем список
    line = line[0] # избавляемся от последнего элемента (\n)
    line = line.split('---', maxsplit=2) # разделяем данные
    addrs[line[0]] = line[1:]
    
#addrs['Paul'] = ['095', 'ул. Крещатик, 3']
#addrs['Ivan'] = ['093', 'ул. Ивана Франка, 1/8']
#addrs['Igor Petrovich'] = ['098', 'пр-т. Петлюры, 4-5']

print ("\n Добро пожаловать в программу 'Адресная книга'\n для поиска контакта введите 'S'\n для добавления контакта введите 'A'\n для вывода всех контактов введите 'P'\n для удаления контакта введите 'DEL'\n для выхода из программы введите 'EXIT'\n")
text = input('Введите что-нибудь --> ')
vvod (text)