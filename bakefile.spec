#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# py.test tests

Summary:	Native makefiles generator
Summary(pl.UTF-8):	Generator natywnych plików typu Makefile
Name:		bakefile
Version:	1.2.5.1
Release:	1
License:	MIT
Group:		Development/Building
#SourceDownload: https://github.com/vslavik/bakefile/releases
Source0:	https://github.com/vslavik/bakefile/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	cfd70a07103a838a97f0b644d28292b1
URL:		http://bakefile.org/
# it's bundled; use system?
#BuildRequires:	java-antlr3
BuildRequires:	jre
BuildRequires:	python-devel >= 1:2.6
%{?with_tests:BuildRequires:	python-pytest}
BuildRequires:	rpm-pythonprov
%{?with_doc:BuildRequires:	sphinx-pdg-2}
# TODO
#Requires:	python-antlr3
Requires:	python-libxml2
Requires:	python-modules >= 1:2.6
# TODO (for color output)
#Suggests:	python-clint
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

%build
%{__make} parser

%if %{with doc}
PYTHONPATH=$(pwd)/src \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-2
%{__rm} -r docs/html/{_sources,.buildinfo,objects.inv}
%endif

%if %{with tests}
%{__python} -m pytest
%endif

%install
rm -rf $RPM_BUILD_ROOT

# make install is not supported

install -d $RPM_BUILD_ROOT{%{_bindir},%{py_sitescriptdir}}
cp -p src/tool.py $RPM_BUILD_ROOT%{_bindir}/bkl
cp -pr src/bkl $RPM_BUILD_ROOT%{py_sitescriptdir}/bkl
# parser antlr3 source files
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/bkl/parser/*.{g,tokens}
# TODO: use some system package for "import antlr3"
cp -pr 3rdparty/antlr3/python-runtime/antlr3 $RPM_BUILD_ROOT%{py_sitescriptdir}/bkl/parser

%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean -x 'plugins/.*'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README %{?with_doc:docs/html}
%attr(755,root,root) %{_bindir}/bkl
%{py_sitescriptdir}/bkl
