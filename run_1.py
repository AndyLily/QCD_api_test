#-*- coding: UTF-8 -*-
# 调用函数，实现接口测试  -- lily 2020-7-2  优化代码，提高代码复用率

#导入自定义的函数
from Read_Write_Excel import read_casedata
from Read_Write_Excel import write_test_result
from HTTP_Requests_1 import HTTP_requests
#给出全局变量
Token=None
Ip='http://120.78.128.25:8766'

def run_test(filename,sheetname,Ip):
    global Token  #声明为全局变量，以便在函数内使用
    req_result=[]  #存放实际结果
    judge_result=[]  #存放判断结果
    all_case=read_casedata(filename,sheetname)
    for i in range(0,len(all_case)):  #遍历测试用例，依次发送请求
        result=HTTP_requests(Ip+all_case[i][4],eval(all_case[i][5]),Token,all_case[i][3])  #注意读取的用例数据是字符串，需要转换成其原本的格式 --eval()
        req_result.append(result)
        if 'login' in all_case[i][4]:  # 用于获取token值
            Token='Bearer ' + result['data']['token_info']['token']
        #判断实际与预期是否相符
        expected_result=eval(all_case[i][6])
        if (result['code']==expected_result['code'] ) and (result['msg']==expected_result['msg']):
            judge_result.append('pass')
        else:
            print("{}接口：第{}条用例执行失败".format(all_case[i][1],all_case[i][0]))
            judge_result.append('no')
    write_test_result(filename,sheetname,req_result,1) #将用例执行实际结果写入excel
    write_test_result(filename,sheetname,judge_result,0) #将用例是否通过的结果写入excel

#注册接口
run_test('QCD_API_casedata.xlsx','register',Ip)
#登录接口
#run_test('QCD_API_casedata.xlsx','login',Ip)
#充值接口
#run_test('QCD_API_casedata.xlsx','recharge',Ip)
#提现接口
#run_test('QCD_API_casedata.xlsx','withdraw',Ip)
#更新昵称接口
# run_test('QCD_API_casedata.xlsx','update_name',Ip)
#项目列表接口
#run_test('QCD_API_casedata.xlsx','loans',Ip)