Summary:	The PHP HTML-embedded scripting language for use with Apache.
Summary(fr):	Le langage de script embarque-HTML PHP pour Apache.
Summary(pl):	Jêzyk skryptowy PHP -- u¿ywany wraz z serwerem Apache.
Name:		php
Version:	4.0.0
Release:	2
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
License: 	The PHP license (see "LICENSE" file included in distribution)
Source0:	http://www.php.net/version4/downloads/%{name}-%{version}.tar.gz
Source1:	FAQ.php
Source2:	php.ini
Source3:	zend.gif
Source4:	http://www.php.net/distributions/manual.tar.gz
Source5:	http://www.php.net/extra/number4.tar.gz
Patch0:		php-imap.patch
Patch1:		php-mysql-socket.patch
Patch2:		php-mail.patch
Patch3:		php-ldap.patch
Patch4:		php-bcmath.patch
Icon:		php4.gif
URL:		http://www.php.net/
BuildRequires:	apache(EAPI)-devel
BuildRequires:	zip
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	db-devel >= 3.0.55
BuildRequires:	freetype-devel
BuildRequires:	gd-devel
BuildRequires:	gdbm-devel
BuildRequires:	imap-devel >= 4.7b-1
# I think jdk is better for java
# BuildRequires: jdk
BuildRequires:	kaffe-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	mm-devel
BuildRequires:	openldap-devel
BuildRequires:	pam-devel
BuildRequires:	pdflib-devel >= 3.0
#BuildRequires:	libxml-devel >= 2.0.0
BuildRequires:	postgresql-devel
BuildRequires:	recode-devel >= 3.5
BuildRequires:	t1lib-devel
# BuildRequires:	unixODBC-devel
BuildRequires:	zlib-devel >= 1.0.9
#BuildRequires:	libmcrypt-devel
Requires:	apache(EAPI) >= 1.3.9
Prereq:		/usr/sbin/apxs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
HTML. Pakiet ten zawiera modu³ przeznaczony dla serwera HTTP (jak np.
Apache), który interpretuje te polecenia.  Umo¿liwia to tworzenie
dynamicznie stron WWW. Spora czê¶æ sk³adni PHP zapo¿yczona zosta³a
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

%description mysql -l pl
Modu³ PHP4 umo¿liwiaj±cy dostêp do bazy danych MySQL.


%package pgsql
Summary:	PostgreSQL database module for PHP4
Summary(pl):	Modu³ bazy danych PostgreSQL dla PHP4
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires: 	%{name} = %{version}

%description pgsql
This is a dynamic shared object (DSO) for Apache that will add PostgreSQL
database support to PHP4.  If you need back-end support for PostgreSQL,
you should install this package in addition to the main %{name} package.

%description pgsql -l pl
Modu³ PHP4 umo¿liwiaj±cy dostêp do bazy danych PostgreSQL.

%package gd
Summary:	GD extension module for PHP4
Summary:	Modu³ GD dla PHP4
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires: 	%{name} = %{version}

%description gd
This is a dynamic shared object (DSO) for Apache that will add GD
support to PHP4. You should install this package in addition to the main
%{name} package if you want to create and manipulate images with PHP.

%description gd -l pl

%package java
Summary:	Java extension module for PHP4
Summary(pl):	Modu³ Javy dla PHP4
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires: 	%{name} = %{version}

%description java
This is a dynamic shared object (DSO) for Apache that will add JAVA
support to PHP4. This extension provides a simple and effective means
for creating and invoking methods on Java objects from PHP.

%description java -l pl

%package xml
Summary:	XML extension module for PHP4
Summary(pl):	Modu³ XML dla PHP4
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires: 	%{name} = %{version}

%description xml
This is a dynamic shared object (DSO) for Apache that will add XML
support to PHP4. This extension lets you create XML parsers and then
define handlers for different XML events. If you want to be able to parse
XML documents you should install this package in addition to the main 
%{name} package.

#%description xml -l pl

