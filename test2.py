
import os
import sys
cur_path = os.path.abspath(os.path.dirname(__file__))
print('cur_path:',cur_path)


root_path = os.path.split(cur_path)[0]
sys.path.append(os.path.split(root_path)[0])


print('rootPath:',root_path)