# coding:utf-8
import requests

# 执行api调用并存储响应

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# 将api响应存储在一个变量中
response_dic = r.json()

# 处理结果
print(response_dic.keys())
print("Total repositories:", response_dic['total_count'])

repo_dics = response_dic['items']
print("repositories returned:" + str(len(repo_dics)))

# 研究一个仓库
repo_dic = repo_dics[0]
print("\nKeys:", str(len(repo_dic)))

print("==================================遍历第一个仓库的Key值=================Start================================")
for key in sorted(repo_dic.keys()):
    print(key)
print("==================================遍历第一个仓库的Key值=================End=============================")
print("Name:", repo_dic['name'])
print("Owner:", repo_dic['owner']['login'])
print("Starts:", repo_dic['stargazers_count'])
print("Repository:", repo_dic['html_url'])
print("Created:", repo_dic['created_at'])
print("Updated:", repo_dic['updated_at'])
print("Description:", repo_dic['description'])
