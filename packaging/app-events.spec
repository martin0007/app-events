
Name: app-events
Epoch: 1
Version: 2.0.18
Release: 1%{dist}
Summary: Event System - Core
License: LGPLv3
Group: ClearOS/Libraries
Source: app-events-%{version}.tar.gz
Buildarch: noarch

%description
The Event System app provides a way for other apps to listen for events that occur on the system

%package core
Summary: Event System - Core
Requires: app-base-core
Requires: clearsync
Obsoletes: app-clearsync-core

%description core
The Event System app provides a way for other apps to listen for events that occur on the system

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/events
cp -r * %{buildroot}/usr/clearos/apps/events/

install -d -m 0755 %{buildroot}/var/clearos/events
install -D -m 0644 packaging/clearsync.php %{buildroot}/var/clearos/base/daemon/clearsync.php
install -D -m 0755 packaging/trigger %{buildroot}/usr/sbin/trigger

%post core
logger -p local6.notice -t installer 'app-events-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/events/deploy/install ] && /usr/clearos/apps/events/deploy/install
fi

[ -x /usr/clearos/apps/events/deploy/upgrade ] && /usr/clearos/apps/events/deploy/upgrade

exit 0

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-events-core - uninstalling'
    [ -x /usr/clearos/apps/events/deploy/uninstall ] && /usr/clearos/apps/events/deploy/uninstall
fi

exit 0

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/events/packaging
%dir /usr/clearos/apps/events
%dir /var/clearos/events
/usr/clearos/apps/events/deploy
/usr/clearos/apps/events/language
/usr/clearos/apps/events/libraries
/var/clearos/base/daemon/clearsync.php
/usr/sbin/trigger
