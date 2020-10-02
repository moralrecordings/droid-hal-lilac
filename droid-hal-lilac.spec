# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device lilac
%define vendor sony

%define vendor_pretty Sony
%define device_pretty Xperia XZ1 Compact

%define droid_target_aarch64 1

%define installable_zip 1

%define straggler_files \
/nonplat_file_contexts \
/nonplat_hwservice_contexts \
/nonplat_property_contexts \
/nonplat_seapp_contexts \
/nonplat_service_contexts \
/plat_file_contexts \
/plat_hwservice_contexts \
/plat_property_contexts \
/plat_seapp_contexts \
/plat_service_contexts \
/sepolicy \
/verity_key \
/vndservice_contexts \
%{nil}

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"
# On Android 8 the system partition is (intended to be) mounted on /.
%define makefstab_skip_entries / /dev/stune /dev/cpuset /sys/fs/pstore /dev/cpuctl

%include rpm/dhd/droid-hal-device.inc
