%define		zope_subname	CPSSkinsTutorial
Summary:	Tutorial for CPSSkins
Summary(pl):	Samouczek dla CPSSkins
Name:		Zope-%{zope_subname}
Version:	0.2
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://www.medic.chalmers.se/~jmo/CPS/%{zope_subname}%{version}.tgz
# Source0-md5:	3ac2fcee53fcef9f244cb6b06d696a8c
URL:		http://www.medic.chalmers.se/~jmo/CPS/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,postun):	/usr/sbin/installzopeproduct
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	Zope-CPSSkins
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tutorial for CPSSkins.

%description -l pl
Samouczek dla CPSSkins.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af Products/%{zope_subname}/{Extensions,i18n,skins,*.py,version.txt,refresh.txt} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc Products/%{zope_subname}/{INSTALL.TXT,*.doc}
%{_datadir}/%{name}
