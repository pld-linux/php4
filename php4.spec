#
# TODO:
# - make sure that session-unregister patch is no longer needed
#   (any crash reports related to session modules?)
#
# Conditional build:
%bcond_with	db3		# use db3 packages instead of db (4.x) for Berkeley DB support
%bcond_with	fdf		# with FDF (PDF forms) module		(BR: proprietary lib)
%bcond_with	interbase_inst	# use InterBase install., not Firebird	(BR: proprietary libs)
%bcond_with	java		# with Java extension module		(BR: jdk)
%bcond_with	oci8		# with Oracle oci8 extension module	(BR: proprietary libs)
%bcond_with	oracle		# with oracle extension module		(BR: proprietary libs)
%bcond_without	cpdf		# without cpdf extension module
%bcond_without	curl		# without CURL extension module
%bcond_without	domxslt		# without DOM XSLT/EXSLT support in DOM XML extension module
%bcond_without	fribidi		# without FriBiDi extension module
%bcond_without	gif		# build GD extension module with gd library without GIF support
%bcond_without	imap		# without IMAP extension module
%bcond_without	interbase	# without InterBase extension module
%bcond_without	ldap		# without LDAP extension module
%bcond_without	mhash		# without mhash extension module
%bcond_without	ming		# without ming extension module
%bcond_without	mm		# without mm support for session storage
%bcond_without	mnogosearch	# without mnogosearch extension module
%bcond_without	msession	# without msession extension module
%bcond_without	mssql		# without MS SQL extension module
%bcond_without	odbc		# without ODBC extension module
%bcond_without	openssl		# without OpenSSL support and OpenSSL extension (module)
%bcond_without	pcre		# without PCRE extension module
%bcond_without	pdf		# without PDF extension module
%bcond_without	pgsql		# without PostgreSQL extension module
%bcond_without	pspell		# without pspell extension module
%bcond_without	recode		# without recode extension module
%bcond_without	qtdom		# without QT DOM extension module
%bcond_without	snmp		# without SNMP extension module
%bcond_without	sybase		# without Sybase and Sybase-CT extension modules
%bcond_without	wddx		# without WDDX extension module
%bcond_without	xmlrpc		# without XML-RPC extension module
%bcond_without	xml		# without XML and DOMXML extension modules
%bcond_without	xslt		# without XSLT extension module
%bcond_without	yaz		# without YAZ extension module
#
%define	_apache2	%(rpm -q apache-devel 2> /dev/null | grep -Eq '\\-2\\.[0-9]+\\.' && echo 1 || echo 0)
%define	apxs		/usr/sbin/apxs
# some problems with apache 2.x
%if %{_apache2}
%undefine	with_recode
%undefine	with_mm
%endif
# x86-only libs
%ifnarch %{ix86}
%undefine	with_interbase
%undefine	with_msession
%endif
%include	/usr/lib/rpm/macros.php
Summary:	The PHP HTML-embedded scripting language for use with Apache
Summary(fr):	Le langage de script embarque-HTML PHP pour Apache
Summary(pl):	JÍzyk skryptowy PHP -- uøywany wraz z serwerem Apache
Summary(pt_BR):	A linguagem de script PHP
Summary(ru):	PHP ˜≈“”…… 4 -- —⁄ŸÀ –“≈–“œ√≈””…“œ◊¡Œ…— HTML-∆¡ Ãœ◊, ◊Ÿ–œÃŒ—≈ÕŸ  Œ¡ ”≈“◊≈“≈
Summary(uk):	PHP ˜≈“”¶ß 4 -- Õœ◊¡ –“≈–“œ√≈”’◊¡ŒŒ— HTML-∆¡ Ã¶◊, ◊…ÀœŒ’◊¡Œ¡ Œ¡ ”≈“◊≈“¶
Name:		php
Version:	4.3.5
%define	_pre	RC3
%define	_version	4.3.5%{_pre}
Release:	0.%{_pre}
Epoch:		3
Group:		Libraries
License:	PHP
#Source0:	http://www.php.net/distributions/%{name}-%{version}.tar.bz2
Source0:	http://downloads.php.net/ilia/%{name}-%{_version}.tar.bz2
# Source0-md5:	efa1b74ed9c34f4801ce576f73bbd29c
Source1:	FAQ.%{name}
Source2:	zend.gif
Source4:	%{name}-module-install
Source5:	%{name}-mod_%{name}.conf
Source6:	%{name}-cgi.ini
Source7:	%{name}-apache.ini
Source8:	%{name}-cli.ini
Patch0:		%{name}-shared.patch
Patch1:		%{name}-pldlogo.patch
Patch2:		%{name}-xml-expat-fix.patch
Patch3:		%{name}-mail.patch
Patch4:		%{name}-link-libs.patch
Patch5:		%{name}-libpq_fs_h_path.patch
Patch6:		%{name}-wddx-fix.patch
Patch7:		%{name}-cpdf-fix.patch
Patch8:		%{name}-hyperwave-fix.patch
Patch9:		%{name}-xslt-gcc33.patch
Patch10:	%{name}-java-norpath.patch
Patch11:	%{name}-mcal-shared-lib.patch
Patch12:	%{name}-msession-shared-lib.patch
Patch13:	%{name}-build_modules.patch
Patch14:	%{name}-sapi-ini-file.patch
Patch15:	%{name}-no-metaccld.patch
Patch16:	%{name}-session-unregister.patch
Patch17:	%{name}-ini.patch
Patch18:	%{name}-acam.patch
Patch19:	%{name}-xmlrpc-fix.patch
Patch20:	%{name}-libtool.patch
Patch21:	%{name}-allow-db31.patch
Patch22:	%{name}-threads-acfix.patch
Patch23:	%{name}-tsrmlsfetchgcc2.patch
Patch24:	%{name}-qt.patch
Patch25:	%{name}-no_pear_install.patch
Patch26:	%{name}-zlib.patch
Patch27:	%{name}-db-shared.patch
Patch28:	%{name}-sybase-fix.patch
Patch29:	%{name}-mssql-fix.patch
Patch30:	%{name}-db42.patch
Patch31:	%{name}-lib64.patch
Icon:		php4.gif
URL:		http://www.php.net/
%{?with_interbase:%{!?with_interbase_inst:BuildRequires:	Firebird-devel >= 1.0.2.908-2}}
BuildRequires:	apache-devel
%{?with_pspell:BuildRequires:	aspell-devel}
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.4d
BuildRequires:	bison
BuildRequires:	bzip2-devel
BuildRequires:	cracklib-devel >= 2.7-15
%{?with_curl:BuildRequires:	curl-devel >= 7.9.8 }
BuildRequires:	cyrus-sasl-devel
%{?with_db3:BuildRequires:	db3-devel >= 3.1}
%{!?with_db3:BuildRequires:	db-devel >= 4.0}
BuildRequires:	elfutils-devel
%if %{with xml} || %{with xmlrpc}
BuildRequires:	expat-devel
%endif
%{?with_fdf:BuildRequires:	fdftk-devel}
BuildRequires:	flex
%if %{with mssql} || %{with sybase}
BuildRequires:	freetds-devel
%endif
BuildRequires:	freetype-devel >= 2.0
%{?with_fribidi:BuildRequires:	fribidi-devel >= 0.10.4}
BuildRequires:	gd-devel >= 2.0.1
%{?with_gif:BuildRequires:	gd-devel(gif)}
%{!?with_gif:BuildConflicts:	gd-devel(gif)}
BuildRequires:	gdbm-devel
BuildRequires:	gmp-devel
%{?with_imap:BuildRequires:	imap-devel >= 1:2001-0.BETA.200107022325.2 }
%{?with_java:BuildRequires:	jdk >= 1.1}
%{?with_cpdf:BuildRequires:	libcpdf-devel >= 2.02r1-2}
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel >= 1.4
BuildRequires:	libmcal-devel
BuildRequires:	libmcrypt-devel >= 2.4.4
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 1.4.3
%{?with_xml:BuildRequires:	libxml2-devel >= 2.2.7}
%{?with_domxslt:BuildRequires:	libxslt-devel >= 1.0.3}
%{?with_mhash:BuildRequires:	mhash-devel}
%{?with_ming:BuildRequires:	ming-devel >= 0.1.0}
%{?with_mm:BuildRequires:	mm-devel >= 1.3.0}
%{?with_mnogosearch:BuildRequires:	mnogosearch-devel >= 3.2.6}
BuildRequires:	mysql-devel >= 3.23.32
BuildRequires:	ncurses-devel
%{?with_ldap:BuildRequires:	openldap-devel >= 2.0}
%if %{with openssl} || %{with ldap}
BuildRequires:	openssl-devel >= 0.9.7d
%endif
BuildRequires:	pam-devel
%{?with_pdf:BuildRequires:	pdflib-devel >= 4.0.0}
BuildRequires:	%{__perl}
%{?with_msession:BuildRequires:	phoenix-devel}
%{?with_pgsql:BuildRequires:	postgresql-devel}
%{?with_pgsql:BuildRequires:	postgresql-backend-devel >= 7.2}
%{?with_qtdom:BuildRequires:	qt-devel >= 2.2.0}
BuildRequires:	readline-devel
%{?with_recode:BuildRequires:	recode-devel >= 3.5d-3}
BuildRequires:	rpm-php-pearprov >= 4.0.2-100
BuildRequires:	rpmbuild(macros) >= 1.120
%{?with_xslt:BuildRequires:	sablotron-devel >= 0.96}
BuildRequires:	t1lib-devel
%{?with_snmp:BuildRequires:	net-snmp-devel >= 5.0.7}
%{?with_odbc:BuildRequires:	unixODBC-devel}
%{?with_xmlrpc:BuildRequires:	xmlrpc-epi-devel}
%{?with_yaz:BuildRequires:	yaz-devel >= 1.9}
BuildRequires:	zip
BuildRequires:	zlib-devel >= 1.0.9
BuildRequires:	zziplib-devel
BuildRequires:	fcgi-devel
# apache 1.3 vs apache 2.0
%if %{_apache2}
BuildRequires:  apr-devel >= 1:0.9.4-1
PreReq:		apache >= 2.0.40
Requires:	apache(modules-api) = %{apache_modules_api}
%else
PreReq:		apache(EAPI) < 2.0.0
PreReq:		apache(EAPI) >= 1.3.9
Requires(post,preun):	%{apxs}
Requires(post,preun):	%{__perl}
%endif
PreReq:		%{name}-common = %{epoch}:%{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	phpfi
Obsoletes:	apache-mod_php

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php
%define		httpdir		/home/services/httpd
%define		_ulibdir	%{_prefix}/lib

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
installer ce package. Vous aurez egalement besoin dinstaller le
serveur web Apache.

%description -l pl
PHP jest jÍzykiem skryptowym, ktÛrego polecenia umieszcza siÍ w
plikach HTML. Pakiet ten zawiera modu≥ przeznaczony dla serwera HTTP
(jak np. Apache), ktÛry interpretuje te polecenia. Umoøliwia to
tworzenie dynamicznie stron WWW. Spora czÍ∂Ê sk≥adni PHP zapoøyczona
zosta≥a z jÍzykÛw: C, Java i Perl.

%description -l pt_BR
PHP: Preprocessador de Hipertexto vers„o 4 È uma linguagem script
embutida em HTML. Muito de sua sintaxe È emprestada de C, Java e Perl,
com algumas caracterÌsticas ˙nicas, especÌficas ao PHP. O objetivo da
linguagem È permitir que desenvolvedores web escrevam p·ginas
dinamicamente geradas de forma r·pida.

%description -l ru
PHP4 - ‹‘œ —⁄ŸÀ Œ¡–…”¡Œ…— ”À“…–‘œ◊, ◊”‘“¡…◊¡≈ÕŸ» ◊ HTML-Àœƒ. PHP
–“≈ƒÃ¡«¡≈‘ …Œ‘≈“«“¡√…¿ ” ÕŒœ÷≈”‘◊œÕ Ûı‚‰, –œ‹‘œÕ’ Œ¡–…”¡Œ…≈ ”À“…–‘œ◊
ƒÃ— “¡¬œ‘Ÿ ” ¬¡⁄¡Õ… ƒ¡ŒŒŸ» œ‘Œœ”…‘≈ÃÿŒœ –“œ”‘œ. Ó¡…¬œÃ≈≈ –œ–’Ã—“Œœ≈
…”–œÃÿ⁄œ◊¡Œ…≈ PHP - ⁄¡Õ≈Œ¡ ƒÃ— CGI ”À“…–‘œ◊.

¸‘œ‘ –¡À≈‘ ”œƒ≈“÷…‘ ”¡Õœƒœ”‘¡‘œﬁŒ’¿ (CGI) ◊≈“”…¿ …Œ‘≈“–“≈‘¡‘œ“¡ —⁄ŸÀ¡.
˜Ÿ ƒœÃ÷ŒŸ ‘¡À÷≈ ’”‘¡Œœ◊…‘ÿ –¡À≈‘ %{name}-common. Â”Ã… ◊¡Õ Œ’÷≈Œ
…Œ‘≈“–“≈‘¡‘œ“ PHP ◊ À¡ﬁ≈”‘◊≈ Õœƒ’Ã— apache, ’”‘¡Œœ◊…‘≈ –¡À≈‘
apache-php.

%description -l uk
PHP4 - √≈ Õœ◊¡ Œ¡–…”¡ŒŒ— ”À“…–‘¶◊, ›œ ◊¬’ƒœ◊’¿‘ÿ”— ◊ HTML-Àœƒ. PHP
–“œ–œŒ’§ ¶Œ‘≈«“¡√¶¿ ⁄ ¬¡«¡‘ÿÕ¡ Ûı‚‰, ‘œÕ’ Œ¡–…”¡ŒŒ— ”À“…–‘¶◊ ƒÃ—
“œ¬œ‘… ⁄ ¬¡⁄¡Õ… ƒ¡Œ…» § ƒœ◊œÃ¶ –“œ”‘…Õ. Ó¡ ¬¶Ãÿ€ –œ–’Ã—“Œ≈
◊…Àœ“…”‘¡ŒŒ— PHP - ⁄¡Õ¶Œ¡ ƒÃ— CGI ”À“…–‘¶◊.

„≈  –¡À≈‘ Õ¶”‘…‘ÿ ”¡Õœƒœ”‘¡‘Œ¿ (CGI) ◊≈“”¶¿ ¶Œ‘≈“–“≈‘¡‘œ“¡ Õœ◊…. ˜…
Õ¡§‘≈ ‘¡Àœ÷ ◊”‘¡Œœ◊…‘… –¡À≈‘ %{name}-common. ÒÀ›œ ◊¡Õ –œ‘“¶¬≈Œ
¶Œ‘≈“–“≈‘¡‘œ“ PHP ◊ —Àœ”‘¶ Õœƒ’Ã— apache, ◊”‘¡Œœ◊¶‘ÿ –¡À≈‘ apache-php.

%package fcgi
Summary:	PHP as FastCGI program
Summary(pl):	PHP jako program FastCGI
Group:		Development/Languages/PHP
PreReq:		%{name}-common = %{epoch}:%{version}
Provides:	php-program = %{epoch}:%{version}-%{release}

%description fcgi
PHP as FastCGI program.

%description fcgi -l pl
PHP jako program FastCGI.

%package cgi
Summary:	PHP as CGI program
Summary(pl):	PHP jako program CGI
Group:		Development/Languages/PHP
PreReq:		%{name}-common = %{epoch}:%{version}
Provides:	php-program = %{epoch}:%{version}-%{release}

%description cgi
PHP as CGI program.

%description cgi -l pl
PHP jako program CGI.

%package cli
Summary:	PHP as CLI interpreter
Summary(pl):	PHP jako interpreter dzia≥aj±cy z linii poleceÒ
Group:		Development/Languages/PHP
PreReq:		%{name}-common = %{epoch}:%{version}
Provides:	php-program = %{epoch}:%{version}-%{release}

%description cli
PHP as CLI interpreter.

%description cli -l pl
PHP jako interpreter dzia≥aj±cy z linii poleceÒ.

%package common
Summary:	Common files needed by both apache module and CGI
Summary(pl):	WspÛlne pliki dla modu≥u apache'a i programu CGI
Summary(ru):	Ú¡⁄ƒ≈Ã—≈ÕŸ≈ ¬…¬Ã…œ‘≈À… ƒÃ— php
Summary(uk):	‚¶¬Ã¶œ‘≈À… ”–¶ÃÿŒœ«œ ◊…Àœ“…”‘¡ŒŒ— ƒÃ— php
Group:		Libraries
Provides:	%{name}-session = %{epoch}:%{version}-%{release}
Provides:	%{name}-openssl = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-session <= %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-openssl <= %{epoch}:%{version}-%{release}

%description common
Common files needed by both apache module and CGI.

%description common -l pl
WspÛlne pliki dla modu≥u apacha i programu CGI.

%description common -l ru
¸‘œ‘ –¡À≈‘ ”œƒ≈“÷…‘ œ¬›…≈ ∆¡ ÃŸ ƒÃ— “¡⁄ŒŸ» ◊¡“…¡Œ‘œ◊ “≈¡Ã…⁄¡√…… PHP
(”¡Õœƒœ”‘¡‘œﬁŒœ  … ◊ À¡ﬁ≈”‘◊≈ Õœƒ’Ã— apache).

%description common -l uk
„≈  –¡À≈‘ Õ¶”‘…‘ÿ ”–¶ÃÿŒ¶ ∆¡ Ã… ƒÃ— “¶⁄Œ…» ◊¡“¶¡Œ‘¶◊ “≈¡Ã¶⁄¡√¶ß PHP
(”¡Õœƒœ”‘¡‘Œÿœß ‘¡ ◊ —Àœ”‘¶ Õœƒ’Ã— apache).

%package devel
Summary:	Files for PHP modules development
Summary(pl):	Pliki do kompilacji modu≥Ûw PHP
Summary(pt_BR):	Arquivos de desenvolvimento para PHP
Summary(ru):	¡À≈‘ “¡⁄“¡¬œ‘À… ƒÃ— –œ”‘“œ≈Œ…— “¡”€…“≈Œ…  PHP4
Summary(uk):	¡À≈‘ “œ⁄“œ¬À… ƒÃ— –œ¬’ƒœ◊… “œ⁄€…“≈Œÿ PHP4
Group:		Development/Languages/PHP
Requires:	%{name}-common = %{epoch}:%{version}
Obsoletes:	%{name}-pear-devel

%description devel
The php-devel package lets you compile dynamic extensions to PHP.
Included here is the source for the php extensions. Instead of
recompiling the whole php binary to add support for, say, oracle,
install this package and use the new self-contained extensions
support. For more information, read the file
SELF-CONTAINED-EXTENSIONS.

%description devel -l pl
Pliki potrzebne do kompilacji modu≥Ûw PHP.

%description devel -l pt_BR
Este pacote contÈm arquivos usados no desenvolvimento de programas ou
mÛdulos PHP.

%description devel -l uk
¡À≈‘ php-devel ƒ¡§ Õœ÷Ã…◊¶”‘ÿ ÀœÕ–¶Ã¿◊¡‘… ƒ…Œ¡Õ¶ﬁŒ¶ “œ⁄€…“≈ŒŒ— PHP.
‰œ –¡À≈‘’ ◊ÀÃ¿ﬁ≈Œœ ◊…»¶ƒŒ…  Àœƒ ƒÃ— “œ⁄€…“≈Œÿ. ˙¡Õ¶”‘ÿ –œ◊‘œ“Œœß
ÀœÕ–¶Ã—√¶ß ¬¶Œ¡“Œœ«œ ∆¡ Ã’ php ƒÃ— ƒœƒ¡ŒŒ—, Œ¡–“…ÀÃ¡ƒ, –¶ƒ‘“…ÕÀ…
oracle, ◊”‘¡Œœ◊¶‘ÿ √≈  –¡À≈‘ ƒÃ— ÀœÕ–¶Ã—√¶ß œÀ“≈Õ…» “œ⁄€…“≈Œÿ.
‰≈‘¡ÃÿŒ¶€¡ ¶Œ∆œ“Õ¡√¶— - ◊ ∆¡ Ã¶ SELF-CONTAINED-EXTENSIONS.

%description devel -l ru
¡À≈‘ php-devel ƒ¡≈‘ ◊œ⁄Õœ÷Œœ”‘ÿ ÀœÕ–…Ã…“œ◊¡‘ÿ ƒ…Œ¡Õ…ﬁ≈”À…≈ “¡”€…“≈Œ…—
PHP. ¡À≈‘ ◊ÀÃ¿ﬁ¡≈‘ …”»œƒŒŸ  Àœƒ ‹‘…» “¡”€…“≈Œ… . ˜Õ≈”‘œ –œ◊‘œ“Œœ 
ÀœÕ–…Ã—√…… ¬…Œ¡“Œœ«œ ∆¡ Ã¡ php ƒÃ— ƒœ¬¡◊Ã≈Œ…—, Œ¡–“…Õ≈“, –œƒƒ≈“÷À…
oracle, ’”‘¡Œœ◊…‘≈ ‹‘œ‘ –¡À≈‘ ƒÃ— ÀœÕ–…Ã…“œ◊¡Œ…— œ‘ƒ≈ÃÿŒŸ» “¡”€…“≈Œ… .
œƒ“œ¬Œœ”‘… - ◊ ∆¡ Ã≈ SELF-CONTAINED-EXTENSIONS.

%package bcmath
Summary:	bcmath extension module for PHP
Summary(pl):	Modu≥ bcmath dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description bcmath
This is a dynamic shared object (DSO) for PHP that will add bc style
precision math functions support.

%description bcmath -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z dok≥adnych funkcji
matematycznych takich jak w programie bc.

%package bzip2
Summary:	Bzip2 extension module for PHP
Summary(pl):	Modu≥ bzip2 dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description bzip2
This is a dynamic shared object (DSO) for PHP that will add
bzip2 compression support to PHP.

%description bzip2 -l pl
Modu≥ PHP umoøliwiaj±cy uøywanie kompresji bzip2.

%package calendar
Summary:	Calendar extension module for PHP
Summary(pl):	Modu≥ funkcji kalendarza dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description calendar
This is a dynamic shared object (DSO) for PHP that will add calendar
support.

%description calendar -l pl
Modu≥ PHP dodaj±cy wsparcie dla kalendarza.

%package cpdf
Summary:	cpdf extension module for PHP
Summary(pl):	Modu≥ cpdf dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description cpdf
This is a dynamic shared object (DSO) for PHP that will add PDF
support through libcpdf library.

%description cpdf -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ plikÛw PDF poprzez bibliotekÍ libcpdf.

%package crack
Summary:	crack extension module for PHP
Summary(pl):	Modu≥ crack dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description crack
This is a dynamic shared object (DSO) for PHP that will add cracklib
support to PHP.

Warning: this is an experimental module.

%description crack -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z biblioteki cracklib.

Uwaga: to jest modu≥ eksperymentalny.

%package ctype
Summary:	ctype extension module for PHP
Summary(pl):	Modu≥ ctype dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description ctype
This is a dynamic shared object (DSO) for PHP that will add ctype
support.

%description ctype -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z funkcji ctype.

%package curl
Summary:	curl extension module for PHP
Summary(pl):	Modu≥ curl dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description curl
This is a dynamic shared object (DSO) for PHP that will add curl
support.

%description curl -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z biblioteki curl.

%package db
Summary:	Old xDBM extension module for PHP
Summary(pl):	Modu≥ xDBM dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description db
This is an old dynamic shared object (DSO) for PHP that will add DBM
databases support.

Warning: this module is deprecated and does not support database
locking correctly. Please use DBA extension which is a fully
operational superset.

%description db -l pl
Stary modu≥ PHP dodaj±cy obs≥ugÍ baz danych DBM.

Uwaga: ten modu≥ jest przestarza≥y i nie obs≥uguje poprawnie
blokowania bazy danych. Zamiast niego lepiej uøywaÊ rozszerzenia DBA,
ktÛre obs≥uguje nadzbiÛr funkcjonalno∂ci tego modu≥u.

%package dba
Summary:	DBA extension module for PHP
Summary(pl):	Modu≥ DBA dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description dba
This is a dynamic shared object (DSO) for PHP that will add flat-file
databases (DBA) support.

%description dba -l pl
Modu≥ dla PHP dodaj±cy obs≥ugÍ dla baz danych opartych na plikach
(DBA).

%package dbase
Summary:	DBase extension module for PHP
Summary(pl):	Modu≥ DBase dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description dbase
This is a dynamic shared object (DSO) for PHP that will add DBase
support.

%description dbase -l pl
Modu≥ PHP ze wsparciem dla DBase.

%package dbx
Summary:	DBX extension module for PHP
Summary(pl):	Modu≥ DBX dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description dbx
This is a dynamic shared object (DSO) for PHP that will add DB
abstraction layer. DBX supports odbc, mysql, pgsql, mssql, fbsql and
more.

%description dbx -l pl
Modu≥ PHP dodaj±cy warstwÍ abstrakcji do obs≥ugi baz danych. DBX
obs≥uguje bazy odbc, mysql, pgsql, mssql, fbsql i inne.

%package dio
Summary:	Direct I/O extension module for PHP
Summary(pl):	Modu≥ Direct I/O dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description dio
This is a dynamic shared object (DSO) for PHP that will add direct
file I/O support.

%description dio -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ bezpo∂rednich operacji I/O na plikach.

%package domxml
Summary:	DOM XML extension module for PHP
Summary(pl):	Modu≥ DOM XML dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description domxml
This is a dynamic shared object (DSO) for PHP that will add DOM XML
support.

Warning: this is an experimental module.

%description domxml -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ DOM XML.

Uwaga: to jest modu≥ eksperymentalny.

%package exif
Summary:	exif extension module for PHP
Summary(pl):	Modu≥ exif dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description exif
This is a dynamic shared object (DSO) for PHP that will add EXIF
tags support in image files.

%description exif -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ znacznikÛw EXIF w plikach obrazkÛw.

%package fdf
Summary:	FDF extension module for PHP
Summary(pl):	Modu≥ FDF dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description fdf
This PHP module adds support for PDF Forms through Adobe FDFTK
library.

%description fdf -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ formularzy PDF poprzez bibliotekÍ Adobe
FDFTK.

%package filepro
Summary:	filePro extension module for PHP
Summary(pl):	Modu≥ filePro dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description filepro
This is a dynamic shared object (DSO) for PHP that will add support
for read-only access to filePro databases.

%description filepro -l pl
Modu≥ PHP dodaj±cy moøliwo∂Ê dostÍpu (tylko do odczytu) do baz danych
filePro.

%package fribidi
Summary:	FriBiDi extension module for PHP
Summary(pl):	Modu≥e FriBiDi dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description fribidi
This extension is basically a wrapper for the FriBidi implementation
of the Unicode Bidi algorithm. The need for such an algorithm rises
from the bidirectional language usage done by applications.
Arabic/Hebrew embedded within English is such a case.

%description fribidi -l pl
To rozszerzenie to g≥Ûwnie interfejs do implementacji FriBiDi
algorytmu Unicode Bidi. Taki algorytm jest potrzebny w przypadku
uøywania dwukierunkowego pisma w aplikacjach - na przyk≥ad przy
tek∂cie arabskim lub hebrajskim osadzonym wewn±trz angielskiego.

%package ftp
Summary:	FTP extension module for PHP
Summary(pl):	Modu≥ FTP dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description ftp
This is a dynamic shared object (DSO) for PHP that will add FTP
support.

%description ftp -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ protoko≥u FTP.

%package gd
Summary:	GD extension module for PHP
Summary(pl):	Modu≥ GD dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}
%{?with_gif:Requires:	gd(gif)}
%{?with_gif:Provides:	%{name}-gd(gif) = %{epoch}:%{version}-%{release}}

%description gd
This is a dynamic shared object (DSO) for PHP that will add GD
support, allowing you to create and manipulate images with PHP.

%description gd -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z biblioteki GD, pozwalaj±cej na
tworzenie i obrÛbkÍ obrazkÛw.

%package gettext
Summary:	gettext extension module for PHP
Summary(pl):	Modu≥ gettext dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description gettext
This is a dynamic shared object (DSO) for PHP that will add gettext
support.

%description gettext -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ lokalizacji przez gettext.

%package gmp
Summary:	gmp extension module for PHP
Summary(pl):	Modu≥ gmp dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description gmp
This is a dynamic shared object (DSO) for PHP that will add arbitrary
length number support with GNU MP library.

%description gmp -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z biblioteki gmp do obliczeÒ na
liczbach o dowolnej d≥ugo∂ci.

%package hyperwave
Summary:	Hyperwave extension module for PHP
Summary(pl):	Modu≥ Hyperwave dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description hyperwave
This is a dynamic shared object (DSO) for PHP that will add Hyperwave
support.

%description hyperwave -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ Hyperwave.

%package iconv
Summary:	iconv extension module for PHP
Summary(pl):	Modu≥ iconv dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description iconv
This is a dynamic shared object (DSO) for PHP that will add iconv
support.

%description iconv -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ iconv.

