# NOTE: for 1.x versions see DEVEL branch; it's not compatible with 0.x, and (according to web site) still work in progress.
Summary:	Native makefiles generator
Summary(pl.UTF-8):	Generator natywnych plików typu Makefile
Name:		bakefile
Version:	0.2.10
Release:	2
License:	MIT
Group:		Development/Building
#SourceDownload: https://github.com/vslavik/bakefile/releases
Source0:	https://github.com/vslavik/bakefile/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f980cdd36268b5d2b23602d454bdf0a4
Patch0:		%{name}-empy.patch
Patch1:		%{name}-versioncompare.patch
URL:		http://bakefile.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.6
BuildRequires:	libtool
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	empy >= 3.1
Requires:	python-libxml2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bakefile is cross-platform, cross-compiler native makefiles generator.
It takes compiler-independent description of build tasks as input and
generate native makefile (autoconf's Makefile.in, Visual C++ project,
bcc makefile etc.).

%description -l pl.UTF-8
Bakefile to generator natywnych plików typu Makefile dla wielu
platform i kompilatorów. Przyjmuje na wejściu niezależny od
kompilatora opis zadań budowania i tworzy natywny plik (Makefile.in
dla autoconfa, projekt dla Visual C++, makefile dla bcc itd.).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I admin
%{__autoconf}
%{__automake}
%configure

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# use system available modules
%{__rm} -r $RPM_BUILD_ROOT%{_libdir}/%{name}/{empy,py25modules}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la
find $RPM_BUILD_ROOT%{_libdir}/%{name} -name '*.py' | grep -E -v '/bakefile(_gen)?\.py' | xargs %{__rm}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README THANKS doc/html
%attr(755,root,root) %{_bindir}/bakefile
%attr(755,root,root) %{_bindir}/bakefile_gen
%attr(755,root,root) %{_bindir}/bakefilize
%{_datadir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.py[oc]
%attr(755,root,root) %{_libdir}/%{name}/_bkl_c.so
%attr(755,root,root) %{_libdir}/%{name}/bakefile.py
%attr(755,root,root) %{_libdir}/%{name}/bakefile_gen.py
%{_aclocaldir}/bakefile*.m4
%{_mandir}/man1/bakefile.1*
%{_mandir}/man1/bakefile_gen.1*
%{_mandir}/man1/bakefilize.1*
