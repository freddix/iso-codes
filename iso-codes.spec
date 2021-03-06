Summary:	List of country and language names
Name:		iso-codes
Version:	3.49
Release:	2
License:	LGPL
Group:		Applications/Text
Source0:	http://ftp.debian.org/debian/pool/main/i/iso-codes/%{name}_%{version}.orig.tar.xz
# Source0-md5:	a0708a81f42c538f4670e3bf3d343dd8
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package aims to provide the list of the country and language (and
currency) names in one place, rather than repeated in many programs.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/{haw,kok,tt@iqtelif}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{_datadir}/xml/iso-codes
%{_npkgconfigdir}/iso-codes.pc

