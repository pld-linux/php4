#
#   oracle - with oracle support 
#   oci8   - with oci8 support
#	
Summary:	The PHP HTML-embedded scripting language for use with Apache.
Summary(fr):	Le langage de script embarque-HTML PHP pour Apache.
Summary(pl):	Jêzyk skryptowy PHP -- u¿ywany wraz z serwerem Apache.
Name:		php
Version:	4.0.3pl1
Release:	1
Epoch:		1
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
License:	The PHP license (see "LICENSE" file included in distribution)
Source0:	http://www.php.net/distributions/%{name}-%{version}.tar.gz
Source1:	FAQ.%{name}
Source2:	%{name}.ini
Source3:	zend.gif
Source4:	http://www.php.net/distributions/manual.tar.gz
Source5:	http://www.php.net/extra/number4.tar.gz
Patch0:		%{name}-imap.patch
Patch1:		%{name}-mysql-socket.patch
Patch2:		%{name}-mail.patch
Patch3:		%{name}-ldap.patch
Patch4:		%{name}-bcmath.patch
Patch5:		%{name}-no_libnsl.patch
Icon:		php4.gif
URL:		http://www.php.net/
BuildRequires:	apache(EAPI)-devel
BuildRequires:	zip
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	db3-devel >= 3.1.17
BuildRequires:	freetype-devel
BuildRequires:	gd-devel >= 1.8.3
BuildRequires:	gdbm-devel
BuildRequires:	imap-devel >= 4.7b-1
# I think jdk is better for java
# BuildRequires:	jdk
BuildRequires:	kaffe-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	mm-devel >= 1.1.3
BuildRequires:	openldap-devel
BuildRequires:	pam-devel
BuildRequires:	pdflib-devel >= 3.0
#BuildRequires:	libxml-devel >= 2.0.0
BuildRequires:	postgresql-devel
BuildRequires:	recode-devel >= 3.5
BuildRequires:	t1lib-devel
# BuildRequires:	unixODBC-devel
BuildRequires:	zlib-devel >= 1.0.9
BuildRequires:	ucd-snmp-devel >= 4.1
BuildRequires:	libmcrypt-devel >= 2.4.4
BuildRequires:	libltdl-devel
Requires:	apache(EAPI) >= 1.3.9
Prereq:		/usr/sbin/apxs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkglibdir	%{_libdir}/apache

%description
PHP is an HTML-embedded scripting language. PHP attempts to make it
easy for developers to write dynamically generated web pages. PHP also
offers built-in database integration for several commercial and
non-commercial database management systems, so writing a
database-enabled web page with PHP is fairly simple. The most common
use of PHP coding is probably as a replacement for CGI scripts. The
mod_php module enables the Apache web server to understand and process
the embedded PHP language in web pages. This package contains PHP
version %{version}. If you use applications which specifically rely on
PHP/FI (PHP v2 and earlier), you should instead install the PHP/FI
module contained in the phpfi package. If you're just starting with
PHP, you should install this package. You'll also need to install the
Apache web server.

%description -l fr
PHP est un langage de script embarque dans le HTM. PHP essaye de
rendre simple aux developpeurs d'ecrire des pages web generees
dynamiquement. PHP incorpore egalement une integration avec plusieurs
systemes de gestion de bases de donnees commerciaux et
non-connerciaux, qui rent facile la creation de pages web liees avec
des bases de donnees. L'utilisation la plus commune de PHP est
probablement en remplacement de scripts CGI. Le module mod_php permet
au serveur web apache de comprendre et de traiter le langage PHP
integre dans des pages web. Ce package contient PHP version
%{version}. Si vous utilisez des applications qui utilisent
specifiquement PHP/FI, vous devrez installer le module PHP/FI inclus
dans le package mod_php. Si vous debutez avec PHP, vous devriez
installer ce package. Vous aurez egalement besoin d'installer le
serveur web Apache.

