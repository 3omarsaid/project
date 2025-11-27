from .repository import dbManager
dbIns = dbManager()
def createTables():
    conn = dbIns.connect()
    curs = conn.cursor()
    #Users
    curs.execute("""create table if not exists users(
                Uid integer primary key autoincrement,
                userName text not null,
                password text not null,
                role text not null)""")
    conn.commit()
    #Exams
    curs.execute("""create table if not exists exams(
                ExID integer primary key autoincrement,
                TchID integer,
                title text,
                timerType text,
                time_S int,
                foreign key (TchID) references users(Uid))""")
    conn.commit()
    #Qustions
    curs.execute("""create table if not exists qustions(
                QusID integer primary key autoincrement,
                ExID integer,
                header text,
                foreign key (ExID) references exams(ExID))""")
    conn.commit()
    #choices
    curs.execute("""create table if not exists choices(
                ChID integer primary key autoincrement,
                QusID integer,
                text text,
                correct bool,
                foreign key (QusID) references qustions(QusID))""")
    conn.commit()
    #attempts
    curs.execute("""create table if not exists attempts(
                AttID integer primary key autoincrement,
                ExID integer,
                StuID integer,
                TchID integer,
                start_at datetime default currunt_timestamp,
                score integer,
                duration_S float,
                foreign key (ExID) references exams(ExID),
                foreign key (StuID) references users(Uid))""")
    conn.commit()
    #Answers
    curs.execute("""create table if not exists answers(
                AnsID integer primary key autoincrement,
                QusID integer,
                AttID integer,
                ChID integer,
                correctnes integer,
                foreign key (QusID) references quistions(QusID),
                foreign key (AttID) references attempts(AttID))""")
    conn.commit()
createTables()