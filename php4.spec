#
# TODO:
# - fastcgi option in cgi SAPI? or separate fcgi SAPI?
#
# Automatic pear requirements finding:
%include	/usr/lib/rpm/macros.php

%define	_apache2	%(rpm -q apache-devel 2> /dev/null | grep -Eq '\\-2\\.[0-9]+\\.' && echo 1 || echo 0)
%define		apxs		/usr/sbin/apxs

%if %{_apache2}
%define _without_recode 1
%define _without_mm 1
%endif

%ifnarch %{ix86}
%define _without_interbase 1
%define _without_msession 1
%endif

# Conditional build:
# _with_db3		- use db3 packages instead of db (4.x) for Berkeley DB support
# _with_interbase_inst	- use InterBase install., not Firebird	(BR: proprietary libs)
# _with_java		- with Java extension module		(BR: jdk)
# _with_oci8		- with Oracle oci8 extension module	(BR: proprietary libs)
# _with_oracle		- with oracle extension module		(BR: proprietary libs)
# _with_pcntl		- with pcntl extension module		(problems: SEGV on exit)
# _without_cpdf		- without cpdf extension module
# _without_curl		- without CURL extension module
# _without_domxslt	- without DOM XSLT/EXSLT support in DOM XML extension module
# _without_gif		- build GD extension module with gd library without GIF support
# _without_imap		- without IMAP extension module
# _without_interbase	- without InterBase extension module
# _without_ldap		- without LDAP extension module
# _without_mhash	- without mhash extension module
# _without_ming		- without ming extension module
# _without_mm		- without mm support for session storage
# _without_mnogosearch	- without mnogosearch extension module
# _without_msession	- without msession extension module
# _without_odbc		- without ODBC extension module
# _without_openssl	- without OpenSSL support and OpenSSL extension module
# _without_pcre		- without PCRE extension module
# _without_pdf		- without PDF extension module
# _without_pgsql	- without PostgreSQL extension module
# _without_pspell	- without pspell extension module
# _without_recode	- without recode extension module
# _without_snmp		- without SNMP extension module
# _without_sybase_ct	- without Sybase-CT extension module
# _without_wddx		- without WDDX extension module
# _without_xmlrpc	- without XML-RPC extension module
# _without_xml		- without XML extension module
# _without_xslt		- without XSLT extension module
# _without_yaz		- without YAZ extension module

Summary:	The PHP HTML-embedded scripting language for use with Apache
Summary(fr):	Le langage de script embarque-HTML PHP pour Apache
Summary(pl):	JÍzyk skryptowy PHP -- uøywany wraz z serwerem Apache
Summary(pt_BR):	A linguagem de script PHP
Summary(ru):	PHP ˜≈“”…… 4 -- —⁄ŸÀ –“≈–“œ√≈””…“œ◊¡Œ…— HTML-∆¡ Ãœ◊, ◊Ÿ–œÃŒ—≈ÕŸ  Œ¡ ”≈“◊≈“≈
Summary(uk):	PHP ˜≈“”¶ß 4 -- Õœ◊¡ –“≈–“œ√≈”’◊¡ŒŒ— HTML-∆¡ Ã¶◊, ◊…ÀœŒ’◊¡Œ¡ Œ¡ ”≈“◊≈“¶
Name:		php
Version:	4.3.0
Release:	1
Epoch:		3
Group:		Libraries
License:	PHP
Source0:	http://www.php.net/distributions/%{name}-%{version}.tar.bz2
Source1:	FAQ.%{name}
Source2:	zend.gif
Source3:	http://www.php.net/distributions/manual/%{name}_manual_en.tar.bz2
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
Patch9:		%{name}-odbc-fix.patch
Patch10:	%{name}-java-norpath.patch
Patch11:	%{name}-mcal-shared-lib.patch
Patch12:	%{name}-msession-shared-lib.patch
Patch13:	%{name}-build_modules.patch
Patch14:	%{name}-sapi-ini-file.patch
Patch15:	%{name}-dl-zlib.patch
Patch16:	%{name}-dl-pcre.patch
Patch17:	%{name}-session-unregister.patch
Patch18:	%{name}-ini.patch
Patch19:	%{name}-acam.patch
Patch20:	%{name}-xmlrpc-fix.patch
Patch21:	%{name}-libtool.patch
Patch22:	%{name}-db4.patch
Icon:		php4.gif
URL:		http://www.php.net/
%{!?_without_interbase:%{!?_with_interbase_inst:BuildRequires:	Firebird-devel}}
BuildRequires:	apache-devel
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.4d
BuildRequires:	bison
BuildRequires:	bzip2-devel
BuildRequires:	cracklib-devel >= 2.7-15
%{!?_without_curl:BuildRequires:	curl-devel >= 7.9.8 }
BuildRequires:	cyrus-sasl-devel
%{?_with_db3:BuildRequires:	db3-devel}
%{!?_with_db3:BuildRequires:	db-devel >= 4.0}
%if %(expr %{?_without_xml:0}%{!?_without_xml:1} + %{?_without_xmlrpc:0}%{!?_without_xmlrpc:1})
BuildRequires:	expat-devel
%endif
BuildRequires:	flex
%{!?_without_sybase_ct:BuildRequires:	freetds-devel}
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	gd-devel >= 2.0.1
%{!?_without_gif:BuildRequires:	gd-devel(gif)}
%{?_without_gif:BuildConflicts: gd-devel(gif)}
BuildRequires:	gdbm-devel
BuildRequires:	gmp-devel
%{!?_without_imap:BuildRequires: imap-devel >= 1:2001-0.BETA.200107022325.2 }
%{?_with_java:BuildRequires:	jdk >= 1.1}
%{!?_without_cpdf:BuildRequires:	libcpdf-devel >= 2.02r1-2}
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel >= 1.4
BuildRequires:	libmcal-devel
BuildRequires:	libmcrypt-devel >= 2.4.4
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 0:1.4.2-9
%{!?_without_xml:BuildRequires:	libxml2-devel >= 2.2.7}
%{!?_without_domxslt:BuildRequires:	libxslt-devel >= 1.0.3}
%{!?_without_mhash:BuildRequires:	mhash-devel}
%{!?_without_ming:BuildRequires:	ming-devel >= 0.1.0}
%{!?_without_mm:BuildRequires:	mm-devel >= 1.1.3}
%{!?_without_mnogosearch:BuildRequires:	mnogosearch-devel >= 3.2.6}
BuildRequires:	mysql-devel >= 3.23.32
%{!?_without_ldap:BuildRequires: openldap-devel >= 2.0}
%if %(expr %{?_without_openssl:0}%{!?_without_openssl:1} + %{?_without_ldap:0}%{!?_without_ldap:1})
BuildRequires:	openssl-devel >= 0.9.7
%endif
BuildRequires:	pam-devel
%{!?_without_pdf:BuildRequires:	pdflib-devel >= 4.0.0}
BuildRequires:	perl
%{!?_without_msession:BuildRequires:	phoenix-devel}
%{!?_without_pgsql:BuildRequires:	postgresql-devel}
%{!?_without_pgsql:BuildRequires:	postgresql-backend-devel >= 7.2}
%{!?_without_pspell:BuildRequires:	pspell-devel}
%{!?_without_recode:BuildRequires:	recode-devel >= 3.5d-3}
BuildRequires:	rpm-php-pearprov >= 4.0.2-100
%{!?_without_xslt:BuildRequires:	sablotron-devel >= 0.96}
BuildRequires:	t1lib-devel
%{!?_without_snmp:BuildRequires: ucd-snmp-devel >= 4.2.6}
%{!?_without_odbc:BuildRequires: unixODBC-devel}
%{!?_without_xmlrpc:BuildRequires:	xmlrpc-epi-devel}
%{!?_without_yaz:BuildRequires:	yaz-devel >= 1.9}
BuildRequires:	zip
BuildRequires:	zlib-devel >= 1.0.9
BuildRequires:	zziplib-devel
#BuildRequires:	fcgi-devel
# apache 1.3 vs apache 2.0
%if %{_apache2}
PreReq:		apache >= 2.0.40
%requires_eq	apache
%else
PreReq:		apache(EAPI) < 2.0.0
PreReq:		apache(EAPI) >= 1.3.9
Requires(post,preun):	%{apxs}
Requires(post,preun):	perl
%endif
PreReq:		%{name}-common = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	phpfi
Obsoletes:	apache-mod_php

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php
%define		httpdir		/home/services/httpd

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

