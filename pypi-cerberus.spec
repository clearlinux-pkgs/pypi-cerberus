#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-cerberus
Version  : 1.3.4
Release  : 10
URL      : https://files.pythonhosted.org/packages/c4/87/55f8b2e36a5f97c5aaf6424e75f7a21cbd69d0365f6e2e332d03d029bb15/Cerberus-1.3.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/c4/87/55f8b2e36a5f97c5aaf6424e75f7a21cbd69d0365f6e2e332d03d029bb15/Cerberus-1.3.4.tar.gz
Summary  : Lightweight, extensible schema and data validation tool for Python dictionaries.
Group    : Development/Tools
License  : ISC
Requires: pypi-cerberus-license = %{version}-%{release}
Requires: pypi-cerberus-python = %{version}-%{release}
Requires: pypi-cerberus-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)

%description
=========================
        |build-status| |python-support| |black|
        
        Cerberus is a lightweight and extensible data validation library for Python.

%package license
Summary: license components for the pypi-cerberus package.
Group: Default

%description license
license components for the pypi-cerberus package.


%package python
Summary: python components for the pypi-cerberus package.
Group: Default
Requires: pypi-cerberus-python3 = %{version}-%{release}

%description python
python components for the pypi-cerberus package.


%package python3
Summary: python3 components for the pypi-cerberus package.
Group: Default
Requires: python3-core
Provides: pypi(cerberus)
Requires: pypi(setuptools)

%description python3
python3 components for the pypi-cerberus package.


%prep
%setup -q -n Cerberus-1.3.4
cd %{_builddir}/Cerberus-1.3.4
pushd ..
cp -a Cerberus-1.3.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656363738
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cerberus
cp %{_builddir}/Cerberus-1.3.4/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cerberus/1887ddf1ee05ccdccdade2ccab4757f2dd1cbb74
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-cerberus/1887ddf1ee05ccdccdade2ccab4757f2dd1cbb74

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