%description -l pl
PHP jest jêzykiem skryptowym, którego polecenia umieszcza siê w
plikach HTML. Pakiet ten zawiera modu³ przeznaczony dla serwera HTTP
(jak np. Apache), który interpretuje te polecenia. Umo¿liwia to
tworzenie dynamicznie stron WWW. Spora czê¶æ sk³adni PHP zapo¿yczona
zosta³a z jêzyków: C, Java i Perl.

%package mysql
Summary:	MySQL database module for PHP4
Summary(pl):	Modu³ bazy danych MySQL dla PHP4
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description mysql
This is a dynamic shared object (DSO) for Apache that will add MySQL
database support to PHP4. If you need back-end support for MySQL, you
should install this package in addition to the main %{name} package.

%description mysql -l pl
Modu³ PHP4 umo¿liwiaj±cy dostêp do bazy danych MySQL.


%package pgsql
Summary:	PostgreSQL database module for PHP4
Summary(pl):	Modu³ bazy danych PostgreSQL dla PHP4
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description pgsql
This is a dynamic shared object (DSO) for Apache that will add
PostgreSQL database support to PHP4. If you need back-end support for
PostgreSQL, you should install this package in addition to the main
%{name} package.

%description pgsql -l pl
Modu³ PHP4 umo¿liwiaj±cy dostêp do bazy danych PostgreSQL.

%package oci8
Summary:	Oracle 8 database module for PHP4
Summary(pl):	Modu³ bazy danych Oracle 8 dla PHP4
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}
Autoreq:	false

%description oci8
This is a dynamic shared object (DSO) for Apache that will add Oracle
8 database support to PHP4. If you need back-end support for Oracle 8,
you should install this package in addition to the main %{name}
package.

%description oci8 -l pl
Modu³ PHP4 umo¿liwiaj±cy dostêp do bazy danych Oracle 8. }

%package oracle
Summary:	Oracle 7 database module for PHP4
Summary(pl):	Modu³ bazy danych Oracle 7 dla PHP4
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}
Autoreq:	false

%description oracle
This is a dynamic shared object (DSO) for Apache that will add Oracle
7 database support to PHP4. If you need back-end support for Oracle 7,
you should install this package in addition to the main %{name}
package.

%description oracle -l pl
Modu³ PHP4 umo¿liwiaj±cy dostêp do bazy danych Oracle 7. }

%package gd
Summary:	GD extension module for PHP4
Summary:	Modu³ GD dla PHP4
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description gd
This is a dynamic shared object (DSO) for Apache that will add GD
support to PHP4. You should install this package in addition to the
main %{name} package if you want to create and manipulate images with
PHP.

%description gd -l pl

%package java
Summary:	Java extension module for PHP4
Summary(pl):	Modu³ Javy dla PHP4
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description java
This is a dynamic shared object (DSO) for Apache that will add JAVA
support to PHP4. This extension provides a simple and effective means
for creating and invoking methods on Java objects from PHP.

%description java -l pl

%package xml
Summary:	XML extension module for PHP4
Summary(pl):	Modu³ XML dla PHP4
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description xml
This is a dynamic shared object (DSO) for Apache that will add XML
support to PHP4. This extension lets you create XML parsers and then
define handlers for different XML events. If you want to be able to
parse XML documents you should install this package in addition to the
main %{name} package.

#%description xml -l pl

%package dba
Summary:	DBA extension module for PHP4
Summary(pl):	Modu³ DBA dla PHP4
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description dba
This is a dynamic shared object (DSO) for Apache that will add
flat-file databases (DBA) support to PHP4.

#%description dba -l pl

%package calendar
Summary:	Calendar extension module for PHP4
Summary(pl):	Modu³ funkcji kalendarza dla PHP4
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description calendar
This is a dynamic shared object (DSO) for Apache that will add
calendar support to PHP4.

#%description calendar -l pl

%package dbase
Summary:	DBase extension module for PHP4
Summary(pl):	Modu³ DBase dla PHP4
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description dbase
This is a dynamic shared object (DSO) for Apache that will add DBase
support to PHP4.

#%description dbase -l pl

