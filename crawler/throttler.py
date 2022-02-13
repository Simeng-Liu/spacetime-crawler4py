import threading

class Throttler(object):
    def __init__(self, config):
      self.config = config
      self.domain_time = {}
      self.lock = threading.Lock()

    def check_polite(self, cur_time, domain):
        self.lock.acquire()
        self.domain_time[domain] = cur_time
        self.lock.release()
        if domain not in self.domain_time:
            return True
        return cur_time >= (self.domain_time[domain] + self.config.time_delay)

    def last_crawl_time(self, domain):
      return self.domain_time[domain]