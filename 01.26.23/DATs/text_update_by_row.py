selected_row = 6
cues = op('table_cues')

for each_cell in cues.row(selected_row)[1:]:
    target_par = cues['par', each_cell.col].val
    if each_cell.val == '':
        pass
    else:
        ipar.Settings[target_par] = each_cell.val
