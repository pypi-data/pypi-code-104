import os

from concurrent.futures.thread import ThreadPoolExecutor
from shield34_reporter.dynamic_locator import DynamicElementLocator
from shield34_reporter.model.contracts.block_contract import BlockContract
from shield34_reporter.model.contracts.block_run_contract import BlockRunContract
from shield34_reporter.model.enums.block_type import BlockType
from shield34_reporter.model.enums.status import Status


class BlockRunReportContainer:
    blockReport = []
    generalReport = None
    blockRunContract = None
    prevBlockRunContract = None
    currentDriver = None
    currentBlockFolderPath = ""
    pool = ThreadPoolExecutor(10)
    webElements = {}
    proxyServers = []
    web_element_descriptors_map = {}
    dynamic_elements_locator = DynamicElementLocator()
    findElementCounter = -1
    in_wait_until = False
    action_started_count = 0
    screen_shot_file_before_quit = None

    def __init__(self):
        self.blockRunContract = BlockRunContract(Status.PENDING, 0, 0, "", "", "", "", "",
                                                 BlockContract(BlockType.UNKNOWN, "", "", 1, "", "", ""))

    def reset_block_run_contract(self):
        self.prevBlockRunContract = self.blockRunContract
        self.blockRunContract = BlockRunContract(Status.PENDING, 0, 0, "", "", "", "", "",
                                                 BlockContract(BlockType.UNKNOWN, "", "", 1, "", "", ""))
        self.currentBlockFolderPath = ""
        self.blockReport = []
        self.generalReport = None
        self.web_element_descriptors_map = {}
        self.findElementCounter = -1
        self.action_started_count = 0
        self.dynamic_elements_locator = DynamicElementLocator()
        self.screen_shot_file_before_quit = None

    def set_block_run_contract(self, block_run_contract):
        try:
            self.blockRunContract = block_run_contract
            self.blockRunContract.blockContract = block_run_contract.blockContract
            self.dynamic_elements_locator.load_dynamic_elements(self.blockRunContract.blockContract.id)
        except Exception as e:
            pass

    def generate_current_block_folder_path(self):
        from shield34_reporter.container.run_report_container import RunReportContainer
        file_name = os.path.join(RunReportContainer.get_reports_folder_path(),
                                 "Shield34-report", "run_" +
                                 self.blockRunContract.runContract.id, "block_run_" +
                                 self.blockRunContract.id)
        os.makedirs(file_name)
        return file_name

    def get_current_test_folder(self):
        if self.currentBlockFolderPath == "":
            self.currentBlockFolderPath = self.generate_current_block_folder_path()
        return self.currentBlockFolderPath

    def shut_down_executor(self):
        self.pool.shutdown(True)

    def reset_executor(self):
        self.pool = ThreadPoolExecutor(10)

    def add_web_element(self, element_id, locator):
        self.webElements[element_id] = locator

    def get_web_element(self, element_id):
        if element_id in self.webElements:
            return self.webElements[element_id]
        return None

    def get_current_driver(self):
        return self.currentDriver

    def set_current_driver(self, driver):
        self.currentDriver = driver

    def update_find_element_counter(self):
        self.findElementCounter += 1

    def action_already_started(self):
        return self.action_started_count > 0

    def get_dynamic_element_locator(self):
        return self.dynamic_elements_locator
