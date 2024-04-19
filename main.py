import requests
import urllib.parse
import webbrowser


def check_interface():
    url = "https://j.biekanle.com/cj.php"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    if data["code"] == 200 and data["msg"] == "成功":
        return data["data"]
    else:
        return None
    
def get_resource():
    data = check_interface()
    if data:
        if data["state"] == "1":
            webbrowser.open("https://blog.biekanle.com/")  # 打开网站
            pw = data["pw"]
            input_password = input("请输入密码: ")
            if input_password != pw:
                print("密码错误，程序终止。") 
                return
        choice = input("获取源码数量: ")
        hex_domain = '%68%74%74%70://%79%6d%2e%61%61%31%2e%63%6e'
        decoded_domain = urllib.parse.unquote(hex_domain)
        url = decoded_domain + "/getList?page=1&limit={}".format(choice)
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data['code'] == 0:
            json_str = data['data']
            for i in json_str:
                 print("名称：{}，下载地址：{}".format(i['title'],i['down_url']))
    else:
        print("接口请求失败或返回数据不正确。")


get_resource()
input('按任意键退出')


