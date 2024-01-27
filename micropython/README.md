# Running on pure micropython
This contains my examples of where to go with pure micropython

1. Start with https://micropython.org/download/LEGO_HUB_NO6/
2. Download [this](https://micropython.org/resources/firmware/LEGO_HUB_NO6-20240105-v1.22.1.dfu) from the above site
3. Install dfu-util if not previously installed from: https://dfu-util.sourceforge.net
4. Put the hub into bootloader mode by holding the BLE button down while plugging in the hub and holding the button down until it flashes between purple, blue, and green.
5. Run `dfu-util --alt 0 -D LEGO_HUB_NO6-20240105-v1.22.1.dfu` from within downloads (since that is where the firmware downloaded) in terminal
6. Then restart the hub and get the standard “cannot read the hard drive” error - but it all worked. (note: I had to disconnect and reconnect my cable once…)
7. You can get rid of the above error by pressing ignore or by making a mboot and deploying that as well.
