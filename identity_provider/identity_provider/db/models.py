import uuid

from identity_provider.db.db_config import Base
from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID


class User(Base):
    __tablename__ = 'user'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(80), nullable=False)
    first_name = Column(String(80), nullable=False)
    second_name = Column(String(80), nullable=False)
    email = Column(String(80), nullable=False)
    hashed_password = Column(String, nullable=False)
    is_superuser = Column(Boolean, nullable=False, default=False)
