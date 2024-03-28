from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
        )

    async def execute(
        self,
        command,  
        *args,
        fetch: bool = False,
        fetchval: bool = False,
        fetchrow: bool = False,
        execute: bool = False,
    ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:                                
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        telegram_id BIGINT NOT NULL UNIQUE,
        full_name VARCHAR(255) NOT NULL,
        username VARCHAR(255) NULL,
        telling VARCHAR(250) NOT NULL,
        gen VARCHAR(10) NOT NULL,
        Age VARCHAR(5) NOT NULL,
        Link_ins VARCHAR(255) NOT NULL,
        Link_tg  VARCHAR(255) NOT NULL,
        Link_you VARCHAR(255) NOT NULL,
        Cards VARCHAR(16) NOT NULL,
        Til VARCHAR(5) NOT NULL,
        sum BIGINT NOT NULL
        
        );
        """
        # ishlagan puli
        # dostar soni

    

    
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, telegram_id, full_name, username, telling, gen, Age, Link_ins, Link_tg ,Link_you ,Cards ,Til ,sum=0):
        sql = "INSERT INTO users (telegram_id ,full_name, username, telling, gen, Age, Link_ins, Link_tg ,Link_you ,Cards ,Til ,sum) VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12) returning *"
        return await self.execute(sql, telegram_id, full_name, username, telling, gen, Age, Link_ins, Link_tg ,Link_you ,Cards ,Til ,sum, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)


    async def select_all_user_one(self, telegram_id):
        sql = "SELECT * FROM Users WHERE telegram_id = $1"
        return await self.execute(sql, telegram_id, fetchrow=True)


    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetch=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def update_user_username(self, username, telegram_id):
        sql = "UPDATE Users SET username=$1 WHERE telegram_id=$2"
        return await self.execute(sql, username, telegram_id, execute=True)


    # async def update_user_sum(self, sum, telegram_id):
    #     sql = "UPDATE Users SET sum=$1 WHERE telegram_id=$2"
    #     return await self.execute(sql, sum, telegram_id, execute=True)


    async def delete_users(self):
        await self.execute("DELETE FROM Users WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)


    async def update_user_til(self, Til, telegram_id):
        sql = "UPDATE Users SET Til=$1 WHERE telegram_id=$2"
        return await self.execute(sql, Til, telegram_id, execute=True)


    async def user_sum(self, sum, telegram_id):
            sql = "SELECT * FROM Users WHERE telegram_id = $1"
            return await self.execute(sql, sum, telegram_id, execute=True)

    async def update_user_telling(self, telling, telegram_id):
        sql = "UPDATE Users SET telling=$1 WHERE telegram_id=$2"
        return await self.execute(sql, telling, telegram_id, execute=True)

    async def update_user_card(self, Cards, telegram_id):
        sql = "UPDATE Users SET Cards=$1 WHERE telegram_id=$2"
        return await self.execute(sql, Cards, telegram_id, execute=True)


    async def update_user_insta(self, Link_ins, telegram_id):
        sql = "UPDATE Users SET Link_ins=$1 WHERE telegram_id=$2"
        return await self.execute(sql, Link_ins, telegram_id, execute=True)


    async def update_user_tele(self, Link_tg, telegram_id):
        sql = "UPDATE Users SET Link_tg=$1 WHERE telegram_id=$2"
        return await self.execute(sql, Link_tg, telegram_id, execute=True)


    async def update_user_you(self, Link_you , telegram_id):
        sql = "UPDATE Users SET Link_you =$1 WHERE telegram_id=$2"
        return await self.execute(sql, Link_you, telegram_id, execute=True)


    async def update_user_full_name(self, full_name , telegram_id):
        sql = "UPDATE Users SET full_name=$1 WHERE telegram_id=$2"
        return await self.execute(sql, full_name, telegram_id, execute=True)


    async def update_user_age(self, Age , telegram_id):
        sql = "UPDATE Users SET Age =$1 WHERE telegram_id=$2"
        return await self.execute(sql, Age, telegram_id, execute=True)


