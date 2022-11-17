from flask import Flask, request, Response
import json

app = Flask(__name__)

def get_total_calc(l):
    ret = 0
    for ele in l:
        try:
            a = int(ele)
            ret += a
        except Exception as e:
            pass

    return ret


@app.route('/')
def get_total():
    mode1 = request.args.get("module_1")
    mode2 = request.args.get("module_2")
    mode3 = request.args.get("module_3")
    mode4 = request.args.get("module_4")
    mode5 = request.args.get("module_5")
    mark1 = request.args.get("mark_1")
    mark2 = request.args.get("mark_2")
    mark3 = request.args.get("mark_3")
    mark4 = request.args.get("mark_4")
    mark5 = request.args.get("mark_5")

    ret = {"error": False}
    total = get_total_calc([mark1, mark2, mark3, mark4, mark5])
    ret["total_marks"] = str(total)

    # 响应体返回，这里是字符串
    response = Response(response=json.dumps(ret), status=200, mimetype='application/json')
    response.headers["Content-Type"] = "application/json"
    response.headers["Access-control-Allow-Origin"] = "*"
    print(json.dumps(ret))
    return response


if __name__ == '__main__':
    app.run()
