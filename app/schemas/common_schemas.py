from enum import Enum


class ErrorCodeCommon(Enum):
    CMN_VAL_001 = 1
    CMN_VAL_002 = 2
    CMN_VAL_003 = 3


class ErrorCodeAISystem(Enum):
    FU_SYS_001 = 1
    FU_SYS_002 = 2
    FU_SYS_003 = 3
    FU_SYS_004 = 4


class ResponseStatus(Enum):
    UNKNOWN_STATUS = 0
    SUCCESS = 1
    FAILED = 2
