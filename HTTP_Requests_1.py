#-*- coding: UTF-8 -*-
# 实现发送HTTP请求功能  -- lily 2020-7-2

import requests
#对代码进一步优化
def HTTP_requests(url, data, token=None, method='POST'):  #实现get和post两种请求方式
    #因为请求头部分，对不同的接口只有'Authorization'项不一样，因此可以其值作为参数
    header={'X-Lemonban-Media-Type': 'lemonban.v2','Authorization':token}
    if method=='GET':
        result=requests.get(url, params=data, headers=header)
    elif method=='PATCH':
        result=requests.patch(url, json=data, headers=header)
    else:
        result = requests.post(url, json=data, headers=header)
    return result.json()

if __name__ == '__main__':  #用于测试函数功能
    log_url='http://120.78.128.25:8766/futureloan/member/login'
    data = {'mobile_phone': '13549468803', 'pwd': 'lemon1234'}
    log_result=HTTP_requests(log_url,data)
    print(type(log_result))
    print('登录返回信息：{}'.format(log_result))