import enum
from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, Enum, Float, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class ProjectStatus(str, enum.Enum):
    DRAFT = "draft"
    DESIGN = "design"
    SUBMITTED = "submitted"
    UNDER_REVIEW = "under_review"
    APPROVED = "approved"


class ProjectType(str, enum.Enum):
    BASEMENT_RENOVATION = "basement_renovation"
    ADDITIONAL_DWELLING_UNIT = "additional_dwelling_unit"
    DECK = "deck"
    GARAGE = "garage"
    ADDITION = "addition"
    OTHER = "other"


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    project_type: Mapped[ProjectType] = mapped_column(
        Enum(ProjectType),
        nullable=False,
    )

    municipality: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    province: Mapped[str] = mapped_column(
        String(50),
        default="Ontario",
        nullable=False,
    )

    address: Mapped[Optional[str]] = mapped_column(
        String(250),
        nullable=True,
    )

    description: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )

    estimated_value: Mapped[Optional[float]] = mapped_column(
        Float,
        nullable=True,
    )

    status: Mapped[ProjectStatus] = mapped_column(
        Enum(ProjectStatus),
        default=ProjectStatus.DRAFT,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )