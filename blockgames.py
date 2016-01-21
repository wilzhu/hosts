#coding:utf-8

import urllib.request as u
import urllib.parse as pa
import time

#过滤器
web_not = []
#网站保存列表
web_list=[]
#百度搜索
url = "http://www.baidu.com/baidu?&ie=utf-8&word="
#成功计数器
count = 0
#网页数
page = 1
print('读取过滤器设置（以下网址将在接下来的操作中排除，你可以在not.ini中设置）：')
f = open('not.ini','rt')
for line in f:
    str1 = line.strip('\n')
    web_not.append(str1)
    print(str1)
f.close()
temp = input('请输入关键词:')
fp = open('hosts','wt')
print('\n正在抓取网址:')
url = url + pa.quote(temp)
ret_flag = 0
while True:
    try:
        req_1 = u.Request(url)
        req_1.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36')
        htm_1 = u.urlopen(req_1).read().decode('utf-8')
    except:
        print('网络出错或下一页url获取失败 5s后结束程序')
        break
    print('第%d页'%page)
    num = 0
    while True:
        num = htm_1.find('<span class="g">', num)
        if num != -1:
            last = num
            num += 16
            end = num
            end = htm_1.find('/',end)
            if end != -1:
                web = htm_1[num:end]
                count += 1
                if web not in web_not and web not in web_list and '<' not in web:
                    web_list.append(web)
                    print(str(count)+'.'+web)
                else:
                    print(str(count)+'.'+'---已过滤')
        else:
            next_page = htm_1.find('下一页', last)
            if next_page != -1:
                next_page -= 12
                break_flag = 0
                for i in range(300):
                    if htm_1[next_page-i-1:next_page-i] == '"':
                        j = next_page - i
                        url_end = htm_1[j:next_page]
                        url = 'http://www.baidu.com'+url_end
                        page += 1
                        break_flag = 1
                        break
                if break_flag == 1:
                    print('++找到‘下一页’网址：')
                    print(url)
                    break;
            else:
                print('已无 下一页 程序将在5s后结束')
                ret_flag = 1
                break
    if ret_flag == 1:
        break
fp.write('#注：本hosts文件由脚本自动抓取并已去重复 可以删除此段文字)\n')
fp.write('#本文件包括 ‘%s’ 关键词的百度前%d页搜索结果 大约 %d条结果\n'%(temp, page, count))
fp.write('#如果此文件对正常网站造成打不开的状况  请在本文件中搜索那个网站地址 并删除那一行\n')
fp.write('\n#下面的网站均在抓取中已忽略 你可以自己添加到hosts文件\n')
for j in web_not:
    fp.write('#'+j+'\n')
fp.write('\n#以下为重定向表\n\n\n')
for i in web_list:
    fp.write('127.0.0.1'+' '+i+'\n')
fp.close()
print('All Done')
time.sleep(5)
