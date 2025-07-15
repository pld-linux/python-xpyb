Summary:	X-protocol Python Binding
Summary(pl.UTF-8):	X-protocol Python Binding - wiązanie Pythona do protokołu X
Name:		python-xpyb
Version:	1.3.1
Release:	4
License:	Public Domain
Group:		Development/Languages/Python
Source0:	http://xcb.freedesktop.org/dist/xpyb-%{version}.tar.bz2
# Source0-md5:	b9b70746cd348836516edcba96d24677
Patch0:		%{name}-dir.patch
Patch1:		git.patch
Patch2:		xpyb-1.3.1-xcbproto-1.13.patch
URL:		http://xcb.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libxcb-devel >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	rpm-pythonprov
BuildRequires:	xcb-proto >= 1.7.1
%pyrequires_eq  python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XPyB provides a Python binding to the X Window System protocol via
libxcb.

%description -l pl.UTF-8
XPyB udostępnia wiązanie Pythona do protokołu X Window System poprzez
libxcb.

%package devel
Summary:	Development files for X Python Binding package
Summary(pl.UTF-8):	Pliki programistyczne pakietu X Python Binding
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxcb-devel >= 1.5
Requires:	python-devel >= 1:2.5

%description devel
Development files for X Python Binding package.

%description devel -l pl.UTF-8
Pliki programistyczne pakietu X Python Binding.

%prep
%setup -q -n xpyb-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-selinux
#	--enable-xinput

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/xcb/*.la
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/xpyb

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README doc/XcbPythonBinding.txt
%dir %{py_sitedir}/xcb
%attr(755,root,root) %{py_sitedir}/xcb/xcb.so
%{py_sitedir}/xcb/*.py[co]

%files devel
%defattr(644,root,root,755)
%{_includedir}/xpyb.h
%{_pkgconfigdir}/xpyb.pc
