import vk
import time

def req_func(off, pep, wom):
    req = api.groups.getMembers(group_id = '', offset = off, fields = ['sex', 'bdate','city'], count = pep)
    req = req['users']
    countWoman = wom

    for i in req:
        if "deactivated" in i:
            pass
        else:
            if i['sex'] == 1:
                if "city" in i:
                    if i['city'] == 4757:
                        print("___________________")
                        print("Павловский Посад")
                        if 'bdate' in i:
                            length =len(i['bdate'])
                            if length > 5:
                                bdate = i['bdate']
                                int_bdate = bdate[length-4:length]
                                print(2016 - int(int_bdate))
                        print(i['first_name'], i['last_name'], sep=' ')
                        print("https://vk.com/id", i['uid'], sep='')
                    else:
                        if i['city'] == 1:
                            print("___________________")
                            print("Москва")
                            if 'bdate' in i:
                                length =len(i['bdate'])
                                if length > 5:
                                    bdate = i['bdate']
                                    int_bdate = bdate[length-4:length]
                                    print(2016 - int(int_bdate))
                                print(i['first_name'], i['last_name'], sep=' ')
                                print("https://vk.com/id", i['uid'], sep='')
                    countWoman += 1
    return countWoman

off = 0
countPeople = 1000
countWoman = 0
id_app = '5009897'              #id приложения
login = ''           #логин от вк
password = ''    #пароль от вк

session = vk.AuthSession(app_id=id_app, user_login=login, user_password=password)
api = vk.API(session)
req = api.groups.getMembers(group_id = '',fields = 'counters')

maxPeople = req['count']
iterator_count_people = maxPeople//1000
it = iter(range(iterator_count_people-1))
print(maxPeople, iterator_count_people)

for i in it:
    countWoman = req_func(off, countPeople, countWoman)
    off += 1000
    countPeople += 1000
    time.sleep(0.5)
print("_______________________________")
print("_______________________________")
print(countWoman)