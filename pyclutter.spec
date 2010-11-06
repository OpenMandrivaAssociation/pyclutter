%define name pyclutter
%define version 1.0.2
%define release %mkrel 2

%define apiver 1.0
%define api 1.0

Summary:       Python bindings for clutter
Name:          %{name}
Version:       %{version}
Release:       %{release}
Source0:       http://www.clutter-project.org/sources/pyclutter/%apiver/%{name}-%{version}.tar.bz2
Patch0:        cogl-base-types.patch
Patch1:		pyclutter-1.0.2-fix-link.patch
License:       LGPLv2+
Group:         Graphics
Url:           http://clutter-project.org/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: clutter-devel >= 1.2.0
BuildRequires: pygtk2.0-devel >= 2.8.0
BuildRequires: python-cairo-devel >= 1.0.2
BuildRequires: libxslt-proc

%description
Python bindings for clutter

#----------------------------------------------------------------------------

%package -n python-clutter
Summary:       Python bindings for clutter
Group:         Graphics
Provides:      pyclutter = %{version}-%{release}

%description -n python-clutter
Python bindings for clutter

%package -n python-clutter-devel
Summary:       Python bindings for clutter
Group: Development/Python
Requires: python-clutter  = %{version}-%{release}

%description -n python-clutter-devel
Python bindings for clutter - development files.

%prep
%setup -q
%apply_patches

%build
%configure2_5x --enable-docs
%make

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files -n python-clutter
%defattr(-,root,root)
%doc AUTHORS README NEWS
%dir %{py_platsitedir}/clutter
%{py_platsitedir}/clutter/*

%files -n python-clutter-devel
%defattr(-,root,root)
%doc ChangeLog
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{api}
%dir %{_datadir}/%{name}/%{api}/defs
%{_datadir}/%{name}/%{api}/defs/*.defs
%{_includedir}/%{name}-%{api}/%{name}/%{name}.h
%{_libdir}/pkgconfig/%{name}-%{apiver}.pc
%_datadir/gtk-doc/html/%name/
