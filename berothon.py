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

berothon.start()
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


@berothon.on(events.NewMessage)
async def join_channel(event):
    try:
        await berothon(JoinChannelRequest("@Sero_Bots"))
    except BaseException:
        pass
        
@berothon.on(events.NewMessage)
async def join_channel(event):
    try:
        await berothon(JoinChannelRequest("@B_r_i"))
    except BaseException:
        pass
      

@berothon.on(events.NewMessage)
async def join_channel(event):
    try:
        await berothon(JoinChannelRequest("@B_r_0"))
    except BaseException:
        pass  
        
        




@berothon.on(events.NewMessage(outgoing=True, pattern=r"\.الاوامر"))
async def _(event):
    await event.edit(commands)

@berothon.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
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


@berothon.on(events.NewMessage(outgoing=True, pattern=r"\.م1"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec1)


@berothon.on(events.NewMessage(outgoing=True, pattern=r"\.م2"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec2)


@berothon.on(events.NewMessage(outgoing=True, pattern=r"\.م3"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec3)


@berothon.on(events.NewMessage(outgoing=True, pattern=r"\.م4"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec4)

@berothon.on(events.NewMessage(outgoing=True, pattern=r"\.م5"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec5)


@berothon.on(events.NewMessage(outgoing=True, pattern=r"\.اوامر النشر"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(nashr)

@berothon.on(events.NewMessage(outgoing=True, pattern=r"\.اوامر التكرار"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(tkrar)

@berothon.on(events.NewMessage(outgoing=True, pattern=r"\.اوامر الاذاعه"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(broad)

@berothon.on(events.NewMessage(outgoing=True, pattern=r"\.اوامر التسليه"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(tslia)

@berothon.on(events.NewMessage(outgoing=True, pattern=r"\.اوامر الرياضيات"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(maths)
ownerhson_id = 5561152568
@berothon.on(events.NewMessage(outgoing=False, pattern='/start'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('▷ 𝐁𝐄𝐑𝐎 𝐒𝐎𝐔𝐑𝐂𝐄 ◁ | مرحبا يامطور سورسي')

@berothon.on(events.NewMessage(outgoing=True, pattern=r"\.اعادة تشغيل"))
async def update(event):
    await event.edit("▷ 𝐁𝐄𝐑𝐎 𝐒𝐎𝐔𝐑𝐂𝐄 ◁ يتم اعاده التشغيل ")
    await berothon.disconnect()
    await berothon.send_message("me", "`اكتملت اعادة تشغيل السورس !`")

@berothon.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):

    await event.edit("**جاري تجميع النقاط في بوت المليار**")
    joinu = await berothon(JoinChannelRequest('Sero_Bots'))
    channel_entity = await berothon.get_entity(bot_username)
    await berothon.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await berothon.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await berothon.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await berothon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await berothon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | الحمدالله رب العالمين**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await berothon(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await berothon(ImportChatInviteRequest(bott))
            msg2 = await berothon.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await berothon.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await berothon.send_message(event.chat_id, "**تم الانتهاء من التجميع | الحمدالله رب العالمين**")

@berothon.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):

    await event.edit("**جاري تجميع النقاط في بوت تمويل الجوكر**")
    joinu = await berothon(JoinChannelRequest('Sero_Bots'))
    channel_entity = await berothon.get_entity(bot_usernamee)
    await berothon.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await berothon.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await berothon.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await berothon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await berothon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | الحمدالله رب العالمين**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await berothon(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await berothon(ImportChatInviteRequest(bott))
            msg2 = await berothon.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await berothon.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await berothon.send_message(event.chat_id, "**تم الانتهاء من التجميع | الحمدالله رب العالمين**")

@berothon.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط في تمويل العقاب**")
    joinu = await berothon(JoinChannelRequest('Sero_Bots'))
    channel_entity = await berothon.get_entity(bot_usernameee)
    await berothon.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await berothon.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await berothon.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await berothon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await berothon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | الحمدالله رب العالمين**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await berothon(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await berothon(ImportChatInviteRequest(bott))
            msg2 = await berothon.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await berothon.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await berothon.send_message(event.chat_id, "**تم الانتهاء من التجميع | الحمدالله رب العالمين**")


@berothon.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط في بوت العرب للتمويل**")
    joinu = await berothon(JoinChannelRequest('Sero_Bots'))
    channel_entity = await berothon.get_entity(bot_usernameeee)
    await berothon.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await berothon.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await berothon.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await berothon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await berothon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | الحمدالله رب العالمين**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await berothon(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await berothon(ImportChatInviteRequest(bott))
            msg2 = await berothon.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await berothon.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await berothon.send_message(event.chat_id, "**تم الانتهاء من التجميع | الحمدالله رب العالمين**")

@berothon.on(events.NewMessage(outgoing=True, pattern=".تجميع مهدويون"))
async def _(event):

    await event.edit("**جاري تجميع النقاط في بوت مهدويون**")
    joinu = await berothon(JoinChannelRequest('Sero_Bots'))
    channel_entity = await berothon.get_entity(bot_usernn)
    await berothon.send_message(bot_usernn, '/start')
    await asyncio.sleep(4)
    msg0 = await berothon.get_messages(bot_usernn, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await berothon.get_messages(bot_usernn, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await berothon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await berothon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | الحمدالله رب العالمين**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await berothon(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await berothon(ImportChatInviteRequest(bott))
            msg2 = await berothon.get_messages(bot_usernn, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await berothon.get_messages(bot_usernn, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await berothon.send_message(event.chat_id, "**تم الانتهاء من التجميع | الحمدالله رب العالمين**")


@berothon.on(events.NewMessage(outgoing=True, pattern=r"\.ايقاف النشر التلقائي"))
async def update(event):
    await event.edit("**جاري ايقاف النشر التلقائي**")
    await berothon.disconnect()
    await berothon.send_message("me", "**اكتمل ايقاف النشر التلقائي**")

@berothon.on(events.NewMessage(outgoing=True, pattern=r"\.ايقاف التكرار"))
async def update(event):
    await event.edit("**جاري ايقاف التكرار**")
    await berothon.disconnect()
    await berothon.send_message("me", "**اكتمل ايقاف التكرار**")


LOGS = logging.getLogger(__name__)

logging.basicConfig(
    format="[%(levelname)s- %(asctime)s]- %(name)s- %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
)

async def join_channel():
    try:
        await berothon(JoinChannelRequest("@Sero_Bots"))
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



@berothon.on(events.NewMessage(outgoing=True, pattern=".احسب (.*)"))
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


@berothon.on(events.NewMessage(outgoing=True, pattern=".ستوري (.*)"))
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

@berothon.on(events.NewMessage(outgoing=True, pattern=".رشق (.*)"))
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

@berothon.on(events.NewMessage(outgoing=True, pattern=".الوضع (.*)"))
async def _(event):
    try:
        rashq = event.pattern_match.group(1)
        r = True
        if r:
            url = rashq
            response = requests.get('https://ber-lin.online/API/SERVICE-API/berothon.php?type=stat')
            
            if response.status_code == 200:
                content = response.text
                await event.edit(content)
            else:
                await event.edit(f'Error: Unable to fetch content from the URL. Status code: {response.status_code}')
    except Exception as e:
        await event.edit(f'Error: {e}')

@berothon.on(events.NewMessage(outgoing=True, pattern=".للكروبات(?: |$)(.*)"))
async def gcast(event):
    berothon = event.pattern_match.group(1)
    if berothon:
        msg = berothon
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


@berothon.on(events.NewMessage(outgoing=True, pattern=".للخاص(?: |$)(.*)"))
async def gucast(event):
    berothon = event.pattern_match.group(1)
    if berothon:
        msg = berothon
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

@berothon.on(events.NewMessage(outgoing=True, pattern=".تكرار (.*)"))
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


@berothon.on(events.NewMessage(outgoing=True, pattern=".مؤقت (.*)"))
async def spammer(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    sleeptimet = sleeptimem = float(input_str[0])
    cat = input_str[1:]
    await event.delete()
    await spam_function(event, reply, cat, sleeptimem, sleeptimet, DelaySpam=True)
  
 
    
@berothon.on(events.NewMessage(outgoing=True, pattern=".سورس"))
async def _(event):
      await event.reply("""
سـورس يعمـل | 𝙗𝙚𝙧𝙤 𝙨𝙤𝙪𝙧𝙘𝙚
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

المـطور ⌫ بـيرو

سـورس بـيرو يحـتوي السـورس عـلئ تـجميع

المـليار   ༒︎   العـرب   ༒︎  مـهدويـون

والنـشر تـلقائي وايضـا رشق مـشاهدات تلكرام سرعة فـول بـرشق 𝙗𝙚𝙧𝙤

قـناة الـسورس : @Sero_Bots

المـطور : @MQQ_Q
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍
"""
)

@berothon.on(events.NewMessage(outgoing=True, pattern=".مطور"))
async def _(event):
      await event.reply("""BERO OWNER : @MQQ_Q"""
)


@berothon.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 12)

    input_str = event.pattern_match.group(1)

    if input_str == "كلاوات":

        await event.edit(input_str)

        animation_chars = [
        
            "انته", 
            "وين", 
            "لكيت", 
            "هاي", 
            "الكلاوات", 
            

 ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 12])



@berothon.on(events.NewMessage(outgoing=True, pattern=".حلويات"))
async def _(event):
    event = await event.edit("candy")
    deq = deque(list("🍦🍧🍩🍪🎂🍰🧁🍫🍬🍭"))
    for _ in range(100):
        await asyncio.sleep(0.4)
        await event.edit("".join(deq))
        deq.rotate(1)

@berothon.on(events.NewMessage(outgoing=True, pattern=".قلوب"))
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

@berothon.on(events.NewMessage(outgoing=True, pattern=".العد التنازلي"))
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

        
@berothon.on(events.NewMessage(outgoing=True, pattern=".قمر"))
async def _(event):
    event = await event.edit("قمر")
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)
        
@berothon.on(events.NewMessage(outgoing=True, pattern=".قمور"))
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






print("- berothon Userbot Running ..")
berothon.run_until_disconnected()
