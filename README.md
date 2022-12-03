# Тестовое задание 📋

[Rishat-stripe-site](https://cw19145-django-sd5kf.tw1.ru) развернут на хостинге, но пока не доступен для тестирования (в течении 3-24 часов сайт должен заработать, как только обновятся DNS-серверы)

## 💻 Как развернуть проект (локально)


Для начала удостоверьтесь, что у вас установлен docker c помощью команды

```
$ docker --version
```
Если Docker нет, то выполните его установку. 

```
$ sudo apt install apt-transport-https ca-certificates curl software-properties-common
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
$ sudo apt update
$ sudo apt install docker-ce
```

После этого загрузите образ прокта из Docker Hub

```
$ sudo docker pull ramses31415/testrishat:latest
```

Запустите скачанный образ при помощи команды

```
$ sudo docker run -d -it -p 8000:8000 ramses31415/testrishat
```

## Пункты тестового задания (выполненный функционал помечен "🚩")

**Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:**    
🚩 Django Модель Item с полями (name, description, price)   
API с двумя методами:  
🚩 GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса  
🚩 GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)  
🚩 Залить решение на Github, описать запуск в Readme.md  
🚩 Опубликовать свое решение чтобы его можно было быстро и легко протестировать.   

**Бонусные задачи**  
    🚩 Запуск используя Docker   
    🚩 Использование environment variables  
    🚩 Просмотр Django Моделей в Django Admin панели (admin: root/1234)  
    🚩 Запуск приложения на удаленном сервере, доступном для тестирования  
    * Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items  
    * Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме. 
    🚩 Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте  
    * Реализовать не Stripe Session, а Stripe Payment Intent.  





## 📞 Contacts

- E-Mail: forwork31415@gmail.com
- Telegram: [@lipp260](https://t.me/lipp260)

 
