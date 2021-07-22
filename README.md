# File-sharing-Bot

  </a>
  <a href="https://t.me/virtualmeresahkan1">
    <img src="https://github.com/ibrasptra791/PyrogramGenStr/blob/main/resources/madebycodex-badge.svg" width="250">
  </a><br>
  <a href="https://t.me/virtualmeresahkan18">
    &nbsp;<img src="https://img.shields.io/badge/Code%20%F0%9D%95%8F%20virtual-Channel-blue?style=flat-square&logo=telegram" width="130" height="18">&nbsp;
  </a>
  <a href="https://t.me/virtualmeresahkan1">
    &nbsp;<img src="https://img.shields.io/badge/Code%20%F0%9D%95%8F%20virtual-Group-blue?style=flat-square&logo=telegram" width="130" height="18">&nbsp;
  </a>  
</p>


Telegram Bot untuk menyimpan Posting dan Dokumen dan dapat Diakses melalui Tautan Khusus.
Saya Kira Ini Akan Bermanfaat Bagi Banyak Orang.....😇.

##

### Features
- Sepenuhnya dapat disesuaikan.
- Pesan selamat datang yang dapat disesuaikan.
- Lebih dari satu Posting dalam Satu Tautan.
- Dapat di-deploy di heroku secara langsung.

### Setup

- Tambahkan bot ke Saluran Basis Data dengan semua izin
- Tambahkan bot ke saluran ForceSub sebagai Admin dengan Undang Pengguna melalui Izin Tautan jika Anda mengaktifkan ForceSub

##
### Installation
#### Deploy on Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)</br>

#### Deploy in your VPS
````bash
git clone https://github.com/ibrasptra791/kon
cd File-Sharing-Bot
pip3 install -r requirements.txt
# <Create config.py appropriately>
python3 main.py
````

### Admin Commands

```
/start - start the bot or get posts

/batch - create link for more than one posts

/genlink - create link for one post

```

### Variables

* `API_HASH` Hash API Anda dari my.telegram.org
* `API_ID` ID API Anda dari my.telegram.org
* `TG_BOT_TOKEN` Token bot Anda dari @BotFather
* `OWNER_ID` Harus memasukkan Id Telegram Anda
* `CHANNEL_ID` ID Saluran Anda, misalnya:- -100xxxxxxxxx
* `ADMINS` Opsional: Daftar user_id Admin yang dipisahkan spasi, mereka hanya dapat membuat tautan
* `START_MESSAGE` Opsional: mulai pesan bot, gunakan HTML dan <a href='https://github.com/shahsad-klr/File-Sharing-Bot/blob/main/README.md#start_message'>isian< /a>
* `FORCE_SUB_CHANNEL` Opsional: ForceSub Channel ID, biarkan 0 jika Anda ingin menonaktifkan force sub

### Fillings
#### START_MESSAGE

* `{first}` - User first name
* `{last}` - User last name
* `{id}` - User ID
* `{mention}` - Mention the user
* `{username}` - Username

#### CUSTOM_CAPTION

* `{namafile}` - nama file Dokumen
* `{previouscaption}` - Teks Asli

