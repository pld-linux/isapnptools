Summary:	Programs to configure ISA Plug-And-Play devices
Summary(pl):	Narz�dzia do konfigurowania urz�dze� Plug-And-Play
Name:		isapnptools
Version:	1.18
Release:	2
Copyright:	GPL
Group:		Utilities/System
Group(pl):	Narz�dzia/System
URL:		ftp://ftp.demon.co.uk/pub/unix/linux/utils/
Source:		%{name}-%{version}.tgz
Patch0:		%{name}.patch
ExcludeArch:	sparc
BuildRoot:	/tmp/buildroot-%{name}-%{version}

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
%setup -q -n %{name}-%{version}
%patch -p1

#for %doc in stupid rpm-2.5.5
chmod 644 READ*

%build
make CPPFLAGS="$RPM_OPT_FLAGS" 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{sbin,usr/man/man5,usr/man/man8,etc/isapnp}

make \
    prefix=$RPM_BUILD_ROOT/usr \
    INSTALLBINDIR=$RPM_BUILD_ROOT/sbin \
    CONFDIR=$RPM_BUILD_ROOT/etc/isapnp \
    install

install *.conf $RPM_BUILD_ROOT/etc/isapnp

gzip -9nf $RPM_BUILD_ROOT/usr/man/man*/*
bzip2 -9 CHANGES READ* *.txt config-scripts/YMH0021

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.bz2 READ* *.txt.bz2 
%doc config-scripts/YMH0021.bz2

%attr(750,root,root) %dir /etc/isapnp
%attr(640,root,root) %config %verify(not size mtime md5) /etc/isapnp/*

%attr(755,root,root) /sbin/*
%attr(644,root, man) /usr/man/man[58]/*

%changelog
* Thu Feb 18 1999 Arkadiusz Mi�kiewicz <misiek@misiek.eu.org>
  [1.18-1d]
- new version
- compressed manual pages

* Sun Sep 27 1998 Marcin Korzonek <mkorz@shadow.eu.org>
  [1.15-3d]
- translation modified for pl,
- defined files permission,
- build against GNU libc-2.1,
- startet at RH spec.
