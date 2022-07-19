# -*- coding: utf8 -*-
import json
import logging
import re

import discord

logger = logging.getLogger(__name__)


def load_config(key, default_value=None, config_file=None):
    if not config_file:
        config_file = 'config.json'

    with open(config_file, mode='r+', encoding='utf-8') as f:
        config = json.load(f)
        try:
            value = config[key]
            logger.info('The value for key {} is {}.'.format(key, value))
        except KeyError:
            value = default_value
            config.update({key: value})
            f.write(json.dumps(config))
            f.truncate()
            logger.info('The value for key {} is {}.'.format(key, value))
    return value


class DiscordBot(object):
    def __init__(self, prompt):
        super().__init__()
        self.client = discord.Client()
        self.prompt = prompt
        self.language = load_config("language", "en")
        self.modrole_name = load_config("modrole_name", 'Modération')
        self.adminrole_name = load_config("adminrole_name", 'Administration')
        self.default_emote = load_config("default_emote", 'robot')
        self.actions = {}
        self.user = None
        self.token = None
        self.scheduler = None

        @self.client.event
        async def on_ready():
            logger.info('Logged in as')
            logger.info(self.client.user.name)
            logger.info(self.client.user.id)
            logger.info('------')
            self.username = self.client.user.name
            self.user = self.client.user

        @self.client.event
        async def on_message(message):
            channel = message.channel
            author = message.author
            content = message.content
            message_obj = message
            if author != self.user:
                logger.info('Message received [{0}]: {1} - "{2}"'.format(channel, author, content))
                for regex, command in self.actions.values():
                    match = re.match(regex, content)
                    if match:
                        try:
                            await command(self, channel, author, content, message, message_obj, *match.groups())
                        except Exception as e:
                            logger.exception(e)
                            await self.say(channel, _("Shoot, looks like there's a problem: " + str(e)))
                        break

                
                        
    def run(self, token):
        self.token = token
        self.client.run(self.token)

    def register_action(self, regex, coro):
        logger.info('Registering action {0}'.format(regex))
        if regex in self.actions:
            logger.info('Overwriting regex {0}'.format(regex))
        self.actions[regex] = (re.compile(regex, re.IGNORECASE), coro)

    async def say(self, channel, message=None, embed=None, image=None):
        await channel.send(message)
