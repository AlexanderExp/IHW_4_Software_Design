# IHW_4_Software_Design

### Работу выполнил Фролов Александр Сергеевич, БПИ217

### Заметки:

1) Работа выболнялась на языке Python 
2) Активно использовался Flask для создания рабочего web-приложения
3) Вместо использования Swagger было решено выпендриться и использовать frontend на html, css, JavaScript.
4) База данных: PostgreSQL
5) Инструмент для работы с базой данных: PgAdmin (для удобства), SQLAlchemy
6) База данных общая для обоих микросервисов
7) Для проверки будет необходимо настроить PostgreSQL и PgAdmin. Если Вы, уважаемый проверяющий, не захотите этого делать, но захотите убедиться в том, что все действительно работает, то прошу написать мне на телеграм. Всё покажу.
8) Микросервисы работают на отдельных портах и имеют доступ друг к другу через такие команды: "redirect('http://localhost:5800?user_id=' + str(user.id))"
9) Общая схема работы программы следующая: 

Есть 2 отдельных микросервиса: authorizationService и orderManagementService, оба на Python, серверная часть обоих 
сделана с помощью Flask, работа с базой данных осуществляется с помощью SQLAlchemy, клиентская сторона работает с сервером за счет 
запросов, отправляемых из JavaScript кода через fetch запросы (асинхронными их сделать не успел). Внешняя часть приложения 
"рисуется" с помощью гольного css и html и того же JavaScript (В основном с помощью него. так как для красоты нужно динамически 
менять интерфейс).

Что было сделано из ТЗ:

1) БД - сделано всё. БД другая, но оттого только проще. Все требования к автоинкрементам, главным ключам и прочему соблюдены, даже добавлено несколько своих доработок. 
2) Микросервис авторизации пользователей: Регистрация, авторизация, выбор ролей, проверка почты, различные http ответы, страница подтверждения, вход пользователя в систему, предоставление информации о пользователе (предоставление информации о пользователе осталось без визуализации, есть только в коде. Работает благодаря current_user из flask.login. Очень удобный инструмент)

<img width="925" alt="image" src="https://github.com/AlexanderExp/IHW_4_Software_Design/assets/95678672/1dc6c0a1-6cc2-4d7d-ba90-e81c7a4a3d8f">


<img width="781" alt="image" src="https://github.com/AlexanderExp/IHW_4_Software_Design/assets/95678672/e465d287-2d96-4bba-9acb-c9ae2d31e60e">


<img width="888" alt="image" src="https://github.com/AlexanderExp/IHW_4_Software_Design/assets/95678672/68214b67-d149-4b19-b612-3c4cd0536ad1">


<img width="869" alt="image" src="https://github.com/AlexanderExp/IHW_4_Software_Design/assets/95678672/f0430819-5e85-4ab1-8cfe-73da2ad15ce2">


<img width="774" alt="image" src="https://github.com/AlexanderExp/IHW_4_Software_Design/assets/95678672/36153e62-4b5f-4852-8e05-9899b4da5f6e">


<img width="689" alt="image" src="https://github.com/AlexanderExp/IHW_4_Software_Design/assets/95678672/b89d8771-a45a-4a7a-9797-5c36cbe0b464">

3) Микросервис обработки заказов

Сделано по-максимуму, но часть функционала не успела приобрести визуальную часть (Есть только в коде).

Из того, что сделано красиво: 

order now - кнопка, добавляющая в заказ блюдо.
Your order - кнопка, переводящая пользователя к его заказу. 
<img width="937" alt="image" src="https://github.com/AlexanderExp/IHW_4_Software_Design/assets/95678672/c6585887-8133-4e2f-9fd6-64b422391d8f">

<img width="939" alt="image" src="https://github.com/AlexanderExp/IHW_4_Software_Design/assets/95678672/4cda7ade-2d45-422c-b68d-d99230a065af">


кнопка remove from order удаляет 1 единицу блюда из заказа. Если в заказе всего одно такое блюдо, то оно исчезнет из заказа полность. Всё, что должно обновляться, обновляется без необходимости перезагружать страницу. 

Кнопка Show Menu переводит пользователя к меню.
<img width="948" alt="image" src="https://github.com/AlexanderExp/IHW_4_Software_Design/assets/95678672/2e1a5866-54b1-458a-ba39-27245747e4e4">

Естественно, заказ доступен только пользователю с ролью Customer. Менеджеру доступен функционал по управлению блюдами и меню в целом. Визуальной части под менеджера сделать не успел. 