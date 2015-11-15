Summary:	GNOME thumbnailer for EPub and MOBI books
Summary(pl.UTF-8):	Narzędzie GNOME do tworzenia miniaturek dla książek EPub oraz MOBI
Name:		gnome-epub-thumbnailer
Version:	1.5
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-epub-thumbnailer/1.5/%{name}-%{version}.tar.xz
# Source0-md5:	d9936c5240a58817a359e32cae3d4bd1
URL:		https://git.gnome.org/browse/gnome-epub-thumbnailer/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libarchive-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnome-epub-thumbnailer is a GNOME thumbnailer for EPub and MOBI books.

%description -l pl.UTF-8
gnome-epub-thumbnailer to narzędzie GNOME do generowania
miniaturek dla książek w formacie EPub oraz MOBI.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/gnome-epub-thumbnailer
%attr(755,root,root) %{_bindir}/gnome-mobi-thumbnailer
%{_datadir}/thumbnailers/gnome-epub-thumbnailer.thumbnailer
%{_datadir}/thumbnailers/gnome-mobi-thumbnailer.thumbnailer