%package cgi
Summary:	PHP as CGI program
Summary(pl):	PHP jako program CGI
Group:		Development/Languages/PHP
PreReq:		%{name}-common = %{version}
Provides:	php-program = %{version}

%description cgi
PHP as CGI program.

%description cgi -l pl
PHP jako program CGI.

%package cli
Summary:	PHP as CLI interpreter
Summary(pl):	PHP jako interpreter dzia≥aj±cy z linii poleceÒ
Group:		Development/Languages/PHP
PreReq:		%{name}-common = %{version}
Provides:	php-program = %{version}

%description cli
PHP as CLI interpreter.

%description cli -l pl
PHP jako interpreter dzia≥aj±cy z linii poleceÒ.

%package common
Summary:	Common files nneded by both apache module and CGI
Summary(pl):	WspÛlne pliki dla modu≥u apache'a i programu CGI
Summary(ru):	Ú¡⁄ƒ≈Ã—≈ÕŸ≈ ¬…¬Ã…œ‘≈À… ƒÃ— php
Summary(uk):	‚¶¬Ã¶œ‘≈À… ”–¶ÃÿŒœ«œ ◊…Àœ“…”‘¡ŒŒ— ƒÃ— php
Group:		Libraries
Provides:	%{name}-session = %{version}
Obsoletes:	%{name}-session <= %{epoch}:%{version}-%{release}

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
Requires:	%{name}-common = %{version}
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

%package doc
Summary:	Online manual for PHP
Summary(pl):	Dokumentacja dla PHP
Summary(pt_BR):	Manual da linguagem PHP, em formato HTML
Group:		Networking/Daemons
Obsoletes:	php-manual

%description doc
Comprehensive documentation for PHP, viewable through your web server,
too!

%description doc -l pl
Dokumentacja dla pakietu PHP. Moøna j± rÛwnieø ogl±daÊ poprzez serwer
WWW.

%description doc -l pt_BR
Manual da linguagem PHP, em formato HTML.

%package bcmath
Summary:	bcmath extension module for PHP
Summary(pl):	Modu≥ bcmath dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description bcmath
This is a dynamic shared object (DSO) for Apache that will add bc
style precision math functions support to PHP.

%description bcmath -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z dok≥adnych funkcji
matematycznych takich jak w programie bc.

%package bzip2
Summary:	Bzip2 extension module for PHP
Summary(pl):	Modu≥ bzip2 dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description bzip2
This is a dynamic shared object (DSO) for Apache that will add
compression (bzip2) support to PHP.

%description bzip2 -l pl
Modu≥ PHP umoøliwiaj±cy uøywanie kompresji (poprzez bibliotekÍ bzip2).

%package calendar
Summary:	Calendar extension module for PHP
Summary(pl):	Modu≥ funkcji kalendarza dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description calendar
This is a dynamic shared object (DSO) for Apache that will add
calendar support to PHP.

%description calendar -l pl
Dynamiczny obiekt wspÛ≥dzielony (DSO) dla Apache'a, dodaj±cy do PHP
wsparcie dla kalendarza.

