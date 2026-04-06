[app]

title = ÖzkanGMİ
package.name = ozkangmi
package.domain = org.ozkan

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy

orientation = portrait

# İzinler
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# 🔥 KRİTİK AYARLAR (HATAYI ÇÖZER)
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build_tools = 33.0.2

# Daha stabil build için
android.accept_sdk_license = True
