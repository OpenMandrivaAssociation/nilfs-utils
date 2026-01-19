%define	major	0
#define libname %mklibname %{name} %{api} %{major}
%define libname	%mklibname %{name}
%define devname	%mklibname %{name} -d

%define	libnilfs	%mklibname nilfs %{major}
%define	libnilfscleaner	%mklibname nilfscleaner %{major}
%define	libnilfsgc	%mklibname nilfsgc %{major}

%define	_root_sbindir	/sbin

Summary:	Tools for nilfs filesystem
Name:		nilfs-utils
Version:	2.2.14
Release:	1
License:	GPLv2+
Group:		System/Base
Source0:  https://nilfs.sourceforge.io/download/nilfs-utils-%{version}.tar.bz2
#Source0:	https://github.com/nilfs-dev/nilfs-utils/releases/download/v%{version}/%{name}-%{version}.tar.bz2
Url:		https://nilfs.sourceforge.io/en/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:	pkgconfig(ext2fs)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(mount)

%description
NILFS is a log-structured file system supporting versioning of the entire 
file system and continuous snapshotting which allows users to even restore 
files mistakenly overwritten or destroyed just a few seconds ago. 

%package -n	%{libnilfs}
Summary:	The libnilfs library for %{name}
Group:		System/Base
License:	LGPLv2.1+
%rename		%{libname}
%rename		%{libname}0

%description -n	%{libnilfs}
This package contains the libnilfs library needed to run programs dynamically
linked with %{name}.

%package -n	%{libnilfscleaner}
Summary:	The libnilfscleaner library for %{name}
Group:		System/Base
License:	LGPLv2.1+
%rename		%{libname}
%rename		%{libname}0

%description -n	%{libnilfscleaner}
This package contains the libnilfscleaner library needed to run programs
dynamically linked with %{name}.

%package -n	%{libnilfsgc}
Summary:	The libnilfsgc library for %{name}
Group:		System/Base
License:	LGPLv2.1+
%rename		%{libname}
%rename		%{libname}0

%description -n	%{libnilfsgc}
This package contains the libnilfsgc library needed to run programs dynamically
linked with %{name}.

%package -n	%{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		System/Base
Requires:	%{name} = %{version}-%{release}
Requires:	%{libnilfs} = %{version}-%{release}
Requires:	%{libnilfsgc} = %{version}-%{release}
Requires:	%{libnilfscleaner} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q
%before_configure

%build
CONFIGURE_TOP="$PWD"

mkdir -p glibc
pushd glibc
%configure --disable-static
%make_build CC=%{__cc}
popd

%install
%make_install -C glibc LDCONFIG=/bin/true

%files
%doc AUTHORS ChangeLog README
%config(noreplace) %{_sysconfdir}/nilfs_cleanerd.conf
%{_bindir}/*
%{_root_sbindir}/*
%{_mandir}/man?/*.*
%{_prefix}/sbin/nilfs*

%files -n %{libnilfs}
%{_libdir}/libnilfs.so.%{major}*

%files -n %{libnilfscleaner}
%{_libdir}/libnilfscleaner.so.%{major}*

%files -n %{libnilfsgc}
%{_libdir}/libnilfsgc.so.%{major}*

%files -n %{devname}
%{_libdir}/libnilfs*.so
%{_includedir}/*.h
