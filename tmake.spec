Summary:	Easy-to-use tool for creating and maintaining portable makefiles
Name:		tmake
Version:	2.12
Release:	8
Group:		Development/Other
License:	Distributable (see LICENSE file)
URL:		https://tmake.sourceforge.net
Source0:	http://heanet.dl.sourceforge.net/sourceforge/tmake/%name-%version.tar.bz2
Source1:	%{name}.rpmlintrc
Requires:	perl
BuildArch:	noarch

%description
Tmake is an easy-to-use tool for creating and maintaining makefiles across
many platforms and compilers. This is a command-line tool based on project
files. The idea is that you should spend your time writing code, not
makefiles.

%prep
%setup -q

%install
install -d %{buildroot}%{_libdir}/%{name}
install -d %{buildroot}%{_bindir}

cp -R lib %{buildroot}%{_libdir}/%{name}
install bin/%name %{buildroot}%{_libdir}/%{name}
install bin/progen %{buildroot}%{_libdir}/%{name}
cat > %{buildroot}%{_bindir}/%{name} <<EOF
export TMAKEPATH=%{_libdir}/%{name}/lib/linux-g++
exec %{_libdir}/%{name}/tmake "\$@"
EOF
cat > %{buildroot}%{_bindir}/progen <<EOF
export TMAKEPATH=%{_libdir}/%{name}/lib/linux-g++
exec %{_libdir}/%{name}/progen "\$@"
EOF

%files
%defattr(755, root, root)
%doc README LICENSE
%doc doc example
%{_libdir}/tmake
%{_bindir}/tmake
%{_bindir}/progen
