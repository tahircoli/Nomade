# ==========================================================
# Group Manager Bot
# Author: learning_bots (https://github.com/learning_bots)
# Support: https://t.me/learning_bots
# Channel: https://t.me/learningbots79
# YouTube: https://youtube.com/@learning_bots
# License: Open-source (keep credits, no resale)
# ==========================================================

import os

# Required configurations (loaded from environment variables)
API_ID = int(os.getenv("29555662", 0))
API_HASH = os.getenv("d5420764bf458365083a59c70748e907", "")
BOT_TOKEN = os.getenv("8491473656:AAEIMXJzMlJMEW4xSBNX_4q20XkrshUrvC4", "")
MONGO_URI = os.getenv("mongodb+srv://ffhackerindia098_db_user:ffhackerindia098_db_user@cluster0.rsb3l7b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", "")
DB_NAME = os.getenv("DB_NAME", "Cluster0")

# Owner and bot details
OWNER_ID = int(os.getenv("7265739086", 0))
BOT_USERNAME = os.getenv("@Tahirmusicbot", "NomadeHelpBot")

# Links and visuals
SUPPORT_GROUP = os.getenv("https://t.me/Music_support_group_Tahir", "https://t.me/learning_bots")
UPDATE_CHANNEL = os.getenv("https://t.me/Tahir_update", "https://t.me/learningbots79")
START_IMAGE = os.getenv("START_IMAGE", "https://files.catbox.moe/j2yhce.jpg")
