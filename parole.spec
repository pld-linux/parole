Summary:	Simple media player based on the GStreamer framework
#Summary(pl.UTF-8):	-
Name:		parole
Version:	0.2.0.2
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://www.xfce.org/archive/src/apps/parole/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	c304b07c3f17feefe3879bacd6e54515
Patch0:		%{name}-ui.patch
URL:		http://www.xfce.org/projects/parole/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dbus-devel >= 0.60
BuildRequires:	dbus-glib-devel >= 0.70
BuildRequires:	gettext-devel
BuildRequires:	gstreamer-devel >= 0.10.11
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gtk+2-devel >= 2:2.16.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel >= 4.8.0
BuildRequires:	libxfce4util-devel >= 4.8.0
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	xfce4-dev-tools >= 4.6.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parole is a modern simple media player based on the GStreamer
framework and written to fit well in the Xfce desktop.
Parole is designed with simplicity, speed and resource usage in mind.

#%description -l pl.UTF-8

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-browser-plugin

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_includedir}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/parole-0/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/parole
%dir %{_libdir}/parole-0
%attr(755,root,root) %{_libdir}/parole-0/*.so
%{_datadir}/parole
%{_desktopdir}/parole.desktop
%{_iconsdir}/hicolor/*/apps/parole.*
