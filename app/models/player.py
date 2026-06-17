from datetime import datetime

from sqlalchemy import BigInteger, DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Player(Base):
    __tablename__ = "players"

    steam_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    persona_name: Mapped[str | None] = mapped_column(String(255))
    avatar: Mapped[str | None] = mapped_column(String(500))
    profile_url: Mapped[str | None] = mapped_column(String(500))
    country_code: Mapped[str | None] = mapped_column(String(5))
    rank_tier: Mapped[int | None] = mapped_column(Integer)
    leaderboard_rank: Mapped[int | None] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    match_players: Mapped[list["MatchPlayer"]] = relationship(back_populates="player")  