# -*- coding: utf-8 -*-
from chatterbot import ChatBot

bot = ChatBot(
    "NaiveBot", # Nom
    storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    logic_adapters=[ # Désactiver le logic_adapters pour le learning
        "chatterbot.logic.BestMatch",
    ],
    database="naive_database.db", # nom de la base d'échanges
    silence_performance_warning=True
)

while True:
    try:
     bot_input = bot.get_response(None)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break