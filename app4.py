from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def input():
  return render_template('input.html', title='入力ページ')

@app.route('/', methods=['POST'])
def output():
  num1 = request.form['num1']
  num2 = request.form['num2']
 
  return render_template('output.html', num1=num1,num2=num2,title='出力ページ')

if __name__ == '__main__':
  app.run(debug=True)