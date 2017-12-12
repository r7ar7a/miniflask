from flask import Flask, request, Response, json

APPLICATION = Flask(__name__)
SEPARATOR = '<|>'


@APPLICATION.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        input1 = request.form['input1']
        input2 = request.form['input2']
        with open('data.txt', 'w') as f:
            f.write(SEPARATOR.join(input1, input2))
            f.write('\n')
        return Response('SUCCESS', mimetype='application/json')
    else:  # request.method == 'GET':
        try:
            with open('data.txt', 'r') as f:
                line = f.readline()
                data1, data2 = line.strip().split(SEPARATOR)
                f.write('\n')
        except Exception as e:
            print(e)
            response = json.dumps({'error': 'NO DATA'})
            return Response(response, status=503, mimetype='application/json')
        return Response(json.dumps([data1, data2]), mimetype='application/json')
