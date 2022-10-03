from flask import Flask 
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route('/')
def index():
  return 'Hi'

@app.route('/<password>')
def hashed(password):
  # generate_password_hash 可將一個字串轉變成雜湊(hash)
  # 雜湊演算法轉換出來的字串是不可逆的，所以時常用來製作密碼等等高機密資料
  hashed_value = generate_password_hash(password)

  # check_password_hash 可直接比對字串經過雜湊演算法後的直是否符合本地已儲存的字串(return boolean)
  mypassword = 'pbkdf2:sha256:260000$4hFXsKMRsaJPdrN5$c669ba954df22670ac0c8a4de4fde85fcc86150fe1340abf83b4f51005dfe983'
  result = check_password_hash(mypassword, password)
  return hashed_value
  # return str(result)

if __name__ == '__main__':
  app.run(debug=True)