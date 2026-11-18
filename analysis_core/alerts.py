def score_slice(rows, minimum):
    """返回原始分数达到给定阈值的告警，不解释核实结果。"""
    if not 0 <= minimum <= 1:
        raise ValueError('threshold outside [0,1]')
    return [dict(r) for r in rows if r['score'] >= minimum]

def visible_label_rows(rows,cutoff):
    """核对截至指定日期已收到的全部原始标签，包括更正记录。"""
    return [dict(r) for r in rows if r['observed_at'] <= cutoff]

def recorded_selection(rows):
    """核对执行日志的选择数与概率合法性。"""
    for r in rows:
        p=r['probability']
        if not 0<=p<=1 or (r['selected'] and p==0):
            raise ValueError('invalid recorded selection probability')
    return dict(total=len(rows),selected=sum(bool(r['selected']) for r in rows))
