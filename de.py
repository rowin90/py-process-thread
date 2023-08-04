import requests

url = "https://detail.tmall.com/item_o.htm?de_count=1&id=556870340427&skuId=5131486927235&spm=a221t.1476805.goodlist.8.11186769Ewaplc&userBucket=10"

payload = {}
headers = {
    'authority': 'detail.tmall.com',
    'accept': 'text/html,applicatixon/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,sq;q=0.7',
    'cache-control': 'no-cache',
    'cookie': 'lid=%E5%97%A8%E5%B1%811024782124; cna=4ulIGeqAMjgCAXyg4Solyisd; tracknick=%5Cu55E8%5Cu5C411024782124; dnk=%5Cu6211%5Cu662F%5Cu4E00%5Cu53EA%5Cu6653%5Cu6653%5Cu5B9D; lgc=%5Cu55E8%5Cu5C411024782124; login=true; cancelledSubSites=empty; enc=Q1SVP1MoSZ8P1O3JLl0DOkviTrv6vutAwiygQTojafi6ZdQBlNGi5FhGN1ZJZn7fpJB9iA1aFEMWYCTGodGM6g%3D%3D; xlly_s=1; uc1=cookie14=Uoe9bFpStPxOlA%3D%3D&cookie21=W5iHLLyFfXVRCJf5lG0u7A%3D%3D&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&existShop=false&cookie15=UIHiLt3xD8xYTw%3D%3D&pas=0; uc3=nk2=gzu8O%2FdrseVApVQ6V4U%3D&vt3=F8dCsGCn964UWM2R8zo%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D&id2=UNJUsD%2BJKw0V; _l_g_=Ug%3D%3D; uc4=nk4=0%40gWTjG8VDt59u8U%2FvbvqpqhHvrbaR9XLIhw%3D%3D&id4=0%40UgXTvjLMZB05NKaq%2FrDYkAbu%2Bdg%3D; unb=325349862; cookie1=AHxGUe66MHB1YPdRVj9eyvXgahky1A3FFTakR%2F3eDLY%3D; cookie17=UNJUsD%2BJKw0V; cookie2=1d2e5bafbcadd0431937a9c78a5334cf; _nk_=%5Cu55E8%5Cu5C411024782124; sgcookie=E100mM1Bn37faU3WUk5omgKUk2KzrXQcwXTxiz%2Fs8g%2FIA1E8%2BrwI9zK%2B0dtqFcmx%2BhZ8VXkR9FcPy1N%2BE1AmTRbIeHFQu9DnheLs7nmVExKEC%2FAD%2BG%2Ft44L709RFwfuP%2FVqn; sg=42d; t=dbf0fb904a04eb564423fec60551b33e; csg=b902582d; _tb_token_=5ee7da35e85e3; _m_h5_tk=ea5a11efe7c511bea58be92f871dcf75_1691051478327; _m_h5_tk_enc=a00067a2cf04be5ff3954403bb00b066; pnm_cku822=098%23E1hv0QvUvbZvUvCkvvvvvjiWnLzv6jECPFdZ6jthPmPWsjEbn2qvlj3ERFcO0jE2i9hvCvvvpZpgvpvhvvCvpvgCvvpvvPMMvvhvC9vhphvvvv9CvhAvXWbmjO0QKfUpahqEDLuTRLa9C7zUdiTAdch%2B%2BE7re8TJO9jEkC465dUf85cGeE9wejnE6WvfVBOqb64B9Cka%2BfvsxI2ZjLeARFxjKvhv8PMMSHzMMQmovvCh89vv9HhvvhNjvvvmjvvvBGwvvv8PvvCh89vvvI%2FUvpvjvpC2pWLhVu9Cvv9vvhjUTijq4p%3D%3D; tfstk=dFf9XNfp3y39sGJAGFe3g8srSO43x1QwvG7SinxihMId4gh07OjcpEshDIAcllSAMHstiObg_iBdba9GDZzwlnsfDnXgK7bN7IRbqiFuZNkHQIZofixK2NR2Gu0nG8VR7glaQnXr52g8eoGFTsY_hJvIUudRsFp92jxKMjUDWdK55HE7VORVZ_FY10xJoAaLJxk2Ceuv3NwF.; l=fBgKpKs4Ne9zKgGbBOfwPurza77OSIRAguPzaNbMi9fPOQfe5SzfB1OGUeTwC3GVF6kDR37fwLl9BeYBcSxMhrD66taWQdkmnmOk-Wf..; isg=BLCw6yzUoHg7vXx8VnF5Gwj6gXgC-ZRDeugtoKoBfIvfZVAPUglk0wbXvW0FdUwb',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
