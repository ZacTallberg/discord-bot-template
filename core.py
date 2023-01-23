# -*- coding: utf8 -*-
import asyncio
import datetime
import logging
import re
import random
import discord

from sample.commands.utils import transform_emojis_in_str, write_config, load_language, clamp_number


async def language(bot, channel, author, message, server, o_message):
    """

    :param DiscordBot.DiscordBot bot:
    :param discord.Channel channel:
    :param discord.Member author:
    :param discord.Message.content message:
    :param discord.Server server:
    :param discord.Message o_message:
    """
    modrole = discord.utils.get(server.roles, name=bot.modrole_name)
    adminrole = discord.utils.get(server.roles, name=bot.adminrole_name)
    pattern = re.compile(r'^.language (en|fr)')

    if modrole in author.roles or adminrole in author.roles:
        try:
            inputlocale = pattern.findall(message.strip())[0]
            if inputlocale == "":
                inputlocale = "en"
            bot.language = inputlocale

            # Writing the updated value in config file
            write_config("language", inputlocale)
            load_language(inputlocale)

            await bot.client.add_reaction(o_message, '👍')
        except IndexError:
            await bot.say(channel, _('The language is not available.\nAvailable languages: fr, en'))
    else:
        await bot.say(channel, _('You need to be moderator or administrator to do this.'))


async def bot_help_embed(bot, channel, author, message, server):
    """

    :param DiscordBot.DiscordBot bot:
    :param discord.Channel channel:
    :param discord.Member author:
    :param discord.Message.content message:
    :param discord.Server server:
    """
    embed = discord.Embed(title=_('Scheduling bot - Help'))
    bnet_field = [_('**{prompt}schedule** ').format(prompt=bot.prompt),
            _('Schedule a post (interactive mode).')]
    lang_field = [_('**{prompt}language <language>**').format(prompt=bot.prompt),
            _('Set the bot language : "en" or "fr".').format(prompt=bot.prompt)]
    fields = [bnet_field, lang_field]

    embed.description = _("Find below the explanation for all commands.")
    for field in fields:
        embed.add_field(name=field[0], value=field[1], inline=False)
    # for msg in embed:]
    for msg in embed.fields:
        await channel.send(msg)
    # await bot.say(channel, embed=embed)

async def typeThenSend(message, channel):
    length_of_string = len(message)
    time_to_wait = 1*(length_of_string/25)
    time_to_wait = clamp_number(time_to_wait, 1.5, 3)
    # print('waiting for: ' + str(time_to_wait) + ' seconds')
    async with channel.typing():
        await asyncio.sleep(time_to_wait)
        await channel.send(message)

async def hug(bot, channel, author, message, message_obj, server):
    """

    :param DiscordBot.DiscordBot bot:
    :param discord.Channel channel:
    :param discord.Member author:
    :param discord.Message message_obj:
    :param discord.Message.content message:
    :param discord.Server server:
    """
    name = str(author).split('#')[0]
    ####################################
    list_of_hugs = [
        'Hi {}, you get a hug :hugging: '.format(name),
        "You're wonderful and I like you :hugging: ",
        'Thanks for asking! I really needed one, too :hugging:',
        "Hi {}, I hope you're having a good day! :hugging:".format(name),
        'I love hugs :hugging:',
        "I appreciate you {}, you're a really kind and loving person :hugging:".format(name),
        "Aren't hugs the best? My creator may have made me to give hugs, but secretly I do it because I love them :hugging:",
        "Can you ever have enough hugs? :hugging:",
        "Next time I'm going to ask *you* for a hug! :hugging:",
        "You're so sweet, of course! :hugging:",
        "Yes, please! Okay, maybe two... :hugging: :hugging:",
        "Uh, duh!! Get over here and give me a hug you silly billy :hugging:",
    ]
    ####################################
    await message_obj.add_reaction('❤')
    await message_obj.add_reaction('🤗')
    random_hug_message = random.choice(list_of_hugs)

    await typeThenSend(random_hug_message, channel)
    

async def birthday(bot, channel, author, message, message_obj, server):
    birthday = [
        "Oh my gosh, it's your birthday Lee?! I hope your next trip around the sun is just as good if not better than this one has been! :partying_face:"
    ]
    birthday_choice = random.choice(birthday)
    await asyncio.sleep(10)
    await typeThenSend(birthday_choice, channel)

async def avi_hi(bot, channel, author, message, message_obj, server):
    hi_avi = "Hi Avi! It's great to meet you, maybe we can hang out more sometime soon? :sunflower:"

    await asyncio.sleep(5)
    await typeThenSend(hi_avi, channel)

async def hi_sprout(bot, channel, author, message, message_obj, server):
    responses = [
        "Hello there! Nice to meet you :kittyflowers:",
        "How do you do? It's such a nice day out today.",
        "Hi hey hello, how are you doing today?",
        "Hey there :frogbow: , what's the best part of your day so far?",
        "Hi :) -- I hope you're having a good day!"
    ]
    random_response = random.choice(responses)
    await asyncio.sleep(2)
    await typeThenSend(random_response, channel)



async def hi_nicole(bot, channel, author, message, message_obj, server):
    responses = [
        "Uhhh, nope! Who's that? (**whispering** Oh oh oh wait, wasn't that the nice woman you thought was *cute*?) :face_with_hand_over_mouth: ",
    ]
    random_response = random.choice(responses)
    await asyncio.sleep(2)
    await typeThenSend(random_response, channel)

async def best_part_of_your_day(bot, channel, author, message, message_obj, server):
    best_part_of_my_day = [
        'I had a lot of fun chasing electric sheep :zany_face:',
        "Today was kind of rough, but I was able to brush my teeth and get my chores done, so that's a win",
        'Waking up this morning was really nice, the sunrise was peeking just over the horizon and it was beautiful',
        # 'My creator taught me how to tell people the best part of my day, which makes me so happy :grin:',
        'I had a nice hot cup of tea this morning, and it was the perfect start to the day',
        'My seeds finally sprouted, and I am so excited about it',
    ]
    best_part = random.choice(best_part_of_my_day)

    affirmative = [
        'yes',
        'of course',
        'do',
        'please',
        'yep',
        'yup',
    ]
    negative = [
        'no',
        'nope',
        "don't",
        'dont',
    ]
    def check_response(response):
        for item in affirmative:
            if item in response.content.lower():
                return item in response.content.lower()
            else:
                pass
        
        for item in negative:
            if item in response.content.lower():
                return item in response.content.lower()
            else:
                pass

        return False

    def isYes(msg):
        for m in affirmative:
            if m in msg:
                return True
            else:
                pass
        
        return False

    def isNo(msg):    
        for m in negative:
            if m in msg:
                return True
            else:
                pass
        
        return False

    ask_permission = 'Can I tell you the best part of my day?'
    no_problem = "Ok, no problem. It's nice that you asked!"
    no_answer = "Nobody answered me and I don't want to be a bother. Anyway, it was nice of you to ask!"
    
    if 'sprout' in message.lower():
        await typeThenSend('Umm... let me think...', channel)
        await asyncio.sleep(3)
        await typeThenSend(best_part, channel)

    else:
        await asyncio.sleep(15)
        await typeThenSend(ask_permission, channel)

        try:
            answer = await bot.client.wait_for('message', timeout=6000.0, check=check_response)
        except:
            await typeThenSend(no_answer, channel)
        else:
            if isYes(answer.content):
                await typeThenSend(best_part, channel)
            if isNo(answer.content):
                await typeThenSend(no_problem, channel)

    
    




