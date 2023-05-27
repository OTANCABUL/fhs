# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL1, FORCE_SUB_CHANNEL2, FORCE_SUB_CHANNEL3, FORCE_SUB_CHANNEL4
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL2 and not FORCE_SUB_CHANNEL3 and not FORCE_SUB_CHANNEL4:
        return [
            [
                InlineKeyboardButton(
                    text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"
                ),
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
    if (
        not FORCE_SUB_CHANNEL4
        and not FORCE_SUB_CHANNEL3
        and not FORCE_SUB_CHANNEL2
    ):
        return [
            [
                InlineKeyboardButton(text="Cʜᴀɴɴᴇʟ-1", url=client.invitelink1),
            ],
            [
                InlineKeyboardButton(
                    text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"
                ),
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
    if FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2 and not FORCE_SUB_CHANNEL3 and not FORCE_SUB_CHANNEL4:
        return [
            [
                InlineKeyboardButton(text="Cʜᴀɴɴᴇʟ-1", url=client.invitelink1),
            ],
            [
                InlineKeyboardButton(text="Cʜᴀɴɴᴇʟ-2", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(
                    text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"
                ),
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
    if FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2 and FORCE_SUB_CHANNEL3 and not FORCE_SUB_CHANNEL4:
        return [
            [
                InlineKeyboardButton(
                    text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(text="Cʜᴀɴɴᴇʟ-1", url=client.invitelink1),
                InlineKeyboardButton(text="Cʜᴀɴɴᴇʟ-2", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="Cʜᴀɴɴᴇʟ-3", url=client.invitelink3),
            ],
            [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
        ]
    if FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2 and FORCE_SUB_CHANNEL3:
        return [
            [
                InlineKeyboardButton(
                    text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(text="Cʜᴀɴɴᴇʟ-1", url=client.invitelink1),
                InlineKeyboardButton(text="Cʜᴀɴɴᴇʟ-2", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="Cʜᴀɴɴᴇʟ-3", url=client.invitelink3),
                InlineKeyboardButton(text="Cʜᴀɴɴᴇʟ-4", url=client.invitelink4),
            ],
            [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
        ]


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL4 and not FORCE_SUB_CHANNEL3 and not FORCE_SUB_CHANNEL2 and FORCE_SUB_CHANNEL1:
        buttons = [
            [
                InlineKeyboardButton(text="Cʜᴀɴɴᴇʟ-1", url=client.invitelink1),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2 and not FORCE_SUB_CHANNEL3 and not FORCE_SUB_CHANNEL4:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ-1", url=client.invitelink1),
            ],
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ-2", url=client.invitelink2),
            ],            
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2 and FORCE_SUB_CHANNEL3 and not FORCE_SUB_CHANNEL4:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ-1", url=client.invitelink1),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ-2", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ-3", url=client.invitelink3),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2 and FORCE_SUB_CHANNEL3:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ-1", url=client.invitelink1),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ-2", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ-3", url=client.invitelink3),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ-4", url=client.invitelink4),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    
