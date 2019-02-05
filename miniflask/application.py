import os
from flask import Flask, request, Response, json

APPLICATION = Flask(__name__)
SEPARATOR = '<|>'


STATIC_FOLDER = os.path.join(os.environ['PWD'], 'client')
APPLICATION = Flask(__name__, static_folder=STATIC_FOLDER)


@APPLICATION.route('/index.html')
@APPLICATION.route('/')
def index_html():
    try:
        return APPLICATION.send_static_file('index.html')
    except Exception as e:
        print(str(e))


@APPLICATION.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        try:
            input1 = data['input1']
            input2 = data['input2']
        except KeyError:
            response = json.dumps({'error': 'Missing input parameter'})
            return Response(response, status=422, mimetype='application/json')
        with open('data.txt', 'w') as f:
            f.write(SEPARATOR.join([input1, input2]))
            f.write('\n')
        return Response(json.dumps('SUCCESS'), mimetype='application/json')
    else:  # request.method == 'GET':
        try:
            with open('data.txt', 'r') as f:
                line = f.readline()
                data1, data2 = line.strip().split(SEPARATOR)
                return Response(json.dumps({'data1': data1, 'data2': data2}))
        except Exception as e:
            print(e)
            response = json.dumps({'error': 'NO DATA'})
            return Response(response, status=503, mimetype='application/json')
        return Response(json.dumps([data1, data2]), mimetype='application/json')


@APPLICATION.route('/simple_data', methods=['GET', 'POST'])
def simple_data():
    if request.method == 'POST':
        data = request.get_json()
        input1 = data['input1']
        input2 = data['input2']
        with open('data.txt', 'w') as f:
            f.write(SEPARATOR.join([input1, input2]))
            f.write('\n')
        return Response(json.dumps('SUCCESS'), mimetype='application/json')
    else:  # request.method == 'GET':
        with open('data.txt', 'r') as f:
            line = f.readline()
            data1, data2 = line.strip().split(SEPARATOR)
            return Response(json.dumps({'data1': data1, 'data2': data2}))
        return Response(json.dumps([data1, data2]), mimetype='application/json')
