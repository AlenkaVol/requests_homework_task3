import requests

date1 = 1690848000
date2 = 1690934400


def questions_stackoverflow_2_days(date1, date2):
    url = "https://api.stackexchange.com/questions"
    params = {'fromdate': date1, 'todate': date2, 'tagged': 'Python', 'sort': 'creation', 'order': 'desc',
          'site': 'stackoverflow'}
    response = requests.get(url, params=params)
    questions = response.json()['items']
    for question in questions:
        title = question['title']
        tags = question['tags']
        link = question['link']
        with open ('questions_stackoverflow.txt', 'a') as f:
            f.write(f'{title}\n{tags}\n{link}\n\n')
    print('Список вопросов с сайта stackoverflow за последние два дня содержащие тэг "Python" записаны в файл '
          'questions_stackoverflow.txt')


questions_stackoverflow_2_days(date1, date2)



