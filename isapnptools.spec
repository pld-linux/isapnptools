Summary:	Programs to configure ISA Plug-And-Play devices
Summary(es):	Programas para configurar dispositivos Plug-And-Play ISA en una mАquina linux
Summary(pl):	NarzЙdzia do konfigurowania urz╠dzeЯ Plug-And-Play
Summary(pt_BR):	Programas para configurar dispositivos Plug-And-Play ISA numa mАquina Linux
Summary(ru):	Программы для конфигурации ISA Plug-And-Play (PnP) устройств
Summary(uk):	Програми для конф╕гурац╕╖ ISA Plug-And-Play (PnP) пристро╖в
Name:		isapnptools
Version:	1.26
Release:	3
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.demon.co.uk/pub/unix/linux/utils/%{name}-%{version}.tgz
Patch0:		%{name}-ac_fix.patch
URL:		http://www.roestock.demon.co.uk/isapnptools/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
Prereq:		sed
ExclusiveArch:	%{ix86} alpha
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

%description -l es
Estos programas permiten que dispositivos ISA Plug-And-Play sean configurados
en una mАquina Linux.  Este programa es apropiado para todos los sistemas,
incluso cuando no tienen un BIOS PnP. AdemАs, un BIOS PnP adiciona algunas
complicaciones, porque puede ya tener activado algunas tarjetas de modo que los
drivers las pueden encontrar, y las herramientas de este paquete pueden
desconfigЗralas, o cambiar sus configuraciones causando efectos desagradables.
Si tienes (por ejemplo) tarjetas de red plug and play que ya funcionan, sugiero
que leas con cuidado la pАgina de manual isapnp.conf(5), sobre el formato del
archivo de configuraciСn.

%description -l pl
Programy zawarte w tym pakiecie umo©liwiaj╠ skonfigurowanie urz╠dzeЯ
Plug-And-Play podЁ╠czonych do szyny ISA.

NarzЙdzia s╠ dostosowane do wszystkich systemСw i nie wymagaj╠
posiadania BIOS-u obsЁuguj╠cego PnP.

%description -l pt_BR
Estes programas permitem que dispositivos ISA Plug-And-Play sejam configurados
numa mАquina Linux.

Este programa И apropriado para todos os sistemas, mesmo que nЦo tenham um BIOS
PnP. AliАs, um BIOS PnP adiciona algumas complicaГУes, porque jА pode ter
ativado algumas placas de modo que os drivers possam achА-las, e as ferramentas
deste pacote podem desconfigurА-las, ou mudar suas configuraГУes causando
efeitos desagradАveis. Se vocЙ tiver (por exemplo) placas de rede plug and play
que jА funcionam, sugiro que vocЙ leia com cuidado a pАgina de manual
isapnp.conf(5), sobre o formato do arquivo de configuraГЦo.

%description -l ru
Пакет isapnptools содержит утилиты для конфигурирования ISA Plug-and-Play
(PnP) карт, отвечающих стандарту PnP ISA Specification Version 1.0a.
Карты ISA PnP используют регистры вместо переключателей для установки
адреса платы и присвоения номера прерывания. Карты также содержат
описание ресурсов, которые необходимо выделить. BIOS вашей машины или
isapnptools используют протокол описанный в спецификации для нахождения
всех плат PnP и выделения ресурсов так, чтобы они не конфликтовали.

BIOS не очень хорошо выполняет работу по распределению ресурсов. Так что
isapnptools подходит для всех систем, независимо от того, включают ли они
PnP BIOS. В действительности, PnP BIOS несколько усложняет дело. Он может
уже активизировать некоторые карты, так чтобы драйверы могли их найти.
После этого эти утилиты могут их "расконфигурировать", вызывая этим
разнообразные неприятные эффекты. Если вы имеете PnP сетевые карты
которые уже работают, вам следует прочитать файлы документации очень
внимательно перед использованием isapnptools.

%description -l uk
Пакет isapnptools м╕стить утил╕ти для конф╕гурування ISA Plug-and-Play
(PnP) карт, як╕ в╕дпов╕дають стандарту PnP ISA Specification Version 1.0a.
Карти ISA PnP використовують рег╕стри зам╕сть перемикач╕в для установки
адреси плати та присво╓ння номеру переривання. Карти також м╕стять опис
ресурс╕в, як╕ потр╕бно вид╕лити. BIOS вашо╖ машини чи isapnptools
використовують протокол, описаний в специф╕кац╕╖, для знаходження вс╕х
плат PnP та вид╕лення ресурс╕в так, щоб вони не конфл╕ктували.

BIOS не дуже добре викону╓ роботу по розпод╕ленню ресурс╕в. Так що
isapnptools п╕дходить для вс╕х систем, незалежно в╕д того, чи включають
вони PnP BIOS. В д╕йсност╕, PnP BIOS дещо ускладню╓ справу. В╕н може
вже активувати деяк╕ карти, так щоб драйвери змогли ╖х знайти. П╕сля
того ц╕ утил╕ти можуть "розконф╕гурувати" ╖х, викликаючи цим р╕зноман╕тн╕
непри╓мн╕ ефекти. Якщо ви ма╓те PnP мережев╕ карти як╕ вже працюють,
вам сл╕д прочитати файли документац╕╖ дуже уважно перед використанням
isapnptools.

%package devel
Summary:	Devel librairies for configuring ISA Plug-and-Play (PnP) devices
Group:		Development/Libraries
PreReq:		%{name} = %{version}

%description devel
The isapnptools package contains utilities for configuring ISA
Plug-and-Play (PnP) cards which are in compliance with the PnP ISA
Specification Version 1.0a.  ISA PnP cards use registers instead of
jumpers for setting the board address and interrupt assignments.  The
cards also contain descriptions of the resources which need to be
allocated.  The BIOS on your system, or isapnptools, uses a protocol
described in the specification to find all of the PnP boards and
allocate the resources so that none of them conflict.

Note that the BIOS doesn't do a very good job of allocating resources.
So isapnptools is suitable for all systems, whether or not they
include a PnP BIOS. In fact, a PnP BIOS adds some complications.  A
PnP BIOS may already activate some cards so that the drivers can find
them.  Then these tools can unconfigure them or change their settings,
causing all sorts of nasty effects. If you have PnP network cards that
already work, you should read through the documentation files very
carefully before you use isapnptools.

Install isapnptools-devel if you need to do development with ISA PnP
cards.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
aclocal
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install etc/* $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f  %{_sysconfdir}/isapnp.conf ]; then
        NEWPORT=`%{_sbindir}/pnpdump | grep READPORT 2>/dev/null`
	if [ -n "$NEWPORT" ]; then
	        mv -f  %{_sysconfdir}/isapnp.conf  %{_sysconfdir}/isapnp.conf.rpmsave
		sed -e "s/^[^#]*(READPORT .*/$NEWPORT/"  %{_sysconfdir}/isapnp.conf.rpmsave > \
		%{_sysconfdir}/isapnp.conf
	fi
fi

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README config-scripts/YMH0021
%attr(750,root,root) %dir %{_sysconfdir}
%attr(640,root,root) %config %verify(not size mtime md5) %{_sysconfdir}/*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man[58]/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_includedir}/isapnp/*.h
