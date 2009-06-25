#!/bin/sh
tag=php_4_4_9
branch=PHP_4_4

if [ ! -d $tag ]; then
	cvs -d :pserver:cvsread@cvs.php.net:/repository checkout -r $tag -d $tag php-src
fi
if [ ! -d $branch ]; then
	cvs -d :pserver:cvsread@cvs.php.net:/repository checkout -r $branch -d $branch php-src
fi

cd $tag && cvs up -d && cd ..
cd $branch && cvs up -d && cd ..

diff -ur $tag $branch > php4-branch.diff
