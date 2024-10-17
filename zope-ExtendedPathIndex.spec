%define Product ExtendedPathIndex
%define product extendedpathindex
%define name    zope-%{Product}
%define version 2.4
%define release %mkrel 7

%define zope_minver     2.7
%define zope_home       %{_prefix}/lib/zope
%define software_home   %{zope_home}/lib/python

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    ExtendedPathIndex
License:    GPL
Group:      System/Servers
URL:        https://plone.org/products/%{product}
Source:     http://plone.org/products/%{product}/releases/%{version}/%{Product}-%{version}.tar.bz2
Requires:   zope >= %{zope_minver}
Requires:   zope-Archetypes
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}


%description
 This is an index that supports depth limiting, and the ability to build a
structure usable for navtrees and sitemaps. The actual navtree implementations
are not (and should not) be in this Product, this is the index implementation
only.



%prep
%setup -c -q

rm -rf `find -type d -name .svn`

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a * %{buildroot}%{software_home}/Products/


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%files
%defattr(-,root,root)
%{software_home}/Products/*
