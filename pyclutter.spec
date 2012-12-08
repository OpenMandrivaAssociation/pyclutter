%define apiver 1.0
%define api 1.0

Summary:	Python bindings for clutter
Name:		pyclutter
Version:	1.3.2
Release:	6
License:	LGPLv2+
Group:		Graphics
Url:		http://clutter-project.org/
Source0:	http://www.clutter-project.org/sources/pyclutter/%apiver/%{name}-%{version}.tar.bz2
Patch1:		pyclutter-1.0.2-fix-link.patch
Patch2:		pyclutter-1.3.2-clutter-1.9.2-compat.patch
Patch3:		pyclutter-1.3.2-clutter-1.9.14-compat.patch
BuildRequires:	clutter-devel >= 1.2.0
BuildRequires:	pygtk2.0-devel >= 2.8.0
BuildRequires:	python-cairo-devel >= 1.0.2
BuildRequires:	libxslt-proc
BuildRequires:	mesa-common-devel

%description
Python bindings for clutter

#----------------------------------------------------------------------------

%package -n python-clutter
Summary:	Python bindings for clutter
Group:		Graphics
Provides:	pyclutter = %{version}-%{release}

%description -n python-clutter
Python bindings for clutter

%package -n python-clutter-devel
Summary:	Python bindings for clutter
Group:		Development/Python
Requires:	python-clutter  = %{version}-%{release}

%description -n python-clutter-devel
Python bindings for clutter - development files.

%prep
%setup -q
%apply_patches

%build
%configure2_5x --enable-docs
%make

%install
%makeinstall_std

%files -n python-clutter
%doc AUTHORS README NEWS
%dir %{py_platsitedir}/clutter
%{py_platsitedir}/clutter/*

%files -n python-clutter-devel
%doc ChangeLog
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{api}
%dir %{_datadir}/%{name}/%{api}/defs
%{_datadir}/%{name}/%{api}/defs/*.defs
%{_includedir}/%{name}-%{api}/%{name}/%{name}.h
%{_libdir}/pkgconfig/%{name}-%{apiver}.pc
%{_datadir}/gtk-doc/html/%{name}/


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.2-2mdv2011.0
+ Revision: 667904
- mass rebuild

* Thu Mar 24 2011 Funda Wang <fwang@mandriva.org> 1.3.2-1
+ Revision: 648202
- new version 1.3.2

* Sat Nov 06 2010 Funda Wang <fwang@mandriva.org> 1.0.2-2mdv2011.0
+ Revision: 593860
- fix link
- drop DEBUG_FLAGS (not there any more)

* Mon Apr 19 2010 Götz Waschk <waschk@mandriva.org> 1.0.2-1mdv2010.1
+ Revision: 536754
- new version
- drop patch

* Wed Mar 17 2010 Götz Waschk <waschk@mandriva.org> 1.0.0-3mdv2010.1
+ Revision: 523880
- patch for clutter 1.2
- fix build deps

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt for 2010.1

* Sat Aug 29 2009 Götz Waschk <waschk@mandriva.org> 1.0.0-1mdv2010.0
+ Revision: 422130
- new version
- drop patch
- remove gst and gtk bindings

* Wed Aug 05 2009 Götz Waschk <waschk@mandriva.org> 0.9.2-2mdv2010.0
+ Revision: 410203
- split out devel package
- enable docs

* Wed Aug 05 2009 Götz Waschk <waschk@mandriva.org> 0.9.2-1mdv2010.0
+ Revision: 410181
- new version
- new apiver
- update deps
- remove cluttercairo

* Thu Feb 12 2009 Funda Wang <fwang@mandriva.org> 0.8.2-1mdv2009.1
+ Revision: 339759
- update versioned BR and file list
- New version 0.8.2

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 0.8.0-0.3273.2mdv2009.1
+ Revision: 323570
- fix linkage
- rebuild

* Sat Sep 13 2008 Colin Guthrie <cguthrie@mandriva.org> 0.8.0-0.3273.1mdv2009.0
+ Revision: 284395
- New snapshot

* Wed Feb 20 2008 Colin Guthrie <cguthrie@mandriva.org> 0.6.0-1mdv2008.1
+ Revision: 173180
- New version

* Thu Jan 24 2008 Colin Guthrie <cguthrie@mandriva.org> 0.4.1-3mdv2008.1
+ Revision: 157487
- Bump release for buildsystem lock.
- New upstream version 0.4.1 (upstream messed up previous release which was not meant to be named 0.4.1)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 08 2007 Colin Guthrie <cguthrie@mandriva.org> 0.4.1-1mdv2008.0
+ Revision: 60563
- Rename package
- Import pyclutter

