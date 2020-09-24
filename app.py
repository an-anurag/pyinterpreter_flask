
import io
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


from flask import Flask, request, render_template, Response, jsonify

from run_py import RunPyCode

app = Flask(__name__)


@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig


@app.route('/', methods=['GET', 'POST'])
def run_py():

    if request.method == 'POST':
        code = request.form['code']
        code_obj = RunPyCode()
        error, output = code_obj.run_py_code(code)
        return jsonify({'output': output, 'error': error})

    else:
        return render_template('index.html')


@app.route('/skulpt', methods=['GET', 'POST'])
def home2():
    return render_template('skulpt.html')


if __name__ == '__main__':
    app.run()
