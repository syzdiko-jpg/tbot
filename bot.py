import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Получаем токен из переменной окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("Ошибка: Токен бота не найден. Укажите BOT_TOKEN в переменных окружения.")

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# --- Клавиатура ---
def get_main_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="ℹ️ О нас")
    builder.button(text="📝 Оставить заявку на участие")
    builder.button(text="📞 Контакты")
    builder.adjust(2, 1)  # Первые две кнопки в один ряд, третью ниже
    return builder.as_markup(resize_keyboard=True)


# --- Обработчик команды /start ---
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    welcome_text = (
        f"Здравствуйте, {message.from_user.first_name}! 👋\n\n"
        "Добро пожаловать в официально разработанный бот **Молодежного ресурсного центра** (МРЦ)!\n\n"
        "Мы помогаем молодежи развиваться, участвовать в волонтерских движениях, "
        "получать консультации, трудоустраиваться (в т.ч. в трудовые отряды «Жасыл ел») "
        "и реализовывать свои социальные и творческие инициативы.\n\n"
        "Выберите нужный раздел в меню ниже ⬇️"
    )
    await message.answer(welcome_text, reply_markup=get_main_keyboard(), parse_mode="Markdown")


# --- Обработчик кнопки "О нас" ---
@dp.message(F.text == "ℹ️ О нас")
async def about_us(message: types.Message):
    about_text = (
        "🏛 **Молодежный ресурсный центр** — это единая платформа для поддержки "
        "и развития молодежи района/города.\n\n"
        "🎯 **Основные направления нашей работы:**\n"
        "• **«Жасыл ел»** — сезонное трудоустройство, озеленение и благоустройство населенных пунктов.\n"
        "• **Волонтерство** — участие в социальных, экологических, спортивных и благотворительных акциях.\n"
        "• **Юридическая и психологическая помощь** — консультации по защите прав, правовой грамотности и поддержке молодежи.\n"
        "• **Профориентация и молодежная политика** — помощь студентам, выпускникам и рабочей молодежи, разъяснение госпрограмм.\n"
        "• **Спорт и досуг** — организация турниров, профилактика правонарушений и поддержка здорового образа жизни."
    )
    await message.answer(about_text, parse_mode="Markdown")


# --- Обработчик кнопки "Оставить заявку на участие" ---
@dp.message(F.text == "📝 Оставить заявку на участие")
async def apply_request(message: types.Message):
    apply_text = (
        "📋 **Заявка на участие в проектах МРЦ**\n\n"
        "Вы можете стать частью нашей команды и принять участие в проектах!\n\n"
        "🔹 **Для вступления в отряд «Жасыл ел»:**\n"
        "— Подготовьте удостоверение личности, справку с места учебы/работы и реквизиты счета.\n\n"
        "🔹 **Для волонтеров:**\n"
        "— Укажите ваши ФИО, возраст, контактный телефон и сферу интересов (экология, социальные акции, мероприятия).\n\n"
        "💬 *Для подачи заявки напишите нашему координатору или отправьте сообщение напрямую в директ/мессенджер МРЦ.*"
    )
    await message.answer(apply_text, parse_mode="Markdown")


# --- Обработчик кнопки "Контакты" ---
@dp.message(F.text == "📞 Контакты")
async def contacts_info(message: types.Message):
    contacts_text = (
        "📍 **Наши контакты и адрес:**\n\n"
        "🏢 **Адрес:** Молодежный ресурсный центр (с. Бесколь / Кызылжарский район)\n"
        "⏰ **Режим работы:** Пн – Пт: с 09:00 до 18:30 (Обед: 13:00 – 14:30)\n"
        "📞 **Телефон для справок:** +7 (705) 000-00-00\n"
        "✉️ **Email:** mrc_kyzylzhar@mail.kz\n\n"
        "📱 **Мы в соцсетях:**\n"
        "• Instagram: [@mrc_kyzylzhar](https://instagram.com)\n"
        "• ВКонтакте: [МРЦ Северо-Казахстанской области](https://vk.com)"
    )
    await message.answer(contacts_text, parse_mode="Markdown", disable_web_page_preview=True)


# --- Запуск бота ---
async def main():
    print("Бот Молодежного ресурсного центра успешно запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())