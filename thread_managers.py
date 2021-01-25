from time import sleep

class ThreadManager:
    def __init__( self, threads):
        self.threads = threads

    def __call__( self):
        for thread in self.threads:
            thread.start()
        for thread in self.threads:
            thread.join()

class PatientThreadManager:
    def __init__( self, threads):
        self.threads = threads

    def __call__(self, VERBOSE=False):
        if VERBOSE:
            n = len( self.threads)
            i = 0
            self.threads = tqdm(self.threads)
        for thread in threads:
            thread.start()
            sleep(0.1)
            if VERBOSE:
                i = i + 1
                self.threads.set_description( f"Starting threads {i} of {n}.")
        if VERBOSE:
            self.threads = tqdm(self.threads)
            n = len( self.threads)
            i = 0
        for thread in threads:
            if VERBOSE:
                i = i + 1
                self.threads.set_description( f"Waiting for thread {i} of {n}.")
            thread.join()

class BatchThreadManager:
    def __init__( self, threads):
        self.threads = threads

    def __call__( self, VERBOSE=False, BATCH_SIZE=10):
        if VERBOSE:
            n = len( self.threads)
            i = 0
            self.threads = tqdm(self.threads)
        for thread in threads:
            thread.start()
            sleep(0.1)
            if VERBOSE:
                i = i + 1
                self.threads.set_description( f"Starting threads {i} of {n}.")
        if VERBOSE:
            self.threads = tqdm(self.threads)
            n = len( self.threads)
            i = 0
        for thread in threads:
            if VERBOSE:
                i = i + 1
                self.threads.set_description( f"Waiting for thread {i} of {n}.")
            thread.join()

        THREAD_COUNT = 0
        thread_groups = [[]]
        if VERBOSE:
            self.threads = tqdm( self.threads)
            n = len( self.threads)
            i = 0
        for thread in self.threads:
            if VERBOSE:
                i = i + 1
                self.threads.set_description( f"Starting threads {i} of {n}.")
                thread_groups[-1].append( thread)
            THREAD_COUNT = THREAD_COUNT + 1
            if THREAD_COUNT == BATCH_SIZE:
                THREAD_COUNT = 0
                thread_groups.append([])
        if VERBOSE:
            i = 0
            n = len( thread_groups)
            thread_groups = tqdm( thread_groups)

        for thread_group in thread_groups:
            if VERBOSE:
                i = i + 1
                thread_group.set_description( f"Processing thread group {i} of {n}.")
            for thread in thread_group:
                thread.start()
            for thread in thread_group:
                thread.join()
