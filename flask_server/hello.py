from flask import Flask, escape, request, render_template
import random
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/myname')
def myname():
    return '송빈산입니당'

# 랜덤으로 점심메뉴 추천해주는 서버
@app.route('/lunch')
def lunch():
    menus = ['양자강','김밥카페','20층','순남시래기']
    lunch = random.choice(menus)
    return lunch

# 아이돌 백과사전
@app.route('/idol')
def idol():
    idols = {
        'bts':{
            '지민':25,
            '랩몬스터':23
        },
        'rv':'레드벨벳',
        '핑클':{
            '이효리':'거꾸로해도이효리',
            '옥주현':'35'
        },
        'SES':['유진','바다','슈']
    }
    return idols

@app.route('/post/<int:num>')
def post(num):
    posts = ['0번 포스트','1번 포스트','2번 포스트']
    return posts[num]

# 실습 cube뒤에 전달된 수의 세제곱수를 화면에 보여주세요
@app.route('/cube/<int:num>')
def cube(num):
    cubed = num*num*num
    return str(cubed)

# 클라이언트에게 html 파일을 주고싶어요!
@app.route('/html')
def html():
    return render_template('hello.html')

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    age = request.args.get('age')
    # age = request.args['age']
    return render_template('pong.html',age_in_html=age)

# 로또번호를 가져와서 보여주는 서버
@app.route('/lotto_result/<int:round>')
def lotto_result(round):
    url = f'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo={round}'
    result = requests.get(url).json()

    winner = []
    for i in range(1,7):
        winner.append(result.get(f'drwtNo{i}'))
        # winner.append(result[f'drwNo{i}'])
    
    winner.append(result.get('bnusNo'))

    return json.dumps(winner)



app.run(debug=True)