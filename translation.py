class Translation(object):
    
    START_TXT = """ <b> Hi {} ,
 I am a powerful rename bot! With 2GB+ file support and custom thumbnail and caption features.</b>
<b>Click help button to know more about me !</b>\n 
"""
    PROGRESS_BAR = """\n
╭───[**🔅Progress Bar🔅**]───⍟
│
├<b>📁 : {1} | {2}</b>
│
├<b>🚀 : {0}%</b>
│
├<b>⚡ : {3}/s</b>
│
├<b>⏱️ : {4}</b>
╰─────────────────⍟"""
    HELP_TXT = """
<b><i><u>✨ AVAILABLE COMMANDS:</u>
➢ /start - check i'm alive 
➢ /plans - check available plan info
➢ /settings - configure your settings 
➢ /queue - check your queued task status
➢ /addcaption - To add your custom caption 
➢ /showcaption - To see your custom caption
➢ /deletecaption - To delete your custom caption
➢ /showthumb - To see your custom thumbnail
➢ /deletethumb - To delete your custom thumbnail
➢ /add_prefix - To add a prefix along with your filename 
➢ /add_suffix - To add a suffix along with your filename 

<u>🔥 FEATURES:</u>
• upgrade your premium plan for Better renaming experience.
• send a photo to me to add as custom Thumbnail.
• send your files to me to rename..</i></b>
""" 
    OWNER_COMMANDS_TXT = """
<b><i><u>👨 OWNER COMMANDS:</u>

• Following commands only can use bot owner.

➢ /ban - To ban a user 
➢ /unban - To unban a user 
➢ /stats - To get bot users stats
➢ /broadcast - To broadcast messages to users</i></b>
"""
    ABOUT_TXT = """
╔════❰ RENAME BOT ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼📃ʙᴏᴛ : [{}](https://t.me/{})
║┣⪼👦Deployer : [GreyMatter's Owner](https://t.me/GreyMatter_Owner)
║┣⪼📡ʜᴏsᴛᴇᴅ ᴏɴ : Koyeb
║┣⪼🗣️ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ3
║┣⪼📚ʟɪʙʀᴀʀʏ : ᴘʏʀᴏɢʀᴀᴍ ᴀsʏɴᴄɪᴏ {} 
║┣⪼🗒️ᴠᴇʀsɪᴏɴ : {}
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁۪۪
"""
    
    THUMBNAIL_TXT = """
<b>🖼️ CUSTOM THUMBNAIL</b>

you can add custom thumbnail simply by sending a photo to me 
"""
    CUSTOM_CAPTION_TXT = """
<b>📝 CUSTOM CAPTION</b>

➢ /addcaption <your caption> - To add your custom caption 

<b>AVAILABLE FILLINGS:</b>
• `{filename}` - new file name
• `{size}` - size of the media
• `{duration}` - duration of the media
"""
    
    SETTINGS_TXT = "<b><u>⚙️ SETTINGS</u>\nConfigure your settings using this buttons</b>"
    BANNED_TXT = "<b>Sorry dude, You would be banned from using me</b>"
    DOWNLOAD_START_TXT = "<b>Downloading To My server !!</b>"
    UPLOAD_START_TXT = "<b>Uploading into telegram</b>"
    UPLOAD_SUCCESS_TXT = "<b>Thank you for Using Me ❤️</b>"
    NEW_CUSTOM_THUMB_TXT = "✔️ Thumbnail Successfully Added"
    REMOVE_CUSTOM_THUMB_TXT = "🗑️ Thumbnail Successfully Removed"
    DOWNLOAD_SUCCESS_TXT = "<b>Media Downloded successfully 🎉</b>"
    THUMB_NOT_FOUND_TXT = "Didn't found any thumbnail yet"
    REPLY_MEDIA_TXT = "<b>Please Reply To An File or video or audio With filename & extension</b>"
