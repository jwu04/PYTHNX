# Epic Games | Jonathan Wu (Loki), Jesse Xie (Polly), William Chen (Cheap), Josephine Lee (Kitty)
# SoftDev
# P04 -- SoftDev Project 2021-22
# 2022-05-24
# 0 minutes

import sqlite3
DB_FILE = "leaderboard.db"
db = sqlite3.connect(DB_FILE, check_same_thread=False)
c = db.cursor()

def create_tables():
    c = db.cursor()
    """Creates the tables in the database to store users"""
    command = 'CREATE TABLE IF NOT EXISTS scores (user_id INTEGER, waveReached INTEGER, teamComposition TEXT)'
    c.execute(command)
    command = 'CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT NOT NULL UNIQUE)'
    c.execute(command)
    db.commit() #save changes
create_tables()