%package imap
Summary:	IMAP extension module for PHP
Summary(pl):	Modu≥ IMAP dla PHP
Summary(pt_BR):	Um mÛdulo para aplicaÁıes PHP que usam IMAP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description imap
This is a dynamic shared object (DSO) for PHP that will add IMAP
support.

%description imap -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ skrzynek IMAP.

%description imap -l pt_BR
Um mÛdulo para aplicaÁıes PHP que usam IMAP.

%package interbase
Summary:	InterBase/Firebird database module for PHP
Summary(pl):	Modu≥ bazy danych InterBase/Firebird dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}
%{?with_interbase_inst:Autoreq:	false}

%description interbase
This is a dynamic shared object (DSO) for PHP that will add InterBase
and Firebird database support.

%description interbase -l pl
Modu≥ PHP umoøliwiaj±cy dostÍp do baz danych InterBase i Firebird.

%package java
Summary:	Java extension module for PHP
Summary(pl):	Modu≥ Javy dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description java
This is a dynamic shared object (DSO) for PHP that will add Java
support to PHP. This extension provides a simple and effective means
for creating and invoking methods on Java objects from PHP.

Note: it requires setting LD_LIBRARY_PATH to JRE directories
containing JVM libraries (e.g. libjava.so, libverify.so and libjvm.so
for Sun's JRE) before starting Apache or PHP interpreter.

%description java -l pl
Modu≥ PHP dodaj±cy wsparcie dla Javy. Umoøliwia odwo≥ywanie siÍ do
obiektÛw Javy z poziomu PHP.

Uwaga: modu≥ wymaga ustawienia LD_LIBRARY_PATH na katalogi JRE
zawieraj±ce biblioteki JVM (np. libjava.so, libverify.so i libjvm.so
dla JRE Suna) przed uruchomieniem Apache'a lub interpretera PHP.

%package ldap
Summary:	LDAP extension module for PHP
Summary(pl):	Modu≥ LDAP dla PHP
Summary(pt_BR):	Um mÛdulo para aplicaÁıes PHP que usam LDAP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description ldap
This is a dynamic shared object (DSO) for PHP that will add LDAP
support.

%description ldap -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ LDAP.

%description ldap -l pt_BR
Um mÛdulo para aplicaÁıes PHP que usam LDAP.

%package mbstring
Summary:	mbstring extension module for PHP
Summary(pl):	Modu≥ mbstring dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description mbstring
This is a dynamic shared object (DSO) for PHP that will add
multibyte string support.

%description mbstring -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ ci±gÛw znakÛw wielobajtowych.

%package mcal
Summary:	mcal extension module for PHP
Summary(pl):	Modu≥ mcal dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description mcal
This is a dynamic shared object (DSO) for PHP that will add mcal
(Modular Calendar Access Library) support.

%description mcal -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z biblioteki mcal (daj±cej dostÍp
do kalendarzy).

%package mcrypt
Summary:	mcrypt extension module for PHP
Summary(pl):	Modu≥ mcrypt dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description mcrypt
This is a dynamic shared object (DSO) for PHP that will add mcrypt
support.

%description mcrypt -l pl
Modu≥ PHP dodaj±cy moøliwo∂Ê szyfrowania poprzez bibliotekÍ mcrypt.

%package mhash
Summary:	mhash extension module for PHP
Summary(pl):	Modu≥ mhash dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description mhash
This is a dynamic shared object (DSO) for PHP that will add mhash
support.

%description mhash -l pl
Modu≥ PHP udostÍpniaj±cy funkcje mieszaj±ce z biblioteki mhash.

%package mime_magic
Summary:	mime_magic extension module for PHP
Summary(pl):	Modu≥ mime_magic dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}
Requires:	/usr/share/file/magic.mime

