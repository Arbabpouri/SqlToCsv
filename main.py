from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import Integer, String, Column, create_engine
from csv import writer
from os.path import exists


class Base(DeclarativeBase):
    pass


class Quests(Base):
    __tablename__ = "answers"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quest_1 = Column("quest_1", String(300), nullable=False)
    quest_2 = Column("quest_2", Integer(), nullable=False)
    quest_3 = Column("quest_3", Integer(), nullable=False)
    quest_4 = Column("quest_4", String(150), nullable=True, default=None)
    quest_5 = Column("quest_5", String(30), nullable=True, default=None)
    quest_6 = Column("quest_6", Integer(), nullable=False)
    quest_7 = Column("quest_7", Integer(), nullable=False)
    quest_8 = Column("quest_8", String(150), nullable=False)
    quest_9 = Column("quest_9", Integer(), nullable=False)
    quest_10 = Column("quest_10", Integer(), nullable=False)
    quest_11 = Column("quest_11", Integer(), nullable=False)
    quest_12 = Column("quest_12", String(30), nullable=False)


def write_in_csv() -> bool:
    
    quests = session.query(Quests).all()
    data = set()

    if not len(quests):
        return False

    for quest in quests:
        data.add(
            (
                quest.id,
                quest.quest_1, 
                quest.quest_2, 
                quest.quest_3, 
                quest.quest_4, 
                quest.quest_5, 
                quest.quest_6, 
                quest.quest_7, 
                quest.quest_8, 
                quest.quest_9,
                quest.quest_10, 
                quest.quest_11, 
                quest.quest_12,  
            )
        )

    with open(file="csv_file.csv", mode="w", encoding="UTF-8") as csv_file:
        
        write = writer(csv_file, delimiter=",")
        write.writerows(data)


def main():
    global session
    database_name = input("enter db name, example -> database.db : ")

    if exists(database_name):
        engine = create_engine('sqlite:///database.db')
        session = sessionmaker(bind=engine)()
        write_in_csv()
        
    else:
        print("file not exist")
        exit(0)



if __name__ == "__main__":
    main()
