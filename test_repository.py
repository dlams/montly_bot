import pytest
from sqlalchemy import select
from config import dubu_streak
from bot import StreakSqlAlchemyRepository, Streak


def test_repository_can_save(session):
    data = ("1234567890", 0, 0)
    streak = Streak(*data)
    
    repo = StreakSqlAlchemyRepository(session)
    repo.add(streak)
    session.commit()
    
    rows = list(session.execute(
        select(Streak).where()
    ))
    
    assert rows[0].Streak == Streak(*data)
