import os
from bottle import Bottle, request  
import sentry_sdk  
from sentry_sdk.integrations.bottle import BottleIntegration  

os.environ['SENTRY_DSN'] = 'https://ba5daac703cb4d14af4de3ce39bede8b@o385522.ingest.sentry.io/5218403'
  
#sentry_sdk.init("https://ba5daac703cb4d14af4de3ce39bede8b@o385522.ingest.sentry.io/5218403", integrations=[BottleIntegration()])  
sentry_sdk.init(dsn=os.environ.get("SENTRY_DSN"), integrations=[BottleIntegration()])  

  
app = Bottle()  

@app.route('/success') 
def success():
    return ("ВСЕ УДАЧНО!")    

@app.route('/fail') 
def fail():    
    raise RuntimeError("Ошибка для проверки в Sentri!")
  
    
app.run(host='localhost', port=8080)