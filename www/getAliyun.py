#!usr/bin/env python
# -*-coding: utf-8 -*-

__author__ = "weely"

'''
    10点抢阿里云免费云接口
    公网地址： 47.100.47.234
    阿里云空间账户： root，  @为220930    远程连接密码： 420698  
'''

import urllib
import requests


HTTPURL = '''https://free.aliyun.com/json/gainTicket.json?trialType=0&umidToken=Y0b03a9b1fde83d89cc199a63e42ae7d5&collina=099%23KAFEU7E6EeUEIYTLEEEEE6twSci7C6P3ScLFC6VqS9lEG6NwZca5A6tEZXw7G6DcSrULE7Eht3BlllfNJGFETRpCD6xsE7E5t3581pCdt3iSseMEs73Sp37XlV%2BNE7EFb%2FR5DK5TEEiStEE7%2FGFETKxqAjFJE7Eht3alluZde7FE5YhL0fmqRHvkLmoZbHUQmQ%2FoJhXdfx%2BI%2BFURyUQnBFt0DUDkun64vm8onhstpxA0DYVB6OT26DXR8PP%2BrCY%2B%2BFURkmwLBwS0Ztgf0OT%2Fff00DYQfE7EIt37E9BfPmn8%2FE7Eht%2FMFE6r3O7FEp3iSlllP%2F3iSt375luZdt9nStTilsyanNliSH3lP%2F393t375luZdtduJE7Jrb4nmei7WadWc73%2F5qa4R1aSpr6hdr4St%2BUZVNLoWwMVtxWywbzoRSqQRzbuC6QUR9MrAAxUVwEO63yaIPL2T1UeprdQncbtc1UeAZwpXx4PR3rXTvRJt3dTRsoE2hLlElow4DO1k%2F%2FslEcpJbRKuEJsR%2FqYWcIVE9BZDDOhnwSn33yB0PRG3iiZprt2B6UZRwFnsNsXawFZK1OLj%2FRz63oa3rM2GbMe6wSZYDw8G%2BYbqCu8Rqaqu94bEPVUyJFbElylYDgCkGRQu1%2FvK8KUE3GbpbMpo8obsLblzZR5U3QOhwRvzbW2qgGbu89hbpb1K%2BM%2FCvphnCGbTcWyC%2FwYREi%2FcPoXGPUQTuasgD%2Bhx3%2Fdu3e9ccORs3%2FduVbq08vQ1uasgSA4yuasl3rywh0UuY%2FbuQfq0rYSqCdXsSRInuasl3rywh0zuE%2FbuQfq0OwlulbwYDzGo%2FUUElu3mhLKu%2FGPlV6kMqytl14eDDRI0uasl3rywh0UuY%2FbuQfq0c7ls3%2Fl8DKI0lnQ1uuyihjvqadlczQI08vQ1uasgSCcx3%2Fdu7sREbOIt1bSqOfYnHQe6w9%2F8SA4Liod6L%2FJw8gNwxSQRb0708LVw1t14Gi8S1SZp1lJw8gNw%2BG%2F3Y3pSbqStaquVD0I0laQuuuyi8CI9E7EFbOR5DE%3D%3D'''
header = {
    "cookie": r'''aliyun_choice=CN; JSESSIONID=MT6668B1-FPJPSLK6V7EE813PDLNM2-6VT9DOBJ-88E8; free_aliyun_com_tmp0=eNrz4A12DQ729PeL9%2FV3cfUxiKrOTLFS8g0xMzOzcDLUdQvwCgj28TYLM3d1tTA0DnDx8fM10jULC7F08Xfy0rWwcLVQ0kkusTI0NTQxNjY3MjA1NjPSSUxGE8itsDKojQIAHQEb0Q%3D%3D; cnz=teHJErTaGXwCAf280d7DHiZ9; _uab_collina=151433720558689040334646; cna=teHJEo6i4TMCAd7RvP15Y0pr; _ga=GA1.2.1740455870.1514337206; _gid=GA1.2.1774595193.1514337206; aliyun_lang=zh; activeRegionId=cn-beijing; _umdata=ED82BDCEC1AA6EB9CACDA7516FB98F202F504BDAB4C286A1B119A9C056A3211475999B42CDC19494CD43AD3E795C914C2D89D5C984BDF01660706482CABAEB31; login_aliyunid="155253****@qq.com"; login_aliyunid_ticket=IZor6q7SCxRtgmGCbifG2Cd4ZWazmBdHI6sgXZqg4XFWQfyKpeu*0vCmV8s*MT5tJl3_1$$wLn3wIKRUsDgafeYr1dlxOt0opKrtnlkKkSSnCQ5LGxf_YNpoU_BOTwChTBoNM1ZJeedfK9zxYnbN5hss0; login_aliyunid_csrf=_csrf_tk_1842114424697995; login_aliyunid_pk=1620010819393360; hssid=1x6AuAHzOnIZGgEHWsKuv3Q1; hsite=6; aliyun_country=CN; aliyun_site=CN; _gat=1; isg=Aj4-QLF46K2K9jyN2BAC14Z5j1SKejbtkFFXSOhHhgF8i99lUA7YCY0td2G8''',
    "user-agent" : r'''Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'''
}
ck = {

}
r = requests.get(HTTPURL, header)