%package filepro
Summary:	FilePro extension module for PHP4
Summary(pl):	Modu³ FilePro dla PHP4
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description filepro
This is a dynamic shared object (DSO) for Apache that will add FilePro
support to PHP4.

#%description filepro -l pl

%package posix
Summary:	POSIX extension module for PHP4
Summary(pl):	Modu³ POSIX dla PHP4
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description posix
This is a dynamic shared object (DSO) for Apache that will add POSIX
functions support to PHP4.

#%description posix -l pl

%package pcre
Summary:	PCRE extension module for PHP4
Summary(pl):	Modu³ PCRE dla PHP4
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description pcre
This is a dynamic shared object (DSO) for Apache that will add Perl
Compatible Regular Expression support to PHP4.

#%description pcre -l pl

%package sysvsem
Summary:	SysV sem extension module for PHP4
Summary(pl):	Modu³ SysV sem dla PHP4
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description sysvsem
This is a dynamic shared object (DSO) for Apache that will add SysV
semafores support to PHP4.

#%description sysvsem -l pl

%package sysvshm
Summary:	SysV shm extension module for PHP4
Summary(pl):	Modu³ SysV shm dla PHP4
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description sysvshm
This is a dynamic shared object (DSO) for Apache that will add SysV
Shared Memory support to PHP4.

#%description sysvshm -l pl

%package yp
Summary:	NIS (yp) extension module for PHP4
Summary(pl):	Modu³ NIS (yp) dla PHP4
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description yp
This is a dynamic shared object (DSO) for Apache that will add NIS
(Yellow Pages) support to PHP4.

#%description yp -l pl

%package bcmath
Summary:	bcmath extension module for PHP4
Summary(pl):	Modu³ bcmath dla PHP4
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description bcmath
This is a dynamic shared object (DSO) for Apache that will add bc
style precision math functions support to PHP4.

#%description bcmath -l pl

%package ftp
Summary:	FTP extension module for PHP4
Summary(pl):	Modu³ FTP dla PHP4
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description ftp
This is a dynamic shared object (DSO) for Apache that will add FTP
support to PHP4.

#%description ftp -l pl

%package zlib
Summary:	Zlib extension module for PHP4
Summary(pl):	Modu³ zlib dla PHP4
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description zlib
This is a dynamic shared object (DSO) for Apache that will add
commpresion (zlib) support to PHP4.

#%description zlib -l pl

%package exif
Summary:	exifextension module for PHP4
Summary(pl):	Modu³ exif dla PHP4
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description exif
This is a dynamic shared object (DSO) for Apache that will add exif
support to PHP4.

#%description exif -l pl

%package recode
Summary:	recodeextension module for PHP4
Summary(pl):	Modu³ recode dla PHP4
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description recode
This is a dynamic shared object (DSO) for Apache that will add recode
support to PHP4.

#%description recode -l pl

%package session
Summary:	sessionextension module for PHP4
Summary(pl):	Modu³ session dla PHP4
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description session
This is a dynamic shared object (DSO) for Apache that will add session
support to PHP4.

#%description session -l pl

%package gettext
Summary:	gettextextension module for PHP4
Summary(pl):	Modu³ gettext dla PHP4
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description gettext
This is a dynamic shared object (DSO) for Apache that will add gettext
support to PHP4.

#%description gettext -l pl


%package snmp
Summary:	snmpextension module for PHP4
Summary(pl):	Modu³ snmp dla PHP4
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description snmp
This is a dynamic shared object (DSO) for Apache that will add snmp
support to PHP4.

#%description snmp -l pl

%package imap
Summary:	imapextension module for PHP4
Summary(pl):	Modu³ imap dla PHP4
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description imap
This is a dynamic shared object (DSO) for Apache that will add imap
support to PHP4.

#%description imap -l pl

%package ldap
Summary:	LDAP extension module for PHP4
Summary(pl):	Modu³ LDAP dla PHP4
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description ldap
This is a dynamic shared object (DSO) for Apache that will add LDAP
support to PHP4.

#%description ldap -l pl

