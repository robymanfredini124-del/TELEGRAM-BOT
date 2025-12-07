"""
╔══════════════════════════════════════════════════════════════════════╗
║                 ⚡ HYPER-X BOT SCRIPT v3.0 (ULTIMATE) ⚡             ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  [REQUIRED PACKAGES]                                                 ║
║  >>> pip install python-telegram-bot httpx                           ║
║                                                                      ║
║  [SYSTEM REQUIREMENTS]                                               ║
║  • Python 3.9+ (Optimized for Speed)                                 ║
║  • 4GB+ RAM Recommended for Multi-Threading                          ║
║                                                                      ║
║  [HOW TO RUN]                                                        ║
║  1. pip install python-telegram-bot httpx                            ║
║  2. python hyper_bot.py                                              ║
║                                                                      ║
║  [HYPER FEATURES]                                                    ║
║  🚀 Asyncio Event Loop Policy Optimized                              ║
║  ⚡ Zero-Latency Dispatcher                                          ║
║  🛡️ Anti-Flood Wait Bypass (Smart Rotation)                          ║
║  🌪️ Multi-Threaded Spam/NC Engine                                    ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""

import asyncio
import os
import sys
import time
import logging
import random
import re
from collections import deque
from datetime import datetime

from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram.constants import ChatType
from telegram.error import RetryAfter, TimedOut, NetworkError, BadRequest, Forbidden

# ⚡ HYPER LOGGING CONFIGURATION
logging.basicConfig(
    format="%(asctime)s - [HYPER] - %(levelname)s - %(message)s",
    level=logging.WARNING
)
logger = logging.getLogger("HyperBot")

# ═══════════════════════════════════════════════════════════════════════
# ⚡ CONFIGURATION - EDIT THESE VALUES
# ═══════════════════════════════════════════════════════════════════════
OWNER_ID = 5206554804
DEFAULT_AUTHORIZED_USERS = {5961069280}
HYPER_MODE = True

# ⚡ TOKEN POOL - ADD YOUR BOT TOKENS HERE
BOT_TOKENS = [
    "7708338822:AAGlO0fvzog9pMcxqB0Qd4cqxPhy9BZgwRA",
    "8224788790:AAHqGq3BJkeb0gw5dIXbA9BR7FxqsrI2T2U",
    "8503654663:AAGKQDNf-fZ0A3FxvyFCLXDBU6H1mSE-SCk",
    "8348897912:AAHk3On2Be2j-oOznNDPr4HgCVhDM51_vpc",
    "7550108763:AAGH0uL7j-ECOl5GfdEAOxZlK19x9nyQNKU",
    "8178216233:AAGulII1mHwmhcWkhIuladAbYXIDBAsRKfI",
    "8040898720:AAGPS-vKUF-J6xuvfHYmGovt2WepjhL-pdw",
    "5688907087:AAH5tm9XoIqVKuCRCELhghbQ_Rlxsiy9Bvs",
    "8131114314:AAExRSGzjSftN3nBqDaRQsUoYH8zLxiwIiI",
    "8196449050:AAHNMroXwQf53rqkPNn4ql781_kNoCJ-6y0",
    "8536542729:AAE3Tf6MBZiZQ2anqImYfv0pTP61nSmUg0w",
]

# ═══════════════════════════════════════════════════════════════════════
# ⚡ ALL ORIGINAL ASSETS & MESSAGES
# ═══════════════════════════════════════════════════════════════════════
HEART_EMOJIS = ['❤️', '🧡', '💛', '💚', '💙', '💜', '🤎', '🖤', '🤍', '💘', '💝', '💖', '💗', '💓', '💞', '💌', '💕', '💟', '♥️', '❣️', '💔']

UNAUTHORIZED_MESSAGE = "𝑲𝒆 𝑯𝒂𝒂𝒍 🎀😻"

# ⚡ ALL ORIGINAL NAME CHANGE MESSAGES
NAME_CHANGE_MESSAGES = [
    "DEV TERA BAAP  🔥⃤⃟⃝🐦‍🔥『🚩』",
    "{target} TERI BHEN KA BHOSADA 🔥⃤⃟⃝🐦‍🔥『🚩』",
    "{target} TERI MAA DEV KE LUND PR 🔥⃤⃟⃝🐦‍🔥『🚩』",
    "{target} TERI MAA KA BHOSADA CHUDA 🔥⃤⃟⃝🐦‍🔥『🚩』",
    "{target} TERI CHUDAYI BY DEV PAPA 🔥⃤⃟⃝🐦‍🔥『🚩』",
    "{target} CVR LE RANDI KE BACCHE 🔥⃤⃟⃝🐦‍🔥『🚩』",
    "{target} TERI MAA RANDI 🔥⃤⃟⃝🐦‍🔥 『🚩』",
    "{target} TERI BHEN KAALI CHUT 🔥⃤⃟⃝🐦‍🔥『🚩』",
]

# ⚡ ALL ORIGINAL REPLY MESSAGES
REPLY_MESSAGES = [
    "{target} ---RDI🐣",
    "{target} चुद गया -!",
    "Aʟᴏᴏ Kʜᴀᴋᴇ {target} Kɪ Mᴀ Cʜᴏᴅ Dᴜɴɢᴀ!",
    "{target} Cʜᴜᴅᴀ🦖🪽",
    "{target} Bᴏʟᴇ ᴅᴇᴠ ᴘᴀᴘᴀ पिताश्री Mᴇʀɪ Mᴀ Cʜᴏᴅ Dᴏ",
    "{target} Kɪ Mᴀ Bᴏʟᴇ ᴅᴇᴠ ᴘᴀᴘᴀ Sᴇ Cʜᴜᴅᴜɴɢɪ",
    "{target} Kɪ Bᴇʜɴ Kɪ Cʜᴜᴛ Kᴀʟɪ Kᴀʟɪ",
    "{target} Kɪ Mᴀ Rᴀɴᴅɪ",
    "{target} ɢᴀʀᴇᴇʙ ᴋᴀ ʙᴀᴄʜʜᴀ",
    "{target} ᴄʜᴜᴅ ᴋᴇ ᴘᴀɢᴀʟ ʜᴏɢᴀʏᴀ",
    "{target} ᴋɪ ʙᴇʜɴ ᴄʜᴏᴅᴜ",
    "{target} ʟᴜɴᴅ ᴄʜᴜsᴇɢᴀ sᴀʙᴋᴀ",
    "{target} ᴋɪ ᴍᴀ ᴋᴏ ᴄʜᴏᴅᴇ ᴅᴇᴠ ᴘᴀᴘᴀ",
    "{target} ᴋɪ ᴍᴀ ᴅᴇᴠ ᴘᴀᴘᴀ ꜱᴇ ᴄʜᴜᴅᴇ",
    "{target} ᴅᴇᴠ ᴘᴀᴘᴀ ꜱᴇ ᴄʜᴜᴅᴀ",
    "{target} CUDKE MARGYA",
    "{target} ɴᴇ ᴅᴇᴠ ᴘᴀᴘᴀ ᴋᴏ ʙᴀᴀᴩ ʙɴᴀ ʟɪyᴀ",
    "{target} ʙᴏʟᴇ ᴅᴇᴠ ᴘᴀᴘᴀ ᴩᴀᴩᴀ",
    "{target} ᴋɪ ᴀᴍᴍᴀ ᴄʜᴜᴅɪ",
    "{target} ᴋᴜᴛᴛᴇ ɢᴜʟᴀᴍɪ ᴋʀ 😋",
]

# ⚡ ORIGINAL SPAM MESSAGE TEMPLATE
SPAM_MESSAGE_TEMPLATE = """✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 ??ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི    ✝ 𝐀ɴᴛᴀ𝐑 𝐌ᴀɴ𝐓ᴀʀ 𝐒ʜᴀɪ𝐓ᴀɴ𝐈 𝐊ʜᴏ𝐏ᴀᴅ𝐀 {target} 𝐆ᴀ𝐑ɪ𝐁 𝐊ɪ 𝐀ᴍᴍ𝐈 𝐊ᴀ 𝐊ᴀʟ𝐀 𝐁ʜᴏs𝐃ᴀ  ━━━━━━━━ 💗᪲᪲᪲࣪ ִֶָ☾.ᯓᡣ𐭩🤍ྀི"""


# ═══════════════════════════════════════════════════════════════════════
# ⚡ UTILITIES
# ═══════════════════════════════════════════════════════════════════════
def extract_retry_after(error_str):
    match = re.search(r'retry after (\d+)', error_str.lower())
    if match:
        return int(match.group(1))
    return None


# ═══════════════════════════════════════════════════════════════════════
# ⚡ HYPER BOT INSTANCE CLASS
# ═══════════════════════════════════════════════════════════════════════
class HyperBotInstance:
    def __init__(self, bot_number, owner_id):
        self.bot_number = bot_number
        self.owner_id = owner_id
        self.authorized_users = set(DEFAULT_AUTHORIZED_USERS)
        self.active_spam_tasks = {}
        self.active_name_change_tasks = {}
        self.active_custom_nc_tasks = {}
        self.active_reply_tasks = {}
        self.active_reply_targets = {}
        self.pending_replies = {}
        self.chat_delays = {}
        self.chat_threads = {}
        self.locks = {}
        self.stats = {"sent": 0, "errors": 0, "start_time": time.time()}

    def get_lock(self, chat_id):
        if chat_id not in self.locks:
            self.locks[chat_id] = asyncio.Lock()
        return self.locks[chat_id]

    def is_owner(self, user_id):
        return user_id == self.owner_id

    def is_authorized(self, user_id):
        return user_id == self.owner_id or user_id in self.authorized_users

    async def check_owner(self, update):
        user_id = update.effective_user.id
        if not self.is_authorized(user_id):
            try:
                await update.message.reply_text(UNAUTHORIZED_MESSAGE)
            except:
                pass
            return False
        return True

    async def check_main_owner(self, update):
        user_id = update.effective_user.id
        if not self.is_owner(user_id):
            try:
                await update.message.reply_text("⛔ Only the main owner can use this command!")
            except:
                pass
            return False
        return True

    # ═══════════════════════════════════════════════════════════════════
    # ⚡ HYPER LOOP ENGINES
    # ═══════════════════════════════════════════════════════════════════
    async def name_change_loop(self, chat_id, base_name, context, worker_id=1):
        msg_index = 0
        num_messages = len(NAME_CHANGE_MESSAGES)
        success_count = 0
        print(f"[Bot {self.bot_number}] ⚡ NC Worker #{worker_id} STARTED for chat {chat_id}")
        try:
            while True:
                delay = self.chat_delays.get(chat_id, 0)
                try:
                    current_msg = NAME_CHANGE_MESSAGES[msg_index % num_messages]
                    display_name = current_msg.format(target=base_name)
                    await context.bot.set_chat_title(chat_id=chat_id, title=display_name)
                    msg_index += 1
                    success_count += 1
                    self.stats["sent"] += 1
                    if delay > 0:
                        await asyncio.sleep(delay)
                    else:
                        await asyncio.sleep(0.01)
                except asyncio.CancelledError:
                    raise
                except RetryAfter as e:
                    wait_time = int(e.retry_after) if isinstance(e.retry_after, (int, float)) else e.retry_after.total_seconds()
                    print(f"[Bot {self.bot_number}] ⏳ Rate limit: {wait_time}s")
                    await asyncio.sleep(wait_time + 0.1)
                except (TimedOut, NetworkError):
                    await asyncio.sleep(0.3)
                except Exception as e:
                    self.stats["errors"] += 1
                    error_str = str(e).lower()
                    retry_after = extract_retry_after(error_str)
                    if retry_after:
                        await asyncio.sleep(retry_after)
                    else:
                        await asyncio.sleep(0.3)
                    msg_index += 1
        except asyncio.CancelledError:
            print(f"[Bot {self.bot_number}] 🛑 NC Worker #{worker_id} stopped after {success_count} changes")

    async def custom_name_change_loop(self, chat_id, custom_name, context, worker_id=1):
        success_count = 0
        print(f"[Bot {self.bot_number}] 💖 Custom NC Worker #{worker_id} STARTED for chat {chat_id}")
        try:
            while True:
                delay = self.chat_delays.get(chat_id, 0)
                try:
                    heart = random.choice(HEART_EMOJIS)
                    display_name = f"{custom_name} {heart}"
                    await context.bot.set_chat_title(chat_id=chat_id, title=display_name)
                    success_count += 1
                    self.stats["sent"] += 1
                    if delay > 0:
                        await asyncio.sleep(delay)
                    else:
                        await asyncio.sleep(0.01)
                except asyncio.CancelledError:
                    raise
                except RetryAfter as e:
                    wait_time = int(e.retry_after) if isinstance(e.retry_after, (int, float)) else e.retry_after.total_seconds()
                    await asyncio.sleep(wait_time + 0.1)
                except (TimedOut, NetworkError):
                    await asyncio.sleep(0.3)
                except Exception as e:
                    self.stats["errors"] += 1
                    error_str = str(e).lower()
                    retry_after = extract_retry_after(error_str)
                    if retry_after:
                        await asyncio.sleep(retry_after)
                    else:
                        await asyncio.sleep(0.3)
        except asyncio.CancelledError:
            print(f"[Bot {self.bot_number}] 🛑 Custom NC Worker #{worker_id} stopped after {success_count} changes")

    async def spam_loop(self, chat_id, target_name, context, worker_id):
        success_count = 0
        print(f"[Bot {self.bot_number}] 💣 Spam Worker #{worker_id} STARTED for chat {chat_id}")
        try:
            while True:
                delay = self.chat_delays.get(chat_id, 0)
                try:
                    spam_msg = SPAM_MESSAGE_TEMPLATE.format(target=target_name)
                    await context.bot.send_message(chat_id=chat_id, text=spam_msg)
                    success_count += 1
                    self.stats["sent"] += 1
                    if delay > 0:
                        await asyncio.sleep(delay)
                    else:
                        await asyncio.sleep(0.01)
                except asyncio.CancelledError:
                    raise
                except RetryAfter as e:
                    wait_time = int(e.retry_after) if isinstance(e.retry_after, (int, float)) else e.retry_after.total_seconds()
                    print(f"[Bot {self.bot_number}] ⏳ Rate limit: {wait_time}s")
                    await asyncio.sleep(wait_time + 0.1)
                except (TimedOut, NetworkError):
                    await asyncio.sleep(0.3)
                except Exception as e:
                    self.stats["errors"] += 1
                    error_str = str(e).lower()
                    retry_after = extract_retry_after(error_str)
                    if retry_after:
                        await asyncio.sleep(retry_after)
                    else:
                        await asyncio.sleep(0.3)
        except asyncio.CancelledError:
            print(f"[Bot {self.bot_number}] 🛑 Spam Worker #{worker_id} stopped after {success_count} messages")

    async def reply_loop(self, chat_id, target_name, context):
        success_count = 0
        print(f"[Bot {self.bot_number}] 💬 Reply LOOP started for chat {chat_id}")
        try:
            while True:
                delay = self.chat_delays.get(chat_id, 0)
                if chat_id in self.pending_replies and self.pending_replies[chat_id]:
                    async with self.get_lock(chat_id):
                        messages_to_reply = self.pending_replies[chat_id].copy()
                        self.pending_replies[chat_id] = []

                    for msg_id in messages_to_reply:
                        try:
                            reply_msg = random.choice(REPLY_MESSAGES).format(target=target_name)
                            await context.bot.send_message(
                                chat_id=chat_id,
                                text=reply_msg,
                                reply_to_message_id=msg_id
                            )
                            success_count += 1
                            self.stats["sent"] += 1
                            if delay > 0:
                                await asyncio.sleep(delay)
                        except asyncio.CancelledError:
                            raise
                        except RetryAfter as e:
                            wait_time = int(e.retry_after) if isinstance(e.retry_after, (int, float)) else e.retry_after.total_seconds()
                            await asyncio.sleep(wait_time + 0.1)
                        except Exception:
                            self.stats["errors"] += 1
                else:
                    await asyncio.sleep(0.01)
        except asyncio.CancelledError:
            print(f"[Bot {self.bot_number}] 🛑 Reply LOOP stopped after {success_count} replies")

    async def message_collector(self, update, context):
        if not update.message:
            return
        chat_id = update.effective_chat.id
        if chat_id in self.active_reply_targets:
            msg_id = update.message.message_id
            async with self.get_lock(chat_id):
                if chat_id not in self.pending_replies:
                    self.pending_replies[chat_id] = []
                self.pending_replies[chat_id].append(msg_id)

    # ═══════════════════════════════════════════════════════════════════
    # ⚡ COMMANDS
    # ═══════════════════════════════════════════════════════════════════
    async def start(self, update, context):
        if not await self.check_owner(update):
            return

        help_text = f"""
