%define name pyclutter
%define version 0.9.2
%define rel 1
%define release %mkrel %rel

%define apiver 0.9
%define api 1.0

Summary:       Python bindings for clutter
Name:          %{name}
Version:       %{version}
Release:       %{release}
Source0:       http://www.clutter-project.org/sources/pyclutter/%apiver/%{name}-%{version}.tar.bz2
Patch0:        pyclutter-linkage.patch
License:       LGPLv2+
Group:         Graphics
Url:           http://clutter-project.org/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: clutter-devel >= 1.0.0
BuildRequires: clutter-gst-devel >= 0.10.0
BuildRequires: clutter-gtk-devel >= 0.10.2
BuildRequires: pygtk2.0-devel >= 2.8.0
BuildRequires: python-cairo-devel >= 1.0.2
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
%setup -q
%patch0 -p1 -b .linkage

%build
%configure2_5x
%make

%install
rm -rf %buildroot

%makeinstall_std

%clean
rm -rf %buildroot

%files -n python-clutter
%defattr(-,root,root)
%dir %{py_platsitedir}/clutter
%{py_platsitedir}/clutter/*
%dir %{py_platsitedir}/cluttergst
%{py_platsitedir}/cluttergst/*
%dir %{py_platsitedir}/cluttergtk
%{py_platsitedir}/cluttergtk/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{api}
%dir %{_datadir}/%{name}/%{api}/defs
%{_datadir}/%{name}/%{api}/defs/*.defs
%{_includedir}/%{name}-%{api}/%{name}/%{name}.h
%{_libdir}/pkgconfig/%{name}-%{apiver}.pc
