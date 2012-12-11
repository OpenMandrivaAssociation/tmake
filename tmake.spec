# Templates avec #! Use ... template as shebang
%define	_requires_exceptions ^Use$

Summary:	Easy-to-use tool for creating and maintaining portable makefiles
Name:		tmake
Version:	2.12
Release:	%mkrel 6
Group:		Development/Other
License:	Distributable (see LICENSE file)
URL:		http://tmake.sourceforge.net
Source0:	http://heanet.dl.sourceforge.net/sourceforge/tmake/%name-%version.tar.bz2
Requires:	perl
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

%description
Tmake is an easy-to-use tool for creating and maintaining makefiles across
many platforms and compilers. This is a command-line tool based on project
files. The idea is that you should spend your time writing code, not
makefiles.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d %buildroot%_libdir/%name
install -d %buildroot%_bindir

cp -R lib %buildroot%_libdir/%name
install bin/%name %buildroot%_libdir/%name
install bin/progen %buildroot%_libdir/%name
cat > %buildroot%_bindir/%name <<EOF
export TMAKEPATH=%_libdir/%name/lib/linux-g++
exec %_libdir/%name/tmake "\$@"
EOF
cat > %buildroot%_bindir/progen <<EOF
export TMAKEPATH=%_libdir/%name/lib/linux-g++
exec %_libdir/%name/progen "\$@"
EOF

%clean
rm -rf %buildroot

%files
%defattr(755, root, root)
%doc README LICENSE
%doc doc example
%_libdir/tmake
%_bindir/tmake
%_bindir/progen





%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.12-6mdv2010.0
+ Revision: 434403
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.12-5mdv2009.0
+ Revision: 261569
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.12-4mdv2009.0
+ Revision: 254658
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.12-2mdv2008.1
+ Revision: 136546
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Jan 06 2007 Pascal Terjan <pterjan@mandriva.org> 2.12-2mdv2007.0
+ Revision: 104789
- Don't require 'Use' which does not exist...

* Fri Dec 01 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 2.12-1mdv2007.1
+ Revision: 89610
- New version 2.12
- import tmake-1.13-1mdk

* Thu Nov 18 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.13-1mdk
- 1.13

