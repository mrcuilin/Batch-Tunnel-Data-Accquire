import sys
import os
print( sys.argv[1] )
os.system("sudo date -s \"" + sys.argv[1] + "\"")

