#
#   oracle - with oracle support 
#   oci8   - with oci8 support
#	
Summary:	The PHP HTML-embedded scripting language for use with Apache
Summary(fr):	Le langage de script embarque-HTML PHP pour Apache
Summary(pl):	Jêzyk skryptowy PHP -- u¿ywany wraz z serwerem Apache
Name:		php
Version:	4.0.4
Release:	2
Epoch:		1
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
License:	The PHP license (see "LICENSE" file included in distribution)
Source0:	http://www.php.net/distributions/%{name}-%{version}.tar.gz
Source1:	FAQ.php
Source2:	%{name}.ini
Source3:	zend.gif
Source4:	http://www.php.net/distributions/manual.tar.gz
Source5:	php-module-install
Patch0:		%{name}-imap.patch
Patch1:		%{name}-mysql-socket.patch
Patch2:		%{name}-mail.patch
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
%{?bcond_on_java:BuildRequires:	kaffe-devel}
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	mm-devel >= 1.1.3
%{!?bcond_off_ldap:BuildRequires: openldap-devel >= 2.0}
BuildRequires:	pam-devel
BuildRequires:	pdflib-devel >= 3.0
#BuildRequires:	libxml-devel >= 2.0.0
BuildRequires:	postgresql-devel
BuildRequires:	recode-devel >= 3.5
BuildRequires:	t1lib-devel
BuildRequires:	unixODBC-devel
BuildRequires:	zlib-devel >= 1.0.9
BuildRequires:	ucd-snmp-devel >= 4.1
BuildRequires:	libmcrypt-devel >= 2.4.4
BuildRequires:	mhash-devel
BuildRequires:	libltdl-devel
BuildRequires:	bzip2-devel
BuildRequires:	gmp-devel
BuildRequires:	curl-devel
%if %(expr %{?bcond_on_openssl:1}%{!?bcond_on_openssl:0} + %{!?bcond_off_ldap:1}%{?bcond_off_ldap:0})
BuildRequires:	openssl-devel >= 0.9.6
%endif
Requires:	apache(EAPI) >= 1.3.9
Prereq:		perl
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
Summary:	MySQL database module for PHP
Summary(pl):	Modu³ bazy danych MySQL dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}

%description mysql
This is a dynamic shared object (DSO) for Apache that will add MySQL
database support to PHP. If you need back-end support for MySQL, you
should install this package in addition to the main %{name} package.

%description mysql -l pl
Modu³ PHP umo¿liwiaj±cy dostêp do bazy danych MySQL.


%package pgsql
Summary:	PostgreSQL database module for PHP
Summary(pl):	Modu³ bazy danych PostgreSQL dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}

%description pgsql
This is a dynamic shared object (DSO) for Apache that will add
PostgreSQL database support to PHP. If you need back-end support for
PostgreSQL, you should install this package in addition to the main
%{name} package.

%description pgsql -l pl
Modu³ PHP umo¿liwiaj±cy dostêp do bazy danych PostgreSQL.

%package oci8
Summary:	Oracle 8 database module for PHP
Summary(pl):	Modu³ bazy danych Oracle 8 dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}
Autoreq:	false

%description oci8
This is a dynamic shared object (DSO) for Apache that will add Oracle
8 database support to PHP. If you need back-end support for Oracle 8,
you should install this package in addition to the main %{name}
package.

%description oci8 -l pl
Modu³ PHP umo¿liwiaj±cy dostêp do bazy danych Oracle 8. }

%package oracle
Summary:	Oracle 7 database module for PHP
Summary(pl):	Modu³ bazy danych Oracle 7 dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}
Autoreq:	false

%description oracle
This is a dynamic shared object (DSO) for Apache that will add Oracle
7 database support to PHP. If you need back-end support for Oracle 7,
you should install this package in addition to the main %{name}
package.

%description oracle -l pl
Modu³ PHP umo¿liwiaj±cy dostêp do bazy danych Oracle 7. }

%package gd
Summary:	GD extension module for PHP
Summary:	Modu³ GD dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}

%description gd
This is a dynamic shared object (DSO) for Apache that will add GD
support to PHP. You should install this package in addition to the
main %{name} package if you want to create and manipulate images with
PHP.

%description gd -l pl

%if %{?bcond_on_java:1}%{!?bcond_on_java:0}
%package java
Summary:	Java extension module for PHP
Summary(pl):	Modu³ Javy dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}

%description java
This is a dynamic shared object (DSO) for Apache that will add JAVA
support to PHP. This extension provides a simple and effective means
for creating and invoking methods on Java objects from PHP.

%description java -l pl
%endif

%package xml
Summary:	XML extension module for PHP
Summary(pl):	Modu³ XML dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}

%description xml
This is a dynamic shared object (DSO) for Apache that will add XML
support to PHP. This extension lets you create XML parsers and then
define handlers for different XML events. If you want to be able to
parse XML documents you should install this package in addition to the
main %{name} package.

