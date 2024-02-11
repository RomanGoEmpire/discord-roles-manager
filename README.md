# Discord Role Bot

This bot assigns a role to a user in a Discord server when they react to a specific message.

## Prerequisites

- Python 3.6 or higher
- `discord.py` library
- `python-dotenv` library

## Setup

0. Add the Bot to the server.
1. Clone this repository to your local machine.
2. Create a .env file in the root directory of the project, and add your Discord bot token, the ID of the message to react to, the reaction emoji, and the role to assign:
   ```
   API_KEY=your_discord_bot_token  
   ROLE_MESSAGE_ID=your_message_id  
   REACTION=your_reaction_emoji  
   ROLE=your_role  
   ```
   Replace your_discord_bot_token, your_message_id, your_reaction_emoji, and your_role with your actual values.

   ### EMOJI HAS TO BE THE ICON e.g. ✅ NOT THE TEXTFORM :<your_emoji>: 
   
4. Start the programm with following command:
   ```sh
   source start.sh
   ```

The bot should now be running and ready to assign roles in your Discord server.
