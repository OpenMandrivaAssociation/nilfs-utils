# api is the part of the library name before the .so
%define	api	0
# major is the part of the library name after the .so
%define	major	0
#define	libname %mklibname %{name} %{api} %{major}
%define	libname	%mklibname %{name} %{major}
%define	devname %mklibname %{name} -d

%define	_root_sbindir	/sbin

Summary: 	Tools for nilfs filesystem
Name: 		nilfs-utils
Version: 	2.1.1
Release: 	1
License:	GPLv2+
Group:		System/Base
Source0:	http://www.nilfs.org/download/%{name}-%{version}.tar.bz2
URL:		http://www.nilfs.org/en/index.html
Buildrequires:  pkgconfig(uuid) pkgconfig(mount)

%description
NILFS is a log-structured file system supporting versioning of the entire 
file system and continuous snapshotting which allows users to even restore 
files mistakenly overwritten or destroyed just a few seconds ago. 

%package -n	%{libname}
Summary:        Main library for %{name}
Group:          System/Base

%description -n	%{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n	%{devname}
Summary:        Headers for developing programs that will use %{name}
Group:          System/Base
Requires:       %{libname} = %{EVRD}
Provides:       %{name}-devel = %{EVRD}
%define	oldlib	%mklibname %{name}
%rename		%{oldlib}

%description -n	%{devname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std LDCONFIG=/bin/true

%files
%doc AUTHORS COPYING ChangeLog README
%{_sysconfdir}/nilfs_cleanerd.conf
%{_bindir}/*
%{_root_sbindir}/*
%{_mandir}/man?/*

%files -n %{libname}
%{_libdir}/libnilfs*.so.%{major}*

%files -n %{devname}
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*.h
