Summary:	Programs to configure ISA Plug-And-Play devices
Summary(pl):	Narzêdzia do konfigurowania urz±dzeñ Plug-And-Play
Name:		isapnptools
Version:	1.22
Release:	1
Copyright:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source:		ftp://ftp.demon.co.uk/pub/unix/linux/utils/%{name}-%{version}.tgz
Patch0:		isapnptools.patch
Patch1:		isapnptools-DESTDIR.patch
ExcludeArch:	sparc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The isapnptools package contains utilities for configuring ISA Plug-and-Play
(PnP) cards/boards which are in compliance with the PnP ISA Specification
Version 1.0a. ISA PnP cards use registers instead of jumpers for setting
the board address and interrupt assignments.  The cards also contain
descriptions of the resources which need to be allocated.  The BIOS on your
system, or isapnptools, uses a protocol described in the specification to
find all of the PnP boards and allocate the resources so that none of them
conflict.

Note that the BIOS doesn't do a very good job of allocating resources.  So
isapnptools is suitable for all systems, whether or not they include a PnP
BIOS. In fact, a PnP BIOS adds some complications.  A PnP BIOS may already
activate some cards so that the drivers can find them.  Then these tools can
unconfigure them or change their settings, causing all sorts of nasty
effects. If you have PnP network cards that already work, you should read
through the documentation files very carefully before you use isapnptools.

Install isapnptools if you need utilities for configuring ISA PnP cards.

%description -l pl
Programy zawarte w tym pakiecie umo¿liwiaj± skonfigurowanie urz±dzeñ
Plug-And-Play pod³±czonych do szyny ISA.

Narzêdzia s± dostosowane do wszystkich systemów i nie wymagaj±
posiadania BIOS-u obs³uguj±cego PnP.

%prep
%setup -q
%patch0 -p1 -b .wiget
#%patch1 -p1

%build
%{__make} CPPFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/sbin,%{_mandir}/man{5,8},/etc/isapnp}

sed -e "s/^\([^#]\)/#\1/" < isapnp.gone > isapnp.tmp
%ifarch alpha
sed -e "s/#IRQ 7/IRQ 7/" < isapnp.tmp > isapnp.tmp2
mv -f isapnp.tmp2 isapnp.tmp
%endif 
mv -f isapnp.tmp isapnp.gone

%{__make} install installdir=$RPM_BUILD_ROOT \
	INSTALLMANDIR=$RPM_BUILD_ROOT%{_mandir} 

install *.conf $RPM_BUILD_ROOT/etc/isapnp

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	CHANGES READ* *.txt config-scripts/YMH0021

%post
if [ -f /etc/isapnp/isapnp.conf ]; then
        NEWPORT=`/sbin/pnpdump | grep READPORT 2>/dev/null`
	if [ -n "$NEWPORT" ]; then
	        mv -f /etc/isapnp/isapnp.conf /etc/isapnp/isapnp.conf.rpmsave
		sed -e "s/^[^#]*(READPORT .*/$NEWPORT/" /etc/isapnp/isapnp.conf.rpmsave > \
		/etc/isapnp/isapnp.conf
	fi
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,READ*,*.txt,config-scripts/YMH0021}.gz

%attr(750,root,root) %dir /etc/isapnp
%attr(640,root,root) %config %verify(not size mtime md5) /etc/isapnp/*
%attr(755,root,root) /sbin/*
%{_mandir}/man[58]/*