%package dba
Summary:	DBA extension module for PHP4
Summary(pl):	Modu³ DBA dla PHP4
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires: 	%{name} = %{version}

%description dba
This is a dynamic shared object (DSO) for Apache that will add flat-file databases (DBA)
support to PHP4. 

#%description dba -l pl

%package calendar
Summary:	Calendar extension module for PHP4
Summary(pl):	Modu³ funkcji kalendarza dla PHP4
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires: 	%{name} = %{version}

%description calendar
This is a dynamic shared object (DSO) for Apache that will add calendar
support to PHP4. 

#%description calendar -l pl

%package dbase
Summary:	DBase extension module for PHP4
Summary(pl):	Modu³ DBase dla PHP4
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires: 	%{name} = %{version}

%description dbase
This is a dynamic shared object (DSO) for Apache that will add DBase
support to PHP4. 

#%description dbase -l pl

%package filepro
Summary:	FilePro extension module for PHP4
Summary(pl):	Modu³ FilePro dla PHP4
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires: 	%{name} = %{version}

%description filepro
This is a dynamic shared object (DSO) for Apache that will add FilePro
support to PHP4. 

#%description filepro -l pl

%package posix
Summary:	POSIX extension module for PHP4
Summary(pl):	Modu³ POSIX dla PHP4
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires: 	%{name} = %{version}

%description posix
This is a dynamic shared object (DSO) for Apache that will add POSIX functions
support to PHP4. 

#%description posix -l pl

%package pcre
Summary:	PCRE extension module for PHP4
Summary(pl):	Modu³ PCRE dla PHP4
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires: 	%{name} = %{version}

%description pcre
This is a dynamic shared object (DSO) for Apache that will add Perl Compatible Regular Expression
support to PHP4. 

#%description pcre -l pl

%package sysvsem
Summary:	SysV sem extension module for PHP4
Summary(pl):	Modu³ SysV sem dla PHP4
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires: 	%{name} = %{version}

%description sysvsem
This is a dynamic shared object (DSO) for Apache that will add SysV semafores
support to PHP4. 

#%description sysvsem -l pl

%package sysvshm
Summary:	SysV shm extension module for PHP4
Summary(pl):	Modu³ SysV shm dla PHP4
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires: 	%{name} = %{version}

%description sysvshm
This is a dynamic shared object (DSO) for Apache that will add SysV Shared Memory
support to PHP4. 

#%description sysvshm -l pl

%package yp
Summary:	NIS (yp) extension module for PHP4
Summary(pl):	Modu³ NIS (yp) dla PHP4
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires: 	%{name} = %{version}

%description yp
This is a dynamic shared object (DSO) for Apache that will add NIS (Yellow Pages)
support to PHP4. 

#%description yp -l pl

%package bcmath
Summary:	bcmath extension module for PHP4
Summary(pl):	Modu³ bcmath dla PHP4
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires: 	%{name} = %{version}

%description bcmath
This is a dynamic shared object (DSO) for Apache that will add bc style precision math functions
support to PHP4. 

#%description bcmath -l pl

%package ftp
Summary:	FTP extension module for PHP4
Summary(pl):	Modu³ FTP dla PHP4
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires: 	%{name} = %{version}

%description ftp
This is a dynamic shared object (DSO) for Apache that will add FTP
support to PHP4. 

#%description ftp -l pl

%package zlib
Summary:	Zlib extension module for PHP4
Summary(pl):	Modu³ zlib dla PHP4
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires: 	%{name} = %{version}

%description zlib
This is a dynamic shared object (DSO) for Apache that will add commpresion (zlib)
support to PHP4. 

#%description zlib -l pl



%package doc
Summary:     Online manual for PHP4
Summary(pl): Dokumentacja dla PHP4
Group:       Networking/Daemons

%description doc
Comprehensive documentation for PHP4, viewable through your web server, too!

