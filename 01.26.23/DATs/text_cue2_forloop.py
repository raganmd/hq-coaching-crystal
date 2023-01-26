for each_row in op('table_cue2').col(0)[1:]:
    par_name = each_row.val
    scene_val = op('table_cue2')[par_name, 1].val

    ipar.Settings[par_name] = scene_val