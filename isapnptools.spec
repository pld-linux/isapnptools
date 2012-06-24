Summary:	Programs to configure ISA Plug-And-Play devices
Summary(pl):	Narz�dzia do konfigurowania urz�dze� Plug-And-Play
Name:		isapnptools
Version:	1.23
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.demon.co.uk/pub/unix/linux/utils/%{name}-%{version}.tgz
Patch0:		%{name}-pnpdump_main.patch
URL:		http://www.roestock.demon.co.uk/isapnptools/
Prereq:		sed
ExcludeArch:	sparc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin
%define		_sysconfdir	/etc/isapnp

%description
The isapnptools package contains utilities for configuring ISA
Plug-and-Play (PnP) cards/boards which are in compliance with the PnP
ISA Specification Version 1.0a. ISA PnP cards use registers instead of
jumpers for setting the board address and interrupt assignments. The
cards also contain descriptions of the resources which need to be
allocated. The BIOS on your system, or isapnptools, uses a protocol
described in the specification to find all of the PnP boards and
allocate the resources so that none of them conflict.

Note that the BIOS doesn't do a very good job of allocating resources.
So isapnptools is suitable for all systems, whether or not they
include a PnP BIOS. In fact, a PnP BIOS adds some complications. A PnP
BIOS may already activate some cards so that the drivers can find
them. Then these tools can unconfigure them or change their settings,
causing all sorts of nasty effects. If you have PnP network cards that
already work, you should read through the documentation files very
carefully before you use isapnptools.

%description -l pl
Programy zawarte w tym pakiecie umo�liwiaj� skonfigurowanie urz�dze�
Plug-And-Play pod��czonych do szyny ISA.

Narz�dzia s� dostosowane do wszystkich system�w i nie wymagaj�
posiadania BIOS-u obs�uguj�cego PnP.

%prep
%setup -q
%patch -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install etc/* $RPM_BUILD_ROOT%{_sysconfdir}

gzip -9nf ChangeLog NEWS README config-scripts/YMH0021

%post
if [ -f  %{_sysconfdir}/isapnp.conf ]; then
        NEWPORT=`%{_sbindir}/pnpdump | grep READPORT 2>/dev/null`
	if [ -n "$NEWPORT" ]; then
	        mv -f  %{_sysconfdir}/isapnp.conf  %{_sysconfdir}/isapnp.conf.rpmsave
		sed -e "s/^[^#]*(READPORT .*/$NEWPORT/"  %{_sysconfdir}/isapnp.conf.rpmsave > \
		%{_sysconfdir}/isapnp.conf
	fi
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz config-scripts/*.gz
%attr(750,root,root) %dir %{_sysconfdir}
%attr(640,root,root) %config %verify(not size mtime md5) %{_sysconfdir}/*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man[58]/*
