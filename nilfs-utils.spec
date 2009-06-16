%define name nilfs-utils
%define version 2.0.12
%define release %mkrel 1
# api is the part of the library name before the .so
%define api 0
# major is the part of the library name after the .so
%define major 0
#define libname %mklibname %{name} %{api} %{major}
%define libname %mklibname %{name}
%define develname %mklibname %{name} -d

%define	_root_sbindir	/sbin

Summary: 	Tools for nilfs filesystem
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License:	GPLv2+
Group:		System/Base
Source0:	%{name}-%{version}.tar.bz2
URL:		http://www.nilfs.org/en/index.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
NILFS is a log-structured file system supporting versioning of the entire 
file system and continuous snapshotting which allows users to even restore 
files mistakenly overwritten or destroyed just a few seconds ago. 

%package -n %{libname}
Summary:        Main library for %{name}
Group:          System/Base
Provides:       %{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{develname}
Summary:        Headers for developing programs that will use %{name}
Group:          System/Base
Requires:       %{libname} = %{version}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std LDCONFIG=/bin/true

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{_sysconfdir}/nilfs_cleanerd.conf
%{_bindir}/*
%{_root_sbindir}/*
%{_mandir}/man?/*.lzma

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{develname}
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*.h
