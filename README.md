# D_2_10

Регистрируемся на Sentry.io-для этого заходим туда 
и жмем Get started

После этого создаем новый Project
При создании выбираем из множества предложенного
Python

После этого преходим по ссылке
https://docs.sentry.io/error-reporting/quickstart/?platform=python

Там смотрим Install an SDK, делаем как там

(Далее запускаем 
pip install --upgrade sentry-sdk[bottle]==0.14.3
Этого достаточно для работы!)

Ниже, в  Configure the SDK уидим строку
Showing configuration for
в ней будет sentry_sdk.init с вашим ID
Эту строку , которая в скобках, нужно будет поставить
в моем модуле после равно в строке
   os.environ['SENTRY_DSN'] = 'https://ba5daac703cb4d14af4de3ce39bede8b@o385522.ingest.sentry.io/5218403'
сохраняем такой же синтаксис! Заменяем на свое только то, что внутри одинарных кавычек!

Запускаем на компе код, преходим по 
http://localhost:8080/fail 
и в своей Sentry.io видим на вкладке Issues ошибки!
