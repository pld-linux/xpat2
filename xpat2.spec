Summary: A set of Solitaire type games for the X Window System.
Name: xpat2
Version: 1.06
Release: 7
Copyright: distributable - most of it GPL
Group: Amusements/Games
Source: ftp://metalab.unc.edu/pub/Linux/games/solitaires/xpat2-%{version}.tar.gz
Source1: xpat2.desktop
Patch: xpat2-1.03-fsstnd.patch
Patch1: xpat2.nomkdirhier.patch
Patch2: xpat2-1.06-nochown.patch
BuildPrereq: tetex-dvips, tetex, tetex-latex, XFree86-devel, glibc-devel
BuildRoot: %{_tmppath}/xpat2-%{version}-root

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
export PATH=/usr/bin/X11:$PATH
make


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/applnk/Games
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/lib/games/xpat
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man6
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/lib/X11/{italian,german,russian,french}/app-defaults

make DESTDIR=$RPM_BUILD_ROOT  XPATMANDIR=%{_mandir}/man6 install
mv $RPM_BUILD_ROOT/usr/X11R6/bin/xpat2 $RPM_BUILD_ROOT/usr/bin/xpat2 

chmod 0644 $RPM_BUILD_ROOT/usr/lib/games/xpat/audio/*.wav

install -m 644 %SOURCE1 $RPM_BUILD_ROOT/etc/X11/applnk/Games/xpat2.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README xpat2/xpat2.tex
/usr/lib/games/xpat
%{_mandir}/*/*
/usr/bin/xpat2
/usr/X11R6/lib/X11/app-defaults/XPat
%config(noreplace) /etc/X11/applnk/Games/xpat2.desktop

%changelog
* Mon Jun 25 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Add some build dependencies
- don't create ps file, ship tex file
- make sure it doesn't try to chown files during install
- don't create the desktop file inside the specfile

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun 13 2000 Trond Eivind Glomsrød <teg@redhat.com>
- use %%{_tmppath} and %%{_mandir}
- Add BuildPrereq: of tetex and tetex-dvips

* Tue Apr 04 2000 Trond Eivind Glomsrød <teg@redhat.com>
- gzipped man page
- changed the permissions on some wav files

* Fri Mar 24 2000 Trond Eivind Glomsrød <teg@redhat.com>
- upgraded to 1.06. This fixes some problems with internationalization.
- Removed xpm patch, as this is no longer necesarry.
- updated URL
- includes doc
  

* Mon Feb 07 2000 Preston Brown <pbrown@redhat.com>
- gzip man page
- wmconfig --> desktop

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 10)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Thu Sep 17 1998 Jeff Johnson <jbj@redhat.com>
- use "mkdir -p" rather than mkdirhier to avoid IFS problem with bash-2.02.

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- wmconfig

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc
