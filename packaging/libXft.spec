Name:           libXft
%define lname	libXft2
Version:        2.3.1
Release:        0
License:        MIT
Summary:        X FreeType library
Url:            http://xorg.freedesktop.org/
Group:          Development/Libraries/C and C++

Source:         %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  autoconf >= 2.60
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontconfig) >= 2.5.92
BuildRequires:  pkgconfig(freetype2) >= 2.1.6
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xrender) >= 0.8.2

%description
Xft is a library that connects X applications with the FreeType font
rasterization library. Xft uses fontconfig to locate fonts so it has
no configuration files.

%package -n %lname
Summary:        X FreeType library
Group:          System/Libraries

%description -n %lname
Xft is a library that connects X applications with the FreeType font
rasterization library. Xft uses fontconfig to locate fonts so it has
no configuration files.

%package devel
Summary:        Development files for the X FreeType library
Group:          Development/Libraries/C and C++
Requires:       %lname = %{version}

%description devel
Xft is a library that connects X applications with the FreeType font
rasterization library. Xft uses fontconfig to locate fonts so it has
no configuration files.

This package contains the development headers for the library found
in %lname.

%prep
%setup -q

%build
autoreconf -fi
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%{_libdir}/libXft.so.2*

%files devel
%defattr(-,root,root)
%{_includedir}/X11/Xft
%{_libdir}/libXft.so
%{_libdir}/pkgconfig/xft.pc
%{_mandir}/man3/*

%changelog
