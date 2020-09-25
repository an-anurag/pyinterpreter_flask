
import io
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


from flask import Flask, request, render_template, Response, jsonify

from run_py import RunPyCode

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        code = request.form['code']
        code_obj = RunPyCode()
        error, output = code_obj.run_py_code(code)
        print(output)
        return jsonify({'output': output, 'error': error})

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
