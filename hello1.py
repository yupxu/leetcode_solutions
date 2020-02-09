import requests

headers = {
	# 'Cookie' : '_zap=81f33f36-28f4-431d-b0dd-d42d850244c6; _xsrf=4bb1c387-03de-47b0-8223-2e6f7664240b; d_c0="AJCi3QGC6g6PTn1RlZWiIlyyUH5JZ1whehs=|1549035723"; q_c1=5418274c2bb549e78cd4d8d06abacc67|1549035726000|1549035726000; __gads=ID=0e258348001c7396:T=1557148687:S=ALNI_MahtULQI6A30Zbd-4IjmjJ78FN6Qw; capsion_ticket="2|1:0|10:1580650752|14:capsion_ticket|44:YjFkNmU0NzYwMzVhNDBmYzhlZWRmNGVjYzhiY2IxMTI=|ca7f57b44761794386ba0535ae9e4448b98ce56ae723e2516fe4186478df9d86"; z_c0="2|1:0|10:1580650771|4:z_c0|92:Mi4xaVNvSEFnQUFBQUFBa0tMZEFZTHFEaVlBQUFCZ0FsVk5FeDhrWHdCbG1iSXJyRVFZVTZNQmJWVEp1SlBidmRIX1JB|aef10fd60ad63d63d5e2549a85903da622700f21a32edd030ccdb781f61c0d5c"; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1580650342,1580650660,1580692385,1580693472; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1580693472; KLBRSID=4843ceb2c0de43091e0ff7c22eadca8c|1580693473|1580691619',
	# 'Host' : 'www.zhihu.com',
	'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) chrome/52.0.2743.116 Safari/537.36'

}
r = requests.get("https://www.xvideos.com/", headers=headers)
print(r.text)