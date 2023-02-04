from whois import whois
i=input('请输入查询域名')
data=whois(i)
print(data)
