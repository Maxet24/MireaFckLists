from flask import Flask, render_template, request, jsonify
import pass_manager
from datetime import datetime, timezone
import pytz

app = Flask(__name__)

@app.route('/add-student/<string:para_hash>', methods=['GET'])
def index(para_hash):
    return render_template('index.html')

@app.route('/get-botaniki/<string:para_hash>', methods=['GET'])
def get_botaniki(para_hash):
    text = ''

    botan_list = pass_manager.get_botaniki(para_hash)['botaniki']
    for botan in botan_list:
        text += pass_manager.get_name_by_vk_id(botan['vk_user_id']) + ' ' + botan['entry_datetime'] + "<br>"

    return text

@app.route('/get-info/<string:para_hash>', methods=['GET'])
def get_lesson_info(para_hash):

    return pass_manager.get_botaniki(para_hash)

@app.route('/del-botaniki/<string:para_hash>', methods=['GET'])
def del_lesson_info(para_hash):

    pass_manager.del_botaniki(para_hash);

    return 'Done'

@app.route('/add-student', methods=['POST'])
def process():
    data = request.get_json()

    pass_manager.add_botanik(data['para_hash'], data['vk_user_id'], datetime.now(pytz.timezone('Europe/Moscow')))

    return 'ok', 200

if __name__ == '__main__':
    app.run(debug=True)
