# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       kde5-baloo

# >> macros
# << macros

Summary:    Library for indexing and search
Version:    4.97.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  kde5-baloo.yaml
Source101:  kde5-baloo-rpmlintrc
Requires:   kde5-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  kde5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-umbrella
BuildRequires:  kde5-kfilemetadata-devel
BuildRequires:  libxapian-devel
BuildRequires:  kf5-kidletime-devel
BuildRequires:  kf5-kcmutils-devel
BuildRequires:  kf5-krunner-devel

%description
Library for indexing and search


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
%kde5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kde5_make_install
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_kde5_libdir}/*.so.*
%{_kde5_plugindir}/*
%{_kde5_bindir}/*
%{_kde5_sysconfdir}/xdg/autostart/baloo_file.desktop
%{_kde5_sysconfdir}/dbus-1/system.d/org.kde.baloo.filewatch.conf
%{_kde5_libexecdir}/kde_baloo_filewatch_raiselimit
%{_kde5_datadir}/dbus-1/system-services/org.kde.baloo.filewatch.service
%{_kde5_datadir}/kservicetypes5
%{_kde5_datadir}/kservices5
%{_kde5_datadir}/polkit-1/actions/org.kde.baloo.filewatch.policy
%{_kde5_datadir}/icons/hicolor/*/apps/baloo.png
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_kde5_libdir}/*.so
%{_kde5_libdir}/cmake/Baloo
%{_includedir}/baloo
%{_kde5_datadir}/dbus-1/interfaces
# >> files devel
# << files devel
