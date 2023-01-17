from chatterbot import ChatBot
bot = ChatBot(
    "Yui", # Nom
    storage_adapter="chatterbot.adapters.storage.JsonFileStorageAdapter",
    input_adapter="chatterbot.adapters.input.TerminalAdapter",
    output_adapter="chatterbot.adapters.output.TerminalAdapter",
    logic_adapters=[ # Desactiver le logic_adapters pour le learning
        "chatterbot.adapters.logic.ClosestMatchAdapter",
],
    database="naive_database.db", # nom de la base d'échanges
    silence_performance_warning=True
)
while True:
    try:
     bot_input = bot.get_response(None)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break