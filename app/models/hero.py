from sqlalchemy import Integer, JSON, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Hero(Base):
    __tablename__ = "heroes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))           
    localized_name: Mapped[str] = mapped_column(String(100)) 
    primary_attr: Mapped[str | None] = mapped_column(String(3))   
    attack_type: Mapped[str | None] = mapped_column(String(10))   
    roles: Mapped[list | None] = mapped_column(JSON)          
    img: Mapped[str | None] = mapped_column(String(500))

    match_players: Mapped[list["MatchPlayer"]] = relationship(back_populates="hero")  
