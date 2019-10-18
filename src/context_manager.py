import tempfile
import os
from contextlib import contextmanager


class TempFile:
    def __init__(self, content):

        self.file = tempfile.NamedTemporaryFile(mode='w', delete=False)

        with self.file as f:
            f.write(content)

    @property
    def filename(self):
        return self.file.name

    def __enter__(self):
        return self

    def __exit__(self, *args):
        os.unlink(self.filename)


with TempFile('Hello World') as tmp_file:
    f = open(tmp_file.filename)
    print(f.read())


@contextmanager
def temp_file(content):
    tmp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
    with tmp_file as f:
        f.write(content)
    yield tmp_file.name
    os.unlink(tmp_file.name)


with temp_file('Hello World2') as tmp_file:
    f = open(tmp_file)
    print(f.read())


with open('/tmp/tmp.txt', 'r') as f:
    lines = f.readlines()
    print(lines)
