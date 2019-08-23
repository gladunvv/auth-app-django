# auth-app-django
Application on Django framework for authentification VK and show five random friends


### Содержание:
+ [Краткое описание](#краткое-описание)
+ [Полезные ссылки](#полезные-ссылки)
+ [Requirements](#requirements)
+ [Сборка и запуск проекта](#сборка-и-запуск)
+ [Screenshots](#screenshots)


## Краткое опиание:

Простое Django приложение для аутентификации через ВК, после прохождения аутентификации пользователь попадает на страницу со своим 
именем, аватаром и пятью рандомными друзьями из социальной сети Вконтакте, у пользователя есть возможность сменить тему на темную 
или светлую путем переключения чекбокса в правом верхнем углу и перейти на страницу одного из своих друзей кликнув на карточку с другом.

## Полезные ссылки:
+ [Django](https://docs.djangoproject.com/en/2.2/)
+ [Social Auth](https://python-social-auth.readthedocs.io/en/latest/backends/)
+ [VK Dev](https://vk.com/dev)

## Requirements:

+ Django==2.2.4
+ oauthlib==3.1.0
+ requests==2.22.0
+ requests-oauthlib==1.2.0
+ social-auth-app-django==3.1.0
+ social-auth-core==3.2.0


## Сборка и запуск:
```
git clone git@github.com:gladunvv/auth-app-django.git
pip install -r requirements.txt
cd myapp/
python manage.py runserver
```
> Приложение будет работать только в том случае если в настройках прописанны ключи доступа к VK приложению.


## Screenshots
### Dark:
![](https://res.cloudinary.com/dtgupwmg6/image/upload/v1566566539/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_%D0%BE%D1%82_2019-08-23_16-05-03_frhkeu.png)
### Light:
![](https://res.cloudinary.com/dtgupwmg6/image/upload/v1566566537/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_%D0%BE%D1%82_2019-08-23_16-04-07_in2wg7.png)