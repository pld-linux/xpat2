Summary:	A set of Solitaire type games for the X Window System.
Name:		xpat2
Version:	1.07
Release:	1
Copyright:	distributable - most of it GPL
Group:		Games
Source0:	ftp://metalab.unc.edu/pub/Linux/games/solitaires/%{name}-%{version}-src.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-qt-path.patch
# Patch0:		%{name}-1.03-fsstnd.patch
# Patch1:		%{name}.nomkdirhier.patch
# Patch2:		%{name}-1.06-nochown.patch
BuildPrereq:	tetex-dvips, tetex, tetex-latex, XFree86-devel, glibc-devel
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define         _mandir         %{_prefix}/man

%description
Xpat2 is a generic patience or Solitaire game for the X Window System.
Xpat2 can be used with different rules sets, so it can be used to play
Spider, Klondike, and other card games.

%prep
%setup -q
%patch -p0
#%patch1 -p0 -b .nobr
#%patch2 -p1 -b .nochown

%build
export PATH=%{_bindir}/X11:$PATH
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Games
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_libdir}/games/xpat
install -d $RPM_BUILD_ROOT%{_mandir}/man6
install -d $RPM_BUILD_ROOT%{_prefix}/X11R6/lib/X11/{italian,german,russian,french}/app-defaults
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/xpat2.tex
%{_libdir}/games/xpat
%{_mandir}/*/*
%attr(755,root,root) %{_bindir}/xpat2
%{_prefix}/lib/X11/app-defaults/XPat
%config(noreplace) %{_applnkdir}/Games/xpat2.desktop
%{_pixmapsdir}/*
