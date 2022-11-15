Name:		texlive-atbegshi
Version:	53051
Release:	1
Summary:	Execute stuff at \shipout time
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/atbegshi
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/atbegshi.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/atbegshi.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/atbegshi.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is a modern reimplementation of package everyshi,
providing various commands to be executed before a \shipout
command. It makes use of e-TeX's facilities if they are
available. The package may be used either with LaTeX or with
plain TeX.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/atbegshi
%{_texmfdistdir}/tex/generic/atbegshi
%doc %{_texmfdistdir}/doc/latex/atbegshi

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
