from flask import Flask, json
from flask.globals import request
import pexpect


api = Flask(__name__)

child = pexpect.spawn('python3 CleverbotFree.py')

@api.route('/chat', methods = ['GET'])
def GetReply():
    message = request.args.get('message', default=0, type = str)
    
    child.sendline(message)
    child.expect('Cleverbot:')
    reply = str(child.readline())
    
    truncated_reply = reply[3:]
    sanitized_reply = truncated_reply.split('\\',1)
    
    if sanitized_reply[0] and not sanitized_reply[0].isspace():
        return json.dumps(sanitized_reply[0])
    else:
        return json.dumps("something went wrong try again")

if __name__ == '__main__':
    api.run(host='0.0.0.0', threaded = True)
