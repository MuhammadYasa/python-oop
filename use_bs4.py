import requests

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200: # apabila response sukses maka akan cetak di bawah
        # print(f'sukses ! {response}') # f digunakan untuk string variabel baru pada python
        print(f'sukses! Response = {response.status_code}') # f digunakan untuk string variabel baru pada python
        print(f'content {response.text}') # di text ini menampilkan teks / kalimat dari respons
    else:
        print(f'terjadi kesalahan pada requests = {response.status_code}') # menampilkan error nilai status code
    # print('\nsukses')
except Exception as e:
    print(f'there is an error {e}') # f digunakan untuk string variabel baru pada python

print('end program')