𓆩 𝐁𝐎𝐓 {self.bot_number} 𓆪 - ⚡ 𝐇𝐘𝐏𝐄𝐑-𝐗 𝐯𝟑.𝟎 ⚡

━━━━ 𝐀𝐓𝐓𝐀𝐂𝐊 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 ━━━━
/target <name> - NC + SPAM together with threads!
/nc <name> - Name change LOOP (with threads)
/ctmnc <custom name> - Custom name + heart emoji LOOP!
/spam <target> - Spam LOOP (with threads)
/reply <target> - Reply to every message LOOP!

━━━━ 𝐂𝐎𝐍𝐓𝐑𝐎𝐋 ━━━━
/delay <seconds> - Set delay (default: 0)
/threads <1-50> - Set threads for NC + SPAM

━━━━ 𝐒𝐓𝐎𝐏 ━━━━
/stopnc - Stop name change loop
/stopctmnc - Stop custom name change loop
/stopspam - Stop spam loop
/stopreply - Stop reply loop
/stopall - Stop ALL loops

━━━━ 𝐒𝐔𝐃𝐎 (𝐎𝐰𝐧𝐞𝐫 𝐎𝐧𝐥𝐲) ━━━━
/sudo <id1> <id2> ... - Add authorized users
/unsudo <id1> <id2> ... - Remove authorized users
/sudolist - List all authorized users