%package cpdf
Summary:	cpdf extension module for PHP
Summary(pl):	Modu≥ cpdf dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description cpdf
This is a dynamic shared object (DSO) for Apache that will add libcpdf
support to PHP.

%description cpdf -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ biblioteki libcpdf.

%package crack
Summary:	crack extension module for PHP
Summary(pl):	Modu≥ crack dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description crack
This is a dynamic shared object (DSO) for Apache that will add
cracklib support to PHP.

Warning: this is an experimental module.

%description crack -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z biblioteki cracklib.

Uwaga: to jest modu≥ eksperymentalny.

%package ctype
Summary:	ctype extension module for PHP
Summary(pl):	Modu≥ ctype dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description ctype
This is a dynamic shared object (DSO) for Apache that will add ctype
support to PHP.

%description ctype -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z funkcji ctype.

%package curl
Summary:	curl extension module for PHP
Summary(pl):	Modu≥ curl dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description curl
This is a dynamic shared object (DSO) for Apache that will add curl
support to PHP.

%description curl -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z biblioteki curl.

%package dba
Summary:	DBA extension module for PHP
Summary(pl):	Modu≥ DBA dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description dba
This is a dynamic shared object (DSO) for Apache that will add
flat-file databases (DBA) support to PHP.

%description dba -l pl
Dynamiczny obiekt wspÛ≥dzielony (DSO) dla Apache'a, dodaj±cy do PHP
wsparcie dla baz danych opartych na plikach (DBA).

%package dbase
Summary:	DBase extension module for PHP
Summary(pl):	Modu≥ DBase dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description dbase
This is a dynamic shared object (DSO) for Apache that will add DBase
support to PHP.

%description dbase -l pl
Modu≥ PHP ze wsparciem dla DBase.

%package dbx
Summary:	DBX extension module for PHP
Summary(pl):	Modu≥ DBX dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description dbx
This is a dynamic shared object (DSO) for Apache that will add DB
abstraction layer to PHP. DBX supports odbc, mysql, pgsql, mssql,
fbsql and more.

%description dbx -l pl
Dynamiczny obiekt wspÛ≥dzielony (DSO) dla Apache'a, dodaj±cy do PHP
warstwÍ abstrakcji do obs≥ugi baz danych. DBX obs≥uguje bazy odbc,
mysql, pgsql, mssql, fbsql i inne.

%package dio
Summary:	Direct I/O extension module for PHP
Summary(pl):	Modu≥ Direct I/O dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description dio
This is a dynamic shared object (DSO) for Apache that will add direct
file I/O support to PHP.

Warning: this is an experimental module.

%description dio -l pl
Dynamiczny obiekt wspÛ≥dzielony (DSO) dla Apache'a, dodaj±cy do PHP
obs≥ugÍ bezpo∂rednich operacji I/O na plikach.

Uwaga: to jest modu≥ eksperymentalny.

%package domxml
Summary:	DOM XML extension module for PHP
Summary(pl):	Modu≥ DOM XML dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description domxml
This is a dynamic shared object (DSO) for Apache that will add DOM XML
support to PHP.

Warning: this is an experimental module.

%description domxml -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ DOM XML.

Uwaga: to jest modu≥ eksperymentalny.

%package exif
Summary:	exif extension module for PHP
Summary(pl):	Modu≥ exif dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description exif
This is a dynamic shared object (DSO) for Apache that will add exif
support to PHP.

%description exif -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ plikÛw EXIF.

%package filepro
Summary:	filePro extension module for PHP
Summary(pl):	Modu≥ filePro dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description filepro
This is a dynamic shared object (DSO) for Apache that will add PHP
support for read-only access to filePro databases.

%description filepro -l pl
Dynamiczny obiekt wspÛ≥dzielony (DSO) dla Apache'a, dodaj±cy do PHP
moøliwo∂Ê dostÍpu (tylko do odczytu) do baz danych filePro.

%package ftp
Summary:	FTP extension module for PHP
Summary(pl):	Modu≥ FTP dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description ftp
This is a dynamic shared object (DSO) for Apache that will add FTP
support to PHP.

%description ftp -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ protoko≥u FTP.

%package gd
Summary:	GD extension module for PHP
Summary(pl):	Modu≥ GD dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}
%{!?_without_gif:Requires:	gd(gif)}
%{!?_without_gif:Provides:	%{name}-gd(gif) = %{epoch}:%{version}-%{release}}

%description gd
This is a dynamic shared object (DSO) for Apache that will add GD
support to PHP. You should install this package in addition to the
main %{name} package if you want to create and manipulate images with
PHP.

%description gd -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z biblioteki GD - do obrÛbki
obrazkÛw z poziomu PHP.

%package gettext
Summary:	gettext extension module for PHP
Summary(pl):	Modu≥ gettext dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description gettext
This is a dynamic shared object (DSO) for Apache that will add gettext
support to PHP.

%description gettext -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ lokalizacji przez gettext.

%package gmp
Summary:	gmp extension module for PHP
Summary(pl):	Modu≥ gmp dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description gmp
This is a dynamic shared object (DSO) for Apache that will add
arbitrary length number support with GNU MP library to PHP.

%description gmp -l pl
Modu≥ PHP umorzliwiaj±cy korzystanie z biblioteki gmp.

%package hyperwave
Summary:	Hyperwave extension module for PHP
Summary(pl):	Modu≥ Hyperwave dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description hyperwave
This is a dynamic shared object (DSO) for Apache that will add
Hyperwave support to PHP.

%description hyperwave -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ Hyperwave.

%package iconv
Summary:	iconv extension module for PHP
Summary(pl):	Modu≥ iconv dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description iconv
This is a dynamic shared object (DSO) for Apache that will add iconv
support to PHP.

%description iconv -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ iconv.

