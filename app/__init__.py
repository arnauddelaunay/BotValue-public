#!flask/bin/python
from flask import Flask, jsonify, request
from bot import launch_bot
# from flask_cors import CORS, cross_origin

def run_app(debug=False):
    bot = launch_bot('BotValue',**dict(
        storage_adapter='chatterbot.storage.JsonFileStorageAdapter', #store conversations locally
        logic_adapters=[
            {
                'import_path' : 'chatterbot.logic.QueryAdapter', #custom adapter for db queries
                'training_file_for_query' : 'query_adapter_training' #training corpus for query adapter
            }
        ],
        trainer='chatterbot.trainers.ListTrainer',
        database="botvalue.db")
)
    app = Flask(__name__, static_url_path='')
    
    @app.route('/', methods=['GET'])
    def index():
        return app.send_static_file('index.html')

    @app.route('/chatbot', methods=['POST'])
    def get_tasks():
        response = bot.get_response(request.form['data'])
        return jsonify({'response': response.text})

    app.run(debug=debug)
