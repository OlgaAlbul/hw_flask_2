# Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".
from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = '497763635af91119a34c372c653a4db3d3d7c114ee57584322e4b50d0ebc1f2d'


@app.route('/')
def start():
    return render_template('start.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        if not request.form['name']:
            flash('Ошибка, введите имя!', 'danger')
            return redirect(url_for('form'))
        name = request.form['name']
        flash('Сообщение отправлено', 'success')
        return redirect(url_for('hello_flash', name=name))
    return render_template('form.html')


@app.route('/hello_flash/<name>')
def hello_flash(name):
    return render_template('hello_flash.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)

