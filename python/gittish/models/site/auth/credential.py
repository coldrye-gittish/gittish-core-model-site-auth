# TBD:LICENSE


from enum import IntEnum, unique

from sqlalchemy import Column
from sqlalchemy.types import String, DateTime

from gittish.core.models.base import Base
from gittish.core.models.mixins.credential import CredentialMixin 


# TBD:DOCUMENT
@unique
class CredentialType(IntEnum):

  # Standard password based authentication
  #
  # Passwords must be encrypted by the client.
  PASSWORD = 0

  # Standard two factor authentication, password based.
  #
  # Note that this is default for the global admin user.
  TWO_FACTOR = 1


# TBD:DOCUMENT
@unique
class CredentialStatus(IntEnum):

  # The credential is valid
  VALID = 0

  # The credential has been invalidated and must be recovered
  INVALID = 1

  # The credential is being recovered
  RECOVERING = 2


# TBD:DOCUMENT
class Credential(Base, CredentialMixin):

	__tablename__ = 'site_auth_credentials'

  __status_class__ = CredentialStatus
  __type_class__ = CredentialType


# vim: expandtab:ts=2:sw=2:
