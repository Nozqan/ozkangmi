[app]

# (str) Title of your application
title = OzkanGMI

# (str) Package name
package.name = ozkangmi

# (str) Package domain (needed for android packaging)
package.domain = org.nozqan

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,kivy==2.2.1,kivymd==1.1.1,hostpython3,certifi

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API - En stabil sürüm 33
android.api = 33

# (int) Minimum API support
android.minapi = 21

# (str) Android SDK Build-Tools version - HATAYI ÇÖZEN SATIR BURASI
# Loglarda çıkan 37 hatasını engellemek için 33.0.0'a sabitliyoruz
android.sdk_build_tools_version = 33.0.0

# (str) Android NDK version
android.ndk = 25b

# (list) Android architectures (Senin Redmi Note 14 Pro için şart)
android.archs = arm64-v8a, armeabi-v7a

# (str) Python-for-android branch
p4a.branch = master

# (str) Bootstrap to use (Logdaki uyarıya göre p4a formatı)
p4a.bootstrap = sdl2

# (bool) Allow backup
android.allow_backup = True

# (str) The format used to package the app
android.release_artifact = apk
android.debug_artifact = apk

[buildozer]

# (int) Log level (2 = debug, hataları görmek için)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