%package sockets
Summary:	sockets extension module for PHP4
Summary(pl):	Modu³ socket dla PHP4
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description sockets
This is a dynamic shared object (DSO) for Apache that will add sockets
support to PHP4.

#%description sockets -l pl

%package mcrypt
Summary:	mcrypt extension module for PHP4
Summary(pl):	Modu³ mcrypt dla PHP4
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description mcrypt
This is a dynamic shared object (DSO) for Apache that will add mcrypt
support to PHP4.

#%description mcrypt -l pl

%package doc
Summary:	Online manual for PHP4
Summary(pl):	Dokumentacja dla PHP4
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery

%description doc
Comprehensive documentation for PHP4, viewable through your web
server, too!

%description doc -l pl
Dokumentacja dla pakietu PHP4. Mo¿na j± równie¿ ogl±daæ poprzez serwer
WWW.

%prep
%setup  -q -a 5
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
CFLAGS="$RPM_OPT_FLAGS -DEAPI -I%{_prefix}/X11R6/include"; export CFLAGS
./buildconf
%configure \
	--with-apxs=%{_sbindir}/apxs \
	--with-config-file-path=%{_sysconfdir}/httpd \
	--with-exec-dir=%{_bindir} \
	--disable-debug \
	--enable-magic-quotes \
	--enable-shared \
	--enable-track-vars \
	--enable-safe-mode \
	--enable-trans-sid \
	--enable-sysvsem=shared \
	--enable-sysvshm=shared \
	--enable-session \
	--enable-exif=shared \
	--with-regex=system \
	--with-gettext=shared \
	--with-ldap=shared \
	--with-mysql=shared \
	--with-mysql-sock=/var/lib/mysql/mysql.sock \
	--with-gd=shared \
	--with-dbase=shared \
	--with-filepro=shared \
	--enable-ftp=shared \
	--with-hyperwave \
	--with-pdflib=shared \
	--with-cpdflib=shared \
	--with-java \
	--with-pgsql=shared,/usr \
	--with-imap=shared \
	--enable-bcmath=shared \
	--enable-calendar=shared \
	--with-mm \
	--with-pcre-regex=shared \
	--enable-posix=shared \
	--with-ttf \
	--with-t1lib \
	--with-recode=shared \
	--enable-ucd-snmp-hack \
	--enable-dba=shared \
	--with-snmp=shared \
	--with-openssl \
	--with-gdbm \
	--with-db3 \
	--enable-yp=shared \
	--with-xml=shared \
	--enable-xml=shared \
	--with-zlib=shared \
	--with-mcrypt=shared \
	--enable-sockets=shared \
	%{?oracle:--with-oracle=shared} \
	%{?oci8:--with-oci8=shared} \
	--without-db2 



# TODO --with-pspell=/usr,shared (pspell missing)
#	--with-unixODBC=shared (nie jest shared)
#	--with-mhash=shared (brak libmhash)
#	--with-curl=shared (brak libcurl)

#	--with-db3 \

# snmp won

#Syntax error on line 228 of %{_sysconfdir}/httpd/httpd.conf: Cannot load %{_libdir}/apache/libphp4.so into server: %{_libdir}/apache/libphp4.so: undefined symbol: phpi_get_le_gd
# Solution: make pdf and cpdf shared
#	--with-gd=shared \

#	--with-unixODBC \

# This option get trouble with imap
#	--enable-versioning \

# To old/new libmcrypt ?
#	--with-mcrypt=shared \
# --with-dom=%{_prefix}/X11R6 \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pkglibdir}/php,%{_sysconfdir}/httpd} \
		$RPM_BUILD_ROOT/home/httpd/html/{icons,docs,docs/php4-doc}

