username = input("Введите Ваше имя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки, например \"Активна\": ")
created_date = input("Введите сегодняшнюю дату в формате \"День-Месяц-Год\": ")
issue_date = input("Введите дату истечения заметки в формате \"День-Месяц-Год\": ")
temp_created_date = created_date[:5]
temp_issue_date = issue_date[:5]
print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", temp_created_date)
print("Дата истечения заметки:", temp_issue_date)