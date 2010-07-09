Summary:	Programs to configure ISA Plug-and-Play devices
Summary(es.UTF-8):	Programas para configurar dispositivos Plug-and-Play ISA en una máquina linux
Summary(pl.UTF-8):	Narzędzia do konfigurowania urządzeń Plug-and-Play
Summary(pt_BR.UTF-8):	Programas para configurar dispositivos Plug-and-Play ISA numa máquina Linux
Summary(ru.UTF-8):	Программы для конфигурации ISA Plug-and-Play (PnP) устройств
Summary(uk.UTF-8):	Програми для конфігурації ISA Plug-and-Play (PnP) пристроїв
Name:		isapnptools
Version:	1.27
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	ftp://metalab.unc.edu/pub/Linux/system/hardware/%{name}-%{version}.tgz
# Source0-md5:	b997ba56583dc850fce9b93d658dfa0c
Patch0:		%{name}-ac_fix.patch
URL:		http://www.roestock.demon.co.uk/isapnptools/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	libtool
Requires(post):	fileutils
Requires(post):	grep
Requires(post):	sed
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

%description -l es.UTF-8
Estos programas permiten que dispositivos ISA Plug-and-Play sean
configurados en una máquina Linux. Este programa es apropiado para
todos los sistemas, incluso cuando no tienen un BIOS PnP. Además, un
BIOS PnP adiciona algunas complicaciones, porque puede ya tener
activado algunas tarjetas de modo que los drivers las pueden
encontrar, y las herramientas de este paquete pueden desconfigúralas,
o cambiar sus configuraciones causando efectos desagradables. Si
tienes (por ejemplo) tarjetas de red plug and play que ya funcionan,
sugiero que leas con cuidado la página de manual isapnp.conf(5), sobre
el formato del archivo de configuración.

%description -l pl.UTF-8
Programy zawarte w tym pakiecie umożliwiają skonfigurowanie urządzeń
Plug-and-Play podłączonych do szyny ISA.

Narzędzia są dostosowane do wszystkich systemów i nie wymagają
posiadania BIOS-u obsługującego PnP.

%description -l pt_BR.UTF-8
Estes programas permitem que dispositivos ISA Plug-and-Play sejam
configurados numa máquina Linux.

Este programa é apropriado para todos os sistemas, mesmo que não
tenham um BIOS PnP. Aliás, um BIOS PnP adiciona algumas complicações,
porque já pode ter ativado algumas placas de modo que os drivers
possam achá-las, e as ferramentas deste pacote podem desconfigurá-las,
ou mudar suas configurações causando efeitos desagradáveis. Se você
tiver (por exemplo) placas de rede plug and play que já funcionam,
sugiro que você leia com cuidado a página de manual isapnp.conf(5),
sobre o formato do arquivo de configuração.

%description -l ru.UTF-8
Пакет isapnptools содержит утилиты для конфигурирования ISA
Plug-and-Play (PnP) карт, отвечающих стандарту PnP ISA Specification
Version 1.0a. Карты ISA PnP используют регистры вместо переключателей
для установки адреса платы и присвоения номера прерывания. Карты также
содержат описание ресурсов, которые необходимо выделить. BIOS вашей
машины или isapnptools используют протокол описанный в спецификации
для нахождения всех плат PnP и выделения ресурсов так, чтобы они не
конфликтовали.

BIOS не очень хорошо выполняет работу по распределению ресурсов. Так
что isapnptools подходит для всех систем, независимо от того, включают
ли они PnP BIOS. В действительности, PnP BIOS несколько усложняет
дело. Он может уже активизировать некоторые карты, так чтобы драйверы
могли их найти. После этого эти утилиты могут их "расконфигурировать",
вызывая этим разнообразные неприятные эффекты. Если вы имеете PnP
сетевые карты которые уже работают, вам следует прочитать файлы
документации очень внимательно перед использованием isapnptools.

%description -l uk.UTF-8
Пакет isapnptools містить утиліти для конфігурування ISA Plug-and-Play
(PnP) карт, які відповідають стандарту PnP ISA Specification Version
1.0a. Карти ISA PnP використовують регістри замість перемикачів для
установки адреси плати та присвоєння номеру переривання. Карти також
містять опис ресурсів, які потрібно виділити. BIOS вашої машини чи
isapnptools використовують протокол, описаний в специфікації, для
знаходження всіх плат PnP та виділення ресурсів так, щоб вони не
конфліктували.

BIOS не дуже добре виконує роботу по розподіленню ресурсів. Так що
isapnptools підходить для всіх систем, незалежно від того, чи
включають вони PnP BIOS. В дійсності, PnP BIOS дещо ускладнює справу.
Він може вже активувати деякі карти, так щоб драйвери змогли їх
знайти. Після того ці утиліти можуть "розконфігурувати" їх, викликаючи
цим різноманітні неприємні ефекти. Якщо ви маєте PnP мережеві карти
які вже працюють, вам слід прочитати файли документації дуже уважно
перед використанням isapnptools.

%package devel
Summary:	Development ISA PnP libraries
Summary(pl.UTF-8):	Biblioteki ISA PnP dla programistów
Group:		Development/Libraries

%description devel
Development libraries for configuring ISA Plug-and-Play (PnP) devices.

%description devel -l pl.UTF-8
Biblioteki do rozwoju programów konfigurujących urządzenia ISA
Plug-and-Play (PnP).

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install etc/* $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_sysconfdir}/isapnp.conf ]; then
        NEWPORT=`%{_sbindir}/pnpdump | grep READPORT 2>/dev/null`
	if [ -n "$NEWPORT" ]; then
		umask 027
	        mv -f  %{_sysconfdir}/isapnp.conf %{_sysconfdir}/isapnp.conf.rpmsave
		sed -e "s/^[^#]*(READPORT .*/$NEWPORT/" %{_sysconfdir}/isapnp.conf.rpmsave > \
			%{_sysconfdir}/isapnp.conf
	fi
fi

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README config-scripts/YMH0021
%attr(750,root,root) %dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/isapnp.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/isapnp.gone
%attr(755,root,root) %{_sbindir}/isapnp
%attr(755,root,root) %{_sbindir}/pnpdump
%{_mandir}/man5/isapnp.conf.5*
%{_mandir}/man8/isapnp.8*
%{_mandir}/man8/pnpdump.8*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libisapnp.a
%{_includedir}/isapnp
