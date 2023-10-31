from fastapi import APIRouter

from app.core.config import settings
from app.schemas.common_schemas import ResponseStatus
from app.schemas.info_schedule import InfoScheduleRequest, InfoScheduleResponse
from app.service.arrange_schedule import arrange_schedule_service
from app.utils import logger

import requests
import random

router = APIRouter()
logger = logger.get_logger(logger_name="ROUTER_ZONE_ARRANGE_SCHEDULE")


@router.post(
    path="/arrange-schedule"
    , description="API for arrange schedule"
    , response_model=InfoScheduleResponse
    , response_model_exclude_none=True
)

async def arrange_schedule(request: dict):
    new_information = {"company_id": request["information"]["company_id"]
                       , "product_id": request["information"]["product_id"]}
    response = InfoScheduleResponse(
        status=ResponseStatus.SUCCESS.name
        , timestamp=request['timestamp']
        , response_id=request['request_id']
        , information=new_information
    )

    try:
        request = InfoScheduleRequest(
            request_id=request['request_id']
            , timestamp=request['timestamp']
            , information=request['information']
            , timeview=request['timeview']
        )
        request_dict = vars(request)
        api_get_settings_url = "http://127.0.0.1:9000/get-settings"
        response_settings = requests.post(api_get_settings_url, json = request_dict)
        response_settings_json = response_settings.json()
        if response_settings_json['status'] == 'SUCCESS':
            api_get_process_list = "http://127.0.0.1:9000/get-process-list"
            response_list_settings = requests.post(api_get_process_list, json = request_dict)
            response_list_settings_json = response_list_settings.json()
            if response_list_settings_json['status'] == 'SUCCESS':
                unique_id = random.randint(1000, 9999)
                api_send_unique_id = "http://127.0.0.1:9000/send-unique-id"
                send_unique_id_data = {'unique_id': unique_id}
                response_send_unique_id = requests.post(api_send_unique_id, json=send_unique_id_data)
                response_send_unique_id_json = response_send_unique_id.json()

                if response_send_unique_id_json['status'] == 'SUCCESS':
                    ### Xử lý hàm
                    a = arrange_schedule_service.some_func()
                    if 
                else:
                    response.status = ResponseStatus.FAILED.name
                    response.message = "Can not send unique_id"
            else:
                response.status = ResponseStatus.FAILED.name
                response.message = response_settings.message
        else:
            response.status = ResponseStatus.FAILED.name
            response.message = response_settings.message
        

    except Exception as e:
        logger.error(e)
        response.status = ResponseStatus.FAILED.name
        response.error_code = e.args[0]
        response.message = str(e)
    return response
