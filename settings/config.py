import  os
import  logging

base_dir = os.path.dirname(os.path.dirname(__file__)).replace('\\','/')


#用例根目录
case_root_path = os.path.join(base_dir,'cases','system')

#测试报告根路径
report_root_path = os.path.join(base_dir,'report')



#邮件配置信息
mail_info = {
    'concent':{
        'host':'mail.tcl.com',
        'port':25
    },
    'login':{
        'username':'tangyong01',
        'passwd':'jy170530.'
    },
    'sender':'tangyong01@kuyumall.com',
    'receiver':['tangyong01@kuyumall.com','tyongjob@163.com','ty334420163@qq.com'],
    'subject':'聚采平台自动化测试'
}


#日志层级
log_level_list={
    'debug':logging.DEBUG,
    'info':logging.INFO,
    'warning':logging.WARNING,
    'error':logging.ERROR,
    'critical':logging.critical
}
log_level = log_level_list['info']
























# from  selenium import  webdriver
# from  selenium.webdriver.common.by import By
# import smtplib
# from email.header import Header
# from email.mime.text import  MIMEText
# from email.mime.multipart import MIMEMultipart
# import  xlrd
# driver  =webdriver.Chrome()
#
# url  = 'http://10.0.101.163:81/JcLogin'
#
# def get_excel_data(row_no,col_no,file_name,sheet_index=0):
#     file_dir = os.path.join(base_dir,'settings',file_name)
#     work_bok = xlrd.open_workbook(file_dir)
#     sheet = work_bok.sheet_by_index(sheet_index)
#     cell_data = sheet.cell(row_no,col_no).value
#     return  cell_data
