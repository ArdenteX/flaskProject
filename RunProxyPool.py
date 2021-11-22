from schedule.PoolSchedule import ExpireCheckProcess, ProxiesCountProcess
from proxyPool.conf import VALID_CHECK_CYCLE
from proxyPool.conf import POOL_LEN_CHECK_CYCLE
from app import app


def run_server():
    process1 = ExpireCheckProcess(VALID_CHECK_CYCLE)
    process2 = ProxiesCountProcess(POOL_LEN_CHECK_CYCLE)
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    app.run()


if __name__ == '__main__':
    run_server()

