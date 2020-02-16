# These and other macros are documented in dhd/droid-hal-device.inc
%define device davinci
%define vendor xiaomi
%define vendor_pretty Xiaomi
%define device_pretty Redmi K20
%define installable_zip 1
%define droid_target_aarch64 1

# Entries migrated from the old rpm/droid-hal-hammerhead.spec
%define enable_kernel_update 1

%define straggler_files \
    /bt_firmware \
    /bugreports \
    /d \
    /cache \
    /sdcard \
    /dsp \
    /firmware \
    /persist \
    /product \
    /odm \
    /system \
    /vendor \
    /verity_key \
    /oem \
%{nil}

%define additional_post_scripts \
/usr/bin/groupadd-user media_rw || :\
%{nil}
 
%define android_config \
#define WANT_ADRENO_QUIRKS 1\
%{nil}

# On Android 8 the system partition is (intended to be) mounted on /.
%define makefstab_skip_entries /vendor /dev/stune /dev/cpuset /sys/fs/pstore /dev/cpuctl

%include rpm/dhd/droid-hal-device.inc