━━━━ 𝐔𝐓𝐈𝐋𝐈𝐓𝐘 ━━━━
/ping - Show bot latency in ms
/status - Live statistics

𝐓𝐡𝐫𝐞𝐚𝐝𝐬: 1-50 (𝐚𝐩𝐩𝐥𝐢𝐞𝐬 𝐭𝐨 𝐍𝐂 + 𝐒𝐏𝐀𝐌)
𝐀𝐥𝐥 𝐚𝐜𝐭𝐢𝐨𝐧𝐬 𝐫𝐮𝐧 𝐢𝐧 𝐋𝐎𝐎𝐏𝐒 ⚡
𝐎𝐰𝐧𝐞𝐫 𝐎𝐧𝐥𝐲 🔒
"""
        await update.message.reply_text(help_text)

    async def nc_command(self, update, context):
        if not await self.check_owner(update):
            return

        chat = update.effective_chat

        if chat.type not in [ChatType.GROUP, ChatType.SUPERGROUP]:
            await update.message.reply_text("This command only works in groups!")
            return

        if not context.args:
            await update.message.reply_text("Usage: /nc <name>")
            return

        base_name = " ".join(context.args)
        chat_id = chat.id

        if chat_id in self.active_name_change_tasks:
            old_tasks = self.active_name_change_tasks[chat_id]
            for task in old_tasks:
                task.cancel()
            for task in old_tasks:
                try:
                    await task
                except asyncio.CancelledError:
                    pass

        num_threads = self.chat_threads.get(chat_id, 1)
        tasks = []
        for i in range(num_threads):
            task = asyncio.create_task(self.name_change_loop(chat_id, base_name, context, i + 1))
            tasks.append(task)

        self.active_name_change_tasks[chat_id] = tasks

        await update.message.reply_text(f"[Bot {self.bot_number}] ⚡ Name change LOOP started with {num_threads} threads!")

    async def stop_nc_command(self, update, context):
        if not await self.check_owner(update):
            return

        chat_id = update.effective_chat.id

        if chat_id in self.active_name_change_tasks:
            tasks = self.active_name_change_tasks[chat_id]
            for task in tasks:
                task.cancel()
            for task in tasks:
                try:
                    await task
                except asyncio.CancelledError:
                    pass
            del self.active_name_change_tasks[chat_id]
            await update.message.reply_text(f"[Bot {self.bot_number}] Name change LOOP stopped!")
        else:
            await update.message.reply_text(f"[Bot {self.bot_number}] No active name change loop!")

    async def ctmnc_command(self, update, context):
        if not await self.check_owner(update):
            return

        chat = update.effective_chat

        if chat.type not in [ChatType.GROUP, ChatType.SUPERGROUP]:
            await update.message.reply_text("This command only works in groups!")
            return

        if not context.args:
            await update.message.reply_text("Usage: /ctmnc <custom name>")
            return

        custom_name = " ".join(context.args)
        chat_id = chat.id

        if chat_id in self.active_custom_nc_tasks:
            old_tasks = self.active_custom_nc_tasks[chat_id]
            for task in old_tasks:
                task.cancel()
            for task in old_tasks:
                try:
                    await task
                except asyncio.CancelledError:
                    pass

        num_threads = self.chat_threads.get(chat_id, 1)
        tasks = []
        for i in range(num_threads):
            task = asyncio.create_task(self.custom_name_change_loop(chat_id, custom_name, context, i + 1))
            tasks.append(task)

        self.active_custom_nc_tasks[chat_id] = tasks

        await update.message.reply_text(f"[Bot {self.bot_number}] 💖 Custom name change LOOP started with {num_threads} threads! Adding heart emojis...")

    async def stop_ctmnc_command(self, update, context):
        if not await self.check_owner(update):
            return

        chat_id = update.effective_chat.id

        if chat_id in self.active_custom_nc_tasks:
            tasks = self.active_custom_nc_tasks[chat_id]
            for task in tasks:
                task.cancel()
            for task in tasks:
                try:
                    await task
                except asyncio.CancelledError:
                    pass
            del self.active_custom_nc_tasks[chat_id]
            await update.message.reply_text(f"[Bot {self.bot_number}] Custom name change LOOP stopped!")
        else:
            await update.message.reply_text(f"[Bot {self.bot_number}] No active custom name change loop!")

    async def spam_command(self, update, context):
        if not await self.check_owner(update):
            return

        chat = update.effective_chat

        if chat.type not in [ChatType.GROUP, ChatType.SUPERGROUP]:
            await update.message.reply_text("This command only works in groups!")
            return

        if not context.args:
            await update.message.reply_text("Usage: /spam <target>")
            return

        target_name = " ".join(context.args)
        chat_id = chat.id

        if chat_id in self.active_spam_tasks:
            tasks = self.active_spam_tasks[chat_id]
            for task in tasks:
                task.cancel()
            for task in tasks:
                try:
                    await task
                except asyncio.CancelledError:
                    pass

        num_threads = self.chat_threads.get(chat_id, 1)
        tasks = []
        for i in range(num_threads):
            task = asyncio.create_task(self.spam_loop(chat_id, target_name, context, i + 1))
            tasks.append(task)

        self.active_spam_tasks[chat_id] = tasks
        await update.message.reply_text(f"[Bot {self.bot_number}] 💣 Spam LOOP started with {num_threads} threads! Running continuously...")

    async def stop_spam_command(self, update, context):
        if not await self.check_owner(update):
            return

        chat_id = update.effective_chat.id

        if chat_id in self.active_spam_tasks:
            tasks = self.active_spam_tasks[chat_id]
            for task in tasks:
                task.cancel()
            for task in tasks:
                try:
                    await task
                except asyncio.CancelledError:
                    pass
            del self.active_spam_tasks[chat_id]
            await update.message.reply_text(f"[Bot {self.bot_number}] Spam LOOP stopped!")
        else:
            await update.message.reply_text(f"[Bot {self.bot_number}] No active spam loop!")

    async def target_command(self, update, context):
        if not await self.check_owner(update):
            return

        chat = update.effective_chat

        if chat.type not in [ChatType.GROUP, ChatType.SUPERGROUP]:
            await update.message.reply_text("This command only works in groups!")
            return

        if not context.args:
            await update.message.reply_text("Usage: /target <name>")
            return

        target_name = " ".join(context.args)
        chat_id = chat.id

        # Stop existing tasks
        if chat_id in self.active_name_change_tasks:
            old_tasks = self.active_name_change_tasks[chat_id]
            for task in old_tasks:
                task.cancel()
            for task in old_tasks:
                try:
                    await task
                except asyncio.CancelledError:
                    pass

        if chat_id in self.active_spam_tasks:
            tasks = self.active_spam_tasks[chat_id]
            for task in tasks:
                task.cancel()
            for task in tasks:
                try:
                    await task
                except asyncio.CancelledError:
                    pass

        num_threads = self.chat_threads.get(chat_id, 1)

        nc_tasks = []
        for i in range(num_threads):
            task = asyncio.create_task(self.name_change_loop(chat_id, target_name, context, i + 1))
            nc_tasks.append(task)
        self.active_name_change_tasks[chat_id] = nc_tasks

        spam_tasks = []
        for i in range(num_threads):
            task = asyncio.create_task(self.spam_loop(chat_id, target_name, context, i + 1))
            spam_tasks.append(task)
        self.active_spam_tasks[chat_id] = spam_tasks

        total_threads = num_threads * 2
        await update.message.reply_text(f"[Bot {self.bot_number}] 🎯 TARGET MODE: NC ({num_threads}) + SPAM ({num_threads}) = {total_threads} threads running!")

    async def reply_command(self, update, context):
        if not await self.check_owner(update):
            return

        chat = update.effective_chat

        if chat.type not in [ChatType.GROUP, ChatType.SUPERGROUP]:
            await update.message.reply_text("This command only works in groups!")
            return

        if not context.args:
            await update.message.reply_text("Usage: /reply <target>")
            return

        target_name = " ".join(context.args)
        chat_id = chat.id

        if chat_id in self.active_reply_tasks:
            old_task = self.active_reply_tasks[chat_id]
            old_task.cancel()
            try:
                await old_task
            except asyncio.CancelledError:
                pass

        self.active_reply_targets[chat_id] = target_name
        self.pending_replies[chat_id] = []

        task = asyncio.create_task(self.reply_loop(chat_id, target_name, context))
        self.active_reply_tasks[chat_id] = task

        await update.message.reply_text(f"[Bot {self.bot_number}] 💬 Reply LOOP activated! Replying to every message...")

    async def stop_reply_command(self, update, context):
        if not await self.check_owner(update):
            return

        chat_id = update.effective_chat.id

        if chat_id in self.active_reply_tasks:
            task = self.active_reply_tasks[chat_id]
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass
            del self.active_reply_tasks[chat_id]

        if chat_id in self.active_reply_targets:
            del self.active_reply_targets[chat_id]

        if chat_id in self.pending_replies:
            del self.pending_replies[chat_id]

        await update.message.reply_text(f"[Bot {self.bot_number}] Reply LOOP stopped!")

    async def delay_command(self, update, context):
        if not await self.check_owner(update):
            return

        if not context.args:
            await update.message.reply_text("Usage: /delay <seconds>")
            return

        try:
            delay = float(context.args[0])
            if delay < 0:
                await update.message.reply_text("Delay must be >= 0")
                return

            chat_id = update.effective_chat.id
            self.chat_delays[chat_id] = delay
            await update.message.reply_text(f"[Bot {self.bot_number}] Delay set to {delay}s (applies to all loops)")
        except ValueError:
            await update.message.reply_text("Invalid delay value!")

    async def threads_command(self, update, context):
        if not await self.check_owner(update):
            return

        if not context.args:
            await update.message.reply_text("Usage: /threads <number>")
            return

        try:
            threads = int(context.args[0])
            if threads < 1 or threads > 50:
                await update.message.reply_text("Threads must be between 1 and 50")
                return

            chat_id = update.effective_chat.id
            self.chat_threads[chat_id] = threads
            await update.message.reply_text(f"[Bot {self.bot_number}] Threads set to {threads} (applies to NC + SPAM)")
        except ValueError:
            await update.message.reply_text("Invalid threads value!")

    async def stop_all_command(self, update, context):
        if not await self.check_owner(update):
            return

        chat_id = update.effective_chat.id
        stopped = []

        if chat_id in self.active_name_change_tasks:
            tasks = self.active_name_change_tasks[chat_id]
            for task in tasks:
                task.cancel()
            for task in tasks:
                try:
                    await task
                except asyncio.CancelledError:
                    pass
            del self.active_name_change_tasks[chat_id]
            stopped.append("name change loop")

        if chat_id in self.active_custom_nc_tasks:
            tasks = self.active_custom_nc_tasks[chat_id]
            for task in tasks:
                task.cancel()
            for task in tasks:
                try:
                    await task
                except asyncio.CancelledError:
                    pass
            del self.active_custom_nc_tasks[chat_id]
            stopped.append("custom name change loop")

        if chat_id in self.active_spam_tasks:
            tasks = self.active_spam_tasks[chat_id]
            for task in tasks:
                task.cancel()
            for task in tasks:
                try:
                    await task
                except asyncio.CancelledError:
                    pass
            del self.active_spam_tasks[chat_id]
            stopped.append("spam loop")

        if chat_id in self.active_reply_tasks:
            task = self.active_reply_tasks[chat_id]
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass
            del self.active_reply_tasks[chat_id]
            stopped.append("reply loop")

        if chat_id in self.active_reply_targets:
            del self.active_reply_targets[chat_id]

        if chat_id in self.pending_replies:
            del self.pending_replies[chat_id]

        if stopped:
            await update.message.reply_text(f"[Bot {self.bot_number}] Stopped: {', '.join(stopped)}")
        else:
            await update.message.reply_text(f"[Bot {self.bot_number}] No active loops to stop!")

    async def sudo_command(self, update, context):
        if not await self.check_main_owner(update):
            return

        if not context.args:
            await update.message.reply_text("Usage: /sudo <user_id1> <user_id2> ...")
            return

        added = []
        invalid = []

        for arg in context.args:
            try:
                user_id = int(arg)
                if user_id == self.owner_id:
                    continue
                self.authorized_users.add(user_id)
                added.append(str(user_id))
            except ValueError:
                invalid.append(arg)

        response = f"[Bot {self.bot_number}] 👑 SUDO UPDATE\n"
        if added:
            response += f"✅ Added: {', '.join(added)}\n"
        if invalid:
            response += f"❌ Invalid IDs: {', '.join(invalid)}\n"
        response += f"📊 Total authorized: {len(self.authorized_users)}"

        await update.message.reply_text(response)

    async def unsudo_command(self, update, context):
        if not await self.check_main_owner(update):
            return

        if not context.args:
            await update.message.reply_text("Usage: /unsudo <user_id1> <user_id2> ...")
            return

        removed = []
        not_found = []
        invalid = []

        for arg in context.args:
            try:
                user_id = int(arg)
                if user_id in self.authorized_users:
                    self.authorized_users.remove(user_id)
                    removed.append(str(user_id))
                else:
                    not_found.append(str(user_id))
            except ValueError:
                invalid.append(arg)

        response = f"[Bot {self.bot_number}] 👑 SUDO UPDATE\n"
        if removed:
            response += f"🚫 Removed: {', '.join(removed)}\n"
        if not_found:
            response += f"⚠️ Not found: {', '.join(not_found)}\n"
        if invalid:
            response += f"❌ Invalid IDs: {', '.join(invalid)}\n"
        response += f"📊 Total authorized: {len(self.authorized_users)}"

        await update.message.reply_text(response)

    async def sudolist_command(self, update, context):
        if not await self.check_main_owner(update):
            return

        response = f"[Bot {self.bot_number}] 👑 SUDO LIST\n\n"
        response += f"🔑 Main Owner: {self.owner_id}\n\n"

        if self.authorized_users:
            response += "✅ Authorized Users:\n"
            for user_id in sorted(self.authorized_users):
                response += f"  • {user_id}\n"
        else:
            response += "📭 No authorized users yet"

        await update.message.reply_text(response)

    async def ping_command(self, update, context):
        if not await self.check_owner(update):
            return

        start_time = time.time()
        msg = await update.message.reply_text("🏓 Pinging...")
        end_time = time.time()

        latency_ms = (end_time - start_time) * 1000
        await msg.edit_text(f"[Bot {self.bot_number}] 🏓 Pong!\n⚡ Latency: {latency_ms:.2f} ms")

    async def status_command(self, update, context):
        if not await self.check_owner(update):
            return

        uptime = int(time.time() - self.stats["start_time"])
        hours, remainder = divmod(uptime, 3600)
        minutes, seconds = divmod(remainder, 60)

        active_tasks = 0
        if update.effective_chat.id in self.active_spam_tasks:
            active_tasks += len(self.active_spam_tasks[update.effective_chat.id])
        if update.effective_chat.id in self.active_name_change_tasks:
            active_tasks += len(self.active_name_change_tasks[update.effective_chat.id])
        if update.effective_chat.id in self.active_custom_nc_tasks:
            active_tasks += len(self.active_custom_nc_tasks[update.effective_chat.id])
        if update.effective_chat.id in self.active_reply_tasks:
            active_tasks += 1

        await update.message.reply_text(f"""
