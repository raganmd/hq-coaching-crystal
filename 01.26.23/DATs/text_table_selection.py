target_table = op('table_cue2')

for each_row in target_table.col(0)[1:]:
    par_name = each_row.val
    scene_val = target_table[par_name, 1].val

    ipar.Settings[par_name] = scene_val