"""
>>> import subprocess
>>> subprocess.check_output('python3 miniwc.py ./testinputs/test1.txt',shell=True)
b'28 213 1187 ./testinputs/test1.txt\\n'

>>> subprocess.check_output('python3 miniwc.py',shell=True)
b"We don't handle that situation yet!\\n"

>>> subprocess.check_output('python3 miniwc.py ./testinputs/test1.txt -help',shell=True)
b"We don't handle that situation yet!\\n"

>>> subprocess.check_output('python3 miniwc.py testinputs',shell=True)
b'File is not accessible.\\n'
"""
