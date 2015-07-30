import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<img src="https://photos-2.dropbox.com/t/2/AABrLyjZnWYER-lNoZHT6-5wccI5iqE18b7MUhTo_pDbgw/12/4779803/png/32x32/1/1438304400/0/2/ac_icon_1024x.png/CJveowIgASACIAMgBCAFIAYgBygBKAIoBw/19xwu_MmUJsWVozbBn0U86eG5pdJWqJyo1p6iiC3tjQ?size=1600x1200&size_mode=2">'

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
