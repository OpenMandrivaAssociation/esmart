%define	name	esmart
%define version 0.9.0.050
%define svnrel	20090708
%define release %mkrel 2.%{svnrel}.2

%define major 	0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} -d

Summary: 	Enlightenment collection of evas smart objects
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://www.enlightenment.org/
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	evas-devel >= 0.9.9.050
BuildRequires:	ecore-devel >= 0.9.9.060
BuildRequires:	imlib2-devel
BuildRequires:	epsilon-devel >= 0.3.0.012
BuildRequires:	cairo-devel
BuildRequires:	edje-devel >= 0.5.0.050, edje >= 0.5.0.050
BuildRequires:  libtool-devel

%description
A collection of evas smart objects.

This package is part of the Enlightenment DR17 desktop shell.

%package -n %libname
Summary: Libraries for the %{name} package
Group: System/Libraries
Requires: %{name}

%description -n %libname
Libraries for %{name}

%package -n %libnamedev
Summary: Headers and development libraries from %{name}
Group: Development/Other
Requires: %libname = %{version}
Provides: %name-devel = %{version}-%{release}

%description -n %libnamedev
%{name} development headers and libraries

%prep
%setup -qn %name

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_bindir}/%{name}_*
%{_libdir}/%name
%{_datadir}/%name

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %libnamedev
%defattr(-,root,root)
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/Esmart

