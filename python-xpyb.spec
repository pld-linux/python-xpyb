Summary:	X-protocol Python Binding
Summary(pl.UTF-8):	X-protocol Python Binding - wiązanie Pythona do protokołu X
Name:		python-xpyb
Version:	1.2
Release:	1
License:	Public Domain
Group:		Development/Languages/Python
Source0:	http://xcb.freedesktop.org/dist/xpyb-%{version}.tar.bz2
# Source0-md5:	953cd851d7ad3e59577062ca53c77f3d
Patch0:		%{name}-dir.patch
URL:		http://xcb.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libxcb-devel >= 1.1
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	rpm-pythonprov
BuildRequires:	xcb-proto >= 1.1
%pyrequires_eq  python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XPyB provides a Python binding to the X Window System protocol via
libxcb.

%description -l pl.UTF-8
XPyB udostępnia wiązanie Pythona do protokołu X Window System poprzez
libxcb.

%prep
%setup -q -n xpyb-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-selinux \
	--enable-xinput

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean
rm $RPM_BUILD_ROOT%{py_sitedir}/xcb/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README doc/XcbPythonBinding.txt
%dir %{py_sitedir}/xcb
%attr(755,root,root) %{py_sitedir}/xcb/xcb.so
%{py_sitedir}/xcb/*.py[co]
# -devel
%{_pkgconfigdir}/xpyb.pc
