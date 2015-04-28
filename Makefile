TEX = intro.tex secret.tex public.tex hash.tex elliptic.tex group.tex pairing.tex homo.tex abe.tex broadcast.tex assumption.tex field_math.tex ec_math.tex search.tex zero.tex pairing_math.tex rand.tex appendix.tex proxy.tex fe.tex
_TEX = _intro.tex _secret.tex _public.tex _hash.tex _elliptic.tex _group.tex _pairing.tex _homo.tex _abe.tex _broadcast.tex _assumption.tex _field_math.tex _ec_math.tex _search.tex _zero.tex _pairing_math.tex _rand.tex _appendix.tex _proxy.tex _fe.tex _kigou.tex
IMG = img/dh.pdf img/dh-ok.pdf img/dh-ng.pdf img/elgamal-weak.pdf \
    img/circle.pdf img/dq3.pdf img/dq3-2.pdf \
    img/elliptic.pdf img/pairing.pdf img/timecapsule.pdf \
    img/kusuri.pdf img/tversky.pdf img/ss.pdf img/extract.pdf \
    img/access-tree.pdf img/no-pfs.pdf img/pfs.pdf \
    img/birthday.pdf img/dh-oracle.pdf img/cbc.pdf img/cbc-dec.pdf \
    img/combi.pdf img/area.pdf img/ec-add.pdf img/p1.pdf img/rho.pdf \
    img/mac.pdf img/iterated-hash.pdf img/bad-hmac.pdf img/protocol.pdf \
    img/broad1.pdf img/broad-tree.pdf img/broad-revocation.pdf \
    img/easy-traitor.pdf img/traitor.pdf img/bdhe.pdf img/pairing2.pdf \
    img/distortion.pdf img/pairing-def.pdf img/mov.pdf img/mov2.pdf \
    img/peks1.pdf img/peks2.pdf img/vote.pdf img/blind.pdf img/psi.pdf \
    img/stream.pdf img/tokei.pdf img/sphere.pdf img/pki.pdf img/homo.pdf \
    img/caesar.pdf img/ctr.pdf img/ind-atk.pdf img/ind-cca.pdf \
    img/ec-op.pdf img/tile.pdf img/ec-neg-add.pdf img/pappus.pdf \
    img/zero.pdf img/miller-line.pdf img/proxy0.pdf img/proxy.pdf \
    img/inner-product.pdf img/mtorsion.pdf img/ec-zero.pdf \
    img/dlin.pdf img/ec_walk.pdf img/base.pdf img/abe.pdf \
    img/contents.pdf img/gcd.pdf img/rlwe.pdf

.pptx.pdf:
    pptx2pdf $?
    pdfcrop $*.pdf $*.pdf

ango.pdf: ango.tex $(_TEX) $(IMG) ref.bib add_idx.py remark.tex custom.tex
    platex ango.tex
    jbibtex ango
    platex ango.tex
    mendex -c -g -S -s dot.ist ango.idx
    ptex2pdf -l -ot -synctex=1 ango.tex

_kigou.tex: kigou.tex
    python add_idx.py $?

_intro.tex: intro.tex
    python add_idx.py $?

_secret.tex: secret.tex
    python add_idx.py $?

_rand.tex: rand.tex
    python add_idx.py $?

_public.tex: public.tex
    python add_idx.py $?

_group.tex: group.tex
    python add_idx.py $?

_elliptic.tex: elliptic.tex
    python add_idx.py $?

_hash.tex: hash.tex
    python add_idx.py $?

_pairing.tex: pairing.tex
    python add_idx.py $?

_homo.tex: homo.tex
    python add_idx.py $?

_abe.tex: abe.tex
    python add_idx.py $?

_fe.tex: fe.tex
    python add_idx.py $?

_broadcast.tex: broadcast.tex
    python add_idx.py $?

_assumption.tex: assumption.tex
    python add_idx.py $?

_field_math.tex: field_math.tex
    python add_idx.py $?

_ec_math.tex: ec_math.tex
    python add_idx.py $?

_search.tex: search.tex
    python add_idx.py $?

_zero.tex: zero.tex
    python add_idx.py $?

_proxy.tex: proxy.tex
    python add_idx.py $?

_pairing_math.tex: pairing_math.tex
    python add_idx.py $?

_appendix.tex: appendix.tex
    python add_idx.py $?

clean:
    rm -rf _*.tex *.blg *.aux *.idx *.ilg *.ind *.log *.toc *.dvi *.out *.pdf *.bbl
