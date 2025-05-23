Summary:	Simple media player based on the GStreamer framework
Name:		parole
Version:	4.20.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	https://archive.xfce.org/src/apps/parole/4.20/%{name}-%{version}.tar.xz
# Source0-md5:	388dee33b1d06ee89f007b4cb08dedaf
URL:		https://www.xfce.org/projects/parole/
BuildRequires:	clutter-devel >= 1.16.4
BuildRequires:	clutter-gtk-devel >= 1.4.4
BuildRequires:	dbus-devel >= 0.60
BuildRequires:	dbus-glib-devel >= 0.70
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.38.0
BuildRequires:	gstreamer-devel >= 1.0.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	gtk-doc
BuildRequires:	libnotify-devel >= 0.7.8
BuildRequires:	libxfce4ui-devel >= 4.18.0
BuildRequires:	libxfce4util-devel >= 4.18.0
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	taglib-devel >= 1.4
BuildRequires:	xfce4-dev-tools >= 4.18.0
BuildRequires:	xfconf-devel >= 4.18.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Suggests:	gstreamer-imagesink-x
Obsoletes:	xfmedia
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parole is a modern simple media player based on the GStreamer
framework and written to fit well in the Xfce desktop. Parole is
designed with simplicity, speed and resource usage in mind.

%prep
%setup -q

%build
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%{__rm} -r $RPM_BUILD_ROOT%{_includedir}

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hye,ie}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hy}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS TODO
%attr(755,root,root) %{_bindir}/parole
%dir %{_libdir}/parole-0
%attr(755,root,root) %{_libdir}/parole-0/*.so
%{_datadir}/parole
%{_desktopdir}/org.xfce.Parole.desktop
%{_iconsdir}/hicolor/*/apps/org.xfce.parole.*
%{_iconsdir}/hicolor/*/apps/parole-extension*
%{_datadir}/metainfo/parole.appdata.xml
