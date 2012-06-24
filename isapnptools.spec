Summary:     Programs to configure ISA Plug-And-Play devices on a linux machine.
Summary(pl): Narz�dzia do konfigurowania urz�dze� Plug-And-Play.
Name:        isapnptools
Version:     1.17
Release:     1
Copyright:   GPL
Group:       Utilities/System
Source:      ftp://ftp.demon.co.uk/pub/unix/linux/utils/%{name}-%{version}.tgz
Patch:       isapnptools-cfg.patch
ExcludeArch: sparc
BuildRoot:   /tmp/%{name}-%{version}-root

%description
These programs allow ISA Plug-And-Play devices to be configured on a Linux
machine.

This program is suitable for all systems, whether or not they include a PnP
BIOS. In fact, a PnP BIOS adds some complications because it may already
activate some cards so that the drivers can find them, and these tools can
unconfigure them, or change their settings causing all sorts of nasty
effects. If you have (for example) plug and play network cards that already
work, I suggest you read section 4 on the format of the configuration file
below very carefully.

%description -l pl
Programy zawarte w tym pakiecie umo�liwiaj� skonfigurowanie urz�dze�
Plug-And-Play pod��czonych do szyny ISA.

Narz�dzia s� dostosowane do wszystkich system�w i nie wymagaj�
posiadania BIOS-u obs�uguj�cego PnP.

%prep
%setup -q
%patch -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{sbin,usr/man/man5,usr/man/man8,etc}

make install \
	prefix=$RPM_BUILD_ROOT/usr \
	INSTALLBINDIR=$RPM_BUILD_ROOT/sbin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc CHANGES README README.ide README.initrd README.modules
%doc isapnpfaq.txt isapnp.lsm config-scripts/YMH0021
%attr(755, root, root) /sbin/*
%attr(644, root,  man) /usr/man/*/*

%changelog
* Sun Sep 27 1998 Marcin Korzonek <mkorz@shadow.eu.org>
  [1.15a-3]
- added pl translation,
- defined files permission.

* Thu Sep 24 1998 Bill Nottingham <notting@redhat.com>
- fixed spec file so it rebuild cleanly

* Fri Aug 07 1998 Bill Nottingham <notting@redhat.com>
- added patch to bump to 1.15a

* Tue Aug 04 1998 Bill Nottingham <notting@redhat.com>
- updated to version 1.15

* Fri Oct 03 1997 Michael Fulbright <msf@redhat.com>
- added code to avoid probing in IO port ranges in /proc/ioports

* Fri Aug 22 1997 Mike Wangsmo <wanger@redhat.com>
- Built against glibc

* Thu Jul 17 1997 Timo Karjalainen <timok@iki.fi>
- Updated to version 1.11
- Added RPM_OPT_FLAGS
- Uses BuildRoot