%description doc -l pl
Dokumentacja dla pakietu PHP4.  Mo¿na j± równie¿ ogl±daæ poprzez serwer WWW.
%prep
%setup  -q -a 5
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
LDFLAGS="-s"; export LDFLAGS
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
	--with-regex=system \
	--with-gettext \
	--with-ldap \
	--with-mysql=shared \
	--with-mysql-sock=/var/state/mysql/mysql.sock \
	--with-gd=shared \
	--with-dbase=shared \
	--with-filepro=shared \
	--enable-ftp=shared \
	--with-hyperwave \
	--with-pdflib=shared \
	--with-cpdflib=shared \
	--with-java \
	--with-pgsql=shared,/usr \
	--with-imap \
	--enable-bcmath=shared \
	--enable-calendar=shared \
	--with-mm \
	--with-pcre-regex=shared \
	--enable-posix=shared \
	--enable-session \
	--with-ttf \
	--with-t1lib \
	--with-recode \
	--enable-ucd-snmp-hack \
	--enable-dba=shared \
	--with-gdbm \
	--with-ndbm \
	--enable-yp=shared \
	--with-xml=shared \
	--enable-xml=shared \
	--with-zlib=shared 


#	--with-db3 \

# snmp won
#	--with-snmp=shared \
#	--with-openssl \

#Syntax error on line 228 of /etc/httpd/httpd.conf: Cannot load /usr/lib/apache/libphp4.so into server: /usr/lib/apache/libphp4.so: undefined symbol: phpi_get_le_gd
# Solution: make pdf and cpdf shared
#	--with-gd=shared \

#	--with-unixODBC \

# This option get trouble with imap
#	--enable-versioning \

# To old/new libmcrypt ?
#	--with-mcrypt=shared \
#	--with-dom=/usr/X11R6 \

make

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

strip --strip-unneeded	\
	$RPM_BUILD_ROOT%{_pkglibdir}/*.so \
	$RPM_BUILD_ROOT%{_pkglibdir}/php/*.so

install %{SOURCE1} .
gzip -9nf CODING_STANDARDS CREDITS FUNCTION_LIST.txt \
      MAINTAINERS MODULES_STATUS NEWS TODO* LICENSE Zend/LICENSE \
      Zend/ZEND_CHANGES

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
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "deactivating module 'mysql.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^extension=mysql.so|;extension=mysql.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
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
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "deactivating module 'pgsql.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^extension=pgsql.so|;extension=pgsql.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

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
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "deactivating module 'gd.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^extension=gd.so|;extension=gd.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
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
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "deactivating module 'xml.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^extension=xml.so|;extension=xml.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
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
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "deactivating module 'dba.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^extension=dba.so|;extension=dba.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
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
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "deactivating module 'calendar.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^extension=calendar.so|;extension=calendar.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
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
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "deactivating module 'dbase.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^extension=dbase.so|;extension=dbase.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
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
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "deactivating module 'libphp_java.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^extension=libphp_java.so|;extension=libphp_java.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
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
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "deactivating module 'filepro.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^extension=filepro.so|;extension=filepro.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
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
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "deactivating module 'pcre.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^extension=pcre.so|;extension=pcre.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
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
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "deactivating module 'posix.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^extension=posix.so|;extension=posix.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
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
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "deactivating module 'sysvsem.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^extension=sysvsem.so|;extension=sysvsem.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
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
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "deactivating module 'sysvshm.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^extension=sysvshm.so|;extension=sysvshm.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
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
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "deactivating module 'yp.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^extension=yp.so|;extension=yp.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
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
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "deactivating module 'ftp.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^extension=ftp.so|;extension=ftp.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
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
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "deactivating module 'zlib.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^extension=zlib.so|;extension=zlib.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
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
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "deactivating module 'bcmath.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^extension=bcmath.so|;extension=bcmath.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi



%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CODING_STANDARDS,CREDITS,FUNCTION_LIST.txt,Zend/ZEND_CHANGES}.gz
%doc {LICENSE,Zend/LICENSE,MAINTAINERS,MODULES_STATUS,NEWS,TODO*}.gz  

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

%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/libphp_java.so

%files doc
/home/httpd/html/docs/php4-doc