%package imap
Summary:	IMAP extension module for PHP
Summary(pl):	Modu≥ IMAP dla PHP
Summary(pt_BR):	Um mÛdulo para aplicaÁıes PHP que usam IMAP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description imap
This is a dynamic shared object (DSO) for Apache that will add IMAP
support to PHP.

%description imap -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ skrzynek IMAP.

%description imap -l pt_BR
Um mÛdulo para aplicaÁıes PHP que usam IMAP.

%package interbase
Summary:	InterBase/Firebird database module for PHP
Summary(pl):	Modu≥ bazy danych InterBase/Firebird dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}
%{?_with_interbase_inst:Autoreq:	false}

%description interbase
This is a dynamic shared object (DSO) for Apache that will add
InterBase and Firebird database support to PHP.

%description interbase -l pl
Modu≥ PHP umoøliwiaj±cy dostÍp do baz danych InterBase i Firebird.

%package java
Summary:	Java extension module for PHP
Summary(pl):	Modu≥ Javy dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description java
This is a dynamic shared object (DSO) for Apache that will add JAVA
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
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description ldap
This is a dynamic shared object (DSO) for Apache that will add LDAP
support to PHP.

%description ldap -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ LDAP.

%description ldap -l pt_BR
Um mÛdulo para aplicaÁıes PHP que usam LDAP.

%package mbstring
Summary:	mbstring extension module for PHP
Summary(pl):	Modu≥ mbstring dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description mbstring
This is a dynamic shared object (DSO) for Apache that will add
multibyte string support to PHP.

%description mbstring -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ ci±gÛw znakÛw wielobajtowych.

%package mcal
Summary:	mcal extension module for PHP
Summary(pl):	Modu≥ mcal dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description mcal
This is a dynamic shared object (DSO) for Apache that will add mcal
(Modular Calendar Access Library) support to PHP.

%description mcal -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z biblioteki mcal (daj±cej dostÍp
do kalendarzy).

%package mcrypt
Summary:	mcrypt extension module for PHP
Summary(pl):	Modu≥ mcrypt dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description mcrypt
This is a dynamic shared object (DSO) for Apache that will add mcrypt
support to PHP.

%description mcrypt -l pl
Modu≥ PHP dodaj±cy moøliwo∂Ê szyfrowania poprzez bibliotekÍ mcrypt.

%package mhash
Summary:	mhash extension module for PHP
Summary(pl):	Modu≥ mhash dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description mhash
This is a dynamic shared object (DSO) for Apache that will add mhash
support to PHP.

%description mhash -l pl
Modu≥ PHP udostÍpniaj±cy funkcje mieszaj±ce z biblioteki mhash.

%package ming
Summary:	ming extension module for PHP
Summary(pl):	Modu≥ ming dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description ming
This is a dynamic shared object (DSO) for Apache that will add ming
(Flash - .swf files) support to PHP.

%description ming -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ plikÛw Flash (.swf) poprzez bibliotekÍ
ming.

%package mnogosearch
Summary:	mnoGoSearch extension module for PHP
Summary(pl):	Modu≥ mnoGoSearch dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description mnogosearch
This is a dynamic shared object (DSO) for Apache that will allow you
to access mnoGoSearch free search engine in PHP.

%description mnogosearch -l pl
Modu≥ PHP dodaj±cy pozwalaj±cy na dostÍp do wolnodostÍpnego silnika
wyszukiwarki mnoGoSearch.

%package msession
Summary:	msession extension module for PHP
Summary(pl):	Modu≥ msession dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description msession
This is a dynamic shared object (DSO) for Apache that will allow you
to use msession in PHP. msession is a high speed session daemon which
can run either locally or remotely. It is designed to provide
consistent session management for a PHP web farm.

%description msession -l pl
Modu≥ PHP dodaj±cy umoøliwiaj±cy korzystanie z demona msession. Jest
to demon szybkiej obs≥ugi sesji, ktÛry moøe dzia≥aÊ lokalnie lub na
innej maszynie. S≥uøy do zapewniania spÛjnej obs≥ugi sesji dla farmy
serwerÛw.

%package mysql
Summary:	MySQL database module for PHP
Summary(pl):	Modu≥ bazy danych MySQL dla PHP
Summary(pt_BR):	Um mÛdulo para aplicaÁıes PHP que usam bancos de dados MySQL
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description mysql
This is a dynamic shared object (DSO) for Apache that will add MySQL
database support to PHP. If you need back-end support for MySQL, you
should install this package in addition to the main %{name} package.

%description mysql -l pl
Modu≥ PHP umoøliwiaj±cy dostÍp do bazy danych MySQL.

%description mysql -l pt_BR
Um mÛdulo para aplicaÁıes PHP que usam bancos de dados MySQL.

%package oci8
Summary:	Oracle 8 database module for PHP
Summary(pl):	Modu≥ bazy danych Oracle 8 dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}
Autoreq:	false

%description oci8
This is a dynamic shared object (DSO) for Apache that will add Oracle
7 and Oracle 8 database support to PHP through Oracle8 Call-Interface
(OCI8).

%description oci8 -l pl
Modu≥ PHP umoøliwiaj±cy dostÍp do bazy danych Oracle 7 i Oracle 8
poprzez interfejs Oracle8 Call-Interface (OCI8).

%package odbc
Summary:	ODBC extension module for PHP
Summary(pl):	Modu≥ ODBC dla PHP
Summary(pt_BR):	Um mÛdulo para aplicaÁıes PHP que usam bases de dados ODBC
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}
Requires:	unixODBC >= 2.1.1-3

%description odbc
This is a dynamic shared object (DSO) for Apache that will add ODBC
support to PHP.

%description odbc -l pl
Modu≥ PHP ze wsparciem dla ODBC.

