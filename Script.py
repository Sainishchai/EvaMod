class script(object):
    START_TXT = """ππ» Hα΄ΚΚα΄ {}.

π¨π πΊπ πΊπππ πΏππππΎπ π»ππ ππππΌπ πΌπΊπ ππππππ½πΎ πππππΎπ ππ ππππ ππππππ. π π½π½ π¬πΎ π³π πΈπππ π¦ππππ πΊππ½ πππππππΎ ππΎ πΊπ πΊπ½πππ ππ ππΎπ ππΎ ππΎπ ππ πΊπΌππππ.

π’πππΌπ ππ πππΎ π§πΎππ π»πππππ πΏππ π¬πππΎ..."""
    URL_TXT = """<b>URL SHORT</b>

<b><u>Cα΄α΄α΄α΄Ι΄α΄s AΙ΄α΄ Usα΄Ι’α΄</u></b>

Use /short the leave a space and paste your link and send me as a message.

Example: <code>/short http://t.me/cv_autofilter_bot</code>
"""
    PING_TXT = """
<b>SPEED</b>

This module helps you to find my speed.

<b><u>Commands and usage:</u></b>

β’ /ping - To get your ping.

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

/imdbΒ  - <code>get the film information from IMDb source.</code>
/set_template - <code>To set Custom template for your group.</code>

<a href=https://t.me/TeamEvamaria/9>Know More....</a>"""
    ABOUT_TXT = """<b>β Nα΄α΄α΄: α΄α΄α΄α΄α΄ Κα΄α΄β’ π€
β CΚα΄α΄α΄α΄Κ: <a href=https://t.me/wudixh1>This Person</a>
β Lα΄Ι΄Ι’α΄α΄Ι’α΄: PΚα΄Κα΄Ι΄ 3
β Dα΄α΄α΄ Bα΄sα΄: Mα΄Ι΄Ι’α΄ DB
β Bα΄α΄ Sα΄Κα΄ α΄Κ: QuickFast</b>"""
    BATCH_TXT = """ 
<b>BATCH</b>

You can use the filestore feature for any public channel without bot being admin in that channel (only media messagesΒ  can be stored). 

</b>Commands & Usage:</b>

1. For a single file use /link command as reply to file.(only video, audio and documents are supported for now.)

2. For creating batch files , use /batch </code><starting message link> <ending message link>.</code>
Example: </code/batch https://t.me/teamEvaMaria/2</code> </code>https://t.me/teamEvaMaria/9</code>

"""
    BATH_TXT = """ 
<b>BATCH</b>

You can use the filestore feature for any public channel without bot being admin in that channel (only media messagesΒ  can be stored). 

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
β’ /filter - <code>add a filter in chat</code>
β’ /filters - <code>list all the filters of a chat</code>
β’ /del - <code>delete a specific filter in chat</code>
β’ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
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
β’ /connect  - <code>connect a particular chat to your PM</code>
β’ /disconnect  - <code>disconnect from a chat</code>
β’ /connections - <code>list all your connections</code>"""

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
/luck - <code>ΰ΄¨ΰ΅ΰ΄ΰ΅ΰ΄ΰ΅ΰ΄ΰ΅ΰ΄ΰ΅ ΰ΄ΰ΄Ύΰ΄°ΰ΅ΰ΄―ΰ΄ ΰ΄ΰ΄²ΰ΅ΰ΄² ΰ΄¨ΰ΄Ώΰ΄¨ΰ΅ΰ΄±ΰ΅ ΰ΄ΰ΄Ύΰ΄°ΰ΅ΰ΄―ΰ΄ ΰ΄ͺΰ΅ΰ΄ΰ΅ΰ΄ΰ΄Ύ β»οΈββ</code>

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
β’ /id - <code>get id of a specified user.</code>
β’ /info  - <code>get information about a user.</code>
β’ /imdb  - <code>get the film information from IMDb source.</code>
β’ /search  - <code>get the film information from various sources.</code>"""
    
    
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
β’ /logs - <code>to get the rescent errors</code>
β’ /stats - <code>to get status of files in db.</code>
β’ /delete - <code>to delete a specific file from db.</code>
β’ /users - <code>to get list of my users and ids.</code>
β’ /chats - <code>to get list of the my chats and ids </code>
β’ /leave  - <code>to leave from a chat.</code>
β’ /disable  -  <code>do disable a chat.</code>
β’ /ban  - <code>to ban a user.</code>
β’ /unban  - <code>to unban a user.</code>
β’ /channel - <code>to get list of total connected channels</code>
β’ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """β Tα΄α΄α΄Κ FΙͺΚα΄s: <code>{}</code>
β Tα΄α΄α΄Κ Usα΄Κs: <code>{}</code>
β Tα΄α΄α΄Κ CΚα΄α΄s: <code>{}</code>
β Usα΄α΄ Sα΄α΄Κα΄Ι’α΄: <code>{}</code> πΌππ±
β FΚα΄α΄ Sα΄α΄Κα΄Ι’α΄: <code>{}</code> πΌππ±"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
