Summary:	OpenSync xmlformat Plugin
Summary(pl.UTF-8):	Wtyczka xmlformat dla szkieletu OpenSync
Name:		libopensync-plugin-xmlformat
Version:	0.39
Release:	3
License:	LGPL
Group:		Libraries
Source0:	http://www.opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	cd0563bb78b50f846b5970b360a49213
URL:		http://www.opensync.org/
BuildRequires:	check-devel
BuildRequires:	cmake
BuildRequires:	glib2-devel >= 1:2.4
BuildRequires:	libopensync-devel >= 1:%{version}
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSync is a synchronization framework that is platform and
distribution independent.

It consists of several plugins that can be used to connect to devices,
a powerful sync-engine and the framework itself.

This package contains xmlformat plugin for OpenSync framework.

%description -l pl.UTF-8
OpenSync to niezależny od platformy i dystrybucji szkielet do
synchronizacji danych.

Składa się z różnych wtyczek, których można używać do łączenia z
urządzeniami, potężnego silnika synchronizacji oraz samego szkieletu.

Ten pakiet zawiera wtyczkę xmlformat dla szkieletu OpenSync.

%prep
%setup -q

%build
mkdir build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopensync1/formats/xmlformat-doc.so
%attr(755,root,root) %{_libdir}/libopensync1/formats/xmlformat.so
%{_datadir}/libopensync1/schemas/xmlformat-calendar.xsd
%{_datadir}/libopensync1/schemas/xmlformat-common.xsd
%{_datadir}/libopensync1/schemas/xmlformat-contact.xsd
%{_datadir}/libopensync1/schemas/xmlformat-event.xsd
%{_datadir}/libopensync1/schemas/xmlformat-note.xsd
%{_datadir}/libopensync1/schemas/xmlformat-todo.xsd