%description odbc -l pt_BR
Um mÛdulo para aplicaÁıes PHP que usam ODBC.

%package openssl
Summary:	OpenSSL extension module for PHP
Summary(pl):	Modu≥ OpenSSL dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description openssl
This is a dynamic shared object (DSO) for Apache that will add OpenSSL
support to PHP.

Warning: this is an experimental module.

%description openssl -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z biblioteki OpenSSL.

Uwaga: to jest modu≥ eksperymentalny.

%package oracle
Summary:	Oracle 7 database module for PHP
Summary(pl):	Modu≥ bazy danych Oracle 7 dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}
Autoreq:	false

%description oracle
This is a dynamic shared object (DSO) for Apache that will add Oracle
7 database support to PHP.

%description oracle -l pl
Modu≥ PHP umoøliwiaj±cy dostÍp do bazy danych Oracle 7.

%package overload
Summary:	Overload extension module for PHP
Summary(pl):	Modu≥ Overload dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description overload
This is a dynamic shared object (DSO) for Apache that will add
user-space object overloading support to PHP.

Warning: this is an experimental module.

%description overload -l pl
Modu≥ PHP umoøliwiaj±cy przeci±øanie obiektÛw.

Uwaga: to jest modu≥ eksperymentalny.

%package pcntl
Summary:	Process Control extension module for PHP
Summary(pl):	Modu≥ Process Control dla PHP
Group:		Libraries
Requires(post,preun):%{name}-program = %{version}
Requires:	%{name}-program = %{version}

%description pcntl
This is a dynamic shared object (DSO) for Apache that will add process
spawning and control support to PHP. It supports functions like
fork(), waitpid(), signal() etc.

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
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description pcre
This is a dynamic shared object (DSO) for Apache that will add Perl
Compatible Regular Expression support to PHP.

%description pcre -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z perlowych wyraøeÒ regularnych
(Perl Compatible Regular Expressions)

%package pdf
Summary:	libPDF module for PHP
Summary(pl):	Modu≥ do tworzenia plikÛw PDF dla PHP
Group:		Libraries
PreReq:		pdflib
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description pdf
This is a dynamic shared object (DSO) for Apache that will add PDF
support to PHP.

%description pdf -l pl
Modu≥ PHP umoøliwiaj±cy tworzenie plikÛw PDF. Wykorzystuje bibliotekÍ
pdflib.

%package pgsql
Summary:	PostgreSQL database module for PHP
Summary(pl):	Modu≥ bazy danych PostgreSQL dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description pgsql
This is a dynamic shared object (DSO) for Apache that will add
PostgreSQL database support to PHP. If you need back-end support for
PostgreSQL, you should install this package in addition to the main
%{name} package.

%description pgsql -l pl
Modu≥ PHP umoøliwiaj±cy dostÍp do bazy danych PostgreSQL.

%description pgsql -l pt_BR
Um mÛdulo para aplicaÁıes PHP que usam bancos de dados postgresql.

%package posix
Summary:	POSIX extension module for PHP
Summary(pl):	Modu≥ POSIX dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description posix
This is a dynamic shared object (DSO) for Apache that will add POSIX
functions support to PHP.

%description posix -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z funkcji POSIX.

%package pspell
Summary:	pspell extension module for PHP
Summary(pl):	Modu≥ pspell dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description pspell
This is a dynamic shared object (DSO) for Apache that will add pspell
support to PHP. It allows to check the spelling of a word and offer
suggestions.

%description pspell -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z pspella. Pozwala on na
sprawdzanie pisowni s≥owa i sugerowanie poprawek.

%package recode
Summary:	recode extension module for PHP
Summary(pl):	Modu≥ recode dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}
Requires:	recode >= 3.5d-3

%description recode
This is a dynamic shared object (DSO) for Apache that will add recode
support to PHP.

%description recode -l pl
Modu≥ PHP dodaj±cy moøliwo∂Ê konwersji kodowania plikÛw (poprzez
bibliotekÍ recode).

%package session
Summary:	session extension module for PHP
Summary(pl):	Modu≥ session dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description session
This is a dynamic shared object (DSO) for Apache that will add session
support to PHP.

%description session -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ sesji.

%package shmop
Summary:	Shared Memory Operations extension module for PHP
Summary(pl):	Modu≥ shmop dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description shmop
This is a dynamic shared object (DSO) for Apache that will add Shared
Memory Operations support to PHP.

Warning: this is an experimental module.

%description shmop -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z pamiÍci dzielonej.

Uwaga: to jest modu≥ eksperymentalny.

%package snmp
Summary:	SNMP extension module for PHP
Summary(pl):	Modu≥ SNMP dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description snmp
This is a dynamic shared object (DSO) for Apache that will add SNMP
support to PHP.

%description snmp -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ SNMP.

%package sockets
Summary:	sockets extension module for PHP
Summary(pl):	Modu≥ socket dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description sockets
This is a dynamic shared object (DSO) for Apache that will add sockets
support to PHP.

Warning: this is an experimental module.

%description sockets -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ gniazdek.

Uwaga: to jest modu≥ eksperymentalny.

%package sybase-ct
Summary:	Sybase-CT extension module for PHP
Summary(pl):	Modu≥ Sybase-CT dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description sybase-ct
This is a dynamic shared object (DSO) for Apache that will add Sybase
and MS SQL databases support through CT-lib to PHP.

%description sybase-ct -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ baz danych Sybase oraz MS SQL poprzez
CT-lib.

%package sysvsem
Summary:	SysV sem extension module for PHP
Summary(pl):	Modu≥ SysV sem dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description sysvsem
This is a dynamic shared object (DSO) for Apache that will add SysV
semafores support to PHP.

%description sysvsem -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z semaforÛw SysV.

