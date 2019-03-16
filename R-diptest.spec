#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-diptest
Version  : 0.75.7
Release  : 14
URL      : https://cran.r-project.org/src/contrib/diptest_0.75-7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/diptest_0.75-7.tar.gz
Summary  : Hartigan's Dip Test Statistic for Unimodality - Corrected
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-diptest-lib
BuildRequires : clr-R-helpers

%description
multimodality and provide a test with simulation based p-values,  where
 the original public code has been corrected.

%package lib
Summary: lib components for the R-diptest package.
Group: Libraries

%description lib
lib components for the R-diptest package.


%prep
%setup -q -c -n diptest

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523302012

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523302012
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library diptest
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library diptest
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library diptest
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library diptest|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/diptest/DESCRIPTION
/usr/lib64/R/library/diptest/INDEX
/usr/lib64/R/library/diptest/Meta/Rd.rds
/usr/lib64/R/library/diptest/Meta/data.rds
/usr/lib64/R/library/diptest/Meta/features.rds
/usr/lib64/R/library/diptest/Meta/hsearch.rds
/usr/lib64/R/library/diptest/Meta/links.rds
/usr/lib64/R/library/diptest/Meta/nsInfo.rds
/usr/lib64/R/library/diptest/Meta/package.rds
/usr/lib64/R/library/diptest/Meta/vignette.rds
/usr/lib64/R/library/diptest/NAMESPACE
/usr/lib64/R/library/diptest/NEWS.Rd
/usr/lib64/R/library/diptest/R/diptest
/usr/lib64/R/library/diptest/R/diptest.rdb
/usr/lib64/R/library/diptest/R/diptest.rdx
/usr/lib64/R/library/diptest/data/exHartigan.R
/usr/lib64/R/library/diptest/data/qDiptab.R
/usr/lib64/R/library/diptest/data/statfaculty.R
/usr/lib64/R/library/diptest/doc/diptest-issues.R
/usr/lib64/R/library/diptest/doc/diptest-issues.Rnw
/usr/lib64/R/library/diptest/doc/diptest-issues.pdf
/usr/lib64/R/library/diptest/doc/diptest.bib
/usr/lib64/R/library/diptest/doc/hist-D11.rda
/usr/lib64/R/library/diptest/doc/index.html
/usr/lib64/R/library/diptest/extraData/qDiptab.rds
/usr/lib64/R/library/diptest/help/AnIndex
/usr/lib64/R/library/diptest/help/aliases.rds
/usr/lib64/R/library/diptest/help/diptest.rdb
/usr/lib64/R/library/diptest/help/diptest.rdx
/usr/lib64/R/library/diptest/help/paths.rds
/usr/lib64/R/library/diptest/html/00Index.html
/usr/lib64/R/library/diptest/html/R.css
/usr/lib64/R/library/diptest/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/diptest/libs/diptest.so
/usr/lib64/R/library/diptest/libs/diptest.so.avx2
/usr/lib64/R/library/diptest/libs/diptest.so.avx512
