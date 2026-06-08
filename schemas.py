from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Dict

# Схеми для отримання даних (з урахуванням мовних словників)
class TranslatableText(BaseModel):
    ua: str
    en: str
    de: str

class NewsResponse(BaseModel):
    id: int
    date: str
    category: str
    title: TranslatableText
    content: TranslatableText

class EventResponse(BaseModel):
    id: int
    date: str
    location: str
    title: TranslatableText
    description: TranslatableText
    what_to_bring: TranslatableText

class TeamResponse(BaseModel):
    id: int
    name: str
    role: TranslatableText
    bio: TranslatableText
    photo_url: str

class PartnerResponse(BaseModel):
    id: int
    name: str
    description: TranslatableText
    site_url: str
    is_active_project: bool

# Схеми для POST-запитів від користувачів
class ContactForm(BaseModel):
    name: str
    email: EmailStr
    department: str = Field(..., description="Правова підтримка, Ментальна підтримка, Протести тощо")
    message: str
    phone: Optional[str] = None

class SubscribeForm(BaseModel):
    email: EmailStr

class JoinForm(BaseModel):
    name: str
    email: EmailStr
    type_of_help: str = Field(..., description="Волонтер, Спонсор, Шукаю допомогу")
    problem_description: Optional[str] = Field(None, description="Опис проблеми для клієнтів")