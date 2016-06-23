import vk
import time

def result_print(sex_flag, city_flag, age_flag, age):
    if sex_flag == 1:
        if city_flag == 0:
            pass
        else:
            if age_flag == 0:
                pass
            else:
                if city_flag == 2:
                    pass
                if age_flag == 2:
                    pass
                if city_flag == 1:
                    if req['city'] == 1:
                        print("Москва")
                    else: print("Павловский Посад")
                if age_flag == 2: pass
                if age_flag == 1: print(age)
                print(i['first_name'], i['last_name'])
                print("https://vk.com/id",i['id'],sep='')


def req_func(off, pep, wom):
    req = api.groups.getMembers(group_id = '', offset = off, fields = ['sex', 'bdate','city'], count = pep) #и сюда id того же паблика
    req = req['users']
    countWoman = wom

    for i in req:

        if "deactivated" in i:
            pass
        else:
            if i['sex'] == 1:
                sex_flag = 1
            else:
                sex_flag = 0
            if "city" in i:
                if i['city'] == 4757:
                        city_flag = 1
                else:
                    if i['city'] == 1:
                        city_flag = 1
                    else:
                        city_flag = 0
            else:
                city_flag = 2
            if 'bdate' in i:
                length =len(i['bdate'])
                if length > 5:
                    bdate = i['bdate']
                    int_bdate = bdate[length-4:length]
                    age = (2016 - int(int_bdate))
                    if age > 17 or age < 20:
                        age_flag = 1
                    else:
                        age_flag = 0
                else:
                    age_flag = 2
            result_print(sex_flag, city_flag, age_flag, age)


off = 0
countPeople = 1000
countWoman = 0
id_app = ''              #id приложения
login = ''           #логин от вк
password = ''    #пароль от вк

session = vk.AuthSession(app_id=id_app, user_login=login, user_password=password)
api = vk.API(session)
req = api.groups.getMembers(group_id = '',fields = 'counters') #id паблика в котором искать

maxPeople = req['count']
iterator_count_people = maxPeople//1000
it = iter(range(iterator_count_people-1))
print(maxPeople, iterator_count_people)

for i in it:
    countWoman = req_func(off,countPeople,countWoman)
    off += 1000
    countPeople += 1000
    time.sleep(0.5)
print(countWoman)
