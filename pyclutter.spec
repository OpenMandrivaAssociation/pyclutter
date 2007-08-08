%define name pyclutter
%define version 0.4.1
%define rel 1
%define svn 0
%if %svn
%define release %mkrel 0.%svn.%rel
%else
%define release %mkrel %rel
%endif

%define api 1.0

Summary:       Python bindings for clutter
Name:          %{name}
Version:       %{version}
Release:       %{release}
%if %svn
Source0:       %{name}-%{svn}.tar.bz2
%else
Source0:       %{name}-%{version}.tar.bz2
%endif
License:       LGPL
Group:         Graphics
Url:           http://clutter-project.org/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: clutter-devel
BuildRequires: clutter-cairo-devel
BuildRequires: clutter-gst-devel
BuildRequires: clutter-gtk-devel
BuildRequires: python-gtk
BuildRequires: python-cairo
BuildRequires: gstreamer0.10-python-devel

%description
Python bindings for clutter

#----------------------------------------------------------------------------

%package -n python-clutter
Summary:       Python bindings for clutter
Group:         Graphics
Provides:      pyclutter = %{version}-%{release}

%description -n python-clutter
Python bindings for clutter

#----------------------------------------------------------------------------

%prep
%if %svn
%setup -q -n %name
./autogen.sh -V
%else
%setup -q
%endif

%build
%configure
%make

%install
rm -rf %buildroot

%makeinstall

%clean
rm -rf %buildroot

%files -n python-clutter
%defattr(-,root,root)
%dir %{py_platsitedir}/clutter
%{py_platsitedir}/clutter/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{api}
%dir %{_datadir}/%{name}/%{api}/defs
%{_datadir}/%{name}/%{api}/defs/*.defs
%dir %{_datadir}/%{name}/defs
%_datadir/%{name}/defs/*.defs
%{_includedir}/%{name}-%{api}/%{name}/%{name}.h

