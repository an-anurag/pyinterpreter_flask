import os
import sys
import subprocess


class RunPyCode:

    def __init__(self, code=None):
        self.code = code
        if not os.path.exists('output'):
            os.mkdir('output')

    def _run_py_prog(self, cmd="prog.py", args=None):
        cmd = [sys.executable, cmd]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = p.wait()
        a, b = p.communicate()
        self.stdout, self.stderr = a.decode("utf-8"), b.decode("utf-8")
        return result

    def run_py_code(self, code=None, command_args=None):
        filename = "./output/prog.py"
        if not code:
            code = self.code
        else:
            with open(filename, "w") as f:
                f.write(code)
        self._run_py_prog(filename, command_args)
        return self.stderr, self.stdout
