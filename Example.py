import  pyshorteners

s=pyshorteners.Shortener()
print("Сокращенная ссылка-",s.tinyurl.short('https://mail.ru/'))