%description mime_magic
This PHP module adds support for MIME type lookup via file magic
numbers using magic.mime database.

%description mime_magic -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ wyszukiwania typÛw MIME wed≥ug magicznych
znacznikÛw plikÛw z uøyciem bazy danych magic.mime.

%package ming
Summary:	ming extension module for PHP
Summary(pl):	Modu≥ ming dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description ming
This is a dynamic shared object (DSO) for PHP that will add ming
(Flash - .swf files) support.

%description ming -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ plikÛw Flash (.swf) poprzez bibliotekÍ
ming.

%package mnogosearch
Summary:	mnoGoSearch extension module for PHP
Summary(pl):	Modu≥ mnoGoSearch dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description mnogosearch
This is a dynamic shared object (DSO) for PHP that will allow you to
access mnoGoSearch free search engine.

%description mnogosearch -l pl
Modu≥ PHP dodaj±cy pozwalaj±cy na dostÍp do wolnodostÍpnego silnika
wyszukiwarki mnoGoSearch.

%package msession
Summary:	msession extension module for PHP
Summary(pl):	Modu≥ msession dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description msession
This is a dynamic shared object (DSO) for PHP that will allow you to
use msession. msession is a high speed session daemon which can run
either locally or remotely. It is designed to provide consistent
session management for a PHP web farm.

%description msession -l pl
Modu≥ PHP dodaj±cy umoøliwiaj±cy korzystanie z demona msession. Jest
to demon szybkiej obs≥ugi sesji, ktÛry moøe dzia≥aÊ lokalnie lub na
innej maszynie. S≥uøy do zapewniania spÛjnej obs≥ugi sesji dla farmy
serwerÛw.

%package mssql
Summary:	MS SQL extension module for PHP
Summary(pl):	Modu≥ MS SQL dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description mssql
This is a dynamic shared object (DSO) for PHP that will add MS SQL
databases support through FreeTDS library.

%description mssql -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ baz danych MS SQL poprzez bibliotekÍ FreeTDS.

%package mysql
Summary:	MySQL database module for PHP
Summary(pl):	Modu≥ bazy danych MySQL dla PHP
Summary(pt_BR):	Um mÛdulo para aplicaÁıes PHP que usam bancos de dados MySQL
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description mysql
This is a dynamic shared object (DSO) for PHP that will add MySQL
database support.

%description mysql -l pl
Modu≥ PHP umoøliwiaj±cy dostÍp do bazy danych MySQL.

%description mysql -l pt_BR
Um mÛdulo para aplicaÁıes PHP que usam bancos de dados MySQL.

%package ncurses
Summary:	ncurses module for PHP
Summary(pl):	Modu≥ ncurses dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-program = %{epoch}:%{version}
Requires:	%{name}-program = %{epoch}:%{version}

%description ncurses
This PHP module adds support for ncurses functions (only for cli and
cgi SAPIs).

%description ncurses -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ funkcji ncurses (tylko do SAPI cli i cgi).

%package oci8
Summary:	Oracle 8 database module for PHP
Summary(pl):	Modu≥ bazy danych Oracle 8 dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}
Autoreq:	false

%description oci8
This is a dynamic shared object (DSO) for PHP that will add Oracle 7
and Oracle 8 database support through Oracle8 Call-Interface (OCI8).

%description oci8 -l pl
Modu≥ PHP umoøliwiaj±cy dostÍp do bazy danych Oracle 7 i Oracle 8
poprzez interfejs Oracle8 Call-Interface (OCI8).

%package odbc
Summary:	ODBC extension module for PHP
Summary(pl):	Modu≥ ODBC dla PHP
Summary(pt_BR):	Um mÛdulo para aplicaÁıes PHP que usam bases de dados ODBC
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}
Requires:	unixODBC >= 2.1.1-3

%description odbc
This is a dynamic shared object (DSO) for PHP that will add ODBC
support.

%description odbc -l pl
Modu≥ PHP ze wsparciem dla ODBC.

%description odbc -l pt_BR
Um mÛdulo para aplicaÁıes PHP que usam ODBC.

%package openssl
Summary:	OpenSSL extension module for PHP
Summary(pl):	Modu≥ OpenSSL dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description openssl
This is a dynamic shared object (DSO) for PHP that will add OpenSSL
support.

Warning: this is an experimental module.

%description openssl -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z biblioteki OpenSSL.

Uwaga: to jest modu≥ eksperymentalny.

%package oracle
Summary:	Oracle 7 database module for PHP
Summary(pl):	Modu≥ bazy danych Oracle 7 dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}
Autoreq:	false

%description oracle
This is a dynamic shared object (DSO) for PHP that will add Oracle 7
database support.

%description oracle -l pl
Modu≥ PHP umoøliwiaj±cy dostÍp do bazy danych Oracle 7.

%package overload
Summary:	Overload extension module for PHP
Summary(pl):	Modu≥ Overload dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description overload
This is a dynamic shared object (DSO) for PHP that will add user-space
object overloading support.

Warning: this is an experimental module.

%description overload -l pl
Modu≥ PHP umoøliwiaj±cy przeci±øanie obiektÛw.

Uwaga: to jest modu≥ eksperymentalny.

%package pcntl
Summary:	Process Control extension module for PHP
Summary(pl):	Modu≥ Process Control dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-program = %{epoch}:%{version}
Requires:	%{name}-program = %{epoch}:%{version}

%description pcntl
This is a dynamic shared object (DSO) for PHP that will add process
spawning and control support. It supports functions like fork(),
waitpid(), signal() etc.

Warning: this is an experimental module. Also, don't use it in
webserver environment!

%description pcntl -l pl
Modu≥ PHP umoøliwiaj±cy tworzenie nowych procesÛw i kontrolÍ nad nimi.
Obs≥uguje funkcje takie jak fork(), waitpid(), signal() i podobne.

Uwaga: to jest modu≥ eksperymentalny. Ponadto nie jest przeznaczony do
uøywania z serwerem WWW - nie prÛbuj tego!

%package pcre
Summary:	PCRE extension module for PHP
Summary(pl):	Modu≥ PCRE dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description pcre
This is a dynamic shared object (DSO) for PHP that will add Perl
Compatible Regular Expression support.

%description pcre -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z perlowych wyraøeÒ regularnych
(Perl Compatible Regular Expressions)

%package pdf
Summary:	PDF creation module module for PHP
Summary(pl):	Modu≥ do tworzenia plikÛw PDF dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description pdf
This is a dynamic shared object (DSO) for PHP that will add PDF
support through pdflib.

%description pdf -l pl
Modu≥ PHP umoøliwiaj±cy tworzenie plikÛw PDF. Wykorzystuje bibliotekÍ
pdflib.

%package pgsql
Summary:	PostgreSQL database module for PHP
Summary(pl):	Modu≥ bazy danych PostgreSQL dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description pgsql
This is a dynamic shared object (DSO) for PHP that will add PostgreSQL
database support.

