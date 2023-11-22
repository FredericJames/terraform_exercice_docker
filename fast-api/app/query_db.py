from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import Session
from sqlalchemy import String
from sqlalchemy import Select

class Base(DeclarativeBase):
    pass

class Role(Base):
    __tablename__ = "public.roles"
    role_id: Mapped[int] = mapped_column(primary_key=True)
    role_name: Mapped[str] = mapped_column(String(255))

    def __repr__(self) -> str:
        return f"Role(role_id={self.role_id!r}, role_name={self.name!r})"

def insertData(engine):
    with Session(engine) as session:
        devrole = Role(role_name = "developper")
        adminrole = Role(role_name = "admin")

        session.add_all([devrole, adminrole])
        session.commit()

def readData(engine) -> list[str]:
    session = Session(engine)
    stmt = Select(Role)

    results = session.scalars(stmt)
    
    roles = []
    for role in results:
        roles.append(repr(role))
    return roles