import datetime
m, d = map(int, input().split())
today = datetime.datetime(2019, m, d)
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

yesterday = str(yesterday)[5:10]
tomorrow = str(tomorrow)[5:10]

yesterday = yesterday.replace('-', '.')
tomorrow = tomorrow.replace('-', '.')
print(yesterday, tomorrow)