%define debug_package %{nil}

Name:		alertmanager
Version:	0.3.0
Release:	1%{?dist}
Summary:	The Alertmanager handles alerts sent by client applications such as the Prometheus server.
Group:		System Environment/Daemons
License:	See the LICENSE file at github.
URL:		https://github.com/prometheus/alertmanager
Source0:	https://github.com/prometheus/alertmanager/releases/download/%{version}/alertmanager-%{version}.linux-amd64.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Requires(pre):  /usr/sbin/useradd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
AutoReqProv:	No

%description

The Alertmanager handles alerts sent by client applications such as the Prometheus server.
It takes care of deduplicating, grouping, and routing them to the correct receiver integration such as email, PagerDuty, or OpsGenie.
It also takes care of silencing and inhibition of alerts.

%prep
%setup -q -n %{name}-%{version}.linux-amd64

%build
echo

%install
mkdir -vp $RPM_BUILD_ROOT/usr/bin
mkdir -vp $RPM_BUILD_ROOT/etc/sysconfig
mkdir -vp $RPM_BUILD_ROOT/var/log/prometheus/
mkdir -vp $RPM_BUILD_ROOT/var/run/prometheus
mkdir -vp $RPM_BUILD_ROOT/var/lib/prometheus
mkdir -vp $RPM_BUILD_ROOT/etc/prometheus
mkdir -vp $RPM_BUILD_ROOT/etc/prometheus/alertmanager
mkdir -vp $RPM_BUILD_ROOT/usr/lib
mkdir -vp $RPM_BUILD_ROOT/usr/lib/systemd
mkdir -vp $RPM_BUILD_ROOT/usr/lib/systemd/system
mkdir -vp $RPM_BUILD_ROOT/var/lib/alertmanager

install -m 644 contrib/alertmanager.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/alertmanager
install -m 644 contrib/alertmanager.yaml $RPM_BUILD_ROOT/etc/prometheus/alertmanager/alertmanager.yaml
install -m 755 alertmanager $RPM_BUILD_ROOT/usr/bin/alertmanager
install -m 755 contrib/alertmanager.service $RPM_BUILD_ROOT/usr/lib/systemd/system/alertmanager.service

%clean

%pre
getent group prometheus >/dev/null || groupadd -r prometheus
getent passwd prometheus >/dev/null || \
  useradd -r -g prometheus -s /sbin/nologin \
    -d $RPM_BUILD_ROOT/var/lib/prometheus/ -c "prometheus Daemons" prometheus
exit 0

%post
chgrp prometheus /var/run/prometheus
chmod 774 /var/run/prometheus
chown prometheus:prometheus /var/log/prometheus
chmod 744 /var/log/prometheus
chown prometheus:prometheus /var/lib/alertmanager
chmod 744 /var/lib/alertmanager

%files
%defattr(-,root,root,-)
/usr/bin/alertmanager
/usr/lib/systemd/system/alertmanager.service
%attr(755, prometheus, prometheus)/var/lib/alertmanager
%config(noreplace) /etc/sysconfig/alertmanager
%config(noreplace) /etc/prometheus/alertmanager/alertmanager.yaml
