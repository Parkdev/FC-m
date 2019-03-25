from statistics import Stat

class DataHandler():
    #compostion
    calculater=Stat()

    @classmethod
    def get_raw_data(cls, filename):
        raw_data = {}
        wb = load_workbook(filename)
        ws = wb.active
        g = ws.rows
        for name_cell, scroll_cell in g:
            raw_data[name_cell.value] = scroll_cell.value
        return raw_data

    def __init__(self,filename):
        self.year_class=filename.split('_')[1]
        self.raw_data=DataHandler.get_raw_data(filename)
        self.scores=list(self.raw_data.values())
        self.cache={}
    # def get_average(self):
    #     avg=self.calculator.get_average()
    #     return avg

    # def get_std_dev(self):
    #     avg=self.get_average()
    #     self.get_vari(avg, self.)

