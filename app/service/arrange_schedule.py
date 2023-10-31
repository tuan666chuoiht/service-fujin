from glob import glob

from app.schemas.common_schemas import ErrorCodeAISystem
from app.utils.exception_utils import ArrangeException, SystemError
from app.utils import logger

logger = logger.get_logger(logger_name="SERVICE_ARRANGE_SCHEDULE")

class ArrangeScheduleService:
    def __int__(self):
        pass

    def some_func():
        try:
            logger.info('Hello there!')
        except Exception as e:
            logger.error(e)
            raise ArrangeException(f"search failed {e}", errors=ErrorCodeAISystem.RAI_SYS_003.name)

        try:
            logger.info('Hello there!')
        except Exception as e:
            logger.error(e)
            raise SystemError(f"system processed failed {e}", errors=ErrorCodeAISystem.RAI_SYS_004.name)


arrange_schedule_service = ArrangeScheduleService()