#%description xml -l pl

%package dba
Summary:	DBA extension module for PHP
Summary(pl):	Modu³ DBA dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}

%description dba
This is a dynamic shared object (DSO) for Apache that will add
flat-file databases (DBA) support to PHP.

#%description dba -l pl

%package odbc
Summary:	ODBC extension module for PHP
Summary(pl):	Modu³ ODBC dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}

%description odbc
This is a dynamic shared object (DSO) for Apache that will add
ODBC support to PHP.

#%description odbc -l pl

%package calendar
Summary:	Calendar extension module for PHP
Summary(pl):	Modu³ funkcji kalendarza dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}

%description calendar
This is a dynamic shared object (DSO) for Apache that will add
calendar support to PHP.

#%description calendar -l pl

%package dbase
Summary:	DBase extension module for PHP
Summary(pl):	Modu³ DBase dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}

%description dbase
This is a dynamic shared object (DSO) for Apache that will add DBase
support to PHP.

#%description dbase -l pl

%package filepro
Summary:	FilePro extension module for PHP
Summary(pl):	Modu³ FilePro dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}

%description filepro
This is a dynamic shared object (DSO) for Apache that will add FilePro
support to PHP.

#%description filepro -l pl

%package posix
Summary:	POSIX extension module for PHP
Summary(pl):	Modu³ POSIX dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}

%description posix
This is a dynamic shared object (DSO) for Apache that will add POSIX
functions support to PHP.

#%description posix -l pl

%package pcre
Summary:	PCRE extension module for PHP
Summary(pl):	Modu³ PCRE dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}

%description pcre
This is a dynamic shared object (DSO) for Apache that will add Perl
Compatible Regular Expression support to PHP.

#%description pcre -l pl

%package sysvsem
Summary:	SysV sem extension module for PHP
Summary(pl):	Modu³ SysV sem dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}

%description sysvsem
This is a dynamic shared object (DSO) for Apache that will add SysV
semafores support to PHP.

#%description sysvsem -l pl

%package sysvshm
Summary:	SysV shm extension module for PHP
Summary(pl):	Modu³ SysV shm dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}

%description sysvshm
This is a dynamic shared object (DSO) for Apache that will add SysV
Shared Memory support to PHP.

#%description sysvshm -l pl

%package yp
Summary:	NIS (yp) extension module for PHP
Summary(pl):	Modu³ NIS (yp) dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}

%description yp
This is a dynamic shared object (DSO) for Apache that will add NIS
(Yellow Pages) support to PHP.

#%description yp -l pl

%package bcmath
Summary:	bcmath extension module for PHP
Summary(pl):	Modu³ bcmath dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}

%description bcmath
This is a dynamic shared object (DSO) for Apache that will add bc
style precision math functions support to PHP.

#%description bcmath -l pl

%package ftp
Summary:	FTP extension module for PHP
Summary(pl):	Modu³ FTP dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}

%description ftp
This is a dynamic shared object (DSO) for Apache that will add FTP
support to PHP.

#%description ftp -l pl

%package zlib
Summary:	Zlib extension module for PHP
Summary(pl):	Modu³ zlib dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}

%description zlib
This is a dynamic shared object (DSO) for Apache that will add
commpresion (zlib) support to PHP.

#%description zlib -l pl

%package exif
Summary:	exifextension module for PHP
Summary(pl):	Modu³ exif dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}

%description exif
This is a dynamic shared object (DSO) for Apache that will add exif
support to PHP.

#%description exif -l pl

%package recode
Summary:	recodeextension module for PHP
Summary(pl):	Modu³ recode dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}

%description recode
This is a dynamic shared object (DSO) for Apache that will add recode
support to PHP.

#%description recode -l pl

%package session
Summary:	sessionextension module for PHP
Summary(pl):	Modu³ session dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}

%description session
This is a dynamic shared object (DSO) for Apache that will add session
support to PHP.

#%description session -l pl

%package gettext
Summary:	gettextextension module for PHP
Summary(pl):	Modu³ gettext dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}

%description gettext
This is a dynamic shared object (DSO) for Apache that will add gettext
support to PHP.

#%description gettext -l pl


%package snmp
Summary:	snmpextension module for PHP
Summary(pl):	Modu³ snmp dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}

%description snmp
This is a dynamic shared object (DSO) for Apache that will add snmp
support to PHP.

#%description snmp -l pl

%package imap
Summary:	imapextension module for PHP
Summary(pl):	Modu³ imap dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}

%description imap
This is a dynamic shared object (DSO) for Apache that will add imap
support to PHP.

#%description imap -l pl

%package ldap
Summary:	LDAP extension module for PHP
Summary(pl):	Modu³ LDAP dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}

