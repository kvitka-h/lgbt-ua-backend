# routers/content.py
from fastapi import APIRouter, Query
from typing import List, Optional
from mock_data import MOCK_DB
from schemas import NewsResponse, EventResponse, TeamResponse, PartnerResponse

router = APIRouter(tags=["Content (Отримання даних)"])

# Логіка фільтрації мови на бекенді може бути реалізована тут, але для простоти ми віддаємо всі мови, а фронт вибирає потрібну:)
def filter_by_lang(data: list, lang: Optional[str]):
    if not lang:
        return data
    return data

@router.get("/news", response_model=List[NewsResponse])
def get_news():
    """Отримати список актуальних новин (Німеччина/Україна)"""
    return MOCK_DB["news"]

@router.get("/events", response_model=List[EventResponse])
def get_events():
    """Отримати календар подій"""
    return MOCK_DB["events"]

@router.get("/team", response_model=List[TeamResponse])
def get_team():
    """Отримати список команди організації"""
    return MOCK_DB["team"]

@router.get("/partners", response_model=List[PartnerResponse])
def get_partners():
    """Отримати інтерактивні картки партнерів"""
    return MOCK_DB["partners"]