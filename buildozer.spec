[app]
title = Shopping List
package.name = shoppinglist
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,sd12_ttf,pillow
orientation = portrait
fullscreen = 0

[android]
android.sdk_path = /path/to/android/sdk
android.ndk_path = /path/to/android/ndk
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.private_storage = True
android.sdk_api = 31
android.minapi = 21
android.target_api = 31

[buildozer]
log_level = 2
warn_on_root = 1
