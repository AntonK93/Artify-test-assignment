#!/usr/bin/env python3
#
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import asyncio
import tornado.escape
import tornado.ioloop
import tornado.locks
import tornado.web
import os.path
import redis

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from tornado.options import parse_command_line
from config.config import Config
from routes.routes import routes

engine = create_engine('mysql+pymysql://%s:%s@%s/%s?charset=utf8' % (Config.DB_USER, Config.DB_PWD, Config.DB_HOST, Config.DB_NAME),
    encoding='utf-8', 
    echo=False,
    pool_size=100,
    pool_recycle=10)

db = scoped_session(sessionmaker(bind=engine,
    autocommit=False, autoflush=True,
    expire_on_commit=False))

redisDb = redis.Redis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB)

def main():
    parse_command_line()
    app = tornado.web.Application(
        routes.get_routes(),
        db=db,
        redisDb=redisDb,
        clientApp=Config.CLIENT_APP,
        config=Config
    )
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
