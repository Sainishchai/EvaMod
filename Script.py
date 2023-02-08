class script(object):
    START_TXT = """👋🏻 Hᴇʟʟᴏ {}.

𝖨𝗆 𝖺𝗇 𝖺𝗎𝗍𝗈 𝖿𝗂𝗅𝗍𝖾𝗋 𝖻𝗈𝗍 𝗐𝗁𝗂𝖼𝗁 𝖼𝖺𝗇 𝗉𝗋𝗈𝗏𝗂𝖽𝖾 𝗆𝗈𝗏𝗂𝖾𝗌 𝗂𝗇 𝗒𝗈𝗎𝗋 𝗀𝗋𝗈𝗎𝗉𝗌. 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 𝖺𝗇𝖽 𝗉𝗋𝗈𝗆𝗈𝗍𝖾 𝗆𝖾 𝖺𝗌 𝖺𝖽𝗆𝗂𝗇 𝗍𝗈 𝗅𝖾𝗍 𝗆𝖾 𝗀𝖾𝗍 𝗂𝗇 𝖺𝖼𝗍𝗂𝗈𝗇.

𝖢𝗅𝗂𝖼𝗄 𝗈𝗇 𝗍𝗁𝖾 𝖧𝖾𝗅𝗉 𝖻𝗎𝗍𝗍𝗈𝗇 𝖿𝗈𝗋 𝖬𝗈𝗋𝖾..."""
    URL_TXT = """<b>URL SHORT</b>

<b><u>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ</u></b>

Use /short the leave a space and paste your link and send me as a message.

Example: <code>/short http://t.me/cv_autofilter_bot</code>
"""
    PING_TXT = """
<b>SPEED</b>

This module helps you to find my speed.

<b><u>Commands and usage:</u></b>

• /ping - To get your ping.

<b>Note:</b> This commands can be used in both pms and groups."""
    SHARE_TXT = """
<b>SHARE TEXT</b>

In this module you can make a link of text.

<b><u>Commands and usage:</u></b>

/share - <code>reply to a text to generate sharable link.</code>"""
    HELP_TXT = """<b>Welcome To My Help Module</b>"""
    IMDB_TXT = """
<b>IMDB</b>

Search IMDB results and customize IMDB Template. You can customize them as per your needs.

<b>Comands & Usage:</b>

/imdb  - <code>get the film information from IMDb source.</code>
/set_template - <code>To set Custom template for your group.</code>

<a href=https://t.me/TeamEvamaria/9>Know More....</a>"""
    ABOUT_TXT = """<b>◎ Nᴀᴍᴇ: ᴋᴜᴛᴛᴜ ʙᴏᴛ™ 🤖
◎ Cʀᴇᴀᴛᴏʀ: <a href=https://t.me/wudixh1>This Person</a>
◎ Lᴀɴɢᴜᴀɢᴇ: Pʏᴛʜᴏɴ 3
◎ Dᴀᴛᴀ Bᴀsᴇ: Mᴏɴɢᴏ DB
◎ Bᴏᴛ Sᴇʀᴠᴇʀ: QuickFast</b>"""
    BATCH_TXT = """ 
<b>BATCH</b>

You can use the filestore feature for any public channel without bot being admin in that channel (only media messages  can be stored). 

</b>Commands & Usage:</b>

1. For a single file use /link command as reply to file.(only video, audio and documents are supported for now.)

2. For creating batch files , use /batch </code><starting message link> <ending message link>.</code>
Example: </code/batch https://t.me/teamEvaMaria/2</code> </code>https://t.me/teamEvaMaria/9</code>

"""
    BATH_TXT = """ 
<b>BATCH</b>

You can use the filestore feature for any public channel without bot being admin in that channel (only media messages  can be stored). 

</b>Commands & Usage:</b>

1. For a single file use /link command as reply to file.(only video, audio and documents are supported for now.)

2. For creating batch files , use /batch </code><starting message link> <ending message link>.</code>
Example: </code/batch https://t.me/teamEvaMaria/2</code> </code>https://t.me/teamEvaMaria/9</code>

"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. This bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/cv_autofilter_bot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""

    BAN_TXT = """

