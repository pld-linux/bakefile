%define		pre	_pre1

Summary:	Native makefiles generator
Summary(pl):	Generator natywnych plik�w typu Makefile
Name:		bakefile
Version:	0.2.1
Release:	0.%{pre}.1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/bakefile/bakefile-%{version}%{pre}.tar.gz
# Source0-md5:	bf4b78fb2afd9f34cb2f845174fc32d0
Patch0:		%{name}-empy.patch
URL:		http://bakefile.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	python-devel
%pyrequires_eq	python-modules
Requires:	python-libxml2
Requires:	empy >= 3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bakefile is cross-platform, cross-compiler native makefiles generator.
It takes compiler-independent description of build tasks as input and
generate native makefile (autoconf's Makefile.in, Visual C++ project,
bcc makefile etc.).

%description -l pl
Bakefile to generator natywnych plik�w typu Makefile dla wielu
platform i kompilator�w. Przyjmuje na wej�ciu niezale�ny od
kompilatora opis zada� budowania  i tworzy natywny plik (Makefile.in
dla autoconfa, projekt dla Visual C++, makefile dla bcc itd.).

%prep
%setup -q -n %{name}-%{version}%{pre} 
%patch0 -p1

%build
%{__aclocal} -I admin
%{__autoconf}
%{__automake}
%configure

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_bindir}}

%{__make} \
	DESTDIR=$RPM_BUILD_ROOT \
	install

# use system available modules
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/{empy,optik}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README THANKS doc/html
%attr(755,root,root) %{_bindir}/*
%{_aclocaldir}/*.m4
%{_datadir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.py[oc]
%attr(755,root,root) %{_libdir}/%{name}/*.so
%attr(755,root,root) %{_libdir}/%{name}/bakefile.py
%attr(755,root,root) %{_libdir}/%{name}/bakefile_gen.py
%{_mandir}/man1/bakefil*.1*
