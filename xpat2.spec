Summary:	A set of Solitaire type games for the X Window System
Summary(es):	X Patience - varios juegos de cartas
Summary(pl):	Zestaw pasjansów dla X Window System
Summary(pt_BR):	X Patience - vários jogos de cartas
Name:		xpat2
Version:	1.07
Release:	10
License:	distributable - most of it GPL
Group:		X11/Applications/Games
Source0:	ftp://metalab.unc.edu/pub/Linux/games/solitaires/%{name}-%{version}-src.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-paths.patch
Patch1:		%{name}-qt-locales.patch
Patch2:		%{name}-fixes.patch
BuildRequires:	XFree86-devel
BuildRequires:	XFree86
BuildRequires:	qt-devel
BuildRequires:	tetex-dvips
BuildRequires:	tetex-latex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Xpat2 is a generic patience or Solitaire game for the X Window System.
Xpat2 can be used with different rules sets, so it can be used to play
Spider, Klondike, and other card games.

%description -l pl
Xpat2 jest zestawem pasjansów dla X Window. Mo¿e byæ u¿ywany z wieloma
ró¿nymi zasadami; mo¿na graæ w Spidera, Klondike i inne gry karciane.

%description -l pt_BR
Em 1989, Dave Lemke, Heather Rose, Donald R. Woods e a Sun
Microsystems, Inc., criaram o jogo de paciência xsol (também conhecido
como klondike no DOS) e as regras de alguns outros jogos de paciência.
As características principais são variáveis com conjuntos de regras e
diferentes conjuntos de cartas para diferentes resoluções de
monitores. xpat2 (X Patience) é uma coleção destes variados jogos de
paciência que irão realmente "testar a sua paciência".

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

# moc files generated for old Qt - removing them causes regeneration for new
rm -f src/{moc_*,mqmaskedit,mqhelpwin}.cpp

%build
cd lib
mv -f german de
mv -f french fr
mv -f italian it
mv -f russian ru
rm -f de_DE fr_FR it_IT
rm -f src/moc*
rm -f src/mqmaskedit.cpp
rm -f src/mqhelpwin.cpp
cd ../src
xmkmf
%{__make} CCOPTIONS="%{rpmcflags}" CXXOPTIONS="%{rpmcflags}"

cd ..
%{__make} manual

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games/Card,%{_pixmapsdir}} \
	$RPM_BUILD_ROOT/var/games

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Card
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

:> $RPM_BUILD_ROOT/var/games/xpat.log

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/xpat2.ps
%attr(2755,root,games) %{_bindir}/xpat2
%attr(664,root,games) /var/games/xpat.log
%{_mandir}/man6/*
%dir %{_datadir}/xpat
%{_datadir}/xpat/???*
%lang(de) %{_datadir}/xpat/de
%lang(fr) %{_datadir}/xpat/fr
%lang(it) %{_datadir}/xpat/it
%lang(ru) %{_datadir}/xpat/ru
%{_libdir}/X11/app-defaults/XPat
%lang(de) %{_libdir}/X11/app-defaults/de/XPat
%lang(fr) %{_libdir}/X11/app-defaults/fr/XPat
%lang(it) %{_libdir}/X11/app-defaults/it/XPat
%lang(ru) %{_libdir}/X11/app-defaults/ru/XPat
%config(noreplace) %{_applnkdir}/Games/Card/xpat2.desktop
%{_pixmapsdir}/*
