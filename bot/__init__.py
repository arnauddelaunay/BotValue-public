# -*- coding: utf-8 -*-
#
# Author : Arnaud Delaunay
# Date : 25.11.2016

from chatterbot import ChatBot


def launch_bot(name, **kwargs):
    bot = ChatBot(name,**kwargs)
    return bot


def run():
    bot = launch_bot('BotValue',**dict(
        # store conversations locally
        storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
        logic_adapters=[
            {  
                # custom adapter for db queries
                'import_path': 'chatterbot.logic.QueryAdapter',
                # training corpus for query adapter
                'training_file_for_query': 'query_adapter_training'  
            }
        ],
        trainer='chatterbot.trainers.ListTrainer',
        # Terminal Version
        input_adapter="chatterbot.input.TerminalAdapter",
        output_adapter="chatterbot.output.TerminalAdapter",
        # name of local db
        database="botvalue.db",
        silence_performance_warning=True
        ))
    while True:
        try:
            bot_input = bot.get_response(None)
        except(KeyboardInterrupt, EOFError, SystemExit):
            break
            