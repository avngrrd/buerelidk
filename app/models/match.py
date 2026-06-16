from sqlalchemy import BigInteger, Boolean, ForeignKey, Integer, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Match(Base):
    __tablename__ = "matches"

    match_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    duration: Mapped[int | None] = mapped_column(Integer)       
    start_time: Mapped[int | None] = mapped_column(BigInteger)  
    game_mode: Mapped[int | None] = mapped_column(SmallInteger)
    lobby_type: Mapped[int | None] = mapped_column(SmallInteger)
    radiant_win: Mapped[bool | None] = mapped_column(Boolean)
    patch: Mapped[int | None] = mapped_column(SmallInteger)
    region: Mapped[int | None] = mapped_column(SmallInteger)
    avg_mmr: Mapped[int | None] = mapped_column(Integer)

    players: Mapped[list["MatchPlayer"]] = relationship(back_populates="match")


class MatchPlayer(Base):
    __tablename__ = "match_players"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    match_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("matches.match_id"), index=True)
    steam_id: Mapped[int | None] = mapped_column(BigInteger, ForeignKey("players.steam_id"), index=True)
    hero_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("heroes.id"))
    slot: Mapped[int | None] = mapped_column(SmallInteger)   
    is_radiant: Mapped[bool | None] = mapped_column(Boolean)
    win: Mapped[bool | None] = mapped_column(Boolean)
    level: Mapped[int | None] = mapped_column(SmallInteger)

    # KDA
    kills: Mapped[int] = mapped_column(SmallInteger, default=0)
    deaths: Mapped[int] = mapped_column(SmallInteger, default=0)
    assists: Mapped[int] = mapped_column(SmallInteger, default=0)

    # Economy
    gold_per_min: Mapped[int] = mapped_column(Integer, default=0)
    xp_per_min: Mapped[int] = mapped_column(Integer, default=0)
    last_hits: Mapped[int] = mapped_column(Integer, default=0)
    denies: Mapped[int] = mapped_column(Integer, default=0)
    net_worth: Mapped[int] = mapped_column(Integer, default=0)

    # Impact
    hero_damage: Mapped[int] = mapped_column(Integer, default=0)
    tower_damage: Mapped[int] = mapped_column(Integer, default=0)
    hero_healing: Mapped[int] = mapped_column(Integer, default=0)

    # Items 
    item_0: Mapped[int | None] = mapped_column(Integer)
    item_1: Mapped[int | None] = mapped_column(Integer)
    item_2: Mapped[int | None] = mapped_column(Integer)
    item_3: Mapped[int | None] = mapped_column(Integer)
    item_4: Mapped[int | None] = mapped_column(Integer)
    item_5: Mapped[int | None] = mapped_column(Integer)
    backpack_0: Mapped[int | None] = mapped_column(Integer)
    backpack_1: Mapped[int | None] = mapped_column(Integer)
    backpack_2: Mapped[int | None] = mapped_column(Integer)
    neutral_item: Mapped[int | None] = mapped_column(Integer)

    match: Mapped["Match"] = relationship(back_populates="players")
    player: Mapped["Player | None"] = relationship(back_populates="match_players") 
    hero: Mapped["Hero | None"] = relationship(back_populates="match_players")  
