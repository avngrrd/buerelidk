from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    localized_name: Mapped[str | None] = mapped_column(String(100))
    cost: Mapped[int | None] = mapped_column(Integer)
    img: Mapped[str | None] = mapped_column(String(500))
