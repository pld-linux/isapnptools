Summary:	Programs to configure ISA Plug-and-Play devices
Summary(es):	Programas para configurar dispositivos Plug-and-Play ISA en una m�quina linux
Summary(pl):	Narz�dzia do konfigurowania urz�dze� Plug-and-Play
Summary(pt_BR):	Programas para configurar dispositivos Plug-and-Play ISA numa m�quina Linux
Summary(ru):	��������� ��� ������������ ISA Plug-and-Play (PnP) ���������
Summary(uk):	�������� ��� ���Ʀ����æ� ISA Plug-and-Play (PnP) ������ϧ�
Name:		isapnptools
Version:	1.26
Release:	6
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.demon.co.uk/pub/unix/linux/utils/%{name}-%{version}.tgz
Patch0:		%{name}-ac_fix.patch
Patch1:		%{name}-getopt.patch
URL:		http://www.roestock.demon.co.uk/isapnptools/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
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

%description -l es
Estos programas permiten que dispositivos ISA Plug-and-Play sean
configurados en una m�quina Linux. Este programa es apropiado para
todos los sistemas, incluso cuando no tienen un BIOS PnP. Adem�s, un
BIOS PnP adiciona algunas complicaciones, porque puede ya tener
activado algunas tarjetas de modo que los drivers las pueden
encontrar, y las herramientas de este paquete pueden desconfig�ralas,
o cambiar sus configuraciones causando efectos desagradables. Si
tienes (por ejemplo) tarjetas de red plug and play que ya funcionan,
sugiero que leas con cuidado la p�gina de manual isapnp.conf(5), sobre
el formato del archivo de configuraci�n.

%description -l pl
Programy zawarte w tym pakiecie umo�liwiaj� skonfigurowanie urz�dze�
Plug-and-Play pod��czonych do szyny ISA.

Narz�dzia s� dostosowane do wszystkich system�w i nie wymagaj�
posiadania BIOS-u obs�uguj�cego PnP.

%description -l pt_BR
Estes programas permitem que dispositivos ISA Plug-and-Play sejam
configurados numa m�quina Linux.

Este programa � apropriado para todos os sistemas, mesmo que n�o
tenham um BIOS PnP. Ali�s, um BIOS PnP adiciona algumas complica��es,
porque j� pode ter ativado algumas placas de modo que os drivers
possam ach�-las, e as ferramentas deste pacote podem desconfigur�-las,
ou mudar suas configura��es causando efeitos desagrad�veis. Se voc�
tiver (por exemplo) placas de rede plug and play que j� funcionam,
sugiro que voc� leia com cuidado a p�gina de manual isapnp.conf(5),
sobre o formato do arquivo de configura��o.

%description -l ru
����� isapnptools �������� ������� ��� ���������������� ISA
Plug-and-Play (PnP) ����, ���������� ��������� PnP ISA Specification
Version 1.0a. ����� ISA PnP ���������� �������� ������ ��������������
��� ��������� ������ ����� � ���������� ������ ����������. ����� �����
�������� �������� ��������, ������� ���������� ��������. BIOS �����
������ ��� isapnptools ���������� �������� ��������� � ������������
��� ���������� ���� ���� PnP � ��������� �������� ���, ����� ��� ��
�������������.

BIOS �� ����� ������ ��������� ������ �� ������������� ��������. ���
��� isapnptools �������� ��� ���� ������, ���������� �� ����, ��������
�� ��� PnP BIOS. � ����������������, PnP BIOS ��������� ���������
����. �� ����� ��� �������������� ��������� �����, ��� ����� ��������
����� �� �����. ����� ����� ��� ������� ����� �� "������������������",
������� ���� ������������� ���������� �������. ���� �� ������ PnP
������� ����� ������� ��� ��������, ��� ������� ��������� �����
������������ ����� ����������� ����� �������������� isapnptools.

%description -l uk
����� isapnptools ͦ����� ���̦�� ��� ���Ʀ��������� ISA Plug-and-Play
(PnP) ����, �˦ צ���צ����� ��������� PnP ISA Specification Version
1.0a. ����� ISA PnP �������������� ��Ǧ���� ��ͦ��� ��������ަ� ���
��������� ������ ����� �� �����Ϥ��� ������ �����������. ����� �����
ͦ����� ���� �����Ӧ�, �˦ ���Ҧ��� ��Ħ����. BIOS ���ϧ ������ ��
isapnptools �������������� ��������, �������� � �����Ʀ��æ�, ���
����������� �Ӧ� ���� PnP �� ��Ħ����� �����Ӧ� ���, ��� ���� ��
����̦�������.

BIOS �� ���� ����� �����դ ������ �� �����Ħ����� �����Ӧ�. ��� ��
isapnptools Ц������� ��� �Ӧ� ������, ��������� צ� ����, ��
��������� ���� PnP BIOS. � Ħ�����Ԧ, PnP BIOS ���� ��������� ������.
��� ���� ��� ���������� ���˦ �����, ��� ��� �������� ������ ��
������. ���� ���� æ ���̦�� ������ "������Ʀ��������" ��, ����������
��� Ҧ�����Φ�Φ ����ɤ�Φ ������. ���� �� ����� PnP ������צ �����
�˦ ��� ��������, ��� �̦� ��������� ����� ���������æ� ���� ������
����� ������������� isapnptools.

%package devel
Summary:	Development ISA PnP libraries
Summary(pl):	Biblioteki ISA PnP dla programist�w
Group:		Development/Libraries

%description devel
Development libraries for configuring ISA Plug-and-Play (PnP) devices.

%description devel -l pl
Biblioteki do rozwoju program�w konfiguruj�cych urz�dzenia ISA
Plug-and-Play (PnP).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__autoheader}
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
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man[58]/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.a
%dir %{_includedir}/isapnp
%{_includedir}/isapnp/*.h
