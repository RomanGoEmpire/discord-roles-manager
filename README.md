# Discord Role Bot

This bot assigns a role to a user in a Discord server when they react to a specific message.

## Prerequisites

- Python 3.6 or higher
- `discord.py` library
- `python-dotenv` library

## Setup

0. Add the Bot to the server.
1. Clone this repository to your local machine.
2. Install the required Python libraries using pip:

```sh
pip install -r requirements.txt
```

3. Create a .env file in the root directory of the project, and add your Discord bot token, the ID of the message to react to, the reaction emoji, and the role to assign:

```
API_KEY=your_discord_bot_token  
ROLE_MESSAGE_ID=your_message_id  
REACTION=your_reaction_emoji  
ROLE=your_role  
```

Replace your_discord_bot_token, your_message_id, your_reaction_emoji, and your_role with your actual values.

Running the Bot
To start the bot, run the following command in your terminal:
```sh
python bot.py
```


The bot should now be running and ready to assign roles in your Discord server.