# Templates avec #! Use ... template as shebang
%define	_requires_exceptions ^Use$

Summary:	Easy-to-use tool for creating and maintaining portable makefiles
Name:		tmake
Version:	2.12
Release:	%mkrel 2
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