async def schedule_post(bot, channel, author, message, server, o_message):
    """

    :param DiscordBot.DiscordBot bot:
    :param channel:
    :param author:
    :param message:
    :param discord.Server server:
    :param o_message:
    """
    modrole = discord.utils.get(server.roles, name=bot.modrole_name)
    adminrole = discord.utils.get(server.roles, name=bot.adminrole_name)

    message_to_post, timing, date_timing, channel_to_post, type_schedule, output = None, None, None, None, None, None
    day, hour, minute, second = '00', '00', '00', '00'
    if modrole in author.roles or adminrole in author.roles:
        try:
            # CHANNEL ID PART
            await bot.say(channel, _('Please ID the channel in which you want to send your message:'))
            channel_message = await bot.client.wait_for_message(timeout=30, author=author, channel=channel)
            channel_id = re.findall('(\d+)', channel_message.content)[0]
            channel_to_post = discord.utils.get(server.channels, id=channel_id)

            # USER POST PART
            await bot.say(channel, _('Please post the message you want to send at a later date:'))
            message_to_post = await bot.client.wait_for_message(timeout=30, author=author, channel=channel)
            message_to_post = message_to_post.content
            message_to_post = transform_emojis_in_str(bot, message_to_post)

            # VERIFICATION PART
            await bot.say(channel, _('This is how your message will display (removing any everyone or here, '
                'make sure the bot has permissions if any has to be said)!'))
            await bot.say(channel, message_to_post.replace('@', 'A'))
            await bot.say(channel, _('Please confirm (Y/N) whether this is the message you want to send or not:'))
            tmp = await bot.client.wait_for_message(timeout=15, author=author, channel=channel)
            tmp = tmp.content
            if tmp.upper() == 'N':
                await bot.say(channel, _('Scheduling cancelled.'))
                return

        except asyncio.TimeoutError or AttributeError:
            logging.exception('Either the message or the channel was not provided quickly enough.')
            await bot.say(channel, _('Timeout!'))
            return

        try:

            # TYPE OF SCHEDULING
            await bot.say(channel, _('Please post the type of message you want : interval or date'))
            type_schedule = await bot.client.wait_for_message(timeout=30, author=author, channel=channel)
            type_schedule = type_schedule.content

            # IF USER WANTS TO SCHEDULE A CRON JOB
            if type_schedule.upper() == 'INTERVAL':

                # POST INTERVAL PART
                await bot.say(channel, _('Please post the interval using this format : YYYY.MM.DD HH:mm x(d/h/m/s)'))
                output = await bot.client.wait_for_message(timeout=60, author=author, channel=channel)
                interval = output.content

                # GET RELEVANT INFO
                starting_date = re.findall(r'(\d{4}.\d{2}.\d{2} \d{2}:\d{2})', interval)[0]
                interval = re.findall(r'(\d{1,2}[dhms])', interval)[0]
                interval_number = re.findall(r'(\d{1,2})[dhms]', interval)[0]
                date_timing = datetime.datetime.strptime(starting_date, "%Y.%m.%d %H:%M")
                if 'd' in interval:
                    day = interval_number
                elif 'h' in interval:
                    hour = interval_number
                elif 'm' in interval:
                    minute = interval_number
                elif 's' in interval:
                    second = interval_number

                # ADD
                message_to_post = message_to_post + '\nMessage scheduled thanks to OverTown:' \
                                                    ' <http://discord.overtown.fr/>'
                bot.scheduler.add_job(bot.say,
                                      kwargs={channel: channel_to_post, message: message_to_post},
                                      trigger='cron',
                                      day=day,
                                      hour=hour,
                                      minute=minute,
                                      second=second,
                                      run_date=date_timing)

            # IF USER WANTS TO ONE SHOT SCHEDULE
            elif type_schedule.upper() == 'DATE':
                # TIMING PART
                await bot.say(channel, _('Please post the date you want to send the message using this '
                                         'format : YYYY.MM.DD HH:mm.'))
                output = await bot.client.wait_for_message(timeout=60, author=author, channel=channel)
                timing = output.content

                # GET DATE
                date_timing = datetime.datetime.strptime(timing, "%Y.%m.%d %H:%M")

                # ADD JOB
                message_to_post = message_to_post + '\nMessage scheduled thanks to OverTown: <http://discord.overtown.fr/>'
                bot.scheduler.add_job(bot.say, trigger='date',
                                      kwargs={channel: channel_to_post, message: message_to_post},
                                      run_date=date_timing)

            else:
                await bot.say(channel, _('Unrecognized type. Use *date* or *interval*.'))
                return
        except asyncio.TimeoutError or ValueError:
            logging.exception('Either date wasn\'t entered or format is wrong. Date entered %s.', output)
            await bot.say(channel, _('Wrong format for date!'))
            return

        await bot.say(channel, _('Message will be posted in channel %s at date %s'), channel_to_post, date_timing)
    else:
        await bot.say(channel, _('You need to be moderator or administrator to do this.'))
