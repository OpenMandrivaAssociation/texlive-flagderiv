# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/flagderiv
# catalog-date 2007-02-22 16:49:05 +0100
# catalog-license gpl
# catalog-version 0.10
Name:		texlive-flagderiv
Version:	0.10
Release:	1
Summary:	Flag style derivation package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/flagderiv
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flagderiv.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flagderiv.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flagderiv.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The flagderiv package is used to create mathematical
derivations using the flag/flagpole notation. The package
features an intuitive command syntax, opening and closing
multiple flagpoles, different comment styles, customizable
symbols and label namespaces.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/flagderiv/flagderiv.sty
%doc %{_texmfdistdir}/doc/latex/flagderiv/README
%doc %{_texmfdistdir}/doc/latex/flagderiv/flagderiv.pdf
#- source
%doc %{_texmfdistdir}/source/latex/flagderiv/flagderiv.dtx
%doc %{_texmfdistdir}/source/latex/flagderiv/flagderiv.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