<b>BAN</b>

Ban lets you ban a user from the group without giving him the possibility to join again using the link of the group.

<b><u>Commands and usage:</u></b>

/ban - <code>Ban a user.</code>
/tban - <code>temporarily ban a user. Eg: Time Values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.</code>
/unban - <code>Unban a user.</code>

"""

    GAMES_TXT = """

<b>GAMES</b>

In this module you can play games.

<b><u>Commands and usage:</u></b>

/dice - <code>roll the dice</code>
/throw or /dart - <code>i don't know wtf is this myr!.</code>
/goal or /shoot - <code>to play football :|</code>
/luck - <code>നോക്കീട്ടു കാര്യം ഇല്ല നിന്റെ കാര്യം പോക്കാ ☻︎‌‌</code>

"""

    PURGE_TXT = """

</b>PURGE<b>

This module help you to delete a lot of messages from group

<b><u>Commands and usage:</u></b>

/purge - <code>Delete all messages from the replied to message, to the current message.</code>

"""

    TELEGRAPH_TXT = """

<b>TELEGRAPH</b>

This Module helps you to upload media file on telegra.ph.

<b><u>Commands and usage:</u></b>

/telegraph - <code>reply this command on a picture or video under 5mb for Telegraph link.</code>

Note: Maximum file size limit is 5mb.

"""


    JSON_TXT = """

<b>JSON</b>

Json can fetch you all the data contained in a telegram message.

<b><u>Commands and usage:</u></b>

/json - <code>to know user details. Supports both PM and Groups.</code>

Note: Everyone can use this command , if spaming happens bot will automatically ban you from the group.

"""


    KICK_TXT = """

<b>KICK</b>

Kick incative members from group. Add me as admin with ban users permission in group.


<b><u>Commands and usage:</u></b>

/inkick - <code>command with required arguments and i will kick members from group.</code>
/instatus - <code>to check current status of chat member from group.</code>
/inkick within_month long_time_ago - <code>to kick users who are offline for more than 6-7 days.</code>
/inkick long_time_ago - <code>to kick members who are offline for more than a month and Deleted Accounts.</code>
/dkick - <code>to kick deleted accounts.</code>

"""


    MUTE_TXT = """

<b>MUTE</b>

Mute puts a user in read-only mode. He can read but he can't send any messages.

<b><u>Commands and usage:</u></b>

/mute - <code>Mute a user.</code>
/unmute - <code>Unmute a user.</code>
/tmute - <code>Temporarily mute a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.</code>

"""


    REPORT_TXT = """

<b>REPORT</b>

This module helps you to report a message or a user to the admins of the respective group.

<b><u>Commands and usage:</u></b>

/report or @admins - <code>to report a message or user to the group admins.</code>

"""


    STICKER_TXT = """

<b>STICKER ID</b>

This Module Helps you to find a sticker's id.

<b><u>Commands and usage:</u></b>

/stickerid - <code>reply to a sticker to know that sticker's id.</code>

"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    
    
    OWNER_INFO = """
○ 𝖢𝗋𝖾𝖺𝗍𝗈𝗋 : <a href='https://t.me/im_goutham_josh'>𝖳𝗁𝗂𝗌 𝖯𝖾𝗋𝗌𝗈𝗇</a>"""
    
    
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """○ Tᴏᴛᴀʟ Fɪʟᴇs: <code>{}</code>
○ Tᴏᴛᴀʟ Usᴇʀs: <code>{}</code>
○ Tᴏᴛᴀʟ Cʜᴀᴛs: <code>{}</code>
○ Usᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{}</code> 𝙼𝚒𝙱
○ Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
