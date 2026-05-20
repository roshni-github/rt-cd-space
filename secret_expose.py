import os
sec = os.environ.get('RT_CDSP_SECRET')

print(sec[:2] + (len(sec)-4)*"*" + sec[-2:])