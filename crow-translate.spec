Name:       crow-translate
Version:    2.9.5
Release:    3%{?dist}
Summary:    A simple and lightweight translator
License:    GPL-3.0-only
URL:        https://crow-translate.github.io/
Source:     https://github.com/crow-translate/crow-translate/releases/download/2.9.5/crow-translate-%{version}-source.tar.gz

Patch0:     https://raw.githubusercontent.com/CarlosEkisde/crow-translate-copr/main/crow-translate-make_static_libs.patch

BuildRequires: cmake
BuildRequires: cmake-rpm-macros
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: git
BuildRequires: hicolor-icon-theme
BuildRequires: qt5-linguist
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: tesseract-devel

Recommends: gstreamer-plugins-good

%description
A simple and lightweight translator that allows to translate and speak
text using Google, Yandex and Bing written with Qt5.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1


%build
%{cmake_kf5}
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc README.md
%{_bindir}/crow
%{_datadir}/icons/hicolor/*
%{_datadir}/Crow*Translate/*/translations/*
%{_datadir}/applications/io.crow_translate.CrowTranslate.desktop
%{_datadir}/metainfo/io.crow_translate.CrowTranslate.metainfo.xml

%changelog
* Sat May 14 2022 Carlis <t.me/pacpacpacpac> 2.9.5-3
- 2.9.5 + fix spec and patch
* Mon Mar 28 2022 Carlis <t.me/pacpacpacpac> 2.9.2-1
- 2.9.2
* Wed May 26 2021 Carlis <t.me/pacpacpacpac> 2.8.3-1
- 2.8.3
* Thu Apr 15 2021 Carlis <t.me/pacpacpacpac> 2.8.2-1
- 2.8.2
* Tue Mar 16 2021 Carlis <t.me/pacpacpacpac> 2.8.0-1
- 2.8.0
* Mon Feb 15 2021 Carlis <t.me/pacpacpacpac> 2.7.1-1
- 2.7.1
* Tue Nov 17 2020 Carlis <t.me/pacpacpacpac> 2.6.1-1
- 2.6.1
* Sat Oct 24 2020 Yury Martynov <email@linxon.ru> 2.6.0-1
- Bump to 2.6.0 version.
* Fri Oct 09 2020 Yury Martynov <email@linxon.ru> 2.5.1-1
- Initial packaging.
