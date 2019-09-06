# -*- coding: utf-8 -*-
# @Time    : 2019-9-6 11:36
# @Author  : 'LiXianfeng'
# @File    : test0906.py
# @Software: PyCharm Community Edition

from phone import Phone

if __name__ == "__main__":
    for line in open("./phone_section.txt", "r"):
        phoneNum = line.strip(" \t\r\n")
        # phoneNum = '19903763750'
        info = Phone().find(phoneNum)
        # print(info)
        try:
            phone = info['phone']
            province = info['province']
            city = info['city']
            zip_code = info['zip_code']
            area_code = info['area_code']
            phone_type = info['phone_type']
            print(phone+"\t"+province+city+"\t"+phone_type+"\t"+zip_code)
        except:
            print(phoneNum+"\t"+'none'+"\t"+"\t")