#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-cerberus
Version  : 1.3.4
Release  : 1
URL      : https://files.pythonhosted.org/packages/c4/87/55f8b2e36a5f97c5aaf6424e75f7a21cbd69d0365f6e2e332d03d029bb15/Cerberus-1.3.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/c4/87/55f8b2e36a5f97c5aaf6424e75f7a21cbd69d0365f6e2e332d03d029bb15/Cerberus-1.3.4.tar.gz
Summary  : Lightweight, extensible schema and data validation tool for Python dictionaries.
Group    : Development/Tools
License  : ISC
Requires: pypi-cerberus-python = %{version}-%{release}
Requires: pypi-cerberus-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)

%description
=========================
        |build-status| |python-support| |black|
        
        Cerberus is a lightweight and extensible data validation library for Python.

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

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639057254
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

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
