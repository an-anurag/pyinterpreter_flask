from flask import Flask, request, render_template
from run_py import RunPyCode
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def run_py():

    if request.method == 'POST':
        code = request.form['code_area']
        command_args = request.form['input_area']
        code_obj = RunPyCode()
        error, output = code_obj.run_py_code(code, command_args=command_args)
        return render_template('index.html', error=error, output=output)

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