%description ldap
This is a dynamic shared object (DSO) for Apache that will add LDAP
support to PHP.

#%description ldap -l pl

%package sockets
Summary:	sockets extension module for PHP
Summary(pl):	Modu³ socket dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}

%description sockets
This is a dynamic shared object (DSO) for Apache that will add sockets
support to PHP.

#%description sockets -l pl

%package mcrypt
Summary:	mcrypt extension module for PHP
Summary(pl):	Modu³ mcrypt dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}

%description mcrypt
This is a dynamic shared object (DSO) for Apache that will add mcrypt
support to PHP.

#%description mcrypt -l pl

%package mhash
Summary:	mhash extension module for PHP
Summary(pl):	Modu³ mhash dla PHP
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:	%{name} = %{version}

%description mhash
This is a dynamic shared object (DSO) for Apache that will add mhash
support to PHP.

#%description mcrypt -l pl


%package doc
Summary:	Online manual for PHP
Summary(pl):	Dokumentacja dla PHP
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery

%description doc
Comprehensive documentation for PHP, viewable through your web
server, too!

%description doc -l pl
Dokumentacja dla pakietu PHP. Mo¿na j± równie¿ ogl±daæ poprzez serwer
WWW.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch5 -p1

%build
CFLAGS="$RPM_OPT_FLAGS -DEAPI -I/usr/X11R6/include"; export CFLAGS
./buildconf
%configure \
	--with-apxs=/usr/sbin/apxs \
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
	--enable-shmop=shared \
	--enable-session \
	--enable-exif=shared \
	--with-regex=system \
	--with-gettext=shared \
	%{!?bcond_off_ldap:--with-ldap=shared} \
	--with-mysql=shared \
	--with-mysql-sock=/var/lib/mysql/mysql.sock \
	--with-gd=shared \
	 --enable-gd-imgstrttf \
	--with-dbase=shared \
	--with-filepro=shared \
	--enable-ftp=shared \
	--with-hyperwave \
	--with-pdflib=shared \
	--with-cpdflib=shared \
	%{?bcond_on_java:--with-java} \
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
	--with-bz2=shared \
	--with-ctype=shared \
	--with-mhash=shared \
	--with-curl=shared \
	--with-gmp=shared \
	%{?bcond_on_openssl:--with-openssl} \
	--with-unixODBC=shared \
	%{?bcond_on_oracle:--with-oracle=shared} \
	%{?bcond_on_oci8:--with-oci8=shared} \
	--without-db2 



# TODO --with-pspell=/usr,shared (pspell missing)
#	--with-unixODBC=shared (nie jest shared)

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
		$RPM_BUILD_ROOT/home/httpd/html/{icons,docs,docs/php4-doc} \
		$RPM_BUILD_ROOT/%{_sbindir}

