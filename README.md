# Тестовое задание 📋

[Rishat-stripe-site](http://cw19145-django-sd5kf.tw1.ru) развернут на хостинге но пока не доступен для тестирования (в течении 3-24 часов домен должен быть обновлен в днс)

## 🤖 Как развернуть проект (локально)


## ⚙️ Первоначальная настройка и виртуальное окружение

Сначала проверьте установлен ли у вам docker c помощью команды

```
$ docker --version
```
Если Docker нет, то выполните его установку

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

## 📞 Contacts

- E-Mail: forwotk31415@gmail.com
- Telegram: [@lipp260](https://t.me/lipp260)

 
