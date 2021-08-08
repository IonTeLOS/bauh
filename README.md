**Waffles** is a graphical interface for managing modern types of Linux applications. Waffles supports the following formats: **AppImage**, **Flatpak**, **Snap** and **Web apps**.

Waffles is a simplified fork of [bauh](https://github.com/vinifmor/bauh) for Debian and Debian-based Linux distributions.

Key features
- A management panel where you can: *search*, *install*, *uninstall*, *upgrade*, *downgrade* and *launch* your AppImage, Flatpak, Snap and Web applications. Runtimes can also be upgraded.
- Tray mode: It launches attached to the system tray and publishes notifications, when there are available software updates.

DISCLAIMERS:
1. Waffles is **not** a .deb package/software manager or builder. There are already a lot of excellent conventional tools for those jobs, usually distro-specific but also some generic ones.
2. Waffles does not imply that you can or should substitute all or most of your .deb files with AppImage, Flatpak, Snap and Web applications. Waffles is here to *supplement* conventional packages and software manager applications. More choice for users means more freedom. And Linux above all *is* about Freedom! Easier app management, less messing with dependencies - versions - distro-specific choices means that more non-technical users will be able to enjoy Linux.
3. Waffles comes with ABSOLUTELY NO WARRANTY to the extent permitted by applicable law.

A testing [.deb package](https://github.com/IonTeLOS/waffles/releases/download/1.1/waffles_1.1-1_amd64.deb) of Waffles, compatible with Debian Bullseye has been released. To try it **now** add our repository to your sources: 

curl -s --compressed "https://iontelos.github.io/repo/KEY.gpg" | sudo apt-key add -
sudo curl -s --compressed -o /etc/apt/sources.list.d/my_list_file.list "https://iontelos.github.io/repo/my_list_file.list"

Alternatively you can directly download the .deb file from our release and install it running following command from the same directory you downloaded the .deb file to : sudo apt install ./waffles_1.1-1_amd64.deb (or whatever package name you are installing)

This will take care of all necessary dependencies automatically. Installing snapd is recommended (and necessary to manage Snap applications), but optional. If you choose to install snapd make sure you also install snap core. Follow the [official instructions](https://snapcraft.io/docs/installing-snapd).

An experimental [AppImage](https://github.com/IonTeLOS/waffles/releases/download/1.1/Waffles-1.1-x86_64.AppImage) of Waffles has been also released.

Download it, open terminal in the same directory and run following command : chmod +x Waffles-1.1-x86_64.AppImage

You can then simply click the AppImage file to run the app.

To be able to run the AppImage successfully, make sure you have already installed the **prerequisites**. Run this command in your terminal :

sudo apt install python3 python3-pip python-pip-whl python3-wheel python3-distutils python3-lib2to3 python3-setuptools python3-dateutil python3-packaging python3-pyparsing python3-colorama python3-yaml libqt5designer5 libqt5help5 libqt5sql5 libqt5test5 libqt5xml5 python3-pyqt5 python3-pyqt5.sip python3-bs4 python3-lxml sqlite3 wget fuse3 aria2 axel python3-soupsieve python3-requests python3-xlib flatpak

We suggest you also install libappindicator3-1 if it is available in your distribution repos.

Waffles application is being tested for possible default inclusion in [**TeLOS Linux**](https://teloslinux.org), our favorite Debian derivative Linux distribution.

More info on Waffles will be added as this project evolves.

Credits :
- bauh application developers and the wonderful Community of Linux users
- The waffles.png Icon is made by [Freepik](https://www.freepik.com) from [Flaticon](https://www.flaticon.com).

You can try Waffles before installation in a virtual env environment :

Before trying make sure you have installed the prerequisites mentioned above plus the python3-venv package.

Then type following commands:

```
python3 -m venv waffles_env # creates an isolated environment inside the directory called "waffles_env"
waffles_env/bin/pip install https://github.com/IonTeLOS/waffles/archive/refs/tags/1.1.tar.gz  # installs Waffles in the isolated environment (replace number with the actual release you are targeting)
waffles_env/bin/waffles # launches Waffles.
For the tray-mode: waffles_env/bin/waffles-tray

To "uninstall" the virtual environment :

waffles_env/bin/waffles --reset  # removes cache and configurations files from HOME
rm -rf waffles_env` (just remove the directory)
...

Enjoy!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
