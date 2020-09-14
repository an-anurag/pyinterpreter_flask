
import io
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


from flask import Flask, request, render_template, Response

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
        code = request.form['code_area']
        command_args = request.form['input_area']
        code_obj = RunPyCode()
        error, output = code_obj.run_py_code(code, command_args=command_args)
        return render_template('index.html', error=error, output=output)

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
