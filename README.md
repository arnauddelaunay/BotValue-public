# BotValue

The idea of BotValue is to run a chatbot which is able, using the [Chatterbot](https://github.com/gunthercox/ChatterBot) lib to transform any natural language request into a database query to get the information.

**Example**

This question : ![NL request](app/img/natural_question.png)

Becomes this query : ![DB query](app/img/db_query.png)

This work has been realised during Contrib' Days at [Linkvalue](www.link-value.fr/fr). 

You can find [here](https://blog.link-value.fr/d%C3%A9velopper-un-chatbot-en-python-3a8b0e518df5) an article in French to explain our first approach.

See Explanations for more details

## Install

Either run these following commands
```
pip install -r requirements.txt
git clone https://github.com/gunthercox/ChatterBot.git
cp -r ChatterBot/chatterbot ./
cp -r chatterbot_fork/* chatterbot/
rm -rf ChatterBot/
```

Or the installer : 
```
chmod +x install.sh
./install.sh
```

## Run BotValue

### Terminal Version

Run `python .`

### Web Version

Run `python . --web-app` and go to `localhost:5000`

![web app for BotValue](app/img/screenshot.png)

> Debug Mode : pass `--debug` as an argument

## Documentation

[Chatterbot Documentation](http://chatterbot.readthedocs.io/en/stable/)

## Key Elements

See into chatterbot, the logic adapters. 
A **QueryAdapter** has been implemented for the v0.2 of the bot ([here](chatterbot_fork/logic/query_adapter.py))