install .libs/*.so	$RPM_BUILD_ROOT%{_pkglibdir}
install modules/*.so	$RPM_BUILD_ROOT%{_pkglibdir}/php

install %{SOURCE2}		$RPM_BUILD_ROOT%{_sysconfdir}/httpd/php.ini
install %{SOURCE3} php4.gif	$RPM_BUILD_ROOT/home/httpd/html/icons

cd $RPM_BUILD_ROOT/home/httpd/html/docs/php4-doc
tar zxf %{SOURCE4}
ln -s manual.html index.html
cd -

install %{SOURCE1} .
gzip -9nf CODING_STANDARDS CREDITS FUNCTION_LIST.txt \
      EXTENSIONS NEWS TODO* LICENSE Zend/LICENSE \
      Zend/ZEND_CHANGES README.SELF-CONTAINED-EXTENSIONS README.EXT_SKEL

%post
/usr/sbin/apxs -e -a -n php4 %{_pkglibdir}/libphp4.so 1>&2
perl -pi -e 's|^#AddType application/x-httpd-php .php|AddType application/x-httpd-php .php|'
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%postun
perl -pi -e 's|^AddType application/x-httpd-php .php|#AddType application/x-httpd-php .php|'
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
	perl -pi -e 's|^;extension=mysql.so|extension=mysql.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun mysql
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/httpd/php.ini ]; then
		echo "deactivating module 'mysql.so' in /etc/httpd/php.ini" 1>&2
		perl -pi -e 's|^extension=mysql.so|;extension=mysql.so|g' \
		%{_sysconfdir}/httpd/php.ini
	fi
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post pgsql
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "activating module 'pgsql.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^;extension=pgsql.so|extension=pgsql.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun pgsql
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/httpd/php.ini ]; then
		echo "deactivating module 'pgsql.so' in /etc/httpd/php.ini" 1>&2
		perl -pi -e 's|^extension=pgsql.so|;extension=pgsql.so|g' \
		%{_sysconfdir}/httpd/php.ini
	fi
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%{?oracle:%post oracle}
%{?oracle:if [ -f %{_sysconfdir}/httpd/php.ini ]; then}
%{?oracle:	echo "activating module 'oracle.so' in /etc/httpd/php.ini" 1>&2}
%{?oracle:	perl -pi -e 's|^;extension=oracle.so|extension=oracle.so|g' %{_sysconfdir}/httpd/php.ini}
%{?oracle:fi}
%{?oracle:if [ -f /var/lock/subsys/httpd ]; then}
%{?oracle:	/etc/rc.d/init.d/httpd restart 1>&2}
%{?oracle:fi}

%{?oracle:%preun oracle}
%{?oracle:if [ "$1" = "0" ]; then}
%{?oracle:	if [ -f %{_sysconfdir}/httpd/php.ini ]; then}
%{?oracle:		echo "deactivating module 'oracle.so' in /etc/httpd/php.ini" 1>&2}
%{?oracle:		perl -pi -e 's|^extension=oracle.so|;extension=oracle.so|g' {_sysconfdir}/httpd/php.ini}
%{?oracle:	fi}
%{?oracle:	if [ -f /var/lock/subsys/httpd ]; then}
%{?oracle:		/etc/rc.d/init.d/httpd restart 1>&2}
%{?oracle:	fi}
%{?oracle:fi}

%{?oci8:%post oci8}
%{?oci8:if [ -f %{_sysconfdir}/httpd/php.ini ]; then}
%{?oci8:	echo "activating module 'oci8.so' in /etc/httpd/php.ini" 1>&2}
%{?oci8:	perl -pi -e 's|^;extension=oci8.so|extension=oci8.so|g' %{_sysconfdir}/httpd/php.ini}
%{?oci8:fi}
%{?oci8:if [ -f /var/lock/subsys/httpd ]; then}
%{?oci8:	/etc/rc.d/init.d/httpd restart 1>&2}
%{?oci8:fi}

%{?oci8:%preun oci8}
%{?oci8:if [ "$1" = "0" ]; then}
%{?oci8:	if [ -f %{_sysconfdir}/httpd/php.ini ]; then}
%{?oci8:		echo "deactivating module 'oci8.so' in /etc/httpd/php.ini" 1>&2}
%{?oci8:		perl -pi -e 's|^extension=oci8.so|;extension=oci8.so|g' %{_sysconfdir}/httpd/php.ini}
%{?oci8:	fi}
%{?oci8:	if [ -f /var/lock/subsys/httpd ]; then}
%{?oci8:		/etc/rc.d/init.d/httpd restart 1>&2}
%{?oci8:	fi}
%{?oci8:fi}

%post gd
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "activating module 'gd.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^;extension=gd.so|extension=gd.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun gd
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/httpd/php.ini ]; then
		echo "deactivating module 'gd.so' in /etc/httpd/php.ini" 1>&2
		perl -pi -e 's|^extension=gd.so|;extension=gd.so|g' \
		%{_sysconfdir}/httpd/php.ini
	fi
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post xml
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "activating module 'xml.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^;extension=xml.so|extension=xml.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun xml
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/httpd/php.ini ]; then
		echo "deactivating module 'xml.so' in /etc/httpd/php.ini" 1>&2
		perl -pi -e 's|^extension=xml.so|;extension=xml.so|g' \
		%{_sysconfdir}/httpd/php.ini
	fi
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post dba
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "activating module 'dba.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^;extension=dba.so|extension=dba.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun dba
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/httpd/php.ini ]; then
		echo "deactivating module 'dba.so' in /etc/httpd/php.ini" 1>&2
		perl -pi -e 's|^extension=dba.so|;extension=dba.so|g' \
		%{_sysconfdir}/httpd/php.ini
	fi
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post calendar
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "activating module 'calendar.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^;extension=calendar.so|extension=calendar.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun calendar
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/httpd/php.ini ]; then
		echo "deactivating module 'calendar.so' in /etc/httpd/php.ini" 1>&2
		perl -pi -e 's|^extension=calendar.so|;extension=calendar.so|g' \
		%{_sysconfdir}/httpd/php.ini
	fi
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post dbase
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "activating module 'dbase.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^;extension=dbase.so|extension=dbase.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun dbase
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/httpd/php.ini ]; then
		echo "deactivating module 'dbase.so' in /etc/httpd/php.ini" 1>&2
		perl -pi -e 's|^extension=dbase.so|;extension=dbase.so|g' \
		%{_sysconfdir}/httpd/php.ini
	fi
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi


%post java
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "activating module 'libphp_java.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^;extension=libphp_java.so|extension=libphp_java.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun java
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/httpd/php.ini ]; then
		echo "deactivating module 'libphp_java.so' in /etc/httpd/php.ini" 1>&2
		perl -pi -e 's|^extension=libphp_java.so|;extension=libphp_java.so|g' \
		%{_sysconfdir}/httpd/php.ini
	fi
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post filepro
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "activating module 'filepro.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^;extension=filepro.so|extension=filepro.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun filepro
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/httpd/php.ini ]; then
		echo "deactivating module 'filepro.so' in /etc/httpd/php.ini" 1>&2
		perl -pi -e 's|^extension=filepro.so|;extension=filepro.so|g' \
		%{_sysconfdir}/httpd/php.ini
	fi
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post pcre
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "activating module 'pcre.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^;extension=pcre.so|extension=pcre.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun pcre
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/httpd/php.ini ]; then
		echo "deactivating module 'pcre.so' in /etc/httpd/php.ini" 1>&2
		perl -pi -e 's|^extension=pcre.so|;extension=pcre.so|g' \
		%{_sysconfdir}/httpd/php.ini
	fi
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post posix
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "activating module 'posix.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^;extension=posix.so|extension=posix.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun posix
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/httpd/php.ini ]; then
		echo "deactivating module 'posix.so' in /etc/httpd/php.ini" 1>&2
		perl -pi -e 's|^extension=posix.so|;extension=posix.so|g' \
		%{_sysconfdir}/httpd/php.ini
	fi
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post sysvsem
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "activating module 'sysvsem.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^;extension=sysvsem.so|extension=sysvsem.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun sysvsem
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/httpd/php.ini ]; then
		echo "deactivating module 'sysvsem.so' in /etc/httpd/php.ini" 1>&2
		perl -pi -e 's|^extension=sysvsem.so|;extension=sysvsem.so|g' \
		%{_sysconfdir}/httpd/php.ini
	fi
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post sysvshm
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "activating module 'sysvshm.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^;extension=sysvshm.so|extension=sysvshm.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun sysvshm
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/httpd/php.ini ]; then
		echo "deactivating module 'sysvshm.so' in /etc/httpd/php.ini" 1>&2
		perl -pi -e 's|^extension=sysvshm.so|;extension=sysvshm.so|g' \
		%{_sysconfdir}/httpd/php.ini
	fi
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post yp
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "activating module 'yp.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^;extension=yp.so|extension=yp.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun yp
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/httpd/php.ini ]; then
		echo "deactivating module 'yp.so' in /etc/httpd/php.ini" 1>&2
		perl -pi -e 's|^extension=yp.so|;extension=yp.so|g' \
		%{_sysconfdir}/httpd/php.ini
	fi
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post ftp
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "activating module 'ftp.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^;extension=ftp.so|extension=ftp.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun ftp
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/httpd/php.ini ]; then
		echo "deactivating module 'ftp.so' in /etc/httpd/php.ini" 1>&2
		perl -pi -e 's|^extension=ftp.so|;extension=ftp.so|g' \
		%{_sysconfdir}/httpd/php.ini
	fi
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post zlib
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "activating module 'zlib.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^;extension=zlib.so|extension=zlib.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun zlib
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/httpd/php.ini ]; then
		echo "deactivating module 'zlib.so' in /etc/httpd/php.ini" 1>&2
		perl -pi -e 's|^extension=zlib.so|;extension=zlib.so|g' \
		%{_sysconfdir}/httpd/php.ini
	fi
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post bcmath
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "activating module 'bcmath.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^;extension=bcmath.so|extension=bcmath.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun bcmath
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/httpd/php.ini ]; then
		echo "deactivating module 'bcmath.so' in /etc/httpd/php.ini" 1>&2
		perl -pi -e 's|^extension=bcmath.so|;extension=bcmath.so|g' \
		%{_sysconfdir}/httpd/php.ini
	fi
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi	
fi

%post exif
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "activating module 'exif.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^;extension=exif.so|extension=exif.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun exif
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/httpd/php.ini ]; then
		echo "deactivating module 'exif.so' in /etc/httpd/php.ini" 1>&2
		perl -pi -e 's|^extension=exif.so|;extension=exif.so|g' \
		%{_sysconfdir}/httpd/php.ini
	fi
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post recode
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "activating module 'recode.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^;extension=recode.so|extension=recode.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun recode
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/httpd/php.ini ]; then
		echo "deactivating module 'recode.so' in /etc/httpd/php.ini" 1>&2
		perl -pi -e 's|^extension=recode.so|;extension=recode.so|g' \
		%{_sysconfdir}/httpd/php.ini
	fi
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

#%post session
#if [ -f %{_sysconfdir}/httpd/php.ini ]; then
#	echo "activating module 'session.so' in /etc/httpd/php.ini" 1>&2
#	perl -pi -e 's|^;extension=session.so|extension=session.so|g' \
#	%{_sysconfdir}/httpd/php.ini
#fi
#if [ -f /var/lock/subsys/httpd ]; then
#	/etc/rc.d/init.d/httpd restart 1>&2
#fi
#
#%preun session
#if [ "$1" = "0" ]; then
#if [ -f %{_sysconfdir}/httpd/php.ini ]; then
#	echo "deactivating module 'session.so' in /etc/httpd/php.ini" 1>&2
#	perl -pi -e 's|^extension=session.so|;extension=session.so|g' \
#	%{_sysconfdir}/httpd/php.ini
#fi
#if [ -f /var/lock/subsys/httpd ]; then
#	/etc/rc.d/init.d/httpd restart 1>&2
#fi
#fi

%post gettext
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "activating module 'gettext.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^;extension=gettext.so|extension=gettext.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun gettext
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/httpd/php.ini ]; then
		echo "deactivating module 'gettext.so' in /etc/httpd/php.ini" 1>&2
		perl -pi -e 's|^extension=gettext.so|;extension=gettext.so|g' \
		%{_sysconfdir}/httpd/php.ini
	fi
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post snmp
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "activating module 'snmp.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^;extension=snmp.so|extension=snmp.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun snmp
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/httpd/php.ini ]; then
		echo "deactivating module 'snmp.so' in /etc/httpd/php.ini" 1>&2
		perl -pi -e 's|^extension=snmp.so|;extension=snmp.so|g' \
		%{_sysconfdir}/httpd/php.ini
	fi
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post imap
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "activating module 'imap.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^;extension=imap.so|extension=imap.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun imap
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/httpd/php.ini ]; then
		echo "deactivating module 'imap.so' in /etc/httpd/php.ini" 1>&2
		perl -pi -e 's|^extension=imap.so|;extension=imap.so|g' \
		%{_sysconfdir}/httpd/php.ini
	fi
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post ldap
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "activating module 'ldap.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^;extension=ldap.so|extension=ldap.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun ldap
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/httpd/php.ini ]; then
		echo "deactivating module 'ldap.so' in /etc/httpd/php.ini" 1>&2
		perl -pi -e 's|^extension=ldap.so|;extension=ldap.so|g' \
		%{_sysconfdir}/httpd/php.ini
	fi
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post sockets
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "activating module 'sockets.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^;extension=sockets.so|extension=sockets.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun sockets
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/httpd/php.ini ]; then
		echo "deactivating module 'sockets.so' in /etc/httpd/php.ini" 1>&2
		perl -pi -e 's|^extension=sockets.so|;extension=sockets.so|g' \
		%{_sysconfdir}/httpd/php.ini
	fi
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mcrypt
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "activating module 'mcrypt.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^;extension=mcrypt.so|extension=mcrypt.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun mcrypt
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/httpd/php.ini ]; then
		echo "deactivating module 'mcrypt.so' in /etc/httpd/php.ini" 1>&2
		perl -pi -e 's|^extension=mcrypt.so|;extension=mcrypt.so|g' \
		%{_sysconfdir}/httpd/php.ini
	fi
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CODING_STANDARDS,CREDITS,FUNCTION_LIST.txt,Zend/ZEND_CHANGES}.gz
%doc {LICENSE,Zend/LICENSE,EXTENSIONS,NEWS,TODO*}.gz  
%doc {README.EXT_SKEL,README.SELF-CONTAINED-EXTENSIONS}.gz

%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd/*
%dir %{_pkglibdir}/php

#%attr(755,root,root) %{_libdir}/apache/php/*.so

/home/httpd/html/icons/*

%attr(755,root,root) %{_pkglibdir}/libphp4.so

%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/mysql.so

%files pgsql
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/pgsql.so

%{?oracle:%files oracle}
%{?oracle:%defattr(644,root,root,755)}
%{?oracle:%attr(755,root,root) %{_pkglibdir}/php/oracle.so}

%{?oci8:%files oci8}
%{?oci8:%defattr(644,root,root,755)}
%{?oci8:%attr(755,root,root) %{_pkglibdir}/php/oci8.so}

%files gd
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/gd.so

%files xml
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/xml.so

%files dba
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/dba.so

%files dbase
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/dbase.so

%files filepro
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/filepro.so

%files pcre
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/pcre.so

%files posix
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/posix.so

%files sysvsem
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/sysvsem.so

%files sysvshm
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/sysvshm.so

%files yp
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/yp.so

%files calendar
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/calendar.so

%files bcmath
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/bcmath.so

%files ftp
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/ftp.so

%files zlib
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/zlib.so

%files exif
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/exif.so

%files recode
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/recode.so

#%files session
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_pkglibdir}/php/session.so

%files gettext
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/gettext.so

%files imap
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/imap.so

%files snmp
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/snmp.so

%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/libphp_java.so

%files ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/ldap.so

%files sockets
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/sockets.so

%files mcrypt
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/mcrypt.so

%files doc
%defattr(644,root,root,755)
/home/httpd/html/docs/php4-doc
