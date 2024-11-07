class PersonalC:

    def __init__(self):
        
        def __init__(self, mother, cpu, gpu, ram, rom, psu, cooler, case):
            
            # Материнская плата
            self._mother = mother
            # Процессор
            self._cpu = cpu
            # Графический процессор
            self._gpu = gpu
            # Оперативная память
            self._ram = ram
            # Постоянная память
            self._rom = rom
            # Блок питания
            self._psu = psu
            # Кулер процессорный
            self._cooler = cooler
            # Корпус
            self._case = case

        # Getters and setters
        @property
        def mother(self):
            return self._mother

        @mother.setter
        def mother(self, value):
            self._mother = value

        @property
        def cpu(self):
            return self._cpu

        @cpu.setter
        def cpu(self, value):
            self._cpu = value

        @property
        def gpu(self):
            return self._gpu

        @gpu.setter
        def gpu(self, value):
            self._gpu = value

        @property
        def ram(self):
            return self._ram

        @ram.setter
        def ram(self, value):
            self._ram = value

        @property
        def rom(self):
            return self._rom

        @rom.setter
        def rom(self, value):
            self._rom = value

        @property
        def psu(self):
            return self._psu

        @psu.setter
        def psu(self, value):
            self._psu = value

        @property
        def cooler(self):
            return self._cooler

        @cooler.setter
        def cooler(self, value):
            self._cooler = value

        @property
        def case(self):
            return self._case

        @case.setter
        def case(self, value):
            self._case = value
