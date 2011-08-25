Summary: A library for locking devices
Name: lockdev
Version: 1.0.1
Release: 18%{?dist}
License: LGPLv2
Group: System Environment/Libraries
URL: http://packages.debian.org/unstable/source/lockdev
Source0: http://ftp.debian.org/debian/pool/main/l/lockdev/%{name}_%{version}.orig.tar.gz
Source1: lockdev.8

Patch0: lockdev-1.0.0-rh.patch
Patch1: lockdev-1.0.0-shared.patch
Patch2: lockdev-1.0.0-signal.patch
Patch3: lockdev-1.0.0-cli.patch
Patch4: lockdev-1.0.1-checkname.patch
Patch5: lockdev-1.0.1-pidexists.patch
Patch6: lockdev-1.0.1-subdir.patch
Patch7: lockdev-1.0.1-fcntl.patch
Patch8: lockdev-1.0.1-32bit.patch
Patch9: lockdev-1.0.1-gccwarn.patch
Patch10: lockdev-1.0.1-man8.patch

Requires(pre): shadow-utils
Requires(post): glibc
Requires(postun): glibc

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Lockdev provides a reliable way to put an exclusive lock to devices
using both FSSTND and SVr4 methods.

%package devel
Summary: The header files and a static library for the lockdev library
Group: System Environment/Libraries
Requires: lockdev = %{version}-%{release}

%description devel
The lockdev library provides a reliable way to put an exclusive lock
on devices using both FSSTND and SVr4 methods. The lockdev-devel
package contains the development headers and a static library.

%prep
%setup -q
%patch0 -p1 -b .redhat
%patch1 -p1 -b .shared
%patch2 -p1 -b .signal
%patch3 -p1 -b .jbj
%patch4 -p1 -b .checkname
%patch5 -p1 -b .pidexists
%patch6 -p1 -b .subdir
%patch7 -p1 -b .fcntl
%patch8 -p1 -b .32bit
%patch9 -p1 -b .warn
%patch10 -p1 -b .man8

cp %SOURCE1 ./docs

%build
make "CFLAGS=${RPM_OPT_FLAGS} -fPIC"

%install
make \
    sbindir=${RPM_BUILD_ROOT}%{_sbindir} \
    libdir=${RPM_BUILD_ROOT}%{_libdir} \
    incdir=${RPM_BUILD_ROOT}%{_includedir} \
    mandir=${RPM_BUILD_ROOT}%{_mandir} \
        install
/sbin/ldconfig -n $RPM_BUILD_ROOT/%{_libdir}

mkdir -p $RPM_BUILD_ROOT/var/lock

%pre
groupadd -g 54 -r -f lock

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENSE
%attr(2711,root,lock)   %{_sbindir}/lockdev
%{_libdir}/*.so.*
%{_mandir}/man8/*

%files devel
%defattr(-,root,root)
%{_libdir}/*.a
%{_libdir}/*.so
%{_mandir}/man3/*
%{_includedir}/*

%changelog
* Tue Dec 01 2009 Jiri Popelka <jpopelka@redhat.com> - 1.0.1-18
- Added license text to package

* Thu Nov 19 2009 Jiri Popelka <jpopelka@redhat.com> - 1.0.1-17
- Fixed mixed-use-of-spaces-and-tabs
- Removed PreReq tag

* Fri Sep 25 2009 Jiri Popelka <jpopelka@redhat.com> - 1.0.1-16
- Manual page for /usr/sbin/lockdev

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct  6 2008 Karel Zak <kzak@redhat.com> - 1.0.1-13
- refresh patches (due --fuzz=0)
- fix compiler warnings

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.1-12.1
- Autorebuild for GCC 4.3

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.1-11.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Thu Apr 12 2007 Karel Zak <kzak@redhat.com> - 1.0.1-11
- fix rpmlint issues
- change lockdev permissions from 2755 to 2711

* Wed Jul 19 2006 Karel Zak <kzak@redhat.com> - 1.0.1-10
- rebuild

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.0.1-9.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.1-9.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.1-9.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Sep 21 2005 Karel Zak <kzak@redhat.com> 1.0.1-9
- fix #165189 - The naming of the lock file by the lockdev command is abnormal.

* Thu Sep  1 2005 Karel Zak <kzak@redhat.com> 1.0.1-8
- fix #163276 - baudboy.h should include fcntl.h

* Sat Mar  5 2005 Karel Zak <kzak@redhat.com> 1.0.1-6
- rebuilt

* Wed Feb 23 2005 Karel Zak <kzak@redhat.com> 1.0.1-5
- lockdev errs on /dev/input/ttyACM0 (3-component pathname) (#126082, #98160, #74454)

* Fri Oct 22 2004 Adrian Havill <havill@redhat.com> 1.0.1-4
- don't unlock files if pid still exists (#128104)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Sep  9 2003 Nalin Dahyabhai <nalin@redhat.com> 1.0.1-1.3
- rebuild

* Mon Sep  8 2003 Nalin Dahyabhai <nalin@redhat.com> 1.0.1-1.2
- rebuild

* Wed Aug 20 2003 Adrian Havill <havill@redhat.com> 1.0.1-1.1
- bump n-v-r for 3.0E

* Fri Aug 15 2003 Adrian Havill <havill@redhat.com> 1.0.1-1
- bumped version
- make the dev rewrite work with ttys in the /dev/input subdir, not just
  the base level dir (#98160)

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 04 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- add symlink to shared lib

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Nov 29 2002 Jeff Johnson <jbj@redhat.com>
- don't segfault if device arg is missing.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jun  5 2002 Jeff Johnson <jbj@redhat.com> 1.0.0-19
- fix: don't ignore signals, use default behavior instead (#63468).

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Feb 25 2002 Nalin Dahyabhai <nalin@redhat.com> 1.0.0-16
- include liblockdev.so so that programs can link to a shared liblockdev
- fix shared library version numbers

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Nov 29 2001 Trond Eivind Glomsrod <teg@redhat.com> 1.0.0-16
- Rebuilt

* Fri Oct 26 2001 Trond Eivind Glomsrod <teg@redhat.com> 1.0.0-15
- Add copyright/license info to baudboy.h (#54321)

* Tue Sep  4 2001 Jeff Johnson <jbj@redhat.com>
- swap egid and gid for lockdev's access(2) device check (#52029).

* Tue Aug 28 2001 Jeff Johnson <jbj@redhat.com>
- typo in include file (#52704).
- map specific errno's into status for return from helper.

* Tue Aug 14 2001 Jeff Johnson <jbj@redhat.com>
- set exit status correctly.

* Thu Aug  9 2001 Bill Nottingham <notting@redhat.com>
- check that we can open the device r/w before locking
- fix calling lockdev without any arguments
- fix waitpid() call in baudboy.h
- use umask(002), not umask(0)

* Wed Aug  8 2001 Bill Nottingham <notting@redhat.com>
- add lock group here, own /var/lock as well

* Sun Aug  5 2001 Jeff Johnson <jbj@redhat.com>
- include setgid helper binary and baudboy.h.

* Mon Jun 18 2001 Trond Eivind Glomsrod <teg@redhat.com>
- Make the -devel depend on the main package

* Sun Aug 06 2000 Trond Eivind Glomsrod <teg@redhat.com>
- rebuild

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sat Jun 17 2000 Bill Nottingham <notting@redhat.com>
- add %%defattr for -devel

* Sat Jun 10 2000 Trond Eivind Glomsrod <teg@redhat.com>
- use %%{_mandir}

* Thu May 04 2000 Trond Eivind Glomsrod <teg@redhat.com>
- first build
