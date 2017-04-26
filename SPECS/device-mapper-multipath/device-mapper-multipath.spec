Summary:    Provide tools to manage multipath devices
Name:       device-mapper-multipath
Version:    0.7.1
Release:    1%{?dist}
License:    GPL+
Group:      System Environment/Base
URL:        http://christophe.varoqui.free.fr/
Source0:    multipath-tools-be1191b.tar.gz
%define git_commit_short be1191b
%define sha1 multipath-tools=20543995feebb122068f2aaac37b16c91e8cb905
BuildRequires:  userspace-rcu-devel
BuildRequires:  librados-devel
BuildRequires:  libaio-devel
BuildRequires:  device-mapper-devel
BuildRequires:  readline-devel
BuildRequires:  ncurses-devel
BuildRequires:  systemd-devel
BuildRequires:  json-c-devel
Requires:   userspace-rcu
Requires:   librados2
Requires:   libaio
Requires:   device-mapper
Requires:   libselinux
Requires:   libsepol
Requires:   readline
Requires:   ncurses
Requires:   kpartx = %{version}-%{release}

%description
Device-mapper-multipath provides tools to manage multipath devices by
instructing the device-mapper multipath kernel module what to do. 

%package -n kpartx
Summary:    Partition device manager for device-mapper devices

%description -n kpartx
kpartx manages partition creation and removal for device-mapper devices.

%package devel
Summary: Development libraries and headers for %{name}
Requires: %{name} = %{version}-%{release}
%description devel
It contains the libraries and header files to create applications

%prep
%setup -qn multipath-tools-%{git_commit_short}

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} \
	SYSTEMDPATH=/lib \
	bindir=%{_sbindir} \
	syslibdir=%{_libdir} \
	libdir=%{_libdir}/multipath \
	pkgconfdir=%{_libdir}/pkgconfig

install -vd %{buildroot}/etc/multipath

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_sbindir}/mpathpersist
%{_sbindir}/multipath
%{_sbindir}/multipathd
/lib/udev/rules.d/*
%{_unitdir}/*
%{_libdir}/*.so
%{_libdir}/*.so.*
%{_libdir}/multipath/*.so
%{_mandir}/man5/*
%{_mandir}/man8/mpathpersist.8.gz
%{_mandir}/man8/multipath.8.gz
%{_mandir}/man8/multipathd.8.gz
%dir /etc/multipath

%files devel
%defattr(-,root,root,-)
%{_mandir}/man3/*
%{_includedir}/*
%{_libdir}/pkgconfig/*

%files -n kpartx
%defattr(-,root,root,-)
%{_sbindir}/kpartx
/lib/udev/kpartx_id
%{_mandir}/man8/kpartx.8.gz

%changelog
*   Tue May 9  2017 Bo Gan <ganb@vmware.com> 0.7.1-1
-   Update to 0.7.1
*   Fri Nov 18 2016 Anish Swaminathan <anishs@vmware.com>  0.5.0-3
-   Change systemd dependency
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 0.5.0-2
-   GA - Bump release of all rpms
*   Mon Jun 22 2015 Divya Thaluru <dthaluru@vmware.com> 0.5.0-1
-   Initial build. First version