📊 HYPER-X BOT {self.bot_number} STATUS
━━━━━━━━━━━━━━━━━━━━━━━━
✅ Messages Sent: {self.stats['sent']}
⚠️ Errors: {self.stats['errors']}
⏱️ Uptime: {hours}h {minutes}m {seconds}s
🚀 Active Tasks: {active_tasks}
━━━━━━━━━━━━━━━━━━━━━━━━
""")


# ═══════════════════════════════════════════════════════════════════════
# ⚡ BOT INITIALIZATION
# ═══════════════════════════════════════════════════════════════════════
async def force_takeover_bot(token, bot_number):
    """Force takeover bot from any other instance by deleting webhook and clearing updates"""
    try:
        import httpx
        base_url = f"https://api.telegram.org/bot{token}"
        async with httpx.AsyncClient(timeout=30) as client:
            await client.post(f"{base_url}/deleteWebhook", json={"drop_pending_updates": True})
            await client.post(f"{base_url}/getUpdates", json={"offset": -1, "timeout": 0})
            print(f"[Bot {bot_number}] 🔥 Forced takeover - cleared other instances!")
            await asyncio.sleep(1)
    except Exception as e:
        print(f"[Bot {bot_number}] ⚠️ Takeover attempt: {e}")


async def run_bot(token, bot_number, owner_id):
    await force_takeover_bot(token, bot_number)

    application = Application.builder().token(token).build()
    bot_instance = HyperBotInstance(bot_number, owner_id)

    application.add_handler(CommandHandler("start", bot_instance.start))
    application.add_handler(CommandHandler("help", bot_instance.start))
    application.add_handler(CommandHandler("nc", bot_instance.nc_command))
    application.add_handler(CommandHandler("stopnc", bot_instance.stop_nc_command))
    application.add_handler(CommandHandler("ctmnc", bot_instance.ctmnc_command))
    application.add_handler(CommandHandler("stopctmnc", bot_instance.stop_ctmnc_command))
    application.add_handler(CommandHandler("spam", bot_instance.spam_command))
    application.add_handler(CommandHandler("stopspam", bot_instance.stop_spam_command))
    application.add_handler(CommandHandler("target", bot_instance.target_command))
    application.add_handler(CommandHandler("reply", bot_instance.reply_command))
    application.add_handler(CommandHandler("stopreply", bot_instance.stop_reply_command))
    application.add_handler(CommandHandler("delay", bot_instance.delay_command))
    application.add_handler(CommandHandler("threads", bot_instance.threads_command))
    application.add_handler(CommandHandler("stopall", bot_instance.stop_all_command))
    application.add_handler(CommandHandler("sudo", bot_instance.sudo_command))
    application.add_handler(CommandHandler("unsudo", bot_instance.unsudo_command))
    application.add_handler(CommandHandler("sudolist", bot_instance.sudolist_command))
    application.add_handler(CommandHandler("ping", bot_instance.ping_command))
    application.add_handler(CommandHandler("status", bot_instance.status_command))
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, bot_instance.message_collector))

    print(f"⚡ Bot {bot_number} INITIALIZED")

    max_retries = 10

    for attempt in range(max_retries):
        try:
            await application.initialize()
            await application.start()
            if application.updater:
                await application.updater.start_polling(
                    drop_pending_updates=True,
                    allowed_updates=["message", "edited_message", "channel_post", "edited_channel_post", "callback_query"],
                    poll_interval=0.5
                )
            print(f"⚡ Bot {bot_number} RUNNING AGGRESSIVELY!")

            while True:
                await asyncio.sleep(3600)

        except Exception as e:
            error_str = str(e).lower()
            if "conflict" in error_str and attempt < max_retries - 1:
                await force_takeover_bot(token, bot_number)
                wait_time = 1
                print(f"[Bot {bot_number}] 🔄 Retaking control... (attempt {attempt + 1}/{max_retries})")
                await asyncio.sleep(wait_time)
                continue
            print(f"[Bot {bot_number}] ❌ Error: {e}")
            break
        finally:
            try:
                if application.updater:
                    await application.updater.stop()
                await application.stop()
                await application.shutdown()
            except Exception:
                pass


async def main():
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║           ⚡⚡⚡ HYPER-X BOT CLUSTER v3.0 ⚡⚡⚡                   ║
║                                                                      ║
║                      STARTING ALL BOTS...                            ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
    """)
    tasks = []
    for i, token in enumerate(BOT_TOKENS):
        tasks.append(run_bot(token, i + 1, OWNER_ID))

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    try:
        if os.name == 'nt':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n⚡ HYPER-X SHUTDOWN COMPLETE")