install .libs/*.so	$RPM_BUILD_ROOT%{_pkglibdir}
install modules/*.so	$RPM_BUILD_ROOT%{_pkglibdir}/php

install %{SOURCE2}		$RPM_BUILD_ROOT%{_sysconfdir}/httpd/php.ini
install %{SOURCE3} php4.gif	$RPM_BUILD_ROOT/home/httpd/html/icons
install %{SOURCE5} $RPM_BUILD_ROOT/%{_sbindir}

tar zxf %{SOURCE4} -C $RPM_BUILD_ROOT/home/httpd/html/docs/php4-doc
ln -s manual.html $RPM_BUILD_ROOT/home/httpd/html/docs/php4-doc/index.html

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


%post bcmath
%{_sbindir}/php-module-install install bcmath /etc/httpd/php.ini

%preun bcmath
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove bcmath /etc/httpd/php.ini
fi

%post calendar
%{_sbindir}/php-module-install install calendar /etc/httpd/php.ini

%preun calendar
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove calendar /etc/httpd/php.ini
fi

%post dba
%{_sbindir}/php-module-install install dba /etc/httpd/php.ini

%preun dba
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove dba /etc/httpd/php.ini
fi

%post dbase
%{_sbindir}/php-module-install install dbase /etc/httpd/php.ini

%preun dbase
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove dbase /etc/httpd/php.ini
fi

%post exif
%{_sbindir}/php-module-install install exif /etc/httpd/php.ini

%preun exif
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove exif /etc/httpd/php.ini
fi

%post filepro
%{_sbindir}/php-module-install install filepro /etc/httpd/php.ini

%preun filepro
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove filepro /etc/httpd/php.ini
fi

%post ftp
%{_sbindir}/php-module-install install ftp /etc/httpd/php.ini

%preun ftp
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove ftp /etc/httpd/php.ini
fi

%post gd
%{_sbindir}/php-module-install install gd /etc/httpd/php.ini

%preun gd
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove gd /etc/httpd/php.ini
fi

%post gettext
%{_sbindir}/php-module-install install gettext /etc/httpd/php.ini

%preun gettext
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove gettext /etc/httpd/php.ini
fi

%post imap
%{_sbindir}/php-module-install install imap /etc/httpd/php.ini

%preun imap
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove imap /etc/httpd/php.ini
fi

%if %{?bond_on_java:1}%{!?bond_on_java:0}
%post java
%{_sbindir}/php-module-install install libphp_java /etc/httpd/php.ini

%preun java
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove libphp_java /etc/httpd/php.ini
fi
%endif

%if %{?bcond_off_ldap:0}%{!?bcond_off_ldap:1}
%post ldap
%{_sbindir}/php-module-install install ldap /etc/httpd/php.ini

%preun ldap
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove ldap /etc/httpd/php.ini
fi
%endif

%post mcrypt
%{_sbindir}/php-module-install install mcrypt /etc/httpd/php.ini

%preun mcrypt
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove mcrypt /etc/httpd/php.ini
fi

%post mhash
%{_sbindir}/php-module-install install mhash /etc/httpd/php.ini

%preun mhash
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove mhash /etc/httpd/php.ini
fi

%post mysql
%{_sbindir}/php-module-install install mysql /etc/httpd/php.ini

%preun mysql
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove mysql /etc/httpd/php.ini
fi

%if %{?bcond_on_oci8:1}%{!?bcond_on_oci8:0}
%post oci8
%{_sbindir}/php-module-install install oci8 /etc/httpd/php.ini

%preun oci8
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove oci8 /etc/httpd/php.ini
fi
%endif

%post odbc
%{_sbindir}/php-module-install install odbc /etc/httpd/php.ini

%preun odbc
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove odbc /etc/httpd/php.ini
fi

%if %{?bcond_on_oracle:1}%{!?bcond_on_oracle:0}
%post oracle
%{_sbindir}/php-module-install install oracle /etc/httpd/php.ini

%preun oracle
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove oracle /etc/httpd/php.ini
fi
%endif

%post pcre
%{_sbindir}/php-module-install install pcre /etc/httpd/php.ini

%preun pcre
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove pcre /etc/httpd/php.ini
fi

%post pgsql
%{_sbindir}/php-module-install install pgsql /etc/httpd/php.ini

%preun pgsql
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove pgsql /etc/httpd/php.ini
fi

%post posix
%{_sbindir}/php-module-install install posix /etc/httpd/php.ini

%preun posix
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove posix /etc/httpd/php.ini
fi

%post recode
%{_sbindir}/php-module-install install recode /etc/httpd/php.ini

%preun recode
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove recode /etc/httpd/php.ini
fi

%post session
%{_sbindir}/php-module-install install session /etc/httpd/php.ini

%preun session
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove session /etc/httpd/php.ini
fi

%post snmp
%{_sbindir}/php-module-install install snmp /etc/httpd/php.ini

%preun snmp
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove snmp /etc/httpd/php.ini
fi

%post sockets
%{_sbindir}/php-module-install install sockets /etc/httpd/php.ini

%preun sockets
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove sockets /etc/httpd/php.ini
fi

%post sysvsem
%{_sbindir}/php-module-install install sysvsem /etc/httpd/php.ini

%preun sysvsem
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove sysvsem /etc/httpd/php.ini
fi

%post sysvshm
%{_sbindir}/php-module-install install sysvshm /etc/httpd/php.ini

%preun sysvshm
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove sysvshm /etc/httpd/php.ini
fi

%post xml
%{_sbindir}/php-module-install install xml /etc/httpd/php.ini

%preun xml
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove xml /etc/httpd/php.ini
fi

%post yp
%{_sbindir}/php-module-install install yp /etc/httpd/php.ini

%preun yp
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove yp /etc/httpd/php.ini
fi

%post zlib
%{_sbindir}/php-module-install install zlib /etc/httpd/php.ini

%preun zlib
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove zlib /etc/httpd/php.ini
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
%attr(755,root,root) %{_sbindir}/*

%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/mysql.so

%files pgsql
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/pgsql.so

%if %{?bcond_on_oracle:1}%{!?bcond_on_oracle:0}
%files oracle
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/oracle.so
%endif

%if  %{?bcond_on_oci8:1}%{!?bcond_on_oci8:0}
%files oci8
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/oci8.so
%endif

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

%if %{?bcond_on_java:1}%{!?bcond_on_java:0}
%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/libphp_java.so
%endif

%if %{?bcond_off_ldap:0}%{!?bcond_off_ldap:1}
%files ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/ldap.so
%endif

%files sockets
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/sockets.so

%files mcrypt
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/mcrypt.so

%files mhash
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/mhash.so

%files odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/odbc.so

%files doc
%defattr(644,root,root,755)
/home/httpd/html/docs/php4-doc
