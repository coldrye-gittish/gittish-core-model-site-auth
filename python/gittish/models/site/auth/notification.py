# TBD:LICENSE


from enum import IntEnum, unique

from sqlalchemy import Column
from sqlalchemy.types import String, DateTime

from gittish.core.models.base import Base
from gittish.core.models.mixins.creatable import CreatableMixin
from gittish.core.models.mixins.modifyable import ModifyableMixin
from gittish.core.models.mixins.status import StatusMixin
from gittish.core.models.mixins.typed import TypedMixin
from gittish.core.models.mixins.owned import OwnedMixin


# TBD:DOCUMENT
@unique
class NotificationConfigType(IntEnum):

  # E-Mail address used for authentication related
  # notification purposes
  #
  # Note: this must be kept in sync with the actor's
  # main e-mail address
  MAIL = 0

  # Possible extensions here:
  # MOBILE = 1


# TBD:DOCUMENT
@unique
class NotificationConfigStatus(IntEnum):

  # The configuration is being validated
  VALIDATING = 0

  # The configuration has been validated
  VALID = 1

  # The validation attempt failed
  INVALID = 2

  # The configuration needs revalidation
  MUST_REVALIDATE = 3


# TBD:DOCUMENT
class NotificationConfig(Base, CreatableMixin, ModifyableMixin, OwnedMixin, TypedMixin, StatusMixin):

  __tablename__ = 'site_auth_notification_configs'

  __status_class__ = NotificationConfigStatus
  __type_class__ = NotificationConfigType

  # Based on the type, this can for example be an email address
  data = Column('data', String, nullable = False)
  valid_since = Column('valid_since', DateTime, nullable = True)
  invalidated_when = Column('invalidated_when', DateTime, nullable = True)
  invalidated_by = Column('invalidated_by', Binary(length = 16), nullable = True)


# vim: expandtab:ts=2:sw=2:
