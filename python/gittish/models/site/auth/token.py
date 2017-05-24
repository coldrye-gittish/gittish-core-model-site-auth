# TBD:LICENSE


from enum import IntEnum, unique

from sqlalchemy import Column
from sqlalchemy.types import String, DateTime

from gittish.core.models.base import Base
from gittish.core.models.mixins.creatable import CreatableMixin
from gittish.core.models.mixins.status import StatusMixin
from gittish.core.models.mixins.typed import TypedMixin
from gittish.core.models.mixins.owned import OwnedMixin


# TBD:DOCUMENT
@unique
class SingleUseTokenType(IntEnum):

  # Password recovery
  RECOVERY = 0

  # Two factor authentication
  AUTHENTICATION = 1

  # Config validation
  VALIDATION = 2


# TBD:DOCUMENT
@unique
class SingleUseTokenStatus(IntEnum):

  # The token is valid
  VALID = 0

  # The token has been used
  USED = 1

  # The token has expired
  EXPIRED = 2


# TBD:DOCUMENT
# the owner is the credential
class SingleUseToken(Base, CreatableMixin, OwnedMixin, TypedMixin, StatusMixin):

  __tablename__ = 'site_auth_single_use_token'

  __status_class__ = SingleUseTokenStatus
  __type_class__ = SingleUseTokenType

  data = Column('data', String, nullable = False)
  valid_until = Column('valid_until', DateTime, nullable = False)


# vim: expandtab:ts=2:sw=2:
