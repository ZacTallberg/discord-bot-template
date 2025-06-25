A friendly, schedulable, and multi-language Discord Bot written in Python using the discord.py library. This bot is designed to be easily configurable and extensible.

This bot features a variety of conversational commands to make it feel more alive, as well as powerful administrative tools for scheduling messages.

## Key Features

* **Interactive Command Handling**: Responds to conversational cues and specific commands.
* **Powerful Message Scheduling**: An interactive, multi-step command for moderators and admins to schedule messages. Supports both one-time posts (at a specific date and time) and recurring interval posts (e.g., every 24 hours).
* **Role-Based Permissions**: Core commands like scheduling and language settings are restricted to users with Moderator or Administrator roles.
* **Localization Support**: Bot responses can be translated into multiple languages using the `gettext` framework. English (`en`) and French (`fr`) are supported out of the box.
* **Configurable**: Key settings like the bot token, command prompt, and language can be easily changed in a configuration file.
* **Natural Interaction**: A "typing" indicator is used before sending messages to feel more like a real user.

## Setup and Installation

Follow these steps to get the bot running on your own server.

### 1. Prerequisites

* Python 3.8 or higher
* A Discord Bot Token

### 2. Create a Discord Bot

1.  Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2.  Click "New Application".
3.  Give your application a name and click "Create".
4.  Navigate to the "Bot" tab on the left.
5.  Click "Add Bot" and confirm.
6.  Under the bot's username, click "Copy" to copy the **Bot Token**. You will need this for the configuration file.
7.  Make sure to enable the **Server Members Intent** and **Message Content Intent** under the "Privileged Gateway Intents" section.

### 3. Installation

1.  Clone the repository:
    ```
    git clone <your-repository-url>
    cd <your-repository-folder>
    ```

2.  Create and populate a `requirements.txt` file with the necessary dependencies:
    ```
    discord.py
    pytz
    apscheduler
    ```

3.  Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

4.  Create a configuration file named `config.json` in the root directory. See the **Configuration** section below for details.

5.  Create a directory for localization files:
    ```
    mkdir res
    ```
    Place your compiled `.mo` language files here (e.g., `res/messages_fr.mo`).

6.  Run the bot:
    ```
    python main.py
    ```

## Configuration

The bot is configured using the `config.json` file. Create this file in the root directory and add the following content, replacing the placeholder values with your own.

```json
{
    "token": "YOUR_DISCORD_BOT_TOKEN_HERE",
    "prompt": "!",
    "language": "en"
}

 * token: (Required) Your secret bot token from the Discord Developer Portal. Do not share this token or commit it to a public repository.
 * prompt: The prefix the bot will use for commands. Defaults to ! if not provided.
 * language: The default language for the bot's responses. Supported values are "en" and "fr".
Note on Roles: The permission-locked commands (language, schedule) require server roles named Moderator and Administrator by default. If your role names are different, you will need to adjust them in the bot's code.
Available Commands
The bot responds to commands based on matching phrases within messages.
Admin & Moderator Commands
 * !language <en|fr>
   Changes the bot's response language. Requires Moderator or Administrator role.
   * Example: !language fr
 * !schedule
   Initiates an interactive setup to schedule a message. The bot will prompt you for the channel, message content, and timing. Requires Moderator or Administrator role.
 * !help
   Displays a helpful embed with a list of available commands.
Conversational Commands
These commands are triggered when a message contains the following phrases.
 * ...hug...
   The bot responds with a friendly hug and reacts to your message.
 * ...hi sprout...
   The bot greets you with one of several randomized friendly messages.
 * ...best part...day...
   The bot will ask for permission to tell you about the best part of its day, and will wait for a "yes" or "no" response.
 * ...hi avi...
   A special greeting for Avi.
 * ...about nicole...
   A special, playful response about Nicole.
Localization
This bot uses the gettext library for localization. To add support for a new language:
 * Create a .po file for your target language (e.g., es for Spanish).
 * Translate the strings from the source code.
 * Compile the .po file into a .mo file.
 * Place the compiled file in the res directory with the name messages_xx.mo, where xx is the two-letter language code (e.g., res/messages_es.mo).
 * Set the "language" in config.json to your new locale (e.g., "es_ES").
Credits
This bot template was created by Zachary Oberg.