%package sysvshm
Summary:	SysV shm extension module for PHP
Summary(pl):	Modu≥ SysV shm dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description sysvshm
This is a dynamic shared object (DSO) for Apache that will add SysV
Shared Memory support to PHP.

%description sysvshm -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z pamiÍci dzielonej SysV.

%package wddx
Summary:	wddx extension module for PHP
Summary(pl):	Modu≥ wddx dla PHP
Group:		Libraries
PreReq:		%{name}-session = %{version}
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description wddx
This is a dynamic shared object (DSO) for Apache that will add wddx
support to PHP.

%description wddx -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z wddx.

%package xml
Summary:	XML extension module for PHP
Summary(pl):	Modu≥ XML dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description xml
This is a dynamic shared object (DSO) for Apache that will add XML
support to PHP. This extension lets you create XML parsers and then
define handlers for different XML events. If you want to be able to
parse XML documents you should install this package in addition to the
main %{name} package.

%description xml -l pl
Modu≥ PHP umoøliwiaj±cy parsowanie plikÛw XML i obs≥ugÍ zdarzeÒ
zwi±zanych z tymi plikami.

%package xmlrpc
Summary:	xmlrpc extension module for PHP
Summary(pl):	Modu≥ xmlrpc dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description xmlrpc
This is a dynamic shared object (DSO) for Apache that will add XMLRPC
support to PHP.

Warning: this is an experimental module.

%description xmlrpc -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ XMLRPC.

Uwaga: to jest modu≥ eksperymentalny.

%package xslt
Summary:	xslt extension module for PHP
Summary(pl):	Modu≥ xslt dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description xslt
This is a dynamic shared object (DSO) for Apache that will add xslt
support to PHP.

%description xslt -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z technologii xslt.

%package yaz
Summary:	yaz extension module for PHP
Summary(pl):	Modu≥ yaz dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}
Requires:	yaz >= 1.9

%description yaz
This is a dynamic shared object (DSO) for Apache that will add yaz
support to PHP. yaz toolkit implements the Z39.50 protocol for
information retrieval.

%description yaz -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z yaz - implementacji protoko≥u
Z39.50 s≥uø±cego do pozyskiwania informacji.

%package yp
Summary:	NIS (yp) extension module for PHP
Summary(pl):	Modu≥ NIS (yp) dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description yp
This is a dynamic shared object (DSO) for Apache that will add NIS
(Yellow Pages) support to PHP.

%description yp -l pl
Dynamiczny obiekt wspÛ≥dzielony (DSO) dla Apache'a, dodaj±cy do PHP
wsparcie dla NIS (Yellow Pages).

%package zip
Summary:	zip extension module for PHP
Summary(pl):	Modu≥ zip dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description zip
This is a dynamic shared object (DSO) for Apache that will add ZZipLib
(read-only access to ZIP archives) support to PHP.

%description zip -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z bibliotekli ZZipLib
(pozwalaj±cej na odczyt archiwÛw ZIP).

%package zlib
Summary:	Zlib extension module for PHP
Summary(pl):	Modu≥ zlib dla PHP
Group:		Libraries
Requires(post,preun):%{name}-common = %{version}
Requires:	%{name}-common = %{version}

%description zlib
This is a dynamic shared object (DSO) for Apache that will add
compression (zlib) support to PHP.

%description zlib -l pl
Modu≥ PHP umoøliwiaj±cy uøywanie kompresji (poprzez bibliotekÍ zlib).

%package pear
Summary:	PEAR - PHP Extension and Application Repository
Summary(pl):	PEAR - Rozszerzenie PHP i Repozytorium Aplikacji
Group:		Development/Languages/PHP
Requires:	%{name}-pcre = %{version}
Requires:	%{name}-xml = %{version}
Obsoletes:	%{name}-pear-additional_classes

%description pear
PEAR - PHP Extension and Application Repository.

%description pear -l pl
PEAR (PHP Extension and Application Repository) - Rozszerzenie PHP i
Repozytorium Aplikacji.


%prep
%setup -q
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
%patch17 -p1
cp php.ini-dist php.ini
%patch18 -p1
# for ac2.53b/am1.6b - AC_LANG_CXX has AM_CONDITIONAL, so cannot be invoked
# conditionally...
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1

install -d manual
bzip2 -dc %{SOURCE3} | tar -xf - -C manual

%build
CFLAGS="%{rpmcflags} -DEAPI=1 -I/usr/X11R6/include"
EXTENSION_DIR="%{extensionsdir}"; export EXTENSION_DIR
./buildconf
%{__libtoolize}
%{__aclocal}
autoconf
PROG_SENDMAIL="/usr/lib/sendmail"; export PROG_SENDMAIL
for i in cgi cli apxs ; do
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
	--enable-bcmath=shared \
	--enable-calendar=shared \
	--enable-ctype=shared \
	--enable-dba=shared \
	--enable-dbx=shared \
	--enable-dio=shared \
	--enable-exif=shared \
	--enable-ftp=shared \
	--enable-gd-native-ttf \
	--enable-magic-quotes \
	--enable-mbstring=shared --disable-mbstr-enc-trans --enable-mbregex \
	--enable-overload=shared \
	%{?_with_pcntl:--enable-pcntl=shared}%{!?_with_pcntl:--disable-pcntl} \
	--enable-posix=shared \
	--enable-session \
	--enable-shared \
	--enable-shmop=shared \
	--enable-sysvsem=shared \
	--enable-sysvshm=shared \
	--enable-track-vars \
	--enable-trans-sid \
	--enable-safe-mode \
	--enable-sockets=shared \
	--enable-ucd-snmp-hack \
	%{!?_without_wddx:--enable-wddx=shared} \
	%{?_without_xml:--disable-xml}%{!?_without_xml:--enable-xml=shared} \
	%{!?_without_xslt:--enable-xslt=shared} \
	--enable-yp=shared \
	--with-bz2=shared \
	%{!?_without_cpdf:--with-cpdflib=shared} \
	--with-crack=shared \
	%{?_without_curl:--without-curl}%{!?_without_curl:--with-curl=shared} \
	%{?_with_db3:--with-db3}%{!?_with_db3:--with-db4} \
	--with-dbase=shared \
	--with-dom=shared \
	%{!?_without_domxslt:--with-dom-xslt=shared --with-dom-exslt=shared} \
