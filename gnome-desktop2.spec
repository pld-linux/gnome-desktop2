Summary:	GNOME desktop library (from GNOME 2)
Summary(pl.UTF-8):	Biblioteka GNOME desktop (z GNOME 2)
Name:		gnome-desktop2
Version:	2.32.1
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-desktop/2.32/gnome-desktop-%{version}.tar.bz2
# Source0-md5:	5c80d628a240eb9d9ff78913b31f2f67
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.26.0
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.20.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gtk+2-devel >= 2:2.18.0
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
BuildRequires:	scrollkeeper
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	xorg-lib-libXrandr-devel >= 1.2
Conflicts:	gnome-desktop-libs < 2.32.1-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System. GNOME is similar in purpose and scope
to CDE and KDE, but GNOME is based completely on free software.

This package contains GNOME desktop library from GNOME 2.

%description -l pl.UTF-8
GNOME (GNU Network Object Model Environment) jest zestawem przyjaznych
dla użytkownika programów i narzędzi biurkowych, których używa się
wraz z zarządcą okien systemu X Window. GNOME przypomina wyglądem i
zakresem funkcjonalności CDE i KDE, jednak GNOME opiera się w całości
na wolnym oprogramowaniu.

Ten pakiet zawiera biblitekę GNOME desktop z GNOME 2.

%package devel
Summary:	GNOME desktop includes (from GNOME 2)
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GNOME desktop (z GNOME 2)
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.18.0
Requires:	startup-notification-devel >= 0.8
Conflicts:	gnome-desktop-devel < 2.32.1-2

%description devel
GNOME desktop header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GNOME desktop.

%prep
%setup -q -n gnome-desktop-%{version}

%build
%{__gtkdocize}
%{__intltoolize}
%{__gnome_doc_prepare}
%{__gnome_doc_common}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-gtk-doc \
	--disable-silent-rules \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# we need only library
%{__rm} $RPM_BUILD_ROOT%{_bindir}/*
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} -r $RPM_BUILD_ROOT%{_desktopdir}
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/{gtk-doc,gnome-about,gnome,omf,libgnome-desktop}
%{__rm} -r $RPM_BUILD_ROOT%{_pixmapsdir}
%{__rm} -r $RPM_BUILD_ROOT%{_mandir}

%find_lang gnome-desktop-2.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f gnome-desktop-2.0.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_libdir}/libgnome-desktop-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnome-desktop-2.so.17

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-desktop-2.so
%{_includedir}/gnome-desktop-2.0
%{_pkgconfigdir}/gnome-desktop-2.0.pc
