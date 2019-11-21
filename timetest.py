from datetime import datetime
import re

e = ('08:15:36.509', 'PDT', 'Sat', 'Sep', '29', '2018')
print(datetime.strptime("{} {} {} {} {}".format(e[3], e[4], e[5], e[0], '-0700'),'%b %d %Y %H:%M:%S.%f %z').timestamp())
