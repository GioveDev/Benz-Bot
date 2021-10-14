from flask import Flask, json
from flask.globals import request

import cleverbotfree

from gevent import monkey
monkey.patch_all()

api = Flask(__name__)

p_w = cleverbotfree.sync_playwright().__enter__()
c_b = cleverbotfree.Cleverbot(p_w)
p_w.stop

@api.route('/chat', methods = ['GET'])
def GetReply():
    message = request.args.get('message', default=0, type = str)
    
    reply = c_b.single_exchange(message)

    if reply:
        return json.dumps(reply)
    else:
        return json.dumps("something went wrong try again")

if __name__ == '__main__':
    api.run(host='0.0.0.0', threaded = True)
