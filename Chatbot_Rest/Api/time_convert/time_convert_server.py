#-*- coding:utf-8 _*-  
""" 
@author:charlesXu
@file: time_convert_server.py 
@desc: 时间转换器接口
@time: 2019/05/24 
"""

import json
import logging
import datetime

from django.http import HttpResponse, JsonResponse
from Chatbot_Model.Time_Convert.TimeNormalizer import TimeNormalizer


logger = logging.getLogger(__name__)

def time_convert(request):
    '''
    时间转换API
    :param request:
    :return:
    '''
    if request.method == 'POST':
        jsonData = json.loads(request.body.decode('utf-8'))
        try:
            msg = jsonData["msg"]

            tn = TimeNormalizer()
            res = tn.parse(msg)
            localtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            dic = {
                "desc": "Success",
                "ques": msg,
                "res": res,
                "time": localtime,
            }
            log_res = json.dumps(dic)
            logger.info(log_res)
            return JsonResponse(dic)
        except Exception as e:
            logger.info(e)
    else:
        return JsonResponse({"desc": "Bad request"}, status=400)
