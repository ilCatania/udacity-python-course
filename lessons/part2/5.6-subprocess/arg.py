import subprocess
import sys
import random


"""
p = subprocess.Popen(("emoj", *(sys.argv[1:])), stdout=subprocess.PIPE)
out, err = p.communicate()
status = p.wait()
"""

out = subprocess.run(("emoj", *(sys.argv[1:])), stdout=subprocess.PIPE).stdout
res = random.choice(out.split()).decode("utf-8")
print(res)

