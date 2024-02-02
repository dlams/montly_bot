import pytest
from ..bot.features.repository.repository import AbstractRepository

def test_repository_can_save(session):
    
    repo = 