from sqlalchemy import Column, Integer, String, ForeignKey
from db import Base


# define models
class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    password = Column(String(length=255), nullable=False)
    email = Column(String(length=255), nullable=False)
    username = Column(String(length=255), nullable=False)


class Roles(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(length=255), nullable=False)


class Permissions(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(length=255), nullable=False)


class RolePermission(Base):
    __tablename__ = "role_permissions"

    role_id = Column(Integer, ForeignKey("roles.id"), primary_key=True, nullable=False)
    permission_id = Column(
        Integer, ForeignKey("permissions.id"), primary_key=True, nullable=False
    )


class UserRoles(Base):
    __tablename__ = "user_roles"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True, nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"), primary_key=True, nullable=False)
