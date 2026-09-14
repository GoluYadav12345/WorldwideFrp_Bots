import os
import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder


BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is missing")


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def main_menu():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="🔗 Connect Account", callback_data="connect")
    keyboard.button(text="📝 Register Account", callback_data="register")
    keyboard.button(text="🔐 Login Account", callback_data="login")
    keyboard.button(text="🟢 Server Status & Price", callback_data="status")
    keyboard.button(text="⬇️ Download Tool", callback_data="download")
    keyboard.button(text="💬 Contact Us", callback_data="contact")

    keyboard.adjust(1, 2, 1, 1, 1)

    return keyboard.as_markup()


@dp.message(CommandStart())
async def start(message: Message):
    text = (
        "🔥 <b>FIRE FRP TOOL</b>\n"
        "Professional Android Service Tool\n\n"
        "🔗 <b>Welcome!</b>\n"
        "Your account is not connected yet.\n\n"
        "Connect your account to access available bot features."
    )

    await message.answer(
        text,
        reply_markup=main_menu(),
        parse_mode="HTML"
    )


@dp.callback_query(F.data == "connect")
async def connect(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "🔗 <b>Connect Account</b>\n\n"
        "Please register or login first.",
        parse_mode="HTML"
    )


@dp.callback_query(F.data == "register")
async def register(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "📝 <b>Register Account</b>\n\n"
        "Registration system coming soon.",
        parse_mode="HTML"
    )


@dp.callback_query(F.data == "login")
async def login(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "🔐 <b>Login Account</b>\n\n"
        "Login system coming soon.",
        parse_mode="HTML"
    )


@dp.callback_query(F.data == "status")
async def status(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "🟢 <b>Server Status & Price</b>\n\n"
        "🟢 Server: Online\n"
        "⚡ Status: Normal\n\n"
        "💰 Price: Contact Admin",
        parse_mode="HTML"
    )


@dp.callback_query(F.data == "download")
async def download(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "⬇️ <b>Download Tool</b>\n\n"
        "Download link will be added here.",
        parse_mode="HTML"
    )


@dp.callback_query(F.data == "contact")
async def contact(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "💬 <b>Contact Us</b>\n\n"
        "Please contact Admin for support.",
        parse_mode="HTML"
    )


async def main():
    print("🔥 FIRE Telegram Bot is running...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
