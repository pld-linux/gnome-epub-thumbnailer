Summary:	GNOME thumbnailer for EPub and MOBI books
Summary(pl.UTF-8):	Narzędzie GNOME do tworzenia miniaturek dla książek EPub oraz MOBI
Name:		gnome-epub-thumbnailer
Version:	1.8
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-epub-thumbnailer/1.8/%{name}-%{version}.tar.xz
# Source0-md5:	137634a46ccef8492c3e1d9d1f1a7a7d
URL:		https://gitlab.gnome.org/GNOME/gnome-epub-thumbnailer/
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libarchive-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
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
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/gnome-epub-thumbnailer
%attr(755,root,root) %{_bindir}/gnome-mobi-thumbnailer
%{_datadir}/thumbnailers/gnome-epub-thumbnailer.thumbnailer
%{_datadir}/thumbnailers/gnome-mobi-thumbnailer.thumbnailer
