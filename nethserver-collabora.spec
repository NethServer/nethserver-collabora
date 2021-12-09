Summary: Nethserver Collabora Online configuration
Name: nethserver-collabora
Version: 0.1.4
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch

Requires: coolwsd CODE-brand >= 21.11
Requires: collaboraoffice-dict-en

BuildRequires: nethserver-devtools

%description
Nethserver Collabora Online configuration

%prep
%setup -q

%build
%{makedocs}
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
%{genfilelist} $RPM_BUILD_ROOT \
> %{name}-%{version}-%{release}-filelist

%post

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING

%changelog
* Mon May 03 2021 Stephane de Labrusse <stephdl@de-labrusse.fr> - 0.1.4-1
- Collabora: Require collaboraoffice6.4-dict-en - NethServer/dev#6501

* Tue Apr 20 2021 Stephane de Labrusse <stephdl@de-labrusse.fr> - 0.1.3-1
- Collabora: Add CODE repository but disabled  - NethServer/dev#6490

* Wed Feb 17 2021 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 0.1.2-1
- Collabora still uses rh-php72 but Nextcloud installs rh-php73 - Bug NethServer/dev#6426

* Fri Jan 24 2020 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 0.1.1-1
- Collabora still uses rh-php71 but Nextcloud installs rh-php72 - Bug NethServer/dev#6035

* Tue Feb 12 2019 Matteo Valentini <matteo.valentini@nethesis.it> - 0.1.0-1
- Collabora Online integration - NethServer/dev#5700

