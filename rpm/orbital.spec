Summary: Orbital is a shell for Wayland's Weston
Name: orbital
Version: 0.0.0
Release: 1
License: LGPL21
Group: Development/Liraries
URL: https://github.com/giucam/orbital.git
Source0: %{name}-%{version}.tar.bz2
BuildRequires: cmake >= 2.8
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
It is composed of a Weston shell plugin and a shell client, made in Qt5,
with the interface in QtQuick 2.
Its goal is to produce a light and self-contained shell running on Wayland,
without many dependencies aside Weston and Qt.

%prep
%setup -q

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