%if %(expr %{?_without_xml:0}%{!?_without_xml:1} + %{?_without_xmlrpc:0}%{!?_without_xmlrpc:1})
	--with-expat-dir=shared,/usr \
%else
	--without-expat-dir \
%endif
	--with-iconv=shared \
	--with-filepro=shared \
	--with-freetype-dir=shared \
	--with-gettext=shared \
	--with-gd=shared,/usr \
	--with-gdbm \
	--with-gmp=shared \
	--with-hyperwave=shared \
	%{!?_without_imap:--with-imap=shared --with-imap-ssl} \
	%{!?_without_interbase:--with-interbase=shared%{!?_with_interbase_inst:,/usr}} \
	%{?_with_java:--with-java=/usr/lib/java} \
	--with-jpeg-dir=shared,/usr \
	%{!?_without_ldap:--with-ldap=shared} \
	--with-mcal=shared,/usr \
	--with-mcrypt=shared \
	%{!?_without_mhash:--with-mhash=shared} \
	%{!?_without_ming:--with-ming=shared} \
	%{!?_without_mm:--with-mm} \
	%{?_without_mnogosearch:--without-mnogosearch}%{!?_without_mnogosearch:--with-mnogosearch=shared,/usr} \
	%{!?_without_msession:--with-msession=shared}%{?_without_msession:--without-msession} \
	--with-mysql=shared,/usr \
	--with-mysql-sock=/var/lib/mysql/mysql.sock \
	%{?_with_oci8:--with-oci8=shared} \
	%{!?_without_openssl:--with-openssl=shared} \
	%{?_with_oracle:--with-oracle=shared} \
	%{?_without_pcre:--without-pcre-regex}%{!?_without_pcre:--with-pcre-regex=shared} \
	%{!?_without_pdf:--with-pdflib=shared} \
	--with-pear=%{php_pear_dir} \
	%{?_without_pgsql:--without-pgsql}%{!?_without_pgsql:--with-pgsql=shared,/usr} \
	--with-png-dir=shared,/usr \
	%{!?_without_pspell:--with-pspell=shared} \
	%{!?_without_recode:--with-recode=shared} \
	--with-regex=php \
	--without-sablot-js \
	%{!?_without_snmp:--with-snmp=shared} \
	%{!?_without_sybase_ct:--with-sybase-ct=shared,/usr} \
	--with-t1lib=shared \
	--with-tiff-dir=shared,/usr \
	%{!?_without_odbc:--with-unixODBC=shared} \
	%{?_without_xmlrpc:--without-xmlrpc}%{!?_without_xmlrpc:--with-xmlrpc=shared,/usr} \
	%{!?_without_xslt:--with-xslt-sablot=shared} \
	%{!?_without_yaz:--with-yaz=shared} \
	--with-zip=shared \
	--with-zlib=shared \
	--with-zlib-dir=shared,/usr

cp -f Makefile Makefile.$i
# left for debugging purposes
cp -f main/php_config.h php_config.h.$i
done

# for now session_mm doesn't work with shared session module...
# --enable-session=shared
# %{?_without_mm:--with-mm=shared,no}%{!?_without_mm:--with-mm=shared}

# TODO:
#	--with-qtdom=shared

%{__make}

# fix install paths, avoid evil rpaths
perl -pi -e "s|^libdir=.*|libdir='%{_libdir}'|" libphp_common.la
perl -pi -e "s|^libdir=.*|libdir='%{_libdir}/apache'|" libphp4.la
perl -pi -e "s|^(relink_command=.* -rpath )[^ ]*/libs |\1%{_libdir}/apache |" libphp4.la

# notes:
# -DENABLE_CHROOT_FUNC=1 (cgi,fcgi) is used in ext/standard/dir.c (libphp_common)
# -DPHP_WRITE_STDOUT is used also for cli, but not set by its config.m4

%{__make} sapi/cgi/php -f Makefile.cgi \
	CFLAGS_CLEAN="%{rpmcflags} -DDISCARD_PATH=1 -DENABLE_PATHINFO_CHECK=1 -DFORCE_CGI_REDIRECT=0 -DPHP_WRITE_STDOUT=1"

# for fcgi: -DDISCARD_PATH=0 -DENABLE_PATHINFO_CHECK=1 -DFORCE_CGI_REDIRECT=0
# -DHAVE_FILENO_PROTO=1 -DHAVE_FPOS=1 -DHAVE_LIBNSL=1(die) -DHAVE_SYS_PARAM_H=1
# -DPHP_FASTCGI=1 -DPHP_FCGI_STATIC=1 -DPHP_WRITE_STDOUT=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/{php,apache},%{_sysconfdir}/{apache,cgi}} \
	$RPM_BUILD_ROOT%{httpdir}/icons \
	$RPM_BUILD_ROOT{%{_sbindir},%{_bindir}} \
	$RPM_BUILD_ROOT/var/run/php \
	$RPM_BUILD_ROOT/etc/httpd/httpd.conf

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	INSTALL_IT="\$(LIBTOOL) --mode=install install libphp_common.la $RPM_BUILD_ROOT%{_libdir} ; \$(LIBTOOL) --mode=install install libphp4.la $RPM_BUILD_ROOT%{_libdir}/apache ; \$(LIBTOOL) --mode=install install sapi/cgi/php $RPM_BUILD_ROOT%{_bindir}/php.cgi" \
	INSTALL_CLI="\$(LIBTOOL) --mode=install install sapi/cli/php $RPM_BUILD_ROOT%{_bindir}/php.cli"

