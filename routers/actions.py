from fastapi import APIRouter, HTTPException, status
from mock_data import SUBMISSIONS
from schemas import ContactForm, SubscribeForm, JoinForm

router = APIRouter(tags=["Actions (Форми зворотного зв'язку)"])

@router.post("/contact", status_code=status.HTTP_201_CREATED)
def submit_contact(form: ContactForm):
    """Форма зворотного зв'язку (скарги, пропозиції, розподіл за підрозділами)"""
    SUBMISSIONS["contacts"].append(form.dict())
    return {"status": "success", "message": "Повідомлення успішно відправлено!"}

@router.post("/subscribe", status_code=status.HTTP_201_CREATED)
def subscribe_news(form: SubscribeForm):
    """Підписка на новини у футері"""
    # Проста перевірка на дублікат у мок-даних
    if any(s["email"] == form.email for s in SUBMISSIONS["subscriptions"]):
        raise HTTPException(status_code=400, detail="Цей email вже підписаний.")
    
    SUBMISSIONS["subscriptions"].append(form.dict())
    return {"status": "success", "message": "Дякуємо за підписку!"}

@router.post("/join", status_code=status.HTTP_201_CREATED)
def join_community(form: JoinForm):
    """CTA: Долучитися (для волонтерів, спонсорів або клієнтів, що потребують допомоги)"""
    SUBMISSIONS["join_requests"].append(form.dict())
    return {"status": "success", "message": "Заявку прийнято. Ми зв'яжемося з вами найближчим часом!"}