%description pgsql -l pl
Modu≥ PHP umoøliwiaj±cy dostÍp do bazy danych PostgreSQL.

%description pgsql -l pt_BR
Um mÛdulo para aplicaÁıes PHP que usam bancos de dados postgresql.

%package posix
Summary:	POSIX extension module for PHP
Summary(pl):	Modu≥ POSIX dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description posix
This is a dynamic shared object (DSO) for PHP that will add POSIX
functions support to PHP.

%description posix -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z funkcji POSIX.

%package pspell
Summary:	pspell extension module for PHP
Summary(pl):	Modu≥ pspell dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description pspell
This is a dynamic shared object (DSO) for PHP that will add pspell
support to PHP. It allows to check the spelling of a word and offer
suggestions.

%description pspell -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z pspella. Pozwala on na
sprawdzanie pisowni s≥owa i sugerowanie poprawek.

%package qtdom
Summary:	QT DOM extension module for PHP
Summary(pl):	Modu≥ QT DOM dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description qtdom
This PHP module adds QT DOM functions support.

%description qtdom -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ funkcji QT DOM.

%package readline
Summary:	readline extension module for PHP
Summary(pl):	Modu≥ readline dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-program = %{epoch}:%{version}
Requires:	%{name}-program = %{epoch}:%{version}

%description readline
This PHP module adds support for readline functions (only for cli and
cgi SAPIs).

%description readline -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ funkcji readline (tylko do SAPI cli i cgi).

%package recode
Summary:	recode extension module for PHP
Summary(pl):	Modu≥ recode dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}
Requires:	recode >= 3.5d-3

%description recode
This is a dynamic shared object (DSO) for PHP that will add recode
support.

%description recode -l pl
Modu≥ PHP dodaj±cy moøliwo∂Ê konwersji kodowania plikÛw (poprzez
bibliotekÍ recode).

%package session
Summary:	session extension module for PHP
Summary(pl):	Modu≥ session dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description session
This is a dynamic shared object (DSO) for PHP that will add session
support.

%description session -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ sesji.

%package shmop
Summary:	Shared Memory Operations extension module for PHP
Summary(pl):	Modu≥ shmop dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description shmop
This is a dynamic shared object (DSO) for PHP that will add Shared
Memory Operations support.

Warning: this is an experimental module.

%description shmop -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z pamiÍci dzielonej.

Uwaga: to jest modu≥ eksperymentalny.

%package snmp
Summary:	SNMP extension module for PHP
Summary(pl):	Modu≥ SNMP dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description snmp
This is a dynamic shared object (DSO) for PHP that will add SNMP
support.

%description snmp -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ SNMP.

%package sockets
Summary:	sockets extension module for PHP
Summary(pl):	Modu≥ socket dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description sockets
This is a dynamic shared object (DSO) for PHP that will add sockets
support.

Warning: this is an experimental module.

%description sockets -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ gniazdek.

Uwaga: to jest modu≥ eksperymentalny.

%package sybase
Summary:	Sybase DB extension module for PHP
Summary(pl):	Modu≥ Sybase DB dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}
Obsoletes:	%{name}-sybase-ct

%description sybase
This is a dynamic shared object (DSO) for PHP that will add Sybase and
MS SQL databases support through SYBDB library.

%description sybase -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ baz danych Sybase oraz MS SQL poprzez
bibliotekÍ SYBDB.

%package sybase-ct
Summary:	Sybase-CT extension module for PHP
Summary(pl):	Modu≥ Sybase-CT dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}
Obsoletes:	%{name}-sybase

%description sybase-ct
This is a dynamic shared object (DSO) for PHP that will add Sybase and
MS SQL databases support through CT-lib.

%description sybase-ct -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ baz danych Sybase oraz MS SQL poprzez
CT-lib.

%package sysvmsg
Summary:	SysV msg extension module for PHP
Summary(pl):	Modu≥ SysV msg dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description sysvmsg
This is a dynamic shared object (DSO) for PHP that will add SysV
message queues support.

%description sysvmsg -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z kolejek komunikatÛw SysV.

%package sysvsem
Summary:	SysV sem extension module for PHP
Summary(pl):	Modu≥ SysV sem dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description sysvsem
This is a dynamic shared object (DSO) for PHP that will add SysV
semaphores support.

%description sysvsem -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z semaforÛw SysV.

%package sysvshm
Summary:	SysV shm extension module for PHP
Summary(pl):	Modu≥ SysV shm dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description sysvshm
This is a dynamic shared object (DSO) for PHP that will add SysV
Shared Memory support.

%description sysvshm -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z pamiÍci dzielonej SysV.

%package wddx
Summary:	wddx extension module for PHP
Summary(pl):	Modu≥ wddx dla PHP
Group:		Libraries
PreReq:		%{name}-session = %{epoch}:%{version}
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description wddx
This is a dynamic shared object (DSO) for PHP that will add wddx
support.

%description wddx -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z wddx.

%package xml
Summary:	XML extension module for PHP
Summary(pl):	Modu≥ XML dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description xml
This is a dynamic shared object (DSO) for PHP that will add XML
support. This extension lets you create XML parsers and then define
handlers for different XML events.

%description xml -l pl
Modu≥ PHP umoøliwiaj±cy parsowanie plikÛw XML i obs≥ugÍ zdarzeÒ
zwi±zanych z tymi plikami. Pozwala on tworzyÊ analizatory XML-a i
nastÍpnie definiowaÊ procedury obs≥ugi dla rÛønych zdarzeÒ XML.

%package xmlrpc
Summary:	xmlrpc extension module for PHP
Summary(pl):	Modu≥ xmlrpc dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description xmlrpc
This is a dynamic shared object (DSO) for PHP that will add XMLRPC
support.

Warning: this is an experimental module.

%description xmlrpc -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ XMLRPC.

Uwaga: to jest modu≥ eksperymentalny.

%package xslt
Summary:	xslt extension module for PHP
Summary(pl):	Modu≥ xslt dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description xslt
This is a dynamic shared object (DSO) for PHP that will add xslt
support.

%description xslt -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z technologii xslt.

%package yaz
Summary:	yaz extension module for PHP
Summary(pl):	Modu≥ yaz dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}
Requires:	yaz >= 1.9

%description yaz
This is a dynamic shared object (DSO) for PHP that will add yaz
support. yaz toolkit implements the Z39.50 protocol for information
retrieval.

%description yaz -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z yaz - implementacji protoko≥u
Z39.50 s≥uø±cego do pozyskiwania informacji.

%package yp
Summary:	NIS (yp) extension module for PHP
Summary(pl):	Modu≥ NIS (yp) dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description yp
This is a dynamic shared object (DSO) for PHP that will add NIS
(Yellow Pages) support.

%description yp -l pl
Modu≥ PHP dodaj±cy wsparcie dla NIS (Yellow Pages).

%package zip
Summary:	zip extension module for PHP
Summary(pl):	Modu≥ zip dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description zip
This is a dynamic shared object (DSO) for PHP that will add ZZipLib
(read-only access to ZIP archives) support.

%description zip -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z bibliotekli ZZipLib
(pozwalaj±cej na odczyt archiwÛw ZIP).

%package zlib
Summary:	Zlib extension module for PHP
Summary(pl):	Modu≥ zlib dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}
Requires:	%{name}-common = %{epoch}:%{version}

%description zlib
This is a dynamic shared object (DSO) for PHP that will add zlib
compression support to PHP.

%description zlib -l pl
Modu≥ PHP umoøliwiaj±cy uøywanie kompresji zlib.

%package pear
Summary:	PEAR - PHP Extension and Application Repository
Summary(pl):	PEAR - Rozszerzenie PHP i Repozytorium Aplikacji
Group:		Development/Languages/PHP
Requires:	%{name}-pcre = %{epoch}:%{version}
Requires:	%{name}-xml = %{epoch}:%{version}
Obsoletes:	%{name}-pear-additional_classes

%description pear
PEAR - PHP Extension and Application Repository.

