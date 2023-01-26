from datetime import datetime

class Controller:

    def __init__(self, myOp):
        self.My_op = myOp
        self.cues_table = myOp.op('table_cues')
        self.lister = myOp.op('lister')
        self.allow_update = False
        self.last_selected_row = None
        print(f'Controller Init @ {datetime.now()}')
    
    def Update_from_lister(self, info_dict:dict) -> None:
        '''
        '''
        current_row = info_dict.get('row')
        self.allow_update = True
        self._update_state(current_row)
        self.last_selected_row = current_row
        self.allow_update = False

    def Update_cue_vals(self, par:callable) -> None:
        '''
        '''
        if self.last_selected_row == None:
            pass
        else:
            current_cue_row = self._get_current_row()
            target_par = par.name
            self.cues_table[current_cue_row, target_par] = par.eval()

    def _get_current_row(self) -> int:
        return self.last_selected_row

    def _update_state(self, target_row:int) -> None:
        '''
        '''
        if self.allow_update:
            for each_cell in self.cues_table.row(target_row)[1:]:
                target_par = self.cues_table[0, each_cell.col]
                ipar.Settings[target_par] = each_cell.val
        else:
            pass