Summary: Orbital is a shell for Wayland's Weston
Name: orbital
Version: 0.0.0
Release: 1
License: LGPL21
Group: Development/Liraries
URL: https://github.com/giucam/orbital.git
Source0: %{name}-%{version}.tar.bz2
#Patch0:  0001-Remove-c-11-override-keyword.patch
#Patch1:  0002-Add-class-keyword-to-to-support-c-11.patch
#Patch2:  0003-ref_count-added-after-wayland-1.2.0.patch
BuildRequires: cmake >= 2.8
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(weston)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: qt5-qttools-linguist
BuildRequires: pkgconfig(nuclear)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(alsa)
BuildRequires: qt5-default

BuildRequires:  qt5-plugin-platform-eglfs
BuildRequires:  qt5-plugin-platform-kms
BuildRequires:  qt5-plugin-platform-minimal
BuildRequires:  qt5-plugin-platform-minimalegl
BuildRequires:  qt5-plugin-platform-linuxfb
BuildRequires:  qt5-plugin-platform-offscreen
BuildRequires:  qt5-plugin-platform-xcb
BuildRequires:  qt5-plugin-imageformat-jpeg
BuildRequires:  qt5-plugin-imageformat-gif
BuildRequires:  qt5-plugin-imageformat-ico
BuildRequires:  qt5-plugin-bearer-nm
BuildRequires:  qt5-plugin-bearer-connman
BuildRequires:  qt5-plugin-bearer-generic

%description
It is composed of a Weston shell plugin and a shell client, made in Qt5,
with the interface in QtQuick 2.
Its goal is to produce a light and self-contained shell running on Wayland,
without many dependencies aside Weston and Qt.

%prep
%setup -q
cd orbital
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1

%build
cd orbital
%cmake
make %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT
cd orbital
make install DESTDIR=%{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/orbital
%{_libdir}/orbital/orbital-shell.so
%{_libdir}/orbital/services/libloginservice.so
%{_libdir}/orbital/services/libmixerservice.so
%{_libdir}/orbital/services/libprocesslauncher.so
%{_libexecdir}/orbital-client
%{_libexecdir}/startorbital
%{_datadir}/orbital/*/

