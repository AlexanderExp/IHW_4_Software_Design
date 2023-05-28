# IHW_4_Software_Design

### Работу выполнил Фролов Александр Сергеевич, БПИ217

### Заметки:

1) Работа выболнялась на языке Python 
2) Активно использовался Flask для создания рабочего web-приложения
3) Вместо использования Swagger было решено выпендриться и использовать frontend на html, css, JavaScript.
4) База данных: PostgreSQL
5) Инструмент для работы с базой данных: PgAdmin (для удобства), SQLAlchemy
6) База данных общая для обоих микросервисов
7) Микросервисы работают на отдельных портах и имеют доступ друг к другу через такие команды: "redirect('http://localhost:5800?user_id=' + str(user.id))"
8) Общая схема работы программы следующая: 

Есть 2 отдельных микросервиса: authorizationService и orderManagementService, оба на Python, серверная часть обоих 
сделана с помощью Flask, работа с базой данных осуществляется с помощью SQLAlchemy, клиентская сторона работает с сервером за счет 
запросов, отправляемых из JavaScript кода через fetch запросы (асинхронными их сделать не успел). Внешняя часть приложения 
"рисуется" с помощью гольного css и html и того же JavaScript (В основном с помощью него. так как для красоты нужно динамически 
менять интерфейс).

Что было сделано из ТЗ:

1) БД - сделано всё 
2) Микросервис авторизации пользователей: Регистрация, авторизация, выбор ролей, проверка почты, различные http ответы, 
страница подтверждения

<img width="925" alt="image" src="https://github.com/AlexanderExp/IHW_4_Software_Design/assets/95678672/1dc6c0a1-6cc2-4d7d-ba90-e81c7a4a3d8f">


<img width="781" alt="image" src="https://github.com/AlexanderExp/IHW_4_Software_Design/assets/95678672/e465d287-2d96-4bba-9acb-c9ae2d31e60e">


<img width="888" alt="image" src="https://github.com/AlexanderExp/IHW_4_Software_Design/assets/95678672/68214b67-d149-4b19-b612-3c4cd0536ad1">


<img width="869" alt="image" src="https://github.com/AlexanderExp/IHW_4_Software_Design/assets/95678672/f0430819-5e85-4ab1-8cfe-73da2ad15ce2">


<img width="774" alt="image" src="https://github.com/AlexanderExp/IHW_4_Software_Design/assets/95678672/36153e62-4b5f-4852-8e05-9899b4da5f6e">


<img width="689" alt="image" src="https://github.com/AlexanderExp/IHW_4_Software_Design/assets/95678672/b89d8771-a45a-4a7a-9797-5c36cbe0b464">

3) 
