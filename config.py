import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("6771117413:AAHM_0qb4BsAahacl_QIsQ0qwbgBJI65TjE", "")

    APP_ID = int(os.environ.get("APP_ID", 28929515))

    API_HASH = os.environ.get("API_HASH", "6cc248d1b0d626232ef66ac5153370b8")
