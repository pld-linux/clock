Summary: A utility for querying and setting system time.
Name: clock
Version: 1.1
Release: 6
ExclusiveArch: sparc alpha
Copyright: distributable
Group: System Environment/Base
Source: clock-1.1.tar.gz
Patch0: clock-1.1-fix.patch
Patch1: clock-1.1-fix2.patch
BuildRoot: /var/tmp/clockroot

%description
The clock utility is used to query and set system time.

The clock program is a basic system utility and should be installed
on your system.

%prep 
%setup
%patch0 -p1 -b .fix
%patch1 -p1 -b .fix2

%build
gcc $RPM_OPT_FLAGS -Wall -o clock clock-$(uname -m).c

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/sbin
mkdir -p $RPM_BUILD_ROOT/usr/man/man8
install -s -m755 clock $RPM_BUILD_ROOT/sbin
install -m 644 clock.8 $RPM_BUILD_ROOT/usr/man/man8

%files
%attr(-,root,root) /sbin/clock
%attr(-,root,root) /usr/man/man8/clock.8

%clean
rm -rf $RPM_BUILD_ROOT
