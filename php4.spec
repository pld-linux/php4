Summary:	The PHP HTML-embedded scripting language for use with Apache.
Summary(fr):	Le langage de script embarque-HTML PHP pour Apache.
Summary(pl):	Jêzyk skryptowy PHP -- u¿ywany wraz z serwerem Apache.
Name:		php
Version:	4.0b4pl1
Release:	1
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
License:	GPL
Source0:	http://www.php.net/distributions/%{name}-%{version}.tar.gz
Source1:	FAQ.php
Source2:	php.ini
Source3:	zend.gif
Icon:		php4.gif
URL:		http://www.php.net/
BuildRequires:	apache-devel
BuildRequires:	zlib-devel
BuildRequires:	mysql-devel >= 3.22.30-2
BuildRequires:	gd-devel
Requires:	apache >= 1.3.9
Prereq:		/usr/sbin/apxs
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_pkglibdir	%{_libdir}/apache

%description
PHP is an HTML-embedded scripting language.  PHP attempts to make it easy
for developers to write dynamically generated web pages.  PHP also offers
built-in database integration for several commercial and non-commercial
database management systems, so writing a database-enabled web page with
PHP is fairly simple.  The most common use of PHP coding is probably as a
replacement for CGI scripts.  The mod_php module enables the Apache web
server to understand and process the embedded PHP language in web pages.
This package contains PHP version %{version}.  If you use applications which
specifically rely on PHP/FI (PHP v2 and earlier), you should instead install
the PHP/FI module contained in the phpfi package.  If you're just starting
with PHP, you should install this package.  You'll also need to install
the Apache web server.

%description -l fr
PHP est un langage de script embarque dans le HTM. PHP essaye de rendre
simple aux developpeurs d'ecrire des pages web generees dynamiquement.
PHP incorpore egalement une integration avec plusieurs systemes de gestion
de bases de donnees commerciaux et non-connerciaux, qui rent facile
la creation de pages web liees avec des bases de donnees. L'utilisation la
plus commune de PHP est probablement en remplacement de scripts CGI. Le
module mod_php permet au serveur web apache de comprendre et de traiter le
langage PHP integre dans des pages web.
Ce package contient PHP version %{version}. Si vous utilisez des
applications qui utilisent specifiquement PHP/FI, vous devrez installer le
module PHP/FI inclus dans le package mod_php. Si vous debutez avec PHP, vous
devriez installer ce package. Vous aurez egalement besoin d'installer le
serveur web Apache.

%description -l pl
PHP jest jêzykiem skryptowym, którego polecenia umieszcza siê w plikach
HTML.  Pakiet ten zawiera modu³ przeznaczony dla serwera HTTP (jak np.
Apache), który interpretuje te polecenia.  Umo¿liwia to tworzenie
dynamicznie stron WWW.  Spora czê¶æ sk³adni PHP zapo¿yczona zosta³a
z jêzyków: C, Java i Perl.

%package mysql
Summary:	MySQL database module for PHP4
Summary(pl):	Modu³ bazy danych MySQL dla PHP4
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires: 	%{name} = %{version}

%description mysql
This is a dynamic shared object (DSO) for Apache that will add MySQL
database support to PHP4.  If you need back-end support for MySQL,
you should install this package in addition to the main %{name} package.

%package gd
Summary:	GD extension module for PHP4
Summary:	Modu³ GD dla PHP4
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires: 	%{name} = %{version}

%description gd
This is a dynamic shared object (DSO) for Apache that will add GD
support to PHP4.

%description gd -l pl

%prep
%setup -q 

%build
LDFLAGS=""; export LDFLAGS
./buildconf
%configure \
	--with-apxs=%{_sbindir}/apxs \
	--with-config-file-path=%{_sysconfdir}/httpd \
	--enable-safe-mode \
	--with-exec-dir=%{_bindir} \
	--disable-debug \
	--with-zlib \
	--enable-magic-quotes \
	--enable-track-vars \
	--with-gd=shared \
	--with-regex=system \
	--with-gettext \
	--with-mysql=shared \
	--enable-shared 
make


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pkglibdir}/php,%{_sysconfdir}/httpd} \
		$RPM_BUILD_ROOT/home/httpd/html/icons


install .libs/*.so	$RPM_BUILD_ROOT%{_pkglibdir}
install modules/*.so	$RPM_BUILD_ROOT%{_pkglibdir}/php

install %{SOURCE2}		$RPM_BUILD_ROOT%{_sysconfdir}/httpd/php.ini
install %{SOURCE3} php4.gif	$RPM_BUILD_ROOT/home/httpd/html/icons

strip --strip-unneeded	\
	$RPM_BUILD_ROOT%{_pkglibdir}/*.so \
	$RPM_BUILD_ROOT%{_pkglibdir}/php/*.so

install  %{SOURCE1}	.
gzip -9nf CODING_STANDARDS CREDITS FAQ* ChangeLog FUNCTION_LIST.txt \
	MAINTAINERS MODULES_STATUS NEWS TODO*

%post
/usr/sbin/apxs -e -a -n php4 %{_pkglibdir}/libphp4.so 1>&2
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi


%preun
if [ "$1" = "0" ]; then
	/usr/sbin/apxs -e -A -n php4 %{_pkglibdir}/libphp4.so 1>&2
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mysql
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "activating module 'mysql.so' in /etc/httpd/php.ini" 1>&2
	sed -e 's|^;extension=mysql.so|extension=mysql.so|g' \
	%{_sysconfdir}/httpd/php.ini > %{_sysconfdir}/httpd/php.ini.new
	mv %{_sysconfdir}/httpd/php.ini.new %{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%postun mysql
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "deactivating module 'mysql.so' in /etc/httpd/php.ini" 1>&2
	sed -e 's|^extension=mysql.so|;extension=mysql.so|g' \
	%{_sysconfdir}/httpd/php.ini > %{_sysconfdir}/httpd/php.ini.new
	mv %{_sysconfdir}/httpd/php.ini.new %{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%post gd
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "activating module 'gd.so' in /etc/httpd/php.ini" 1>&2
	sed -e 's|^;extension=gd.so|extension=gd.so|g' \
	%{_sysconfdir}/httpd/php.ini > %{_sysconfdir}/httpd/php.ini.new
	mv %{_sysconfdir}/httpd/php.ini.new %{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%postun gd
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "deactivating module 'gd.so' in /etc/httpd/php.ini" 1>&2
	sed -e 's|^extension=gd.so|;extension=gd.so|g' \
	%{_sysconfdir}/httpd/php.ini > %{_sysconfdir}/httpd/php.ini.new
	mv %{_sysconfdir}/httpd/php.ini.new %{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CODING_STANDARDS,CREDITS,FAQ*,ChangeLog,FUNCTION_LIST.txt}.gz
%doc {MAINTAINERS,MODULES_STATUS,NEWS,TODO*}.gz  

%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd/*
%dir %{_pkglibdir}/php

#%attr(755,root,root) %{_libdir}/apache/php/*.so

/home/httpd/html/icons/*

%attr(755,root,root) %{_pkglibdir}/libphp4.so

%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/mysql.so

%files gd
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/gd.so