Please note that this package provides only basic directory structure.
If you want to use base PEAR classes (PEAR.php, PEAR/*.php), that come
with PHP, please install appropriate php-pear-* (php-pear-PEAR,
php-PEAR-Archive_Tar, etc) packages.

%description pear -l pl
PEAR (PHP Extension and Application Repository) - Rozszerzenie PHP i
repozytorium aplikacji.

PamiÍtaj, øe ten pakiet dostarcza tylko podstawow± strukturÍ
katalogÛw. Je∂li chcesz uøyÊ podstawowych klas PEAR (PEAR.php
PEAR/*.php), dostarczanych z PHP, zainstaluj odpowiednie pakiety
php-pear-* (php-pear-PEAR, php-pear-Archive_Tar, itp).

%prep
%setup -q -n %{name}-%{_version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
cp php.ini-dist php.ini
%patch17 -p1
# for ac2.53b/am1.6b - AC_LANG_CXX has AM_CONDITIONAL, so cannot be invoked
# conditionally...
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%ifarch amd64
%patch31 -p1
%endif

%build
CFLAGS="%{rpmcflags} -DEAPI=1 -I/usr/X11R6/include"
EXTENSION_DIR="%{extensionsdir}"; export EXTENSION_DIR
./buildconf --force
%{__libtoolize}
%{__aclocal}
%{__autoconf}
PROG_SENDMAIL="/usr/lib/sendmail"; export PROG_SENDMAIL
for i in fcgi cgi cli apxs ; do
%configure \
	`[ $i = cgi ] && echo --enable-discard-path` \
	`[ $i = cli ] && echo --disable-cgi` \
	`[ $i = fcgi ] && echo --enable-fastcgi --with-fastcgi=/usr` \
%if %{_apache2}
	`[ $i = apxs ] && echo --with-apxs2=%{apxs}` \
%else
	`[ $i = apxs ] && echo --with-apxs=%{apxs}` \
%endif
	--with-config-file-path=%{_sysconfdir} \
	--with-exec-dir=%{_bindir} \
	--%{!?debug:dis}%{?debug:en}able-debug \
	--enable-memory-limit \
	--enable-bcmath=shared \
	--enable-calendar=shared \
	--enable-ctype=shared \
	--enable-dba=shared \
	--enable-dbx=shared \
	--enable-dio=shared \
	--enable-exif=shared \
	--enable-ftp=shared \
	--enable-filepro=shared \
	--enable-gd-native-ttf \
	--enable-magic-quotes \
	--enable-mbstring=shared,all --enable-mbregex \
	--enable-overload=shared \
	--enable-pcntl=shared \
	--enable-posix=shared \
	--enable-session \
	--enable-shared \
	--enable-shmop=shared \
	--enable-sysvmsg=shared \
	--enable-sysvsem=shared \
	--enable-sysvshm=shared \
	--enable-track-vars \
	--enable-trans-sid \
	--enable-safe-mode \
	--enable-sockets=shared \
	--enable-ucd-snmp-hack \
	%{?with_wddx:--enable-wddx=shared} \
	%{!?with_xml:--disable-xml}%{?with_xml:--enable-xml=shared} \
	%{?with_xslt:--enable-xslt=shared} \
	--enable-yp=shared \
	--with-bz2=shared \
	%{?with_cpdf:--with-cpdflib=shared} \
	--with-crack=shared \
	%{!?with_curl:--without-curl}%{?with_curl:--with-curl=shared} \
	--with-db=shared \
	%{?with_db3:--with-db3}%{!?with_db3:--with-db4} \
	--with-dbase=shared \
	%{?with_xml:--with-dom=shared} \
	%{?with_domxslt:--with-dom-xslt=shared --with-dom-exslt=shared} \
%if %{with xml} || %{with xmlrpc}
	--with-expat-dir=shared,/usr \
%else
	--without-expat-dir \
%endif
	%{?with_fdf:--with-fdftk=shared} \
	%{?with_fribidi:--with-fribidi=shared} \
	--with-iconv=shared \
	--with-filepro=shared \
	--with-freetype-dir=shared \
	--with-gettext=shared \
	--with-gd=shared,/usr \
	--with-gdbm \
	--with-gmp=shared \
	--with-hyperwave=shared \
	%{?with_imap:--with-imap=shared --with-imap-ssl} \
	%{?with_interbase:--with-interbase=shared%{!?with_interbase_inst:,/usr}} \
	%{?with_java:--with-java=/usr/lib/java} \
	--with-jpeg-dir=shared,/usr \
	%{?with_ldap:--with-ldap=shared} \
	--with-mcal=shared,/usr \
	--with-mcrypt=shared \
	%{?with_mhash:--with-mhash=shared} \
	--with-mime-magic=shared,/usr/share/file/magic.mime \
	%{?with_ming:--with-ming=shared} \
	%{?with_mm:--with-mm} \
	%{!?with_mnogosearch:--without-mnogosearch}%{?with_mnogosearch:--with-mnogosearch=shared,/usr} \
	%{?with_msession:--with-msession=shared}%{!?with_msession:--without-msession} \
	%{?with_mssql:--with-mssql=shared} \
	--with-mysql=shared,/usr \
	--with-mysql-sock=/var/lib/mysql/mysql.sock \
	--with-ncurses=shared \
	%{?with_oci8:--with-oci8=shared} \
	%{?with_openssl:--with-openssl} \
	%{?with_oracle:--with-oracle=shared} \
	%{!?with_pcre:--without-pcre-regex}%{?with_pcre:--with-pcre-regex=shared} \
	%{?with_pdf:--with-pdflib=shared} \
	--with-pear=%{php_pear_dir} \
	%{!?with_pgsql:--without-pgsql}%{?with_pgsql:--with-pgsql=shared,/usr} \
	--with-png-dir=shared,/usr \
	%{?with_pspell:--with-pspell=shared} \
	--with-readline=shared \
	%{?with_recode:--with-recode=shared} \
	--with-regex=php \
	%{?with_qtdom:--with-qtdom=shared} \
	--without-sablot-js \
	%{?with_snmp:--with-snmp=shared} \
	%{?with_sybase:--with-sybase-ct=shared,/usr --with-sybase=shared,/usr} \
	--with-t1lib=shared \
	--with-tiff-dir=shared,/usr \
	%{?with_odbc:--with-unixODBC=shared} \
	%{!?with_xmlrpc:--without-xmlrpc}%{?with_xmlrpc:--with-xmlrpc=shared,/usr} \
	%{?with_xslt:--with-xslt-sablot=shared} \
	%{?with_yaz:--with-yaz=shared} \
	--with-zip=shared \
	--with-zlib=shared \
	--with-zlib-dir=shared,/usr
# --with-openssl=shared not supported in 4.3.2

cp -f Makefile Makefile.$i
# left for debugging purposes
cp -f main/php_config.h php_config.h.$i
done

# for now session_mm doesn't work with shared session module...
# --enable-session=shared
# %{!?with_mm:--with-mm=shared,no}%{?with_mm:--with-mm=shared}

# TODO:
#	--with-qtdom=shared

%{__make}

# fix install paths, avoid evil rpaths
%{__perl} -pi -e "s|^libdir=.*|libdir='%{_libdir}'|" libphp_common.la
%{__perl} -pi -e "s|^libdir=.*|libdir='%{_libdir}/apache'|" libphp4.la
%{__perl} -pi -e 's|^(relink_command=.* -rpath )[^ ]*/libs |$1%{_libdir}/apache |' libphp4.la

# for fcgi: -DDISCARD_PATH=0 -DENABLE_PATHINFO_CHECK=1 -DFORCE_CGI_REDIRECT=0
# -DHAVE_FILENO_PROTO=1 -DHAVE_FPOS=1 -DHAVE_LIBNSL=1(die) -DHAVE_SYS_PARAM_H=1
# -DPHP_FASTCGI=1 -DPHP_FCGI_STATIC=1 -DPHP_WRITE_STDOUT=1

%{__make} sapi/cgi/php -f Makefile.fcgi \
	CFLAGS_CLEAN="%{rpmcflags} -DDISCARD_PATH=0 -DENABLE_PATHINFO_CHECK=1 -DFORCE_CGI_REDIRECT=0 -DHAVE_FILENO_PROTO=1 -DHAVE_FPOS=1 -DHAVE_LIBNSL=1 -DHAVE_SYS_PARAM_H=1 -DPHP_FASTCGI=1 -DPHP_FCGI_STATIC=1 -DPHP_WRITE_STDOUT=1"
cp -r sapi/cgi sapi/fcgi
rm -rf sapi/cgi/.libs sapi/cgi/*.lo

# notes:
# -DENABLE_CHROOT_FUNC=1 (cgi,fcgi) is used in ext/standard/dir.c (libphp_common)
# -DPHP_WRITE_STDOUT is used also for cli, but not set by its config.m4

%{__make} sapi/cgi/php -f Makefile.cgi \
	CFLAGS_CLEAN="%{rpmcflags} -DDISCARD_PATH=1 -DENABLE_PATHINFO_CHECK=1 -DFORCE_CGI_REDIRECT=0 -DPHP_WRITE_STDOUT=1"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/{php,apache},%{_sysconfdir}/{apache,cgi}} \
	$RPM_BUILD_ROOT%{httpdir}/icons \
	$RPM_BUILD_ROOT{%{_sbindir},%{_bindir}} \
	$RPM_BUILD_ROOT/var/run/php \
	$RPM_BUILD_ROOT/etc/httpd/httpd.conf

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	INSTALL_IT="\$(LIBTOOL) --mode=install install libphp_common.la $RPM_BUILD_ROOT%{_libdir} ; \$(LIBTOOL) --mode=install install libphp4.la $RPM_BUILD_ROOT%{_libdir}/apache ; \$(LIBTOOL) --mode=install install sapi/cgi/php $RPM_BUILD_ROOT%{_bindir}/php.cgi ; \$(LIBTOOL) --mode=install install sapi/fcgi/php $RPM_BUILD_ROOT%{_bindir}/php.fcgi" \
	INSTALL_CLI="\$(LIBTOOL) --mode=install install sapi/cli/php $RPM_BUILD_ROOT%{_bindir}/php.cli"

# compatibility (/usr/bin/php used to be CGI SAPI)
ln -sf php.cgi $RPM_BUILD_ROOT%{_bindir}/php

%{?with_java:install ext/java/php_java.jar $RPM_BUILD_ROOT%{extensionsdir}}

install php.ini	$RPM_BUILD_ROOT%{_sysconfdir}/php.ini
install %{SOURCE6} %{SOURCE7} %{SOURCE8} $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/php-cgi-fcgi.ini
install %{SOURCE2} php.gif $RPM_BUILD_ROOT%{httpdir}/icons
install %{SOURCE4} $RPM_BUILD_ROOT%{_sbindir}
install %{SOURCE5} $RPM_BUILD_ROOT/etc/httpd/httpd.conf/70_mod_php.conf

install %{SOURCE1} .

cp -f Zend/LICENSE{,.Zend}

# Directories created for pear:
install -d $RPM_BUILD_ROOT%{php_pear_dir}/{Archive,Console,Crypt,HTML/Template,Image,Net,Science,XML}

%ifarch amd64
ln -sf ../../lib/%{name}/build $RPM_BUILD_ROOT%{_libdir}/%{name}/build
%endif

rm -f $RPM_BUILD_ROOT%{_libdir}/apache/libphp4.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
%if ! %{_apache2}
%{__perl} -pi -e 's|^#AddType application/x-httpd-php \.php|AddType application/x-httpd-php .php|' \
	/etc/httpd/httpd.conf
%{apxs} -e -a -n php4 %{_pkglibdir}/libphp4.so 1>&2
%endif
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%if %{_apache2}
%postun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi
%else
%preun
if [ "$1" = "0" ]; then
	%{apxs} -e -A -n php4 %{_pkglibdir}/libphp4.so 1>&2
	%{__perl} -pi -e \
		's|^AddType application/x-httpd-php \.php|#AddType application/x-httpd-php .php|' \
		/etc/httpd/httpd.conf
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi
%endif

%post	common -p /sbin/ldconfig
%postun	common -p /sbin/ldconfig

%post bcmath
%{_sbindir}/php-module-install install bcmath %{_sysconfdir}/php.ini

%preun bcmath
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove bcmath %{_sysconfdir}/php.ini
fi

%post bzip2
%{_sbindir}/php-module-install install bz2 %{_sysconfdir}/php.ini

%preun bzip2
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove bz2 %{_sysconfdir}/php.ini
fi

%post calendar
%{_sbindir}/php-module-install install calendar %{_sysconfdir}/php.ini

%preun calendar
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove calendar %{_sysconfdir}/php.ini
fi

%post cpdf
%{_sbindir}/php-module-install install cpdf %{_sysconfdir}/php.ini

%preun cpdf
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove cpdf %{_sysconfdir}/php.ini
fi

%post crack
%{_sbindir}/php-module-install install crack %{_sysconfdir}/php.ini

%preun crack
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove crack %{_sysconfdir}/php.ini
fi

%post ctype
%{_sbindir}/php-module-install install ctype %{_sysconfdir}/php.ini

%preun ctype
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove ctype %{_sysconfdir}/php.ini
fi

%post curl
%{_sbindir}/php-module-install install curl %{_sysconfdir}/php.ini

%preun curl
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove curl %{_sysconfdir}/php.ini
fi

%post db
%{_sbindir}/php-module-install install db %{_sysconfdir}/php.ini

%preun db
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove db %{_sysconfdir}/php.ini
fi

%post dba
%{_sbindir}/php-module-install install dba %{_sysconfdir}/php.ini

%preun dba
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove dba %{_sysconfdir}/php.ini
fi

%post dbase
%{_sbindir}/php-module-install install dbase %{_sysconfdir}/php.ini

%preun dbase
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove dbase %{_sysconfdir}/php.ini
fi

%post dbx
%{_sbindir}/php-module-install install dbx %{_sysconfdir}/php.ini

%preun dbx
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove dbx %{_sysconfdir}/php.ini
fi

%post dio
%{_sbindir}/php-module-install install dio %{_sysconfdir}/php.ini

%preun dio
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove dio %{_sysconfdir}/php.ini
fi

%post domxml
%{_sbindir}/php-module-install install domxml %{_sysconfdir}/php.ini

%preun domxml
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove domxml %{_sysconfdir}/php.ini
fi

%post exif
%{_sbindir}/php-module-install install exif %{_sysconfdir}/php.ini

%preun exif
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove exif %{_sysconfdir}/php.ini
fi

%post fdf
%{_sbindir}/php-module-install install fdf %{_sysconfdir}/php.ini

%preun fdf
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove fdf %{_sysconfdir}/php.ini
fi

%post filepro
%{_sbindir}/php-module-install install filepro %{_sysconfdir}/php.ini

%preun filepro
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove filepro %{_sysconfdir}/php.ini
fi

%post fribidi
%{_sbindir}/php-module-install install fribidi %{_sysconfdir}/php.ini

%preun fribidi
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove fribidi %{_sysconfdir}/php.ini
fi

%post ftp
%{_sbindir}/php-module-install install ftp %{_sysconfdir}/php.ini

%preun ftp
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove ftp %{_sysconfdir}/php.ini
fi

%post gd
%{_sbindir}/php-module-install install gd %{_sysconfdir}/php.ini

%preun gd
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove gd %{_sysconfdir}/php.ini
fi

%post gettext
%{_sbindir}/php-module-install install gettext %{_sysconfdir}/php.ini

%preun gettext
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove gettext %{_sysconfdir}/php.ini
fi

%post gmp
%{_sbindir}/php-module-install install gmp %{_sysconfdir}/php.ini

%preun gmp
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove gmp %{_sysconfdir}/php.ini
fi

%post hyperwave
%{_sbindir}/php-module-install install hyperwave %{_sysconfdir}/php.ini

%preun hyperwave
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove hyperwave %{_sysconfdir}/php.ini
fi

%post iconv
%{_sbindir}/php-module-install install iconv %{_sysconfdir}/php.ini

%preun iconv
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove iconv %{_sysconfdir}/php.ini
fi

%post imap
%{_sbindir}/php-module-install install imap %{_sysconfdir}/php.ini

%preun imap
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove imap %{_sysconfdir}/php.ini
fi

%post interbase
%{_sbindir}/php-module-install install interbase %{_sysconfdir}/php.ini

%preun interbase
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove interbase %{_sysconfdir}/php.ini
fi

%post java
%{_sbindir}/php-module-install install java %{_sysconfdir}/php.ini

%preun java
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove java %{_sysconfdir}/php.ini
fi

%post ldap
%{_sbindir}/php-module-install install ldap %{_sysconfdir}/php.ini

%preun ldap
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove ldap %{_sysconfdir}/php.ini
fi

%post mbstring
%{_sbindir}/php-module-install install mbstring %{_sysconfdir}/php.ini

%preun mbstring
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove mbstring %{_sysconfdir}/php.ini
fi

%post mcal
%{_sbindir}/php-module-install install mcal %{_sysconfdir}/php.ini

%preun mcal
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove mcal %{_sysconfdir}/php.ini
fi

%post mcrypt
%{_sbindir}/php-module-install install mcrypt %{_sysconfdir}/php.ini

%preun mcrypt
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove mcrypt %{_sysconfdir}/php.ini
fi

%post mhash
%{_sbindir}/php-module-install install mhash %{_sysconfdir}/php.ini

%preun mhash
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove mhash %{_sysconfdir}/php.ini
fi

%post mime_magic
%{_sbindir}/php-module-install install mime_magic %{_sysconfdir}/php.ini

%preun mime_magic
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove mime_magic %{_sysconfdir}/php.ini
fi

%post ming
%{_sbindir}/php-module-install install ming %{_sysconfdir}/php.ini

%preun ming
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove ming %{_sysconfdir}/php.ini
fi

%post mnogosearch
%{_sbindir}/php-module-install install mnogosearch %{_sysconfdir}/php.ini

%preun mnogosearch
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove mnogosearch %{_sysconfdir}/php.ini
fi

%post msession
%{_sbindir}/php-module-install install msession %{_sysconfdir}/php.ini

%preun msession
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove msession %{_sysconfdir}/php.ini
fi

%post mssql
%{_sbindir}/php-module-install install mssql %{_sysconfdir}/php.ini

%preun mssql
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove mssql %{_sysconfdir}/php.ini
fi

%post mysql
%{_sbindir}/php-module-install install mysql %{_sysconfdir}/php.ini

%preun mysql
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove mysql %{_sysconfdir}/php.ini
fi

%post ncurses
if [ -f %{_sysconfdir}/php-cgi.ini ]; then
%{_sbindir}/php-module-install install ncurses %{_sysconfdir}/php-cgi.ini
fi
if [ -f %{_sysconfdir}/php-cli.ini ]; then
%{_sbindir}/php-module-install install ncurses %{_sysconfdir}/php-cli.ini
fi

%preun ncurses
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/php-cgi.ini ]; then
	%{_sbindir}/php-module-install remove ncurses %{_sysconfdir}/php-cgi.ini
	fi
	if [ -f %{_sysconfdir}/php-cli.ini ]; then
	%{_sbindir}/php-module-install remove ncurses %{_sysconfdir}/php-cli.ini
	fi
fi

%post oci8
%{_sbindir}/php-module-install install oci8 %{_sysconfdir}/php.ini

%preun oci8
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove oci8 %{_sysconfdir}/php.ini
fi

%post odbc
%{_sbindir}/php-module-install install odbc %{_sysconfdir}/php.ini

%preun odbc
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove odbc %{_sysconfdir}/php.ini
fi

%post openssl
%{_sbindir}/php-module-install install openssl %{_sysconfdir}/php.ini

%preun openssl
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove openssl %{_sysconfdir}/php.ini
fi

%post oracle
%{_sbindir}/php-module-install install oracle %{_sysconfdir}/php.ini

%preun oracle
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove oracle %{_sysconfdir}/php.ini
fi

%post overload
%{_sbindir}/php-module-install install overload %{_sysconfdir}/php.ini

%preun overload
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove overload %{_sysconfdir}/php.ini
fi

%post pcntl
if [ -f %{_sysconfdir}/php-cgi.ini ]; then
%{_sbindir}/php-module-install install pcntl %{_sysconfdir}/php-cgi.ini
fi
if [ -f %{_sysconfdir}/php-cli.ini ]; then
%{_sbindir}/php-module-install install pcntl %{_sysconfdir}/php-cli.ini
fi

%preun pcntl
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/php-cgi.ini ]; then
	%{_sbindir}/php-module-install remove pcntl %{_sysconfdir}/php-cgi.ini
	fi
	if [ -f %{_sysconfdir}/php-cli.ini ]; then
	%{_sbindir}/php-module-install remove pcntl %{_sysconfdir}/php-cli.ini
	fi
fi

%post pcre
%{_sbindir}/php-module-install install pcre %{_sysconfdir}/php.ini

%preun pcre
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove pcre %{_sysconfdir}/php.ini
fi

%post pdf
%{_sbindir}/php-module-install install pdf %{_sysconfdir}/php.ini

%preun pdf
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove pdf %{_sysconfdir}/php.ini
fi

%post pgsql
%{_sbindir}/php-module-install install pgsql %{_sysconfdir}/php.ini

%preun pgsql
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove pgsql %{_sysconfdir}/php.ini
fi

%post posix
%{_sbindir}/php-module-install install posix %{_sysconfdir}/php.ini

%preun posix
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove posix %{_sysconfdir}/php.ini
fi

%post pspell
%{_sbindir}/php-module-install install pspell %{_sysconfdir}/php.ini

%preun pspell
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove pspell %{_sysconfdir}/php.ini
fi

%post qtdom
%{_sbindir}/php-module-install install qtdom %{_sysconfdir}/php.ini

%preun qtdom
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove qtdom %{_sysconfdir}/php.ini
fi

%post readline
if [ -f %{_sysconfdir}/php-cgi.ini ]; then
%{_sbindir}/php-module-install install readline %{_sysconfdir}/php-cgi.ini
fi
if [ -f %{_sysconfdir}/php-cli.ini ]; then
%{_sbindir}/php-module-install install readline %{_sysconfdir}/php-cli.ini
fi

%preun readline
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/php-cgi.ini ]; then
	%{_sbindir}/php-module-install remove readline %{_sysconfdir}/php-cgi.ini
	fi
	if [ -f %{_sysconfdir}/php-cli.ini ]; then
	%{_sbindir}/php-module-install remove readline %{_sysconfdir}/php-cli.ini
	fi
fi

%post recode
%{_sbindir}/php-module-install install recode %{_sysconfdir}/php.ini

%preun recode
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove recode %{_sysconfdir}/php.ini
fi

%post session
%{_sbindir}/php-module-install install session %{_sysconfdir}/php.ini

%preun session
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove session %{_sysconfdir}/php.ini
fi

%post shmop
%{_sbindir}/php-module-install install shmop %{_sysconfdir}/php.ini

%preun shmop
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove shmop %{_sysconfdir}/php.ini
fi

%post snmp
%{_sbindir}/php-module-install install snmp %{_sysconfdir}/php.ini

%preun snmp
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove snmp %{_sysconfdir}/php.ini
fi

%post sockets
%{_sbindir}/php-module-install install sockets %{_sysconfdir}/php.ini

%preun sockets
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove sockets %{_sysconfdir}/php.ini
fi

%post sybase
%{_sbindir}/php-module-install install sybase %{_sysconfdir}/php.ini

%preun sybase
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove sybase %{_sysconfdir}/php.ini
fi

%post sybase-ct
%{_sbindir}/php-module-install install sybase_ct %{_sysconfdir}/php.ini

%preun sybase-ct
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove sybase_ct %{_sysconfdir}/php.ini
fi

%post sysvmsg
%{_sbindir}/php-module-install install sysvmsg %{_sysconfdir}/php.ini

%preun sysvmsg
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove sysvmsg %{_sysconfdir}/php.ini
fi

%post sysvsem
%{_sbindir}/php-module-install install sysvsem %{_sysconfdir}/php.ini

%preun sysvsem
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove sysvsem %{_sysconfdir}/php.ini
fi

%post sysvshm
%{_sbindir}/php-module-install install sysvshm %{_sysconfdir}/php.ini

%preun sysvshm
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove sysvshm %{_sysconfdir}/php.ini
fi

%post wddx
%{_sbindir}/php-module-install install wddx %{_sysconfdir}/php.ini

%preun wddx
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove wddx %{_sysconfdir}/php.ini
fi

%post xml
%{_sbindir}/php-module-install install xml %{_sysconfdir}/php.ini

%preun xml
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove xml %{_sysconfdir}/php.ini
fi

%post xmlrpc
%{_sbindir}/php-module-install install xmlrpc %{_sysconfdir}/php.ini

%preun xmlrpc
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove xmlrpc %{_sysconfdir}/php.ini
fi

%post xslt
%{_sbindir}/php-module-install install xslt %{_sysconfdir}/php.ini

%preun xslt
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove xslt %{_sysconfdir}/php.ini
fi

%post yaz
%{_sbindir}/php-module-install install yaz %{_sysconfdir}/php.ini

%preun yaz
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove yaz %{_sysconfdir}/php.ini
fi

%post yp
%{_sbindir}/php-module-install install yp %{_sysconfdir}/php.ini

%preun yp
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove yp %{_sysconfdir}/php.ini
fi

%post zip
%{_sbindir}/php-module-install install zip %{_sysconfdir}/php.ini

%preun zip
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove zip %{_sysconfdir}/php.ini
fi

%post zlib
%{_sbindir}/php-module-install install zlib %{_sysconfdir}/php.ini

%preun zlib
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove zlib %{_sysconfdir}/php.ini
fi

%files
%defattr(644,root,root,755)
%if %{_apache2}
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/httpd/httpd.conf/*_mod_php.conf
%endif
%attr(755,root,root) %{_libdir}/apache/libphp4.so
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/php-apache.ini

%files fcgi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/php.fcgi
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/php-cgi-fcgi.ini

%files cgi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/php.cgi
%attr(755,root,root) %{_bindir}/php
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/php-cgi.ini

%files cli
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/php.cli
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/php-cli.ini
%{_mandir}/man1/php.1*

%files common
%defattr(644,root,root,755)
%doc php.ini-*
%doc CODING_STANDARDS CREDITS Zend/ZEND_CHANGES
%doc LICENSE Zend/LICENSE.Zend EXTENSIONS NEWS TODO*
%doc README.EXT_SKEL README.SELF-CONTAINED-EXTENSIONS

%dir %{_sysconfdir}
%attr(644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/php.ini
%attr(730,root,http) %dir %verify(not group mode) /var/run/php

%{httpdir}/icons/*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/libphp_common-*.so
%dir %{extensionsdir}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/phpextdist
%attr(755,root,root) %{_bindir}/phpize
%attr(755,root,root) %{_bindir}/php-config
%attr(755,root,root) %{_libdir}/libphp_common.so
%{_libdir}/libphp_common.la
%{_includedir}/php
%{_libdir}/php/build
%ifarch amd64
%{_ulibdir}/php/build
%endif

%files bcmath
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/bcmath.so

%files bzip2
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/bz2.so

%files calendar
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/calendar.so

%if %{with cpdf}
%files cpdf
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/cpdf.so
%endif

%files crack
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/crack.so

%files ctype
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/ctype.so

%if %{with curl}
%files curl
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/curl.so
%endif

%files db
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/db.so

%files dba
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/dba.so

%files dbase
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/dbase.so

%files dbx
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/dbx.so

%files dio
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/dio.so

%if %{with xml}
%files domxml
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/domxml.so
%endif

%if %{with fdf}
%files fdf
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/fdf.so
%endif

%files exif
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/exif.so

%files filepro
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/filepro.so

%if %{with fribidi}
%files fribidi
%defattr(644,root,root,755)
%doc ext/fribidi/{CREDITS,README}
%attr(755,root,root) %{extensionsdir}/fribidi.so
%endif

%files ftp
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/ftp.so

%files gd
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/gd.so

%files gettext
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/gettext.so

%files gmp
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/gmp.so

%files hyperwave
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/hyperwave.so

%files iconv
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/iconv.so

%if %{with imap}
%files imap
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/imap.so
%endif

%if %{with interbase}
%files interbase
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/interbase.so
%endif

%if %{with java}
%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/java.so
%{extensionsdir}/php_java.jar
%endif

%if %{with ldap}
%files ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/ldap.so
%endif

%files mbstring
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/mbstring.so

%files mcal
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/mcal.so

%files mcrypt
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/mcrypt.so

%if %{with mhash}
%files mhash
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/mhash.so
%endif

%files mime_magic
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/mime_magic.so

%if %{with ming}
%files ming
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/ming.so
%endif

%if %{with mnogosearch}
%files mnogosearch
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/mnogosearch.so
%endif

%if %{with msession}
%files msession
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/msession.so
%endif

%if %{with mssql}
%files mssql
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/mssql.so
%endif

%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/mysql.so

%files ncurses
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/ncurses.so

%if %{with oci8}
%files oci8
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/oci8.so
%endif

%if %{with odbc}
%files odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/odbc.so
%endif

# shared openssl module not supported in 4.3.2
#%if %{with openssl}
#%files openssl
#%defattr(644,root,root,755)
#%attr(755,root,root) %{extensionsdir}/openssl.so
#%endif

%if %{with oracle}
%files oracle
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/oracle.so
%endif

%files overload
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/overload.so

%files pcntl
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/pcntl.so

%if %{with pcre}
%files pcre
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/pcre.so
%endif

%if %{with pdf}
%files pdf
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/pdf.so
%endif

%if %{with pgsql}
%files pgsql
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/pgsql.so
%endif

%files posix
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/posix.so

%if %{with pspell}
%files pspell
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/pspell.so
%endif

%if %{with qtdom}
%files qtdom
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/qtdom.so
%endif

%files readline
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/readline.so

%if %{with recode}
%files recode
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/recode.so
%endif

# session_mm doesn't work with shared session
#%files session
#%defattr(644,root,root,755)
#%attr(755,root,root) %{extensionsdir}/session.so

%files shmop
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/shmop.so

%if %{with snmp}
%files snmp
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/snmp.so
%endif

%files sockets
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/sockets.so

%if %{with sybase}
%files sybase
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/sybase.so

%files sybase-ct
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/sybase_ct.so
%endif

%files sysvmsg
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/sysvmsg.so

%files sysvsem
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/sysvsem.so

%files sysvshm
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/sysvshm.so

%if %{with wddx}
%files wddx
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/wddx.so
%endif

%if %{with xml}
%files xml
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/xml.so
%endif

%if %{with xmlrpc}
%files xmlrpc
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/xmlrpc.so
%endif

%if %{with xslt}
%files xslt
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/xslt.so
%endif

%if %{with yaz}
%files yaz
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/yaz.so
%endif

%files yp
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/yp.so

%files zip
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/zip.so

%files zlib
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/zlib.so

%files pear
%defattr(644,root,root,755)
%dir %{php_pear_dir}
%dir %{php_pear_dir}/Archive
%dir %{php_pear_dir}/Console
%dir %{php_pear_dir}/Crypt
%dir %{php_pear_dir}/HTML
%dir %{php_pear_dir}/HTML/Template
%dir %{php_pear_dir}/Image
%dir %{php_pear_dir}/Net
%dir %{php_pear_dir}/Science
%dir %{php_pear_dir}/XML
