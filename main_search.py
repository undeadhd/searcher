import vk
import time

def req_func(off, pep, wom, group):
    req = api.groups.getMembers(group_id = group, offset = off, fields = ['sex', 'bdate','city'], count = pep)
    req = req['users']
    countWoman = wom
    for i in req:
        if "deactivated" in i:
            pass
        else:
            if i['sex'] == 1:
                if "city" in i and "bdate" in i:
                    length = len(i['bdate'])
                    if length > 5:
                        year = i['bdate']
                        age = year[length-4:length]
                        age = int(age)
                        age = 2016 - age
                        if (i['city'] == 4757 or i['city'] == 1) and (age >= 17 and age < 22):
                            print(i['first_name'], i['last_name'])
                            print(age)
                            countWoman += 1
                            if i['city'] == 1:
                                print('Москва')
                                print("https://vk.com/id", i['uid'], sep='')
                                print('____________________________')
                            else:
                                print('Павловский Посад')
                                print("https://vk.com/id", i['uid'], sep='')
                                print('____________________________')
    return countWoman


off = 0
countPeople = 1000
countWoman = 0
id_app = ''		#enter your app ID
print('Введите логин')
login = input()
print('Введите пароль')
password = input()

session = vk.AuthSession(app_id=id_app, user_login=login, user_password=password)
api = vk.API(session)
print('ID группы')
group = input()
req = api.groups.getMembers(group_id = group,fields = 'counters')

maxPeople = req['count']
iterator_count_people = maxPeople//1000
it = iter(range(iterator_count_people-1))
print(maxPeople, iterator_count_people)

for i in it:
    countWoman = req_func(off, countPeople, countWoman, group)
    off += 1000
    countPeople += 1000
    time.sleep(0.5)
print("_______________________________")
print("_______________________________")
print(countWoman)