Summary:	A set of Solitaire type games for the X Window System.
Name:		xpat2
Version:	1.06
Release:	7
Copyright:	distributable - most of it GPL
Group:		Games
Source0:	ftp://metalab.unc.edu/pub/Linux/games/solitaires/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-1.03-fsstnd.patch
Patch1:		%{name}.nomkdirhier.patch
Patch2:		%{name}-1.06-nochown.patch
BuildPrereq:	tetex-dvips, tetex, tetex-latex, XFree86-devel, glibc-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xpat2 is a generic patience or Solitaire game for the X Window System.
Xpat2 can be used with different rules sets, so it can be used to play
Spider, Klondike, and other card games.

%prep
%setup -q
%patch -p1
%patch1 -p0 -b .nobr
%patch2 -p1 -b .nochown

%build
export PATH=%{_bindir}/X11:$PATH
%{__make}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/applnk/Games
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_libdir}/games/xpat
install -d $RPM_BUILD_ROOT/%{_mandir}/man6
install -d $RPM_BUILD_ROOT%{_prefix}/X11R6/lib/X11/{italian,german,russian,french}/app-defaults

%{__make} DESTDIR=$RPM_BUILD_ROOT  XPATMANDIR=%{_mandir}/man6 install
mv $RPM_BUILD_ROOT%{_prefix}/X11R6/bin/xpat2 $RPM_BUILD_ROOT%{_bindir}/xpat2


install %SOURCE1 $RPM_BUILD_ROOT%{_sysconfdir}/X11/applnk/Games/xpat2.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README xpat2/xpat2.tex
%{_libdir}/games/xpat
%{_mandir}/*/*
%attr(755,root,root) %{_bindir}/xpat2
%{_prefix}/X11R6/lib/X11/app-defaults/XPat
%config(noreplace) %{_sysconfdir}/X11/applnk/Games/xpat2.desktop
