
%include	/usr/lib/rpm/macros.python

Summary:	Native makefiles generator
Name:		bakefile
Version:	0.1.1
%define		snap 20030922
Release:	0.%{snap}.1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://bakefile.sourceforge.net/snapshot/bakefile-%{version}.%{snap}.tar.gz
# Source0-md5:	52d8894603886844df68004e3bb8fd6c
URL:		http://bakefile.sourceforge.net/
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-libxml2
Requires:	empy >= 3.1
Requires:	python-optik >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bakefile is cross-platform, cross-compiler native makefiles generator. It takes
compiler-independent description of build tasks as input and generate native
makefile (autoconf's Makefile.in, Visual C++ project, bcc makefile etc.).

%prep
%setup -q -n %{name}-%{version}.%{snap}

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_bindir}}

%{__make} \
	DESTDIR=$RPM_BUILD_ROOT \
	install

# use system available modules
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/src/{empy,optik}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README THANKS doc/html
%attr(755,root,root) %{_bindir}/*
%{_aclocaldir}/*.m4
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/output
%{_datadir}/%{name}/rules
%dir %{_datadir}/%{name}/src
%{_datadir}/%{name}/src/*.py[oc]
%attr(755,root,root) %{_datadir}/%{name}/src/bakefile.py
%attr(755,root,root) %{_datadir}/%{name}/src/bakefile_gen.py
