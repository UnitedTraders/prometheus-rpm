%define debug_package %{nil}

Name:		prometheus_scollector
Version:	0.1.0
Release:	1%{?dist}
Summary:	Tamás Gulác's Application for collecting metrics from Bosun scollectors and representation to Prometheus server.
Group:		System Environment/Daemons
License:	See the LICENSE file at github.
URL:            https://github.com/gitinsky-bot/prometheus_scollector
Source0:        prometheus_scollector-0.1.0.linux-amd64.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Requires(pre):  /usr/sbin/useradd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
AutoReqProv:	No

%description

Original Tamás Gulácsi'application for collecting metrics from Bosun scollectors and representation to Prometheus server.
Application is builded and tested for CentOS7 and ready for deployment by ansible and work with alot of Bosun scollectors at endpoints.

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
mkdir -vp $RPM_BUILD_ROOT/usr/lib
mkdir -vp $RPM_BUILD_ROOT/usr/lib/systemd
mkdir -vp $RPM_BUILD_ROOT/usr/lib/systemd/system

install -m 644 prometheus_scollector.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/prometheus_scollector
install -m 644 prometheus_scollector.conf $RPM_BUILD_ROOT/etc/prometheus/prometheus_scollector.conf
install -m 755 prometheus_scollector $RPM_BUILD_ROOT/usr/bin/prometheus_scollector
install -m 755 prometheus_scollector.service $RPM_BUILD_ROOT/usr/lib/systemd/system/prometheus_scollector.service

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

%files
%defattr(-,root,root,-)
/usr/bin/prometheus_scollector
/usr/lib/systemd/system/prometheus_scollector.service
%config(noreplace) /etc/sysconfig/prometheus_scollector
%config(noreplace) /etc/prometheus/prometheus_scollector.conf
