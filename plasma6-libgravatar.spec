%define major 6
%define libname %mklibname KPim6Gravatar
%define devname %mklibname KPim6Gravatar -d

Name: plasma6-libgravatar
Version:	24.01.85
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/libgravatar-%{version}.tar.xz
Summary: KDE library for Gravatar support
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(KPim6PimCommon)
BuildRequires: cmake(KF6CalendarCore)
BuildRequires: cmake(KPim6Akonadi)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: boost-devel
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt6-qttools-assistant

%description
KDE library for Gravatar support.

%package -n %{libname}
Summary: KDE library for Gravatar support
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE library for Gravatar support.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1 -n libgravatar-%{version}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libgravatar

%files -f libgravatar.lang
%{_datadir}/qlogging-categories6/libgravatar.categories
%{_datadir}/qlogging-categories6/libgravatar.renamecategories

%files -n %{libname}
%{_libdir}/*.so*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/cmake/*
