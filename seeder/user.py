import os

import firebase_admin
from dotenv import load_dotenv
from firebase_admin import auth
from sqlalchemy.exc import IntegrityError
from src.database.db import async_engine, async_session
from src.database.objects.user import User as UserSave


async def main() -> None:
    load_dotenv(verbose=True)
    dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
    load_dotenv(dotenv_path)

    async with async_session() as db:
        try:
            auth.create_user(
                email="admin@purplepalette.net",
                email_verified=True,
                uid="admin",
                display_name="Administrator",
            )
        except firebase_admin._auth_utils.UidAlreadyExistsError:
            print("Firebase User already exists, skipping.")
        else:
            print("Firebase User created.")
        db.add(
            UserSave(
                id=1,
                userId="admin",
                testId="admin",
                accountId="admin",
                description="Administrator",
                isAdmin=True,
                isDeleted=False,
            )
        )
        try:
            await db.commit()
        except IntegrityError:
            print("DB user already exists, skipping.")
        else:
            print("DB user created.")

    await async_engine.dispose()
