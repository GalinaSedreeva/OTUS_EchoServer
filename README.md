# Echo Сервер

## Описание

Это реализация простого **HTTP echo-сервера**, написанного с использованием модуля `socket` стандартной библиотеки Python. Цель сервера — принимать HTTP-запросы от клиентов и возвращать информацию о полученном запросе: метод, заголовки и статус, указанный в параметре `status`.

## Функционал

Сервер поддерживает следующие функции:

- ✅ Возвращает метод HTTP-запроса (например, `GET`, `POST`)
- ✅ Отображает IP-адрес и порт клиента
- ✅ Поддерживает параметр `status` в URL для установки HTTP-статуса ответа (например, `/?status=404`)
- ✅ Если параметр `status` не передан или невалиден, возвращается статус `200 OK`
- ✅ Использует стандартный модуль `http` для получения фразы статуса (например, `OK`, `Not Found`)
- ✅ Возвращает все полученные заголовки в теле ответа
- ✅ Сервер продолжает работать после обработки каждого соединения

## Технические детали

- Протокол: HTTP/1.1 
- Порт: `5000` как указано в фикстурах
- Реализовано без использования сторонних библиотек, только стандартная библиотека Python
- Все тесты из `test_echo_server.py` успешно пройдены

## Тестирование

Тесты реализованы с использованием `pytest` и проверяют работу сервера на соответствие требованиям задания.
