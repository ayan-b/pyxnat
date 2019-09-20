import os.path as op
from .. import Interface

fp = op.join(op.dirname(op.abspath(__file__)), 'central.cfg')

central = Interface(config=fp)

def test_freesurfer_stats():
    r = central.select.experiment('CENTRAL04_E00637').resource('FREESURFER6')
    hv = r.hippoSfVolumes()
    hv = r.aparc()
    hv = r.aseg()
    v = hv.query('region=="TotalGrayVol"')['value'].tolist()[0]
    assert(v == 857168.580741)

def test_ashs_stats():
    r = central.select.experiment('CENTRAL04_E00637').resource('ASHS')
    hv = r.stats()
    v = hv.query('region=="CA1" & side=="left"')['volume'].tolist()[0]
    assert(v == 1585.838)