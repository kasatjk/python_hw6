from django.shortcuts import render
import datetime
import random

QUOTES = [
    "Футы-нуты, лапти гнуты! (Не знаю, де це почув)",
    "Карти - це найвеличніші поеми, написані лініями та кольорами. (Ґілберт Гросвенор)",
    "Якщо працює - не чіпай. (Перше правило програмістів)",
    "Людина з інтелектом може все. (Тетяна Каришева - вчителька біології)"
]

DAYS_OF_WEEK = {
    0: "Понеділок",
    1: "Вівторок",
    2: "Середа",
    3: "Четвер",
    4: "П'ятниця",
    5: "Субота",
    6: "Неділя",
}

def main(request):
    today = datetime.date.today()
    day = DAYS_OF_WEEK.get(today.weekday())
    quote = random.choice(QUOTES)

    context = {
        "day": day,
        "quote": quote,
    }
    return render(request, "main.html", context)
