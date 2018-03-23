''' using list as queue'''

from collections import deque
q=deque(['eric','berg','shalini','pewds'])
q.append("terry")
q.append('jenna')
q.popleft()
q.popleft()
q.appendleft('jerry')