# compatibility (/usr/bin/php used to be CGI SAPI)
ln -sf php.cgi $RPM_BUILD_ROOT%{_bindir}/php

%{?_with_java:install ext/java/php_java.jar $RPM_BUILD_ROOT%{extensionsdir}}

install php.ini	$RPM_BUILD_ROOT%{_sysconfdir}/php.ini
install %{SOURCE6} %{SOURCE7} %{SOURCE8} $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE2} php.gif $RPM_BUILD_ROOT%{httpdir}/icons
install %{SOURCE4} $RPM_BUILD_ROOT%{_sbindir}
install %{SOURCE5} $RPM_BUILD_ROOT/etc/httpd/httpd.conf/70_mod_php.conf

install %{SOURCE1} .

cp -f Zend/LICENSE{,.Zend}

# Directories created for pear:
install -d $RPM_BUILD_ROOT%{php_pear_dir}/{Archive,Console,Crypt,HTML/Template,Image,Net,Science,XML}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%if ! %{_apache2}
perl -pi -e 's|^#AddType application/x-httpd-php \.php|AddType application/x-httpd-php .php|' \
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
	perl -pi -e \
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
%{_sbindir}/php-module-install install dbx %{_sysconfdir}/php.ini

%preun dio
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove dbx %{_sysconfdir}/php.ini
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

%post filepro
%{_sbindir}/php-module-install install filepro %{_sysconfdir}/php.ini

%preun filepro
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove filepro %{_sysconfdir}/php.ini
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

%post mysql
%{_sbindir}/php-module-install install mysql %{_sysconfdir}/php.ini

%preun mysql
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove mysql %{_sysconfdir}/php.ini
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

%post sybase-ct
%{_sbindir}/php-module-install install sybase_ct %{_sysconfdir}/php.ini

%preun sybase-ct
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove sybase_ct %{_sysconfdir}/php.ini
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

%files cgi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/php.cgi
%attr(755,root,root) %{_bindir}/php
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/php-cgi.ini

%files cli
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/php.cli
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/php-cli.ini

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

%files doc
%defattr(644,root,root,755)
%doc manual/*

%files bcmath
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/bcmath.so

%files bzip2
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/bz2.so

%files calendar
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/calendar.so

%if %{?_without_cpdf:0}%{!?_without_cpdf:1}
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

%if %{!?_without_curl:1}%{?_without_curl:0}
%files curl
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/curl.so
%endif

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

%files domxml
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/domxml.so

%files exif
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/exif.so

%files filepro
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/filepro.so

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

%if %{?_without_imap:0}%{!?_without_imap:1}
%files imap
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/imap.so
%endif

%if %{?_without_interbase:0}%{!?_without_interbase:1}
%files interbase
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/interbase.so
%endif

%if %{?_with_java:1}%{!?_with_java:0}
%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/java.so
%{extensionsdir}/php_java.jar
%endif

%if %{?_without_ldap:0}%{!?_without_ldap:1}
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

%if %{!?_without_mhash:1}%{?_without_mhash:0}
%files mhash
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/mhash.so
%endif

%if %{!?_without_ming:1}%{?_without_ming:0}
%files ming
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/ming.so
%endif

%if %{!?_without_mnogosearch:1}%{?_without_mnogosearch:0}
%files mnogosearch
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/mnogosearch.so
%endif

%if %{?_without_msession:0}%{!?_without_msession:1}
%files msession
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/msession.so
%endif

%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/mysql.so

%if %{?_with_oci8:1}%{!?_with_oci8:0}
%files oci8
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/oci8.so
%endif

%if %{?_without_odbc:0}%{!?_without_odbc:1}
%files odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/odbc.so
%endif

%if %{?_without_openssl:0}%{!?_without_openssl:1}
%files openssl
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/openssl.so
%endif

%if %{?_with_oracle:1}%{!?_with_oracle:0}
%files oracle
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/oracle.so
%endif

%files overload
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/overload.so

%if %{?_with_pcntl:1}%{!?_with_pcntl:0}
%files pcntl
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/pcntl.so
%endif

%if %{?_without_pcre:0}%{!?_without_pcre:1}
%files pcre
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/pcre.so
%endif

%if %{?_without_pdf:0}%{!?_without_pdf:1}
%files pdf
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/pdf.so
%endif

%if %{!?_without_pgsql:1}%{?_without_pgsql:0}
%files pgsql
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/pgsql.so
%endif

%files posix
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/posix.so

%if %{!?_without_pspell:1}%{?_without_pspell:0}
%files pspell
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/pspell.so
%endif

%if %{?_without_recode:0}%{!?_without_recode:1}
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

%if %{?_without_snmp:0}%{!?_without_snmp:1}
%files snmp
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/snmp.so
%endif

%files sockets
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/sockets.so

%if %{?_without_sybase_ct:0}%{!?_without_sybase_ct:1}
%files sybase-ct
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/sybase_ct.so
%endif

%files sysvsem
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/sysvsem.so

%files sysvshm
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/sysvshm.so

%if %{?_without_wddx:0}%{!?_without_wddx:1}
%files wddx
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/wddx.so
%endif

%if %{?_without_xml:0}%{!?_without_xml:1}
%files xml
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/xml.so
%endif

%if %{?_without_xmlrpc:0}%{!?_without_xmlrpc:1}
%files xmlrpc
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/xmlrpc.so
%endif

%if %{?_without_xslt:0}%{!?_without_xslt:1}
%files xslt
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/xslt.so
%endif

%if 0%{!?_without_yaz:1}
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
