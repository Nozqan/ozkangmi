[app]
title = OzkanGMI
package.name = ozkangmi
package.domain = org.nozqan
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0

# KivyMD ve Pillow eksiksiz eklendi
requirements = python3,kivy==2.2.1,kivymd==1.1.1,pillow,hostpython3,certifi

orientation = portrait
fullscreen = 1
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.sdk_build_tools_version = 33.0.0
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
p4a.branch = master
p4a.bootstrap = sdl2
android.release_artifact = apk
android.debug_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 1
