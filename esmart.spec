%define	name	esmart
%define version 0.9.0.042
%define release %mkrel 2

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
BuildRequires:	evas-devel >= 0.9.9.042
BuildRequires:	ecore-devel >= 0.9.9.042
BuildRequires:	imlib2-devel
BuildRequires:	epsilon-devel >= 0.3.0.012
BuildRequires:	edje-devel >= 0.5.0.042, edje >= 0.5.0.042
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
Provides: lib%{name}-devel
Provides: %name-devel

%description -n %libnamedev
%{name} development headers and libraries

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

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

