%define major 8
%define libname %mklibname tifiles2 %{major}
%define develname %mklibname tifiles2 -d

Name: libtifiles2
Version: 1.1.5
Release: 1
Url: http://sourceforge.net/projects/tilp
Source0: http://downloads.sourceforge.net/project/tilp/tilp2-linux/tilp2-1.16/%{name}-%{version}.tar.bz2
Group: System/Libraries
License: GPLv2+
BuildRequires: libusb1-devel, glib2-devel
BuildRequires: autoconf automake libtool gettext-devel pkgconfig(libusb)
Requires: udev >= 154
Summary: Library for handling TI link cables
%description
Library for handling TI link cables

%package  -n %develname
Summary: Development files for %{name}
Group: Development/C
Requires: %libname = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release} 

%description -n %develname
This package contains the files necessary to develop applications using the
%{name} library.

%package  -n %libname
Summary: Development files for %{name}
Group: System/Libraries

%description -n %libname
This package contains the files necessary to develop applications using the
%{name} library.

%prep
%setup -q
autoreconf -i -f

%build
%configure2_5x
%make

%install
%makeinstall_std
rm -f %buildroot%{_libdir}/*.la

%files -n %libname
%{_libdir}/libtifiles2.so.%{major}*

%files -n %develname
%{_includedir}/tilp2
%{_libdir}/libtifiles2.so
%{_libdir}/pkgconfig/tifiles2.pc
%{_datadir}/locale/fr/LC_MESSAGES/*.mo
