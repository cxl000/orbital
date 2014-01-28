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
BuildRequires: kde-solid-devel
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

Requires:       icon-theme

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
%ifnarch %{ix86} x86_64
# HACK!!! Please remove when possible.
# cmake is accelerated but version is too old
mkdir /tmp/bin
cp -a /usr/bin/cmake /usr/share/cmake/Modules /usr/share/cmake/Templates /tmp/bin/
PATH=/tmp/bin:$PATH
/tmp/bin/cmake -DCMAKE_VERBOSE_MAKEFILE=ON -DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_INSTALL_LIBDIR:PATH=/usr/lib -DINCLUDE_INSTALL_DIR:PATH=/usr/include -DLIB_INSTALL_DIR:PATH=/usr/lib -DSYSCONF_INSTALL_DIR:PATH=/etc -DSHARE_INSTALL_PREFIX:PATH=/usr/share -DCMAKE_SKIP_RPATH:BOOL=ON -DBUILD_SHARED_LIBS:BOOL=ON . -DCMAKE_BUILD_TYPE=RelWithDebInfo
%else
%cmake
%endif

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
#%{_libdir}/orbital/orbital-shell.so
%{_libdir}/orbital/services/libloginservice.so
%{_libdir}/orbital/services/libmixerservice.so
%{_libdir}/orbital/services/libprocesslauncher.so
%{_libdir}/orbital/services/libdatetime.so
%{_libdir}/orbital/services/libhardwareservice.so
%{_libexecdir}/orbital-client
%{_libexecdir}/startorbital
%{_datadir}/orbital/*/
%{_libexecdir}/orbital-splash
