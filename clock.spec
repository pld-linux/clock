Summary:	A utility for querying and setting system time
Summary(pl):	Narzêdzie do odczytu i ustawiania zegara systemowego
Name:		clock
Version:	1.1
Release:	7
Copyright:	distributable
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	clock-1.1.tar.gz
Patch0:		clock-fix.patch
Patch1:		clock-fix2.patch
ExclusiveArch:	sparc alpha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The clock utility is used to query and set system time.

%description -l pl
Narzêdzie clock s³u¿y do odczytywania i ustawiania zegara systemowego.

%prep 
%setup -q
%patch0 -p1
%patch1 -p1

%build
gcc $RPM_OPT_FLAGS -Wall -o clock clock-$(uname -m).c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/sbin,%{_mandir}/man8}

install -s clock $RPM_BUILD_ROOT/sbin
install clock.8  $RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf %{_mandir}/man8/clock.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/clock

%{_mandir}/man8/clock.8.gz
