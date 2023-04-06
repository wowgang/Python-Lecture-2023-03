from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return ''' 
        <h1>Hello GARAM!!!</h1>
        <hr>
        <p>디버그 모드에서는 변경사항이 발생하면 자동적으로 서버가 재실행됩니다.(수정후 저장하고 cmd보면 cmd자동으로 업데이트? 바꼈다는말인가봄)</p>
        <p>
            <ul>
                <li>cmd에서 입력< python 02.flask.py</li>
                <li>웹에서 http://localhost:5000/ 엔터</li>
                <li>127.0.0.1 생략되어있음</li>
                <li>http://localhost:5000  5000뒤에 / 생략되어있음</li>
                <li>http://localhost:5000/clock</li>
            </ul>
        </p>
        <p>
            # 폴더를 templates로 만들고 폴더안에 chart.html파일을 넣고 웹에서 http://localhost:5000/chart 실행
        </p>
    '''

@app.route('/chart') # 엣점라우트 해서 주소를 지정
def chart(): # 함수 이름
    return render_template('chart.html') # 폴더를 templates로 만들고 폴더안에 chart.html파일을 넣고 웹에서 http://localhost:5000/chart 실행

@app.route('/clock') 
def clock():    # 함수 이름도 바꾸기
    return render_template('clock.html') # 폴더를 templates로 만들고 폴더안에 chart.html파일을 넣고 웹에서 http://localhost:5000/chart 실행


if __name__ == '__main__':
    app.run(debug=True)


# cmd에서 입력< python 02.flask.py
# 웹에서 http://localhost:5000/ 엔터
# 127.0.0.1
#          http://localhost:5000/
#                                /chart
# http://localhost:5000/clock
