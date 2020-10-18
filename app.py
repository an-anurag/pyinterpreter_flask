from flask import Flask, request, render_template

from run_py import RunPyCode

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    """
    import matplotlib.pyplot as plt

    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig, ax = plt.subplots()
    ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    :return:
    """
    if request.method == 'POST':
        code = request.form['editor']

        # matplotlib graph handler
        if 'matplotlib' in code:
            updated_code = "import mpld3\n" + code + "\nmpld3.save_json(fig, fileobj='json_fig.json')"
            code_obj = RunPyCode()
            error, output = code_obj.run_py_code(updated_code)
            # read json from file
            with open('json_fig.json', 'r') as json_fig_file:
                json_fig = json_fig_file.read()
            # flush the json file
            open('json_fig.json', 'w').close()
            return render_template('index.html', output=output, error=error, is_chart=True, chart=json_fig, code=code)

        # normal python code handler
        code_obj = RunPyCode()
        error, output = code_obj.run_py_code(code)
        return render_template('index.html', output=output, error=error, is_chart=False, code=code)

